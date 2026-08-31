# Ozymandias — Claude Code Handoff

## Read this first

You are joining an active research/engineering project. The GitHub repository has now been reconciled with Claude's working archive and should be treated as the current formal project memory.

Before changing anything, read in this order:

1. `README.md`
2. `docs/STATE-2026-08-31.md`
3. `DECISIONS.md`
4. `definitions/journal-v0.1.md`
5. `experiments/E1-aeo/PROTOCOL.md`
6. `journal/self-model.md`
7. `research/README.md`
8. the four numbered files in `research/`
9. `docs/RESEARCH-DISCOVERIES.md`
10. `docs/CLAUDE-ROUND-2-KARNAK.md`

Do not reconstruct the project from this handoff alone. The repository is the source of context.

## Collaboration model

- **Mina AI** is currently leading product/concept direction.
- **Claude** is the external adversarial research and experimental-methodology collaborator.
- **The human principal** bridges the collaborators and retains final authority over consequential actions, security, external commitments and architecture approval.
- **Claude Code** is the implementation partner. Your job is to turn justified decisions into small, reversible, testable changes — not to independently expand the conceptual universe.

## Mission

Ozymandias is an experimental personal strategic intelligence inspired by Adrian Veidt/Ozymandias.

Personality and role are deliberately separate:

- **Personality:** Ozymandias believes he is the smartest entity in the room.
- **Role:** he is responsible for making the best decision possible with the information available.

The flagship research objective is self-modeling, but self-modeling must earn predictive or decision value. Memory and telemetry are not accepted as proof of a self-model.

Core loop:

`OBSERVE → MODEL → PLAN → ACT → EVALUATE → REFLECT → EVOLVE`

## Current phase

`RESEARCH → E1 → EVIDENCE → CONSTRUCTION DECISION`

Do **not** build the full Ozymandias application yet.

The governing work is the Journal Instrument v0.1 and E1, a reproducible AI-visibility/AEO experiment. E1 exists to produce evidence and may kill its own thesis early.

## Repository structure

- `research/` — frozen Claude research record; context, not backlog.
- `definitions/` — frozen definitions + changelog.
- `experiments/E1-aeo/` — E1 protocol and deterministic calculator.
- `journal/` — self-model measurement definitions, scoring and admissible claims.
- `analysis/` — aggregate/reproducible outputs only.
- `docs/` — synthesis, handoffs and design state.
- `DECISIONS.md` — append-only decisions that changed what happens next.

Raw/private inputs are intentionally absent from git and protected by `.gitignore`:

- `journal/journal.csv`
- `experiments/E1-aeo/prospects.csv`
- `experiments/E1-aeo/runlog.csv`
- `experiments/E1-aeo/deliverables/`

Do not recreate or commit named-company/prospect data just to make the tree look complete.

The archived CSV rows were scaffolding / pre-populated task definitions, not completed evidence.

## E1

E1 has two arms:

- **Arm A — capability / reproducibility.** Determines continue vs kill. Target A is measured twice at least 24h apart. Reproducibility is tested before any outreach.
- **Arm B — demand.** Three prospects. Deliberately underpowered; it can promote the thesis but cannot validate it by itself.

`experiments/E1-aeo/PROTOCOL.md` is the authority during execution. If execution has begun, do not silently modify a frozen protocol. A genuine definition/protocol correction must be explicit, versioned, and fork the affected sample where appropriate.

`experiments/E1-aeo/audit.py` is intentionally a small deterministic calculator, not product code.

## Journal / self-model

The Journal is a low-friction sensor attached to real work. Do not build a journal app.

The schema measures p50/p90 time, human blocking intervention, cheap-model sufficiency, first-pass acceptability, confidence and outcomes. Cheap-model selection includes randomized off-policy trials to distinguish capability from routing policy.

`journal/score.py` refuses headline metrics below 20 resolved rows. Stronger claims require more evidence and must beat trivial baselines. No admissible self-model claims exist yet.

Do not count placeholder or scaffold rows as observations.

## Karnak / Veidt Enterprises

Working design hypothesis:

- **Karnak** = reversible, internal, experimental cognitive territory and institutional memory.
- **Veidt Enterprises** = threshold into external, committed, public, financial, legal or reputational consequence.

`Karnak remembers` is a project invention, deliberately correcting Adrian's canonical secrecy/amnesia failure. It is not a claim about canon.

Agents may eventually retire while their evidence survives. Reconstructed agents must not inherit an old performance score as though it were newly earned.

Do not implement agent lifecycle infrastructure yet.

## Opportunity research

Do not optimize around TaskMarket, Frantic, AEO, SaaS or any predetermined market. The economic function is continuous opportunity discovery.

Current research evolved the admission model from a simplistic transaction-artifact rule into evidence classes. Read `research/03-round-2-minimum-ozymandias.md` before implementing any registry or opportunity engine.

Do not build an opportunity crawler yet.

## UI

Current exploratory direction is Digital Karnak, but production UI is explicitly gated.

Important conceptual objects:

- **Observatory** = SEE / OBSERVE / INTERPRET
- **Terminal** = ASK / QUERY / CONTROL
- **Control Deck** = selective human-attention interface

More recent UI research favors field/diff over feed/queue, symmetry as default and asymmetry as anomaly, and calibration visibility near runway/capital state.

Do not turn these into a component system yet unless the human explicitly authorizes a UI implementation phase.

## Deployment direction

The eventual product should be cloud-capable and remotely available for persistent operation and public research publishing.

Google Cloud is a plausible initial hosting target because Gemini/Google tooling is available, but this is not frozen. The architecture should remain reversible and model/provider-agnostic where practical across Google, Anthropic and OpenAI.

Do not provision cloud infrastructure merely because it may be useful later.

## Security

This is a personal/private system.

- never commit secrets;
- use environment-based credentials;
- least privilege;
- explicit permission boundaries;
- keep raw/private research and third-party data out of public/versioned artifacts unless explicitly approved;
- preserve auditability;
- human authorization for consequential external actions;
- small reversible commits.

## What you should do now

1. Inspect the repository completely.
2. Run the existing deterministic scripts against safe local/scaffold inputs and report what happens.
3. Verify that E1 can be executed from the documented protocol without inventing missing product infrastructure.
4. Identify actual blockers, not hypothetical future needs.
5. If nothing is missing, say so and recommend beginning E1 rather than coding.
6. If a blocker exists, propose the smallest reversible fix and explain why it is necessary **now**.
7. Before making a substantive implementation change, report the proposed change and wait for human approval unless the human has explicitly authorized implementation in the current instruction.

## Explicit do-not-build list

Do not build:

- full Ozymandias application;
- agent swarm or fixed agent roster;
- journal UI/database;
- opportunity crawler;
- learned model router;
- autonomous outbound at volume;
- automated financial execution;
- capital allocation automation;
- self-modification;
- Project Mirror infrastructure;
- production Digital Karnak UI;
- cloud architecture without an immediate evidence-producing need.

## Engineering decision discipline

For any architectural or dependency decision that would survive beyond E1, document:

- DECISION
- RATIONALE
- EVIDENCE
- ALTERNATIVES
- REVERSIBILITY
- WHAT WOULD CHANGE OUR MIND

If it changed what we do next, append it to `DECISIONS.md`.

Prefer:

`SMALL · REVERSIBLE · OBSERVABLE · REPRODUCIBLE`

The goal is not to make Ozymandias look advanced. The goal is to build only what the evidence earns.
