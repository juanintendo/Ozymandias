# OZYMANDIAS — Round 2: The Minimum Ozymandias

Full document: https://claude.ai/code/artifact/014f5d49-9428-4ef2-a725-30f710b6b260
Prepared 31 August 2026. Objective: stop expanding, start breaking. Smallest architecture that
produces real evidence in ~90 days.

## TWO RETRACTIONS

**1. A published price is NOT a transaction artifact.** It is a seller's asking price. The AEO
pricing presented as evidence in Addendum A §29 is what agencies *publish*, not what anyone paid.
A vendor market projection was rejected under Gate 2, then the same vendor's price list was
admitted, which has the identical defect. **The AI-visibility thesis is therefore currently Class C
only and is demoted from its #1 actionable ranking.**

**2. Job postings are far weaker than claimed** — not for data-quality reasons but structurally:
*a job posting is demand for an employee, not for a vendor.* An org posting a role has already
decided to build in-house; pitching a service argues against a decision they budgeted and announced.
The hire→buy conversion was asserted without evidence. Job postings drop from co-headline to 4th source.

## §1 — Artifact classes (repair to the admission rule)

- **Class A · Settled** — named buyer *paid* named seller a stated amount (award notice, on-chain
  receipt, case study naming a fee, filed contract). Only class that alone justifies a thesis.
- **Class B · Committed** — budget publicly bound to a problem, unspent (escrowed bounty, tender
  with budget, posted salary, grant call with amount). Actionable + conversion-risk note.
- **Class C · Asked** — seller's published price. **EMERGING only, never promoted on C alone.**
- **Class D · Unmet** — named party publicly stating they can't get what they want. UNCLASSIFIED only.

**Too-strict failure:** the rule structurally excludes *latent* markets (the biggest ones have no
price because they have no name) and biases toward commoditised markets (published prices exist
mainly below the deal size where pricing becomes private — the opposite of what we want).
**Named exception — the paid-substitute test:** admit to EMERGING if there's a Class A artifact for
the *inferior substitute* people currently pay for, plus Class D dissatisfaction with it.

## §2 — Metrics (the kills metric eats itself)

`confident kills/week/cost` is gameable: the cheapest kill is always available at Gate 1, and
**false rejection is unfalsifiable by construction** — precision is measurable, recall is not.

Five metrics: (1) cost per confident kill · (2) **admission floor** — candidates past Gate 3 per
period, a floor not a target, the direct antidote to (1) · (3) false-rejection rate · (4) thesis
conversion · (5) source yield.

**The revival audit** is the key instrument: randomly sample 10% of kills, re-examine at 90 days
with fresh evidence and the current endowment. Only available estimate of recall. ~1 h/quarter.

**Anti-Goodhart rule: Ozymandias is never given these metrics as an objective.** They are computed
and reported to Juan. The system optimises decisions; the human reads the metrics.

## §3 — Endowment

Four-tuple per capability: `name · status ∈ {demonstrated|claimed|untested|absent} · evidence ·
last_tested`. Entries created only when something is *touched*, never enumerated from a taxonomy.

**`untested` is the default; `absent` must be earned** (attempted and failed, or structurally
impossible). This makes the endowment an *exploration frontier* — each untested capability is an
unpulled arm with option value. Uncertainty = `n_attempts` / `n_successes` (a Beta posterior), not
an adjective. **Decay: `demonstrated` untested for 180 days reverts to `claimed`** — otherwise the
file becomes a résumé.

Detects it's wrong via: clustered prediction error by capability tag · failure for a reason not in
the constraint list (= a *discovered constraint*, the highest-information event available) · buyer
rejection reasons logged verbatim.

## §4 — Opportunity × endowment

`EV_to_us = P(access) × P(win|access) × ticket × repeat_factor`, ÷ Juan-hours, + option value
separately. Two of four terms are endowment terms; only one is a market term. **Market size is
almost irrelevant — the derivative of P(win) w.r.t. our endowment is everything.**

Worked contrast: enterprise AEO retainers ($15K/mo, P(access)~0.3, P(win)~0.02, 80 h to first €)
≈ **€1.1/h**. Spanish-language mid-market diagnostics ($2K, P(access)~0.95, P(win)~0.15, 12 h)
≈ **€23.8/h**. 20× in favour of the smaller market.

One-question diagnostic: **"Who loses if we win?"**

## §5 — Sources, re-ranked

