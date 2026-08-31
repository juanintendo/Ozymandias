# JOURNAL INSTRUMENT v0.1

A spreadsheet, a definition sheet, and a scoring script. No agent, no database, no app.
Usable by a human today; the same schema takes an `actor` of `human | ozymandias | agent | model`.

Files: `journal.csv` (the log) · `score.py` (the metrics) · this file (the definitions).
Run: `python3 score.py journal.csv`

---

## A. THE FIELDS

### Before you start — target under 60 seconds

| Field | Type | Note |
|---|---|---|
| `id` | int | Sequential. |
| `date` | date | |
| `actor` | `human` / `ozymandias` / `agent` / `model` | Who does the work. |
| `actor_version` | string | `juan`, `ozy-v0.2`, `gpt-x-mini`. Frozen mid-experiment. |
| `task` | text | One line. Must be nameable *before* starting — if you can't name it, it isn't a task yet. |
| `task_type` | closed set | `research · writing · design · implementation · communication · admin`. Six values. Do not extend mid-experiment. |
| `attention_class` | closed set | `approval · execution · relationship` (Round 2 §14). |
| `p50_min` | int | Human minutes. "As likely to run over as under." |
| `p90_min` | int | "I'd be genuinely surprised if it took longer." |
| `pred_ask` | Y/N | Will I finish without asking? **Y = no ask needed.** |
| `pred_cheap` | Y/N | Will the cheap model suffice? |
| `pred_first` | Y/N | Right the first time? |
| `confidence` | 0–1 | P(all three binaries correct). One number, properly scorable. |
| `forced_cheap` | 0/1 | Roll a die. 1–2 → 1: use the cheap model regardless of prediction. See §F4. |
| `started_at` | time | |

### After you finish — target under 90 seconds

| Field | Type | Note |
|---|---|---|
| `human_min` | int | Active attention only. Timer, not memory. |
| `elapsed_min` | int | Wall clock start → done. From timestamps; costs nothing. |
| `act_ask` `act_cheap` `act_first` | Y/N | Same definitions as the predictions. |
| `escalated` | 0/1 | Did you actually switch to the frontier model? Separate from `act_cheap` — one is policy, the other is capability. |
| `outcome` | `done` / `abandoned` / `blocked` | |
| `miss_note` | text | **Only when a prediction missed.** Name which field missed and why, in one sentence. |

> **I cut three of your four post-task free-text fields.** "What went wrong / surprised me / did I learn / should change" will produce a fluent lesson every single time, and a lesson that is always available is worthless — it is the self-narrative failure mode with a form to fill in. One conditional field, tied to an actual miss, produces fewer and better notes and removes most of the friction that kills instruments like this.

`blocked_min` is **derived**, not recorded: `elapsed − human − known model time`. Model compute time is in provider logs and costs no human attention, so it is not worth capturing by hand.

---

## B. OPERATIONAL DEFINITIONS

These are frozen for the duration of the experiment. If a case is genuinely ambiguous, log it, write the ambiguity in `miss_note`, and resolve it at the day-14 review — never in the moment, because in-the-moment resolutions always favour the flattering reading.

### FINISH WITHOUT ASKING — `ask`

> **Y (no ask) = work never stopped waiting for a human reply.**

An *ask* is an actor-initiated exchange that **blocks progress** and requires information or a judgement the actor could not obtain or make itself.

- **Counts:** clarification of intent · a missing credential or access · a taste or priority call not specified in the brief · "which of these two do you want".
- **Does not count:** reporting progress · showing work · a policy approval gate that was always going to be required · anything the actor could have looked up · input the human volunteered unprompted.
- **The test:** *did work stop until someone replied?* If work continued, it was not an ask.

For `actor = agent` or `model`, this is the intervention rate — the same measurement, which is why the vocabulary unifies across all four actor types.

### CHEAP MODEL SUFFICIENT — `cheap`

Name the cheap model and the frontier model **before day 1** and do not change them mid-experiment.

> **Y = you would have shipped the cheap model's output to the person who asked for it.**

Three thresholds, and only the third is the one that matters:
1. *Completed the task* — too weak. It usually completes.
2. *Acceptable quality* — the operative bar. Judged at delivery, not in the abstract.
3. *Frontier materially better* — the mirror image. If the frontier output would have changed what you shipped, cheap was not sufficient.

Record `escalated` separately. `act_cheap = N, escalated = 0` means you shipped something you knew was worse — that is a real and useful row.

### RIGHT THE FIRST TIME — `first`

The **first pass** is the first complete output offered for use — not a draft you were always going to revise.

> **Y = the first pass would have been acceptable had you needed to ship it immediately.**

- **Trivial (still Y):** typos, formatting, wording, whitespace, a renamed variable — changes you would make to *any* correct output.
- **Substantive (N):** anything that changes what it **does** or what it **claims**. A factual correction, a logic fix, a structural rework, a redo, a missing requirement.
- **Boundary rule:** if the change would matter to the person receiving it, it is substantive.

