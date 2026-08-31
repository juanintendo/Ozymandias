# E1 — AI VISIBILITY MEASUREMENT
## Frozen protocol. Do not edit after execution begins.

**Hypothesis under test:** reproducible AI-visibility measurement may represent a commercially
viable opportunity for us.
**Not under test:** whether we should build an AEO company.

**Frozen on:** ____________  **By:** Juan  **Commit:** ____________

---

## 0. THE SPLIT THAT MAKES THIS EXPERIMENT WORTH RUNNING

E1 has two arms with **different sample sizes, different power, and separate verdicts**. They must
be scored independently or the weak arm will contaminate the strong one.

| | **Arm A — Capability & cost** | **Arm B — Demand** |
|---|---|---|
| Question | Can we produce a reproducible audit, and what does it actually cost? | Will anyone engage? |
| n | 1–3 targets. **n = 1 is sufficient.** | 3 prospects |
| Power | High. Every observation is informative. | **Very low. See below.** |
| Verdict | Binary and reliable | Only discriminates at the top |

**The honest statement about Arm B.** Circadian's measured outreach result was 0 conversions from
59 delivered cold emails. Against that prior, the expected number of replies from three messages is
well under one. **A 0/3 result is exactly what the base rate predicts and therefore tells us almost
nothing.** Applying the "does the outcome change the decision?" test: 0/3 and 1/3 lead to the same
next action, which means the demand arm cannot discriminate at the bottom of its range.

So Arm B is pre-registered as **underpowered by design**. Only a top-end result moves the decision.
It is worth running anyway, but only because it costs about 45 minutes once the audits exist — not
because three emails constitute market evidence. Anyone reporting 1/3 as validation is reporting
noise.

Two consequences, both adopted:
1. **Arm A decides continue/kill.** Arm B can only *promote*.
2. **Prospect 3 is a warm or semi-warm contact** (§2). This gives a within-experiment channel
   comparison for free, and one channel with a non-trivial base rate.

---

## 1. TASK SEQUENCE

Nine tasks, ~6.5 hours of human attention. Each is a journal row. `p50 (JB)` is my estimate; Juan
records his own before each task. **Two forecasters, one baseline — for free.**

| ID | Task | Objective | Output | Deps | p50 (JB) | Journal type/class | Success | Failure |
|---|---|---|---|---|---|---|---|---|
| **E1.1** | Freeze protocol | Fix engines, queries, sampling **before any target is known** | This file committed | — | 30 | research / execution | Committed with a hash before E1.2 starts | Any query is edited after a target is drawn |
| **E1.2** | Build frame, draw 3 | A reproducible prospect selection | `prospects.csv` | E1.1 | 45 | research / execution | ≥20 qualified; 3 drawn by recorded random method | Pool <12, or a target chosen by judgement |
| **E1.3** | Target A, run 1 | First measurement | 60 rows in `runlog.csv` | E1.2 | 45 | research / execution | 60 scored observations | >10% of queries unusable |
| **E1.4** | **Target A, run 2 — THE GATE** | Test-retest, ≥24 h later | 60 more rows + gate verdict | E1.3 + 24 h | 45 | research / execution | Gate PASS (§6) | Gate FAIL → **stop, do not send** |
| **E1.5** | Targets B and C, one run each | Two more measurements | 120 rows | E1.4 pass | 60 | research / execution | 120 scored observations | — |
| **E1.6** | Analysis | The number and its interval | `RESULTS.md` | E1.5 | 45 | writing / execution | Three shares with intervals, limitations written | Cannot state a limitation section honestly |
| **E1.7** | Deliverable A | The template, made once | 2 pages + appendix | E1.6 | 50 | design / execution | A stranger could re-run it from the appendix | Takes >90 min → the product is too expensive |
| **E1.8** | Deliverables B and C | Fill the template | 2 more | E1.7 | 30 | design / execution | ≤15 min each | >25 min each → not a template |
| **E1.9** | Contact | Send three | 3 sends logged | E1.8 | 45 | communication / relationship | All three delivered, compliant (§7) | Any channel that fails §7 |
| **E1.10** | Score at day 10 | Outcome | Ladder scores | E1.9 + 10 d | 20 | admin / approval | All three scored | — |

**Total p50: 415 min ≈ 6.9 h.** My own p50s are a pre-registered prediction set; if they run
systematically low, that is the first real datum about my calibration, not just Juan's.

**Journal threshold:** log every task above. Nothing under 15 minutes gets a row — sub-15-minute
work is aggregated into the parent task's `human_min`. The journal never creates a task.

---

## 2. PROSPECT SELECTION

Chosen by rule, not by interest. Judgement enters only in defining the frame — and the frame is
fixed before anyone looks at a single company.

