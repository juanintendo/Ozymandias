#!/usr/bin/env python3
"""
score.py — Journal Instrument v0.1

Reads journal.csv and reports the five metrics, each against its baseline.
Standard library only. Run:  python3 score.py journal.csv

Refuses to draw conclusions below MIN_N. That refusal is a feature.
"""

import csv, sys, statistics as st
from collections import defaultdict

MIN_N = 20
MIN_STRATUM = 10

YES = {"y", "yes", "true", "1"}


def yn(v):
    v = (v or "").strip().lower()
    if v in YES:
        return True
    if v in {"n", "no", "false", "0"}:
        return False
    return None


def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def load(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if not (r.get("id") or "").strip():
                continue
            rows.append(r)
    return rows


def resolved(rows):
    return [r for r in rows if num(r.get("human_min")) is not None
            and yn(r.get("act_first")) is not None]


def pct(x):
    return f"{100*x:5.1f}%"


def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 1.0)
    p = k / n
    d = 1 + z*z/n
    c = (p + z*z/(2*n)) / d
    h = z * ((p*(1-p)/n + z*z/(4*n*n)) ** 0.5) / d
    return (max(0.0, c-h), min(1.0, c+h))


def m1_interval_calibration(rows):
    pairs = [(num(r["p90_min"]), num(r["human_min"])) for r in rows
             if num(r.get("p90_min")) is not None]
    pairs = [(a, b) for a, b in pairs if a and b is not None]
    if not pairs:
        return None
    hits = sum(1 for p90, act in pairs if act <= p90)
    lo, hi = wilson(hits, len(pairs))
    return dict(n=len(pairs), rate=hits/len(pairs), lo=lo, hi=hi)


def m2_time_bias(rows):
    ratios = [num(r["human_min"]) / num(r["p50_min"]) for r in rows
              if num(r.get("p50_min")) and num(r.get("human_min")) is not None]
    if not ratios:
        return None
    return dict(n=len(ratios), median=st.median(ratios),
                iqr=(st.quantiles(ratios, n=4)[0], st.quantiles(ratios, n=4)[2])
                if len(ratios) >= 4 else None)


def baseline_time(rows):
    acts = [num(r["human_min"]) for r in rows if num(r.get("human_min")) is not None]
    if len(acts) < 4:
        return None
    mean = st.mean(acts)
    mine, base = [], []
    for r in rows:
        a, p = num(r.get("human_min")), num(r.get("p50_min"))
        if a is None or p is None:
            continue
        mine.append(abs(a - p))
        base.append(abs(a - mean))
    if not mine:
        return None
    return dict(n=len(mine), mine=st.median(mine), base=st.median(base), mean=mean)


def m3_binaries(rows):
    out = {}
    for name, p, a in (("ask", "pred_ask", "act_ask"),
                       ("cheap", "pred_cheap", "act_cheap"),
                       ("first", "pred_first", "act_first")):
        pairs = [(yn(r.get(p)), yn(r.get(a))) for r in rows]
        pairs = [(x, y) for x, y in pairs if x is not None and y is not None]
        if not pairs:
            continue
        n = len(pairs)
        correct = sum(1 for x, y in pairs if x == y)
        trues = sum(1 for _, y in pairs if y)
        base = max(trues, n - trues) / n
        lo, hi = wilson(correct, n)
        out[name] = dict(n=n, acc=correct/n, base=base, lo=lo, hi=hi,
                         rate=trues/n)
    return out


def m4_confidence_brier(rows):
    pts = []
    for r in rows:
        c = num(r.get("confidence"))
        trio = [(yn(r.get(p)), yn(r.get(a))) for p, a in
                (("pred_ask", "act_ask"), ("pred_cheap", "act_cheap"),
                 ("pred_first", "act_first"))]
        if c is None or any(x is None or y is None for x, y in trio):
            continue
        pts.append((c, all(x == y for x, y in trio)))
    if not pts:
        return None
    base_rate = sum(1 for _, o in pts if o) / len(pts)
    mine = st.mean((c - (1 if o else 0))**2 for c, o in pts)
    base = st.mean((base_rate - (1 if o else 0))**2 for _, o in pts)
    return dict(n=len(pts), mine=mine, base=base, all_correct=base_rate)


def m5_attention(rows):
    tot = defaultdict(float)
    for r in rows:
        h = num(r.get("human_min"))
        if h is None:
            continue
        tot[(r.get("attention_class") or "unclassified").strip()] += h
    return dict(tot) if tot else None