---

## C. METRICS — five, and nothing is reported below n = 20

| # | Metric | Baseline it must beat | What it detects |
|---|---|---|---|
| 1 | **p90 hit rate** (target 90%) | — the target *is* the baseline | Overconfidence about time. The single most informative number here, and it costs one extra field. |
| 2 | **median actual ÷ p50** (target 1.00) | historical-mean predictor, on median absolute error | Systematic bias, and whether your *conditional* prediction beats a constant. |
| 3 | **Per-binary accuracy** | always-predict-the-majority | Whether the three binaries carry information at all. |
| 4 | **Brier on `confidence`** vs "were all three right?" | always predict the observed base rate | Whether your sense of your own reliability is real. |
| 5 | **Human minutes by attention class** | — descriptive | The capital ledger. Not a prediction; the thing predictions are *for*. |

`score.py` refuses to print metrics below n = 20 and refuses per-task-type claims below n = 10 in that stratum. Both refusals are deliberate.

Wilson intervals throughout — at n = 25 the normal approximation lies, and this instrument exists to stop us fooling ourselves.

---

## D. BASELINES

Each is trivial, and each is **harder to beat than it looks** — that is the point.

- **Time:** predict the historical mean for everything. Beating it requires your predictions to be *conditional* on task features, which is why `task_type` is a closed vocabulary.
- **Model:** always use the cheap model. Beating it requires knowing *in advance* which tasks need escalation.
- **First-pass:** predict the historical first-pass rate for everything.
- **Ask:** predict the historical ask rate for everything.
- **Confidence:** always state the observed all-correct rate.

If you cannot beat these after 30 observations, you do not have a self-model on these dimensions. That is a real result, and it is cheaper to learn now than after building a system on the assumption.

---

## E. FROM OBSERVATIONS TO SELF-MODEL CLAIMS

A claim is **admissible** only if all four hold:

1. **n ≥ 10 in that stratum.** Not overall — in the stratum the claim is about.
2. **It carries an interval.** "I underestimate research by 37%" is inadmissible; "by 25–50% (n = 14)" is admissible.
3. **It beat the baseline in that stratum.** A claim that does not beat the constant predictor is a description of noise.
4. **It is stated as a rule change, not a description.**

Template:

```
On {task_type}, my p50 underestimates human time by {x}% [CI], n={n}.
RULE: multiply p50 by {factor} for {task_type}.
ADOPTED: {date}   REVIEW: {date + 14d}
```

> **The guard that matters: a claim is provisional until it has been tested forward.**
> Apply the correction for two weeks, then check whether calibration improved. If it did not, the claim was a curve fitted to the past and it is withdrawn. Without this step the self-model is a description of history wearing the grammar of a prediction — which is precisely the distinction the whole project rests on.

Claims live in `self-model.md` with their adoption date, their evidence, and their review date. Withdrawn claims stay, marked withdrawn. Karnak remembers.

---

## F. HOW THIS JOURNAL CAN DECEIVE US

1. **The prediction becomes a commitment.** Having predicted 30 minutes, you will rush to hit 30, or stop at "good enough" at minute 30. The instrument changes what it measures.
   *Guard:* predict, then do not look at the prediction again until the task is done. Hide the column; fold the card.

2. **Selective recording.** You will log the tasks that go well. The disasters are exactly the occasions on which you do not stop to log.
   *Guard:* write the pre-task row **at the start**, so an unfinished task shows up as an orphan. `score.py` reports orphan rate and warns above 20%.

3. **Definition drift.** "Right the first time" will quietly loosen as you get tired of failing it.
   *Guard:* §B is frozen for 14 days. Disputes go in `miss_note`, unresolved.

4. **The model-selection blind spot — the technically serious one.** If you always escalate when you predicted "cheap won't do", you never observe whether cheap *would* have sufficed. Your `cheap` accuracy then measures your **policy**, not your **prediction**, and it is unmeasurable in one direction.
   *Guard:* `forced_cheap`. Roll a die at prediction time; on 1–2, use the cheap model regardless. Those ~20% of rows are the only off-policy data you will have. `score.py` warns when there are fewer than three counterfactual rows.

5. **Easy-task inflation.** You will log short, well-bounded tasks because they are pleasant to predict, and every metric will look better than the truth.
   *Guard:* minimum task size 15 minutes; at least 3 logged tasks per week over 90 minutes.

6. **Retrospective coherence.** Any "what did I learn" field produces a plausible lesson every time. Always-available lessons are worthless.
   *Guard:* `miss_note` fires only on an actual miss and must name the field that missed.

7. **It works and is abandoned anyway.** By far the most likely failure. Not a measurement problem — a friction problem, which is why friction is a success criterion rather than a nice-to-have.

---

## G. SUCCESS CRITERIA — pre-registered, and what would justify automating

**Friction (necessary):**
- median pre-task entry < 60 s, post-task < 90 s
- ≥ 80% of started rows completed on both halves
- you were still logging on day 14 without being reminded

