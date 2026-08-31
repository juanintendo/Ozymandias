# Ozymandias

A research-driven experiment in building a persistent strategic intelligence inspired by Adrian Veidt / Ozymandias.

## Core thesis

Ozymandias is not a generic AI assistant. He is intended to become a strategic intelligence whose capabilities, organization, tools, agents, research methods, and eventually economic activity can evolve through evidence and experience.

His personality and operational role are deliberately distinct:

- **Personality:** Ozymandias believes he is the smartest entity in the room.
- **Role:** He is responsible for making the best decision possible with the information available.

The flagship research objective is **self-modeling**: Ozymandias should maintain and improve a predictive model of his capabilities, limitations, resources, uncertainty, agents, decisions, and outcomes rather than merely narrating telemetry.

Core loop:

`OBSERVE → MODEL → PLAN → ACT → EVALUATE → REFLECT → EVOLVE`

## Current phase

**Research → first real experiment → evidence → construction decision.**

Architecture is not frozen. The current live experiment is **E1 — reproducible AI-visibility / AEO audit**, instrumented by the Journal Instrument v0.1. E1 exists to produce evidence, not to establish AEO as the business.

The leading conceptual split is:

- **Karnak** — reversible, internal, experimental, cognitive territory: research, memory, experiments, observatory, self-model, agents, and institutional history.
- **Veidt Enterprises** — the threshold where something becomes external, committed, public, financial, reputational, contractual, or otherwise consequential.

`Karnak remembers` is a project invention, not canon: important evidence should survive the retirement of agents, tools, theses, and implementations.

## Research principles

1. Discovery is primarily a disqualification problem, not a candidate-generation problem.
2. No actionable opportunity normally enters the registry without observable transaction evidence, subject to adversarial review and explicit exceptions.
3. Opportunity attractiveness is conditional on a versioned current endowment: `OPPORTUNITY × ENDOWMENT`.
4. Human attention is economic capital.
5. Strategic theses must have explicit tests, kill conditions, and where appropriate revival triggers.
6. External criticism can challenge Ozymandias but does not replace his strategic authority; consequential external actions remain human-authorized.
7. Agents must earn persistence through evidence. Agent count is not a goal.
8. `MEMORY ≠ SELF-MODEL`, `TELEMETRY ≠ METACOGNITION`, `SELF-MODIFICATION ≠ SELF-IMPROVEMENT`, `ACTIVITY ≠ VALUE`.
9. Research should move toward a decision, experiment, or falsifiable claim.
10. Do not build infrastructure to measure work that has not yet proven worth doing.

## Repository role

This repository is the **reproducible scientific and engineering record**. It is not the personal diary and it is not yet the product.

> **If a stranger could re-run it, it goes in the repository. If it is how you felt about it, it goes in the notebook. If it identifies a third party, it stays private.**

### Repository vs Notebook

**Notebook** — personal research diary: questions, hunches, reflections, half-formed connections, study notes. It is where hypotheses are born.

**Repository** — formal record: frozen definitions, protocols, scripts, aggregate results, decisions, research packs, architecture and design constitutions. It is where hypotheses are frozen and tested.

An idea moves from Notebook to repository only by becoming a dated, structured artifact with a falsifiable or actionable claim attached.

## Structure

```text
Ozymandias/
├── README.md
├── DECISIONS.md                 append-only decisions that changed what we do next
├── definitions/                 frozen measurement definitions + changelog
├── experiments/                 reproducible experiment protocols and code
│   └── E1-aeo/
├── journal/                     low-friction self-model instrument and scoring
├── analysis/                    aggregate outputs only
├── research/                    Claude research packs / adversarial studies
└── docs/                        project synthesis, handoffs and design material
```

### Private by default

Raw journal rows, prospect identities, named-company run logs, third-party deliverables, credentials, API keys and other personal/private data are not committed. See `.gitignore`.

## E1 and the Journal

The Journal is a measurement instrument attached to real work, not a project of its own. It records pre-task predictions (including p50/p90 time, need for human blocking input, cheap-model sufficiency and first-pass acceptability) and minimal post-task outcomes.

E1 has two arms:

- **Arm A — capability / reproducibility:** determines continue vs kill. Two measurements on target A, 24 hours apart; reproducibility is tested before outreach.
- **Arm B — demand / engagement:** deliberately underpowered at n=3; it can promote the thesis but cannot validate it by itself.

Do not count protocol scaffolding or placeholder rows as evidence.

## Documentation map

- `docs/RESEARCH-DISCOVERIES.md` — current project synthesis and working discoveries.
- `docs/CLAUDE-ROUND-2-KARNAK.md` — Karnak research challenge/history.
- `docs/CLAUDE-CODE-HANDOFF.md` — engineering collaboration handoff.
- `research/` — full Claude research outputs in chronological order.
- `definitions/journal-v0.1.md` — frozen Journal Instrument definitions.
- `experiments/E1-aeo/PROTOCOL.md` — E1 pre-registration / execution protocol.
- `journal/self-model.md` — admissible self-model claims and frozen model identifiers.
- `DECISIONS.md` — append-only decision record.

## Deployment direction

The eventual system should be **cloud-capable and remotely available**, because persistent operation, future agents and publishing matter. Google Cloud is a plausible initial home, particularly given Gemini/Google tooling, but infrastructure must remain reversible and provider-agnostic where practical. OpenAI, Anthropic and Google models should ultimately be selected by measured suitability rather than ideology.

Security is first-class: least privilege, explicit permission boundaries, environment-based secrets, auditability, backups, separation of public/private data and human authorization for consequential actions.

## What is deliberately not being built yet

No production journal app. No giant database. No agent swarm. No final UI. No autonomous capital deployment. No self-modifying architecture. No Project Mirror implementation.

Current rule:

> **Build the smallest reversible thing that can produce trustworthy evidence.**