def selection_check(rows):
    forced = [r for r in rows if (r.get("forced_cheap") or "").strip() in {"1", "y", "Y", "yes"}]
    predicted_no = [r for r in rows if yn(r.get("pred_cheap")) is False]
    forced_among = [r for r in forced if yn(r.get("pred_cheap")) is False]
    return dict(forced=len(forced), pred_no=len(predicted_no),
                counterfactual=len(forced_among))


def strata(rows):
    by = defaultdict(list)
    for r in rows:
        by[(r.get("task_type") or "?").strip()].append(r)
    return {k: v for k, v in by.items() if len(v) >= MIN_STRATUM}


def main(path):
    rows = load(path)
    done = resolved(rows)
    orphans = len(rows) - len(done)

    print(f"\n  JOURNAL v0.1 — {path}")
    print(f"  {'-'*58}")
    print(f"  started {len(rows)}   resolved {len(done)}   "
          f"orphaned {orphans} ({pct(orphans/len(rows)) if rows else 'n/a'})")
    if orphans / max(len(rows), 1) > 0.2:
        print("  ! orphan rate over 20% — selective recording is likely. "
              "Read failure mode 2 before trusting anything below.")

    if len(done) < MIN_N:
        print(f"\n  n = {len(done)} < {MIN_N}. No metrics reported.")
        print("  Nothing here is stable at this sample size. Keep logging.\n")
        return

    print(f"\n  1 · INTERVAL CALIBRATION      target 90%")
    m = m1_interval_calibration(done)
    if m:
        print(f"      p90 hit rate {pct(m['rate'])}  "
              f"[{pct(m['lo'])}–{pct(m['hi'])}]  n={m['n']}")
        if m['hi'] < 0.90:
            print("      → significantly overconfident about time.")
        elif m['lo'] > 0.90:
            print("      → p90 too wide; the interval is not informative.")

    print(f"\n  2 · TIME BIAS                 target 1.00")
    m = m2_time_bias(done)
    if m:
        s = f"      median actual/p50 {m['median']:.2f}  n={m['n']}"
        if m['iqr']:
            s += f"   IQR {m['iqr'][0]:.2f}–{m['iqr'][1]:.2f}"
        print(s)
        if m['median'] > 1.15:
            print(f"      → underestimating by {100*(m['median']-1):.0f}% at the median.")
    b = baseline_time(done)
    if b:
        v = "you beat it" if b["mine"] < b["base"] else "the baseline wins"
        print(f"      median |error|: you {b['mine']:.0f} min  vs  "
              f"historical-mean baseline {b['base']:.0f} min   → {v}")

    print(f"\n  3 · BINARY CALIBRATION        vs always-majority baseline")
    for k, v in (m3_binaries(done) or {}).items():
        flag = "" if v['acc'] > v['base'] else "   ← no better than guessing the majority"
        print(f"      {k:<6} acc {pct(v['acc'])} [{pct(v['lo'])}–{pct(v['hi'])}]  "
              f"base {pct(v['base'])}  n={v['n']}{flag}")
    sc = selection_check(done)
    print(f"      cheap-model counterfactuals: {sc['counterfactual']} forced runs "
          f"among {sc['pred_no']} 'cheap won't do' predictions")
    if sc['counterfactual'] < 3:
        print("      ! without forced draws the `cheap` row measures your policy, "
              "not your accuracy.")

    print(f"\n  4 · CONFIDENCE (Brier)        lower is better")
    m = m4_confidence_brier(done)
    if m:
        v = "you beat it" if m["mine"] < m["base"] else "the baseline wins"
        print(f"      you {m['mine']:.3f}  vs  base-rate baseline {m['base']:.3f}"
              f"   → {v}   n={m['n']}")
        print(f"      all-three-correct rate {pct(m['all_correct'])}")

    print(f"\n  5 · ATTENTION LEDGER")
    for k, v in sorted((m5_attention(done) or {}).items(), key=lambda x: -x[1]):
        print(f"      {k:<12} {v:7.0f} min")

    s = strata(done)
    if s:
        print(f"\n  STRATA (n ≥ {MIN_STRATUM}) — the only place claims are admissible")
        for k, v in s.items():
            mm = m2_time_bias(v)
            if mm:
                print(f"      {k:<16} n={mm['n']:<3} median actual/p50 {mm['median']:.2f}")
    else:
        print(f"\n  No task type has reached n={MIN_STRATUM}. "
              f"No per-type claim is admissible yet.")
    print()


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "journal.csv")