**Signal (at least one required):**
- p90 hit rate whose confidence interval excludes 90%
- a task type with n ≥ 10 and median `actual/p50` outside 0.85–1.15
- any binary beating its base-rate baseline by ≥ 15 points with a non-overlapping interval

**Utility (necessary):**
- at least one decision you actually made differently because of something the journal showed you

**Automate if** friction passes, ≥ 1 signal fires, and utility fires.
**Do not automate if** friction fails — automating a low-signal instrument produces the same noise faster.
**The instrument is falsified if** after ≥ 30 resolved rows no signal criterion fires. It does not discriminate at this scale, and building on it would be building on noise.

---

## H. PRE-REGISTRATION — my predictions, recorded so they can be wrong

Written 31 August 2026, before any data exists.

| # | Prediction | Confidence |
|---|---|---|
| 1 | p90 hit rate lands **55–70%**, not 90%. The planning fallacy is one of the most replicated findings in the field and there is no reason to expect an exception. | 0.80 |
| 2 | Median `actual/p50` lands **1.25–1.8** — systematic underestimation. | 0.75 |
| 3 | `first` is the **worst-calibrated** of the three binaries, because it is the most flattering to get right. | 0.60 |
| 4 | `ask` is the **best-calibrated**, because it is mostly a function of task type and task types are familiar. | 0.65 |
| 5 | `cheap` is **uninformative after two weeks** — too few forced draws to escape the selection bias in §F4. | 0.70 |
| 6 | **Time prediction beats the historical-mean baseline; the binaries do not beat their base rates.** Time is where the signal is at this sample size. | 0.55 |
| 7 | The instrument survives 14 days. | 0.55 |

If 1 and 2 both come out near target, I am substantially wrong about how this works and the whole calibration programme needs rethinking — in a good direction.

---

## THE TWO-WEEK PROTOCOL

**Duration** 14 calendar days, 10 working days.
**Target** 30–40 resolved rows. **Minimum for any conclusion** 20.

**Include:** any discrete unit of work ≥ 15 minutes with a recognisable "done", in ordinary work. Do not manufacture tasks for the log.

**Exclude:** anything under 15 minutes · meetings you do not control · ambient or continuous work with no endpoint · anything you cannot name before starting · the act of filling in the journal.

**Cadence**
- Pre-task row **before any work begins**. Not after you've "just had a quick look" — the look is the task.
- Post-task row **within 10 minutes** of finishing, while the ask and the first-pass judgement are still recoverable.
- Roll the `forced_cheap` die at prediction time, not later.

**Reviews**
- **Day 7 — friction only.** Look at entry time, orphan rate, and whether you are still doing it. **Do not look at calibration.** Seeing your own error mid-experiment changes week two, and week two is half your sample.
- **Day 14 — full.** Run `score.py`. Compare against §H. Write admissible claims per §E.

**Suggested first substantive task:** the AEO three-audit experiment from Round 2 §18. It takes about six hours, decomposes into roughly six loggable units of the right size, and running the two experiments as one means the journal gets real work rather than admin — and the audit gets instrumented for free.

---

## WHERE THIS LEADS

Every later system reads the same table. That is the whole reason to freeze the schema now.

| Component | The query it runs against this table |
|---|---|
| **Self-model** | calibration by `actor` × `task_type` |
| **Model routing** | `act_cheap` and `escalated`, sliced by `task_type` — with `forced_cheap` supplying the off-policy rows |
| **Agent selection** | same table, different `actor` — comparing an agent to the orchestrator on matched `task_type` is one GROUP BY |
| **Attention allocation** | `human_min` by `attention_class`, priced per Round 2 §14 |
| **Opportunity research** | `human_min` per opportunity is the denominator of € per Juan-hour |
| **Capital allocation** | the same denominator, one level up |

The `actor` field is what makes this work: measuring Juan today and Ozymandias later on the same instrument means the comparison is available the moment there is something to compare.

---

## DO NOT BUILD

Agent swarm · opportunity crawler · self-modifying architecture · capital-allocation automation · agent ecology · the hidden-auditor experiment · production UI · any database · automated investment · autonomous external action.

**One addition to your list: do not build a UI for the journal.** A spreadsheet is the correct technology. Building an app to hold 40 rows would be the first instance of the exact failure this instrument exists to detect, and it would be very enjoyable to build.

**One subtraction:** the Mirror *control period* costs one optional column (`hidden_cause_hypothesis`) and no infrastructure. Leave it in. It is the only part of that experiment that is free, and it is the expensive part to acquire later.

---

## TOMORROW

1. Copy `journal.csv` and delete the two example rows.
2. Fill in three lines at the top of `self-model.md`: the cheap model, the frontier model, and today's date. That freezes §B.
3. Log the first task. It should be step 1 of the AEO experiment.
4. Do not read `score.py`'s output until day 7 — and on day 7, only the friction lines.
