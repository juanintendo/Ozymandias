# OZYMANDIAS — Addendum A: The Opportunity Engine (§23–32)

Full document: https://claude.ai/code/artifact/7dee4b5f-282d-4e93-926c-0539d6ffa695
Supersedes the venue framing of Research Pack v0.1 §09–§11. Prepared 31 August 2026.

## Standing correction (from Juan)

Ozymandias must NOT be designed around TaskMarket, Frantic or any predetermined channel. Those are
case studies and evaluation instruments. The economic function must continuously discover and
evaluate opportunities across any legitimate accessible market, and must be able to discover new
market structures rather than search a predefined list. "TaskMarket is strategically irrelevant" is
a valid successful outcome.

## §23 — The inversion

Market candidates are free and infinite; a frontier model produces 200 plausible market names for a
cent, none with evidence anyone ever paid. **Disqualification is the scarce resource.** The engine's
health metric is *confident kills per week ÷ (€ + Juan-hours)* — never candidates surfaced, markets
under evaluation, or theses open. An engine designed as a generator is the §19 failure mode wearing
a new costume.

## §24 — The endowment asymmetry

The question specifies "given the capabilities... currently available", and that clause is where the
work is. The endowment is not uniform:
- **Commodity (no edge):** frontier models, compute, APIs. Any market where the winning input is
  "has a good model" is structurally worthless.
- **Weak edge:** tireless 24/7 execution — only matters where work is volume-bound and objectively
  scored (competitions yes; attention-bound bounty boards no).
- **Decisive edge:** Juan — verified identity, company, bank account, EU/ES + English access
  (this is the §11 access wall from the inside); UX/UI capability, shipped interfaces, portfolio,
  studio identity; and his attention as the binding constraint.

Therefore: **the endowment is a first-class, versioned, machine-readable object re-read before every
scoring pass.** A thesis is a claim about a *pairing* — market × endowment — and half of it is
currently undocumented. Uniform search spends the budget where the answer is structurally known to
be bad; that is not open-mindedness.

## §25 — The admission rule (most important mechanism)

**Nothing enters the registry without a transaction artifact:** a URL/document/record showing a
named party has paid, is paying, has budgeted, or has publicly asked to pay. A price, a funded
bounty, a posted salary, a tender, a grant call with an amount, an invoice, a pricing tier.
An LLM-generated market name is not one. Neither is an analyst projection or a trend piece.
Single exception, UNCLASSIFIED only, never promoted: documented unmet demand from a *named* party.

## §26 — Signal sources (job postings + procurement are the under-exploited pair)

Ranked by quality: job postings (a posted role is the most expensive demand signal a company can
emit — named buyer, confirmed budget, written scope) · public procurement / TED / tenders
(machine-readable by legal mandate, confirmed budgets, award history, inaccessible to anonymous
agents) · grant calls · published pricing pages and *changes* to them · freelance RFP:bidder ratios ·
competition boards · funded OSS issues · complaint corpora (only source for markets with no category
yet) · new API launches (where adjacent markets appear). Agent-native venues: demoted to instrument.

Hypothesis to test in one week: scan job postings mentioning a capability we have, filter to orgs
too small to hire for it. Every hit is a named org with confirmed budget announcing it cannot solve
the problem.

## §27 — Registry and funnel

Four registers with mechanical admission rules. KNOWN: ≥3 artifacts from ≥2 sellers. EMERGING:
artifacts exist but pricing varies >5× or category <2 years old. ADJACENT: gap must be *named and
singular*. UNCLASSIFIED: **hard cap 50** — full means the weakest is dropped, forcing a ranking.