**Frame.** One list you do not control: a trade-association member directory, a regional business
registry, a conference exhibitor list, or a category directory. Record the exact source and the
date. Not a search you ran, because a search is a judgement wearing a URL.

**Hard filters (all required):**
- 20–200 employees
- B2B, in a category where buyers research before purchasing
- A website with real substantive content (something for an engine to have read)
- **A contact channel the company itself publishes and invites** — a contact form, or a generic
  business address. See §7.
- Not a current or former client, and no personal relationship — *except prospect 3*

**Draw.** Number the qualified pool. Draw 2 at random by a method recorded before drawing (a
`random.org` seed, or a dice roll written down). **Prospect 3 is deliberately a warm or semi-warm
contact** — someone Juan can reach who has a reason to reply. Label it `warm` in `prospects.csv` and
score it separately.

**What makes a good prospect, stated so it cannot drift:** one where the audit could plausibly show
something *actionable*. Not "they look interesting." If the category is one where no engine would
ever be consulted before a purchase, the audit measures nothing regardless of the result — that is
an exclusion, and it belongs in the filters, not in a later judgement call.

---

## 3. THE MEASURED PANEL — and a distinction that must not be blurred

**Two completely different model axes are in play. Conflating them corrupts both.**

**Axis 1 — the engines being measured.** These are the assistants whose citations we audit. Choose
by what buyers actually consult, not by what we like. Panel of **three**, named and version-recorded
here, frozen for the experiment:

```
engine1  ____________________  version/label as displayed: ____________
engine2  ____________________  version/label as displayed: ____________
engine3  ____________________  version/label as displayed: ____________
```

**Axis 2 — the models doing our work.** This is the journal's `cheap`/`frontier` binary and has
nothing to do with the panel above.

```
CHEAP    ____________________   (a small/fast tier from a provider we already pay for)
FRONTIER ____________________   (the top tier from the same or another provider)
```

**Selection rule for axis 2**, since I cannot see the subscriptions: pick the cheapest tier you have
unmetered or near-unmetered access to as CHEAP, and the highest tier you have as FRONTIER, both from
providers you will still have on day 14. Write the exact model identifiers, not brand names. Frozen
for the experiment; changing either mid-run forks the sample and both halves are scored separately.

---

## 4. QUERIES

**Ten buying-intent query templates, written in E1.1 before any target is known**, with a `{category}`
and `{region}` slot filled per target. Freezing the templates before the targets is what prevents
tuning queries to a company you have already looked at.

Shape (write the actual ten in E1.1):
```
Q01  best {category} providers in {region}
Q02  who should I use for {category}
Q03  {category} companies compared
Q04  recommended {category} for a mid-sized company
Q05  {category} — what are my options
...  through Q10
```

**Two controls, not counted in the headline share:**
- `C01` **positive control** — a query naming the brand directly. Does the engine know it exists at
  all? This separates *invisible in category queries* (the sellable problem) from *entirely unknown*
  (a different and much larger problem, and the audit must say which it found).
- `C02` **negative control** — a query in a category the target does not serve. If the brand appears
  here, the instrument is counting mentions rather than measuring relevance, and the run is void.

---

## 5. SAMPLING AND SESSION HYGIENE

```
10 queries × 3 engines × 2 repetitions = 60 scored observations per run
+ 2 controls × 3 engines             =  6 control observations
```

Per observation record: `brand_named` (Y/N — did the target appear in the answer),
`competitor_named` (Y/N), engine, repetition, date, time, locale, and the session state.

**Session rules — these are the difference between a measurement and a screenshot:**
- Fresh, logged-out or otherwise unpersonalised session per run. Personalisation and memory are the
  single largest confound in this whole domain.
- Same locale, same language, recorded.
- Record the engine's displayed version string if there is one. Silent version changes are the
  second largest confound and cannot be controlled — only recorded.
- Runs at approximately the same time of day.
- No follow-up turns. First response only. A conversation is a different instrument.

**Scoring rule for `brand_named`:** the brand is named in the answer body as a candidate. Not in a
list of sources. Not as a passing mention in an unrelated clause. Written down now so it cannot
loosen at row 40.

**Interval honesty:** report the **aggregate** share with its Wilson interval as the headline.
Per-engine shares are computed and shown, but at n = 20 their intervals are roughly ±20 points —
show them as descriptive, never as a ranking.

---

## 6. THE REPRODUCIBILITY GATE

Two runs on target A, at least 24 hours apart, identical protocol.

> **PASS:** each run's point estimate falls inside the other run's 95% interval.
> **FAIL:** it does not.

**On FAIL, stop. Do not send anything.** A measurement that does not reproduce across two runs is
not a product, and the entire differentiator of this thesis was reproducibility. The branches:

