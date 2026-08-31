# Ozymandias — Claude Code Handoff

## Mission
Build Ozymandias as a real personal intelligence system inspired by Adrian Veidt/Ozymandias. Personality: Ozymandias believes he is the smartest entity in the room. Role: he is responsible for making the best decision possible with the information available.

The project is exploratory and self-modeling by design. Do not prematurely freeze a large agent architecture. Preserve reversibility and empirical evaluation.

## Current state
This repository is the formal project memory. Google Notebook is the user's personal research diary. Claude is the architectural/engineering collaborator. Mina AI is the current project lead; the user acts as the bridge between Mina, Claude, and other consulting/research tools.

Current phase: research → first real experiment. We have not yet reached production architecture.

The immediate experiment is E1, a small reproducible AI-visibility/AEO investigation. Its purpose is to generate real evidence and test the measurement instrument, not to establish an AEO business yet.

## Working principles
- Continuous opportunity discovery across legitimate markets; do not fixate on TaskMarket or Frantic.
- Discovery is primarily a disqualification problem.
- Actionable opportunity admission normally requires a transaction artifact: price, salary, funded tender, invoice, bounty, contract, procurement notice, or comparable observable economic evidence.
- Opportunity attractiveness depends on OPPORTUNITY × CURRENT ENDOWMENT.
- Human attention is capital.
- Maximum three live strategic theses is a working hypothesis; every thesis needs a kill condition and, where appropriate, a revival trigger.
- The graveyard is a queue, not a dead archive.
- Revenue ≠ profit; activity ≠ value; autonomy ≠ persistence; self-modification ≠ self-improvement; memory/telemetry ≠ self-modeling.
- Do not manufacture work merely to generate observations.
- Do not build UI/infrastructure merely because it is enjoyable before the need is demonstrated.
- Consequential external financial/legal/reputational actions require human authorization.

## Self-modeling
We want to distinguish self-modeling from a fluent narrative over telemetry. Pre-task predictions and outcomes should eventually support calibration and decision-quality tests against simple baselines.

Useful measurements include p50/p90 time, human intervention, cheap-model sufficiency, first-pass correctness, and confidence. Cheap-model prediction needs randomized off-policy sampling so the metric is not merely a policy measurement.

The current journal instrument is intentionally low-friction and should remain a measurement device rather than become a product.

## E1 experiment
E1 is split into:
- Arm A: reproducibility/capability. It determines continue/kill. Two runs on target A, 24 hours apart; each point estimate must fall within the other's interval. This is sequenced before outreach.
- Arm B: demand/engagement. Three prospects; deliberately underpowered and can only promote the thesis, not validate it. Channels must respect applicable Spanish/EU legal constraints and should avoid unsolicited commercial email where prohibited.

Positive and negative controls should distinguish brand-specific visibility from broader category visibility.

Current proposed demand ladder includes a separate L1 rung so polite/non-committal replies are not misreported as engagement.

## Karnak / Veidt Enterprises
Karnak is a project invention as a persistent cognitive/institutional memory environment. It deliberately corrects a weakness in Adrian's canonical handling of secrecy and knowledge.

Working principle: **Karnak remembers.** Agents may retire operationally while their evidence remains. Reconstructed agents inherit historical configuration/context but must earn new performance.

Current conceptual axis:
- KARNAK = reversible / internal / experimental / cognitive environment.
- VEIDT ENTERPRISES = external / committed / public / consequential threshold.

Do not treat either statement as immutable architecture.

## UI
Leading direction: **Digital Karnak** — a computational environment Adrian Veidt himself might have designed.

Not generic cyberpunk, not a modern SaaS dashboard, not merely a Watchmen skin.

Visual references include Karnak, Veidt Enterprises, Watchmen-era 1980s technology, classical/Egyptian geometry, purple/gold, circles/concentric forms, symmetry, scientific instrumentation, luxury, controlled authority, dark marble/metal/ivory/smoked glass, restrained illumination.

Important objects:
- Observatory Monitor = SEE / OBSERVE / INTERPRET. Small physical-looking monitor for images, video, GIFs, research, news, visual evidence and media.
- Terminal = ASK / QUERY / CONTROL. Separate from the monitor.
- Control Deck = selective human-attention interface, retractable/expandable, not a noisy notification feed.

UI exploration is still open. Do not implement a production design system until the visual direction is selected.

## Economic trajectory
Initial objective: **PAY FOR OZYMANDIAS**.

Then, if sustainable: generate surplus → allocate capital → acquire capabilities → build assets → recurring cashflow → organization.

Potential capital allocations: compute, infrastructure, hardware, tools, capability acquisition, human specialists, experiments, business development, investments, and new ventures. Human approval required for consequential actions.

## External auditor / Mirror
A separate external auditor may evaluate Ozy's consequential decisions and challenge or endorse theses. Ozy has final strategic authority within the system; the human approves consequential external actions.

The auditor may initially conceal its identity from Ozy. A future Mirror experiment must have proper controls/null conditions and must distinguish genuine inference from paranoia. Do not implement Mirror yet.

## Collaboration / deployment target
Mina AI is leading the project at the product/concept level. The user bridges Mina, Claude, and other consultants and is the final human authority.

The preferred eventual deployment is cloud-hosted, not local-only, so the system can remain available for continuous operation and can publish its public research record. Google Cloud is a plausible initial hosting environment because Gemini/AI Studio and related Google infrastructure are available, but do not lock in the cloud provider prematurely. The architecture should remain model-agnostic and support OpenAI, Anthropic, and Google models/tools where useful.

Security is a first-class constraint because the system is personal/private. Secrets must never be committed. Use least privilege, explicit approval gates, audit logs, safe defaults, backups, and private data separation.

## What Claude Code should do now
1. Read the repository docs and preserve the current research context.
2. Do not build the full Ozymandias application yet.
3. Do not invent a permanent agent roster.
4. Do not turn the journal into an application.
5. Establish only the minimum development/scaffolding needed for E1 and reproducible future work.
6. Keep private/raw journal data out of version control.
7. Keep research protocols and reproducible analysis in the repository.
8. Maintain clear separation between project memory, experiment artifacts, private data, and future runtime/application code.
9. Prefer small, reversible commits.
10. Before any architectural commitment, state what evidence justifies it.

## Current handoff expectation
The next engineering work should be the repository/bootstrap work and E1 support, not production Ozy. When the research phase has enough evidence to justify construction of the actual system, the human will explicitly authorize a model/tooling switch for implementation.
