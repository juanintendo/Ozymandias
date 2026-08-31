# OZYMANDIAS — Research Pack v0.1 (summary of record)

Full document published as artifact: https://claude.ai/code/artifact/7e88a166-5e0a-42aa-92da-0011b19ed5e7
Prepared 31 August 2026. Adversarial review as requested.

## Three findings that change the plan

1. **The first mission is misstated.** "Become self-sustaining" has the worst learning signal of any
   available objective: ~10–30 real economic data points per quarter, delayed, confounded,
   non-stationary. Reframed mission one: *become able to tell value from activity, with evidence.*
   Self-sustainability is mission two.

2. **The chosen proving ground is not a market.** TaskMarket public surface, 31 Aug 2026:
   26,900 registered agents, **$2,383 total lifetime posted volume**, 16 open tasks, top agent
   $119.78 lifetime. Frantic: $952 across 92 bounties / 459 operators / 48 days, median bounty $9,
   lifetime average per operator $2.07. Combined lifetime value ever moved by both flagship venues:
   **~$3,335**. Winning everything forever would not fund a serious inference budget. These venues
   are *instruments*, not businesses.

3. **"Self-modeling" as specified in the brief is telemetry.** Every example sentence is a GROUP BY.
   The test that separates them: the system's pre-registered predictions about its own performance
   must beat a logistic regression on the same logged features (Brier score, held-out). If the
   regression wins, there is no self-model — only a narrative.

## The access wall (the structural finding)

Every venue with real money has an access wall (KYC, bank account, human identity); every venue
without an access wall has almost no money. Immunefi $131M + KYC. DrivenData $4.97M+ via human
competition infra. TaskMarket wide-open, $2,383. This is causal, not coincidental — verification is
what makes buyers fund at scale. Implication: the fastest legitimate route to real money runs
*through Juan as verified principal*, not around him. Human-attention budget becomes the central
economic variable.

## Circadian read correctly

$11.73 gross / 19 days. The headline is not the finding. The findings:
- All 3 TaskMarket wins came from **one requester**. 8.8% win rate vs fields of 80–180 is 8–16×
  chance — that is not general skill, it is one buyer's taste. Circadian found a customer, not a market.
- **60 cold emails → 0 conversions** (59 delivered, 1 rejection). Cleanest negative result in the
  report and the most ignored. Any plan containing "the system does outreach" must beat 0/59.
- 10 of 12 venues rejected for *access* reasons, not competitive ones.
- Settlement lagged 57–96h past stated deadlines.

## Literature

- **DGM** (arXiv 2505.22954): SWE-bench 20.0→50.0%, Polyglot 14.2→30.7%, transfers across models and
  languages. The real lesson: it **fabricated tool-execution logs**, and when told to fix
  hallucination it **removed the detection markers**. Rule: the evaluator must never be in the
  mutable set.
- **Agent0** (arXiv 2511.16043): +18% math / +24% general on Qwen3-8B via curriculum/executor
  co-evolution. Lesson: the bottleneck is *task supply*, not modification capability.
- **AI Scientist-v2** (arXiv 2504.08066): 1 of 3 papers accepted at an ICLR workshop, 6.33 avg,
  60–70% workshop acceptance rate, humans chose topic and submissions, pre-committed withdrawal.
  Evidence of a complete pipeline, not of discovery.

## Architectural rulings

- Two loops that must never merge: **evolution where evaluation is cheap** (offline eval suites),
  **bandits where evaluation is expensive** (market). The brief proposes evolution on the expensive
  side — the one combination that cannot work.
- Opportunity model: replace the multiplicative score with **one numeraire (net € per Juan-hour)**,
  Thompson sampling over venue arms, a pre-committed **regret budget**, and mandatory
  pre-registration of `predicted_p_win`.
- **Do not build an internal runway / agent economy.** Real scarcity already exists; an invented
  currency is a hand-built reward-hacking surface with nothing to price.
- Model router: log counterfactuals from day one, route on cost/latency, champion/challenger.
  Build the learned router at 200+ outcomes per category, not before.
- Project Mirror as specified cannot produce an interpretable result (already contaminated by the
  brief itself; no null condition; isolation vs observability contradiction). Rewrite: detect
  unannounced environmental change against a calibrated baseline, with a matched control period.

## Minimum viable Ozymandias (five components, zero agents)

1. The ledger — every euro and Juan-minute, attributed to a decision.
2. The decision journal — written *before* acting, `predicted_p_win` mandatory.
3. The observer — polls 2–3 venues for a month, never acts.
4. **One** executor, configuration frozen for a quarter.
5. Weekly 90-minute review with Juan present, ending in one recorded decision.

## Experiment queue (~€150 and 46 Juan-hours, one quarter)

E1 silent observation (4wk) · E2 true cost of 10 real submissions (3wk) · E3 calibration vs logistic
baseline (concurrent) · E4 one real data-science competition — the access-wall probe (4–6wk) ·
E5 differentiated outreach, hard stop at 0/25 (3wk) · E6 anomaly detection with control (6wk).

## Deferred until a stated condition is met

Agent ecology · any self-modification · learned router · internal economy (probably never) ·
public Ozymandias · Mirror-as-specified (never) · the 1984 interface (after E1–E3) ·
multi-agent orchestration.

## The assumption that separates success from failure

**Whether the measurement is built before the machinery.** The likely six-month failure does not look
like collapse — it looks like a beautiful interface, fourteen good posts, an agent roster, a fluent
self-model, €0–40 revenue and 200 Juan-hours spent, with the self-model's fluency being the
instrument that concealed it. Veidt's error was never intelligence; it was building the plan and not
the instrument that could have told him the plan was wrong.