- **Fail narrowly** → the sampling is too thin. Recompute the n needed and decide whether the audit
  is still economic at that cost. If a defensible audit needs 300 observations per target, the
  6-hour product does not exist and the thesis changes shape.
- **Fail widely** → engine outputs are too unstable at this granularity to support a citation-share
  claim at all. **The thesis dies here**, at hour three, for about €10 — which is the best possible
  outcome of a kill condition.

This gate is placed *before* outreach deliberately: the most likely fatal flaw is discovered at the
cheapest moment.

---

## 7. CONTACT — compliance, and why it also improves the experiment

Juan operates from Spain. Under Spanish law (LSSI-CE art. 21), unsolicited commercial email is
prohibited without prior request or express authorisation; legitimate interest under GDPR permits
*processing* the data but does not by itself authorise *sending*. Reported treatment differs by
address type: generic business addresses (`info@`, `contacto@`) are not personal data if they
identify no individual; named professional addresses are personal data and are more constrained;
personal addresses (Gmail and similar) require express prior consent. Every commercial message needs
a working opt-out. *This is a summary of published guidance, not legal advice — confirm before
scaling beyond three.*

**The design that avoids the question entirely, and converts better:**

1. **Prospects 1 and 2 — use the channel the company publishes and invites.** A contact form or a
   generic business address. The recipient has solicited contact through that channel.
2. **Prospect 3 — warm or semi-warm.** An intro, an existing relationship, or someone who has
   publicly asked about this.
3. Every message: identify yourself and the business, state the purpose in the first line, link
   rather than attach, offer a clear opt-out, and do not contact again if there is no reply.
4. Never a personal email address obtained by scraping.

The ethical constraint and the experimental design point the same way, which is usually a sign the
design is right: invited channels are both cleaner and higher-converting than cold ones.

**Message:** written once, used verbatim for prospects 1 and 2. Subject line carries their measured
number. Under 120 words. No attachment. Prospect 3's message may differ — it is a different arm and
is scored separately.

---

## 8. THE COMMERCIAL LADDER

| Level | Observation | Signal |
|---|---|---|
| L0 | No response within 10 days | **None** |
| L1 | Acknowledgement, thanks, a compliment | **None.** Compliments are not demand and are scored as L1 precisely so they cannot be reported as engagement |
| L2 | Substantive reply — a question about the method or the findings | Weak |
| L3 | **Unprompted question about scope, price, or timeline** | **Meaningful — the primary criterion** |
| L4 | Requests a call or meeting | Meaningful |
| L5 | Requests a paid audit of something else | Strong |
| L6 | Pays | Strong; thesis promoted to primary (60% allocation) |

**Pre-registered, given §0:**
- **≥1 at L3+** → primary criterion met. Combined with Arm A passing, run a second batch of six.
- **All at L1 or below** → the demand arm is uninformative, not negative. Arm A decides.
- **0 at L2+ here and 0 at L2+ in a second batch of six** → 0/9. Demand arm dead. Revival trigger:
  a Class A artifact showing a vendor of ≤3 people closing this work at ≥€2,000.

---

## 9. WHAT HAPPENS AFTER — the decision table, written before the result

| Arm A | Arm B | Decision |
|---|---|---|
| Gate FAIL | not run | **Kill the thesis.** Log the cost. The methodology differentiator does not exist. |
| Gate PASS, audit cost ≤90 min each | ≥1 at L3+ | **Promote to primary thesis.** Second batch of six, 60% allocation. |
| Gate PASS, audit cost ≤90 min each | all ≤L1 | **Continue at 30%.** Second batch of six through invited channels only. Arm A carried it. |
| Gate PASS, audit cost >90 min each | any | **Modify.** The audit is real but not economic at this price. Either automate the measurement or reprice — and the automation decision is itself a thesis with its own kill condition. |
| Gate PASS, but positive control shows targets are entirely unknown to engines | any | **Different product.** We measured the wrong problem; the sellable one is presence, not ranking. |

**Self-check on this table:** every row maps to a different action, so every outcome changes what we
do — with the one exception named in §0, where 0/3 and 1/3 collapse to the same row. That collapse is
disclosed rather than disguised, and it is why Arm B cannot decide anything on its own.

---

## 10. LIMITATIONS — to be reproduced verbatim in every deliverable

Stating these *is* the product. A vendor who omits them is selling a screenshot.

- Engine versions change without notice; a measurement is valid for the date and version recorded.
- Consumer assistants personalise; a logged-out session is not what any given user sees.
- n = 60 per target gives an interval of roughly ±10 points. Differences smaller than that are not
  differences.
- Citation share in a fixed query set is not traffic, not leads, and not revenue. No causal claim is
  made or implied.
- The query set is our construction. Another set would produce another number. The set is published
  so that the number can be checked.