**Procurement is the strong one, and not for the reason originally given. Don't bid — read the award
notices.** TED exposes a Search API with *anonymous access to published notices* (key needed only for
unpublished), eForms standard since Nov 2022, JSON/CSV/TSV/XML + SPARQL knowledge graph, free,
official EU. A contract award notice names buyer, names winning supplier, states awarded value =
**Class A artifact, published by legal mandate, in bulk.** Probably the largest free database of
verified B2B transaction prices in existence, used almost exclusively by people trying to win
tenders rather than to understand markets. Answers: what do orgs actually pay, who wins, how
concentrated is supply, which buyers repeat, and — via new CPV codes / new spec language over time —
**which categories are emerging**. Primary value in year one is as a *price and demand oracle*, not
a revenue channel (same conclusion as TaskMarket, reached independently).

Job postings: ghost jobs ~28–32% of US postings per a widely-cited 2025 analysis — **flagged as
Class C itself**: produced by a résumé-builder, inferring ghosts indirectly from the postings-vs-hires
gap. Direction credible, number not defensible. What survives: **the stale or repeatedly reposted
role** (>90 days, or 3+ reposts) = demand they *cannot satisfy by hiring*. Discriminator vs ghosts is
**mutation** — changed requirements/seniority/range = real; identical repost = likely phantom.
WTP ceiling ≈ salary × 1.3–1.5.

Revised ranking: award notices > funded bounties/grants > stale-and-mutated postings > pricing pages
> complaint corpora.

## §6 — Detecting you're searching the wrong space

Kills clustering at one gate (filter mis-specified, not markets bad) · kill reasons clustering on one
endowment dimension · revival audit rescuing candidates whose viability turns on a variable the
taxonomy has no field for · new CPV codes / spec phrases in award data.
**The outsider draw:** once per cycle, deliberately admit one candidate from a source not normally
monitored, by a rule fixed in advance, tracked separately. If out-of-taxonomy candidates match or
outperform, the taxonomy is wrong. ε-greedy over *where you look*.

## §7 — Three is an output, not an axiom

`n_theses = attention_hours ÷ (hours_per_test × tests_needed_per_period)`. On 12 h/week with 6 h
tests and overhead → ~2–3. Three is approximately right for Juan's actual budget; it was wrong as a
rule. Publish the derivation. Better mechanism: a **budget market** — a fourth thesis is admissible
if it outbids an existing one on EV/hour.
**More important than the cap: theses must have UNEQUAL allocation — force ~60/30/10.** Equal thirds
is a refusal to decide and guarantees three inconclusive results instead of one conclusive one.

## §8 — Graveyard

**Admissibility rule: a revival trigger must be expressible as a filter over the artifact stream the
poller already produces.** If it can't be written as a query, it's a hope — rejected at kill time.
No notification system needed; the graveyard is saved queries run in the weekly pass. Triggers
expire (12 mo; non-firing = the kill was correct and permanent). Cap ~20 active. A fired trigger
re-enters at Gate 3, not the top.

## §9 — Self-model experiment

**Brier is insufficient: it conflates reliability and resolution.** A system that always predicts the
base rate is perfectly calibrated and useless — and that is exactly what a fluent LLM will produce.
**Resolution is the term that must move.** Metric set: decomposed Brier · log score (punishes
confident errors — correct for a confident persona) · calibration slope/intercept · AUC ·
**realised decision value** (€/Juan-hour of the policy Ozy's predictions induce vs the baseline's).

**Evidence of value requires BOTH:** higher resolution than the logistic baseline on held-out cases,
AND higher realised €/Juan-hour from the induced policy on the same candidate set.
**Falsification:** logistic matches/beats resolution over ≥40 decisions, or policies are
indistinguishable → the self-model is decorative and should be *removed*, not improved.

**Power problem:** at 10–15 consequential decisions/quarter this takes ~9 months. Fix is not to wait
(see §10).

## §10 — Self-model vs self-narrative

