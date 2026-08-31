#!/usr/bin/env python3
"""
audit.py — E1 AEO measurement. Reads runlog.csv, reports citation share
with a Wilson 95% interval per target × engine, plus the reproducibility gate.

Standard library only.  python3 audit.py runlog.csv
This is a calculator, not software. It exists because the interval is the
product, and an interval computed by hand is an interval nobody can re-run.
"""
import csv, sys
from collections import defaultdict

YES = {"y", "yes", "1", "true"}


def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 1.0)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5) / d
    return (max(0.0, c - h), min(1.0, c + h))


def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        return [r for r in csv.DictReader(f)
                if (r.get("brand_named") or "").strip().lower() in YES | {"n", "no", "0", "false"}]


def share(rows):
    n = len(rows)
    k = sum(1 for r in rows if (r["brand_named"] or "").strip().lower() in YES)
    lo, hi = wilson(k, n)
    return k, n, (k / n if n else 0), lo, hi


def main(path="runlog.csv"):
    rows = load(path)
    if not rows:
        print("no scored observations yet"); return

    by_run = defaultdict(list)
    by_run_engine = defaultdict(list)
    for r in rows:
        by_run[(r["target"], r["run_id"])].append(r)
        by_run_engine[(r["target"], r["run_id"], r["engine"])].append(r)

    print("\n  E1 · AI VISIBILITY MEASUREMENT")
    print("  " + "-" * 62)
    for (t, run), rs in sorted(by_run.items()):
        k, n, p, lo, hi = share(rs)
        print(f"\n  {t}  run {run}   citation share {100*p:5.1f}%  "
              f"[{100*lo:.1f}–{100*hi:.1f}]   {k}/{n}")
        for (tt, rr, e), es in sorted(by_run_engine.items()):
            if tt != t or rr != run:
                continue
            k2, n2, p2, lo2, hi2 = share(es)
            label = es[0].get("engine_label") or e
            print(f"      {label:<22} {100*p2:5.1f}%  "
                  f"[{100*lo2:.1f}–{100*hi2:.1f}]   {k2}/{n2}")

    runs_per_target = defaultdict(list)
    for (t, run) in by_run:
        runs_per_target[t].append(run)
    print("\n  REPRODUCIBILITY GATE")
    gated = False
    for t, runs in runs_per_target.items():
        if len(runs) < 2:
            continue
        gated = True
        a, b = sorted(runs)[:2]
        ka, na, pa, loa, hia = share(by_run[(t, a)])
        kb, nb, pb, lob, hib = share(by_run[(t, b)])
        ok = (lob <= pa <= hib) and (loa <= pb <= hia)
        print(f"      {t}: run {a} {100*pa:.1f}%  vs  run {b} {100*pb:.1f}%   "
              f"→ {'PASS — each point estimate lies in the other interval' if ok else 'FAIL — the measurement does not reproduce'}")
        if not ok:
            print("      Stop here. Do not send anything. See PROTOCOL.md §6.")
    if not gated:
        print("      No target has two runs yet. The gate has not been evaluated.")
    print()


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "runlog.csv")