The 15 dimensions are the right dimensions and the wrong order of operations. Staged funnel,
cheapest kills first:
- **Gate 0** legitimacy/policy (binary, free)
- **Gate 1** access — identity, KYC, bank, jurisdiction, licensing (kills most, free)
- **Gate 2** money observably changing hands, artifact dated <12 months (kills speculation, free)
- **Gate 3** endowment fit — differentiated or commodity? (~10 min)
- **Gate 4** ticket size > 4 Juan-hours at his real rate (~10 min)
- **Gate 5** a cheap falsification test exists, <€50 and <4 h — if not, **defer, don't reject**
- **Full evaluation** for survivors only, collapsing to three numbers: net € per Juan-hour, its
  variance, and option value (kept separate so it can't be smuggled in as optimism).

Gates 1–2 would have killed 10 of Circadian's 12 venues for free; Gate 4 kills TaskMarket.

## §28 — Thesis lifecycle and the graveyard

Thesis = five mandatory fields: CLAIM · ENTRY_TEST (cost stated up front) · **KILL_CONDITION written
before entry** · REVIVAL_TRIGGER (monitorable by the poller) · REVIEW_DATE. Plus endowment_version.

A kill condition written afterwards is a negotiation — sunk effort makes every disappointment
explainable, and a model will generate those explanations indefinitely. Same mechanism as
pre-registered `predicted_p_win` in §08, one level up.

The graveyard is a **queue, not an archive**: revival triggers become standing watches on the
poller; when one fires the thesis returns automatically with prior evidence plus "what changed".
Hard limits: max 3 live theses · a dead thesis is never revived by re-scoring, only by a fired
trigger or a new endowment version.

## §29 — Worked example: AI-visibility audits

Evidence (published agency pricing, Aug 2026): entry retainers $1,000–2,500/mo; mid-market
$2,000–8,000/mo; enterprise $10,000–25,000+/mo; freelance projects $150–2,000; programmes "from
$3,000". Buyers: mid-market B2B SaaS, healthcare/biotech, professional services, multi-location
service businesses.
Vendor projection of $4.39B (2026) → $10.72B (2031) is **explicitly not evidence** and does not pass
Gate 2 — included to demonstrate correct handling.

Passes all six gates; Gate 4 by ~3 orders of magnitude vs TaskMarket's $0.32–$24.20 tasks.
Adversarial case: crowded (every SEO agency repositioned), deliverable commoditising, measurement
not reproducible across runs/sessions/model versions, buyers cannot verify quality.

**Where the objections invert:** non-reproducibility is the market's weakness and therefore its only
defensible position. A vendor publishing a *reproducible methodology* — stated sampling, run counts,
confidence intervals, versioned models — sells something structurally different.

> **Highest-leverage structural hypothesis in the project:** the self-modeling/calibration machinery
> §13 requires the system to build for itself IS the first commercial product, pointed outward.
> If true, the research programme and the revenue programme stop competing for the same hours.
> Falsifiable in ~6 hours: three unsolicited audits for named targets, differentiator = reproducibility.

Uncomfortable observation: this took two web searches and ~20 minutes to reach a decision-grade
verdict, and is 100–1000× larger per engagement than the venues v0.1 spent eleven sections on. That
is the argument for the engine — and the argument that v1 of the engine can be very simple.

## §30 — Minimum viable engine (revises v0.1 §21; nothing is an agent)

1. Endowment file (versioned) · 2. Signal poller (start: job postings + one procurement feed) ·
3. Registry (one table, admission rules enforced, UNCLASSIFIED capped) · 4. The funnel as a
checklist — **the kill log is the market map** · 5. Thesis files, max 3 live · 6. Graveyard queue ·
7. The unchanged weekly 90-minute review with Juan, ending in one recorded decision.

## §31 — Prohibitions

No invented markets · no entry without a pre-written kill condition · never more than 3 live theses ·
no revival by re-scoring · projections and the system's own reasoning are never evidence · do not
build it as agents · do not optimise for breadth of coverage.

## §32 — Provisional ranking (a prior to be destroyed, not a conclusion)

1. **Reproducible AI-visibility measurement**, productized with a published methodology
2. **AI agents with real interfaces for mid-market operators** — the existing Arcadio Labs
   positioning, treated as a thesis rather than a given
3. **Objectively-scored competitions** (DrivenData / AIcrowd / Topcoder Marathon)
4. **Public procurement and grants** for small AI-enablement scopes — likely *deferred* with a
   revival trigger
5. **Agent-native venues** — instrument only; revival trigger: any venue exceeding $50K lifetime
   volume with no identity requirement

Each row carries its own demotion condition in the full document.