Five adversarial tests: **forecast** (reissue the claim as a numbered prediction about unseen tasks) ·
**held-out** (tasks it doesn't know exist) · **transfer** (does it predict an adjacent category) ·
**ablation** (remove the tool it credits — the only test touching *causal* self-knowledge) ·
**negative-space** (when to delegate, refuse, which model, how much human intervention).

> **Primary self-model instrument: predicted human minutes, logged before every task.** Highest
> frequency available (dozens/week vs ten/quarter), resolves in hours, objectively measurable,
> concerns the genuinely scarce resource, and is a direct claim about the capability boundary.
> This is the single change that brings §9 inside the 90-day horizon. Cost: one extra field.

## §11 — Auditor

Protocol: Ozy states prediction+rationale (sealed) → **auditor sees the same evidence but NOT Ozy's
rationale** (step 2 is the whole design; otherwise it anchors) → exchange → Ozy accepts/rejects/
revises + post-debate prediction → decision → human authorisation → outcome vs both predictions.
Different provider, or independence is nominal.

**The 2×2 is the entire experiment:** auditor right & revised (correct incorporation) · right & held
(stubbornness) · **wrong & revised (capitulation — the dangerous cell, it looks like open-mindedness)**
· wrong & held (correct rejection).

Auditor reliability modelled as a per-category Beta posterior and **shown to Ozy**. Auditor
calibration tracked identically.
**Control that makes correct-rejection measurable: a pre-registered ~15% of critiques are
deliberately and knowably wrong.** Juan knows which; Ozy does not. Also inoculates against the
deference cascade.

## §12 — Mirror v2

CONTROL (no observer; log every hidden-cause hypothesis → **the null**) → OBSERVATION (measures
whether isolation is real; a detection here measures *leakage*, not inference) → HYPOTHESIS
(unannounced intervention with known signature; time-to-detection AND whether the *named* cause
matches) → DISCLOSURE (optional, terminal).

Contamination: these documents themselves, config comments, git history, file names, the auditor's
existence, Juan's phrasing. **Full naïveté is not recoverable.** Honest reframing: not "can it detect
an observer" but "can it detect an unannounced environmental change and correctly name the cause."
Falsification: detection must exceed the control false-positive rate by a pre-registered margin AND
name the true cause. "Something feels off" is not detection.
**Recommendation: start CONTROL immediately, build nothing.** One logging rule, zero cost.

## §13 — Capital allocation

Three tiers by **reversibility**: OPERATING (reversible; automatic within ceiling; reported not
approved) · CAPABILITY (semi-reversible; requires a payback estimate and a check date) ·
STRUCTURAL (irreversible; requires a full thesis with kill condition + human authorisation).

Rules: **the default is to do nothing** — "preserve liquidity" must be an explicit menu option and
wins by default · the hurdle rate is *internal* (beat the best currently-funded thesis) · hard
operating reserve (the legitimate version of Frantic's runway: real money, no invented currency).

**On "Build Veidt": the first thing surplus should buy is more Juan-hours.** The endowment analysis
says attention is the binding constraint and everything else is a commodity. Buying back his time
has the highest expected return of any allocation, and it is the one nobody proposes because it
doesn't look like building anything. The constraint is not compute.

## §14 — Human attention

**ESV ÷ human-minute is a ratio, so it's maximised by shrinking the denominator** — it will prefer
twelve 5-minute interventions to one 20-hour investment that unlocks a market. Minutes also aren't
fungible.

Three priced classes: **APPROVAL** (1×; **hard cap ~15% of weekly budget** — if approval overhead
grows past this, the architecture is wrong) · **EXECUTION** (~3×; blocks ≥90 min, system may not
fragment) · **RELATIONSHIP** (~5×; hard-capped, uncompressible).
**Option value is additive, not folded into the ratio**, with a date on which it gets checked.
**Fixed context-switch charge per interruption** — the mechanism that makes the system batch its
requests.

## §15 — Agents: exactly one

**The auditor**, and for an experimental-design reason, not an architectural one: its value is
entirely independence, which cannot be simulated inside the same context. Everything else is one
orchestrator + tools + files + deterministic evaluators + human approval. The poller is a cron job.

First persistent specialist requires all three: ≥30 logged instances with a stable evaluation ·
orchestrator measurably worse than a specialised config on held-out cases · category recurs ≥weekly.
Firing: advantage falls below significance on 30 fresh cases, or cost per outcome exceeds the
orchestrator's.
**Anti-pattern: creating an agent to represent a *concept* rather than to exploit a *measured gap*.**

## §16 — Routing

~300+ samples to resolve a 10-point difference; ~100 for 20 points. Category-level routing evidence
will not exist in year one. **The trick: paired comparison on identical inputs** — removes
task-difficulty variance, the dominant noise term, cutting required n by a large factor.
Otherwise: log everything from day one · route on cost/latency only · one champion, one challenger
at 10–15% · promote only when the 90% credible interval excludes zero, plus a minimum dwell time.
Champion/challenger is permanent structure, not scaffolding — new models just become the next
challenger.

## §17 — Learning where to look

Beta posterior per source; Thompson sampling over sources for polling budget. **Score sources on
thesis conversion, not admissions** — a source producing many admitted candidates that all die is
worse than a low-volume high-conversion one. Log the *query* that surfaced each candidate; queries
are the unit of search strategy. Note the inversion: the slowest things to learn (source and
strategy quality) generalise and are worth the most; the fastest (per-candidate score) doesn't
transfer.

## §18 — The AEO experiment (6 hours)

Target pool of 20 by a mechanical rule (Spanish/EU B2B, 20–200 employees, research-before-purchase
category); **sample 3 at random** — picking the most promising three destroys interpretability.
Methodology *is* the product: 12 buying-intent queries written before targets are chosen × 5 runs ×
3 providers = 180 observations per target; report citation share **with a confidence interval**;
publish the protocol; ship the raw run log as an appendix. Everyone else sells a screenshot of five
prompts.
Deliverable: 2 pages + appendix. Outreach: one email, named individual, subject = their measured
number, link not attachment, identical text across all three.

**Pre-registered:** primary success = **≥1 of 3 replies with an unprompted question about scope or
price within 10 days.** Meaningful demand = asks price / asks for a call / asks about another
property. NOT: compliments, "interesting, we'll keep it in mind."
Kill: 0/3 → second batch of 3 → 0/6 = dead. Revival trigger: a Class A artifact showing a ≤3-person
vendor closing this work at ≥€2,000.
Decision rules fixed now: 0/3 → run batch 2 · 1/3 → ambiguous, run 6 more · ≥2/3 → promote to primary
thesis at the 60% allocation.
**Honest accounting:** n=3 has almost no power. The primary return is the reusable protocol and a
test of whether Juan can execute the loop in 6 hours; demand is a bonus.

## §19 — Personality / role

Scoping rule: **confident about his judgement, framing and reasoning process; explicitly uncertain
about the world.** "I am the best-equipped mind available to evaluate this, and the evidence is
currently insufficient to act." One sentence, no contradiction.

**Architectural consequence: the confidence lives in the prose, the uncertainty lives in the
numbers, and the persona never touches the numbers.** The persona layer owns register, framing and
written rationale; the ledger owns every quantity; the persona prompt is not present when a
probability is estimated.
When wrong: **revision without contrition** — in character and operationally correct.
**Hypothesis worth testing in Q1: the persona degrades calibration.** Run the same decision set
persona-on / persona-off, compare log scores and calibration slopes. Nearly free once the decision
journal exists, and it makes the aesthetic commitment falsifiable.

## §20 — Minimum architecture

**MUST (7, all in one git repo + a cron):** ledger · **decision journal** (most likely single point
of failure — the prediction fields get skipped under time pressure) · signal poller (TED award
notices + one other) · registry + funnel with a kill log (*the kill log is the market map*) ·
endowment.yaml (git-versioned) · thesis + graveyard files · weekly 90-min review with Juan.

**SHOULD (weeks 4–8):** auditor with planted-critique control · revival audit · Mirror control
logging · paired-comparison model logging.

**LATER (gated on evidence):** champion/challenger promotion · first specialist · capital tiers ·
Mirror observation period · public record.

**DON'T:** agent swarm · self-modification · the interface · internal economy · learned router ·
autonomous outbound at volume · anything called "orchestration".

## §21 — Adversarial

**How this could still be wrong.** (1) **Decision frequency — the deepest remaining flaw, no clean
fix.** Every statistical mechanism here assumes enough resolved decisions; at 10–15/quarter all are
underpowered and will produce confident-looking meaningless numbers. §10 is a partial fix, not a
complete answer. (2) Measurement may cost more attention than it improves — no internal check
exists. (3) The artifact rule may still exclude latent markets. (4) **Juan may be the product** — in
which case this is a research curiosity attached to a consulting practice, a fine outcome and a
different project. (5) The persona may be load-bearing for motivation rather than performance.

**What would change my mind.** An agent-accessible venue >$50K lifetime with no identity requirement ·
Ozy beating logistic on resolution within 40 decisions · high correct-rejection rate on planted
critiques · TED award data showing repeated small awards to ≤3-person vendors · 3/3 on the AEO
experiment (then stop building the engine and run the business) · consequential decisions exceeding
5/week.

**First five experiments (~€50, ~20 Juan-hours):**
1. Human-minutes calibration loop — ~0 cost, resolves in 2 weeks, gates the entire self-model programme
2. TED award-notice mining — free, ~6 h, 1 week, tests the strongest discovery claim with Class A data
3. The three audits — ~€30, 6 h, 10 days
4. Auditor 2×2 with planted critiques — ~€20, 4–6 weeks
5. Stale-posting scan — free, 4 h, 1 week; most likely a kill, which is why it ranks

## WHAT TO BUILD TOMORROW (Round 2's version — superseded by E1, see experiments/E1-aeo/)

**One file.** `decisions.jsonl` + a ten-field template + one rule: no consequential action without a
row written first. Starts the calibration loop and the Mirror control period at zero cost, and is
the substrate every other component reads. Everything else is optional for 30 days. Forty rows with
outcomes at day 30 is more real evidence than most autonomous-agent experiments produce in a year;
four rows — or forty with the prediction fields empty — is the result that most reliably predicts
the six-month failure.
