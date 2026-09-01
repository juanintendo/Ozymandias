# Ozymandias / Veidt Enterprises — Architecture Thesis v0.1

**Date:** 2026-09-01  
**Status:** Architecture thesis / research synthesis. **Not implementation. Not frozen.**  
**Purpose:** Consolidate the architectural implications of the Ozymandias research and the Perplexity Portable Computer precedent before construction begins.

---

## 0. The central distinction

Ozymandias is not the agent that performs every task.

Veidt Enterprises is not the entity that decides which work deserves to exist.

The intended division is:

> **Ozymandias decides. Veidt Enterprises executes. Karnak remembers.**

The system is therefore not primarily a chatbot, an agent swarm, or a larger model. It is a decision-and-execution organism in which models are replaceable capabilities inside a governed runtime.

---

## 1. Ozymandias — the decision layer

Ozymandias is responsible for decisions whose consequences extend beyond the execution of one task.

### Responsibilities

- opportunity discovery;
- thesis formation;
- economic evaluation;
- task admission and **DECLINE** decisions;
- resource and budget governance;
- capital allocation when Ozymandias eventually owns capital;
- self-modeling and calibration;
- deciding when external capacity is worth requesting;
- deciding whether an auditor's critique should change its course;
- deciding whether an investment or capability upgrade is justified.

### Non-responsibilities

Ozymandias should not directly become the default tool executor merely because it can reason about execution. Its strategic role must remain distinguishable from the operational organization that carries out admitted work.

The highest-value decision may be **not to execute**.

---

## 2. Veidt Enterprises — the execution layer

Veidt Enterprises is the operational organization created by Ozymandias' decisions.

It should be able to turn an admitted decision into real work: research, coding, document production, web work, data processing, deployment, monitoring, and eventually commercial operations.

The important conceptual point is:

> **Veidt Enterprises is a computer that can perform work under the direction of an entity that decides what work deserves to be developed.**

It is not merely an interface around a model. It is the execution environment, harness, tools, skills, task state, and eventually specialized agents that make owned intelligence useful.

---

## 3. The Work Order — the contract between the layers

The boundary between Ozymandias and Veidt Enterprises should be an explicit artifact: a **Work Order**.

A Work Order should eventually contain at least:

```text
id
thesis / reason for doing the work
objective
expected value
budget / authorized resources
success condition
kill condition
reversibility
human-attention budget
deadline
evidence required
authorized actions
prohibited actions
```

The conceptual lifecycle is:

```text
world
  ↓
signal
  ↓
opportunity
  ↓
thesis
  ↓
admit / decline
  ↓
WORK ORDER
  ↓
VEIDT ENTERPRISES
  ↓
result / artifact / money / failure
  ↓
evidence
  ↓
KARNAK
  ↓
self-model / strategy
  ↓
OZYMANDIAS
```

A Work Order is therefore **budgeted and falsifiable**, not merely a task description.

---

## 4. Deterministic orchestrator, probabilistic models

The strongest transferable lesson from the Perplexity Portable Computer research is the separation between the model and the execution authority.

The orchestrator should eventually be deterministic code responsible for:

- assembling context;
- enforcing resource policy;
- deciding which tools are available;
- loading skills on demand;
- managing checkpoints and task state;
- invoking models;
- enforcing approval boundaries;
- recording actions and outcomes.

The model proposes actions. The harness decides whether those actions are permitted and how they execute.

This is a design thesis, not yet an implementation requirement.

### Why this matters

A model should not be able to bypass resource policy merely by generating an instruction that contradicts the policy. Governance belongs in code wherever deterministic enforcement is possible.

Perplexity's current Portable Computer explicitly keeps its orchestrator, planner, tool router, scheduler, durable task queue, and local search index on-device; local work starts on-device and cloud escalation is permission-gated. citeturn0search2turn0search5

---

## 5. Local-first resource hierarchy

The current owned resource hierarchy is:

```text
Qwen 3 abliterated 8B
        ↓
Qwen 3 14B
        ↓
human-authorized external capacity
```

This is a resource hierarchy, not yet a router.

The governing economic principle is:

> **Do not spend external resources when owned capability is sufficient.**

External models may be useful, but current external OpenAI / Google / Claude capacity belongs to the human principal, not Ozymandias. It requires explicit authorization and is not Ozymandias-owned capital.

Eventually, when Ozymandias earns and retains capital, the same hierarchy can expand:

```text
owned local compute
        ↓
owned paid inference
        ↓
owned hardware / capability acquisition
        ↓
external resources where economically justified
```

The order should be determined by measured return, not prestige.

---

## 6. External advisor — intelligence without hands

A frontier or strategic advisor should not automatically receive execution authority.

Preferred pattern:

```text
local executor
      ↓
capability insufficiency
      ↓
request for strategic guidance
      ↓
external advisor
      ↓
textual guidance / critique
      ↓
local executor
      ↓
execution
```

The advisor can challenge the plan, identify blind spots, propose alternatives, or improve a strategy. The execution authority remains local.

This is especially appropriate for Claude's current role: strategic architecture, self-modeling, adversarial review, and co-research rather than routine task execution.

---

## 7. Two auditors, not one

The project has two conceptually different audit functions.

### Strategic auditor

A high-reasoning external reviewer can inspect:

- theses;
- decisions;
- opportunity quality;
- architecture;
- self-model claims;
- investment proposals.

Its output can be:

```text
support
challenge
uncertainty
recommended debate
recommended action
```

Ozymandias retains the final decision.

The auditor's identity may be concealed from Ozymandias if useful, but its existence and critique should not be concealed. The intended property is **unattributed critique**, not invisible governance.

### Execution auditor

A deterministic or narrowly scoped runtime auditor should observe:

- tool calls;
- file access;
- credential use;
- network boundaries;
- external inference requests;
- spend / quota;
- policy violations;
- destructive actions.

This auditor should not require a frontier LLM to enforce rules that can be expressed deterministically.

---

## 8. Karnak — evidence, not belief

Karnak is the organizational memory layer.

The metaphor is deliberately an invention rather than a claim about canon: canonical Karnak is associated with destruction and secrecy; our Karnak is designed to correct that failure mode.

Karnak should preserve:

```text
knowledge
raw evidence
sessions
trajectories
decisions
theses
opportunities
predictions
outcomes
failures
agent histories
economic history
self-model evidence
```

### Memory is not self-model

Karnak stores evidence.

The self-model makes predictions from that evidence.

```text
KARNAK
  ↓
historical evidence
  ↓
SELF-MODEL
  ↓
prediction
  ↓
outcome
  ↓
calibration evidence
  ↓
KARNAK
```

Ozymandias must not be allowed to rewrite its own history simply because a later narrative sounds more coherent.

---

## 9. Staged memory updates

A future memory system should treat generated memory as a proposal until verified.

Preferred pattern:

```text
new evidence
    ↓
proposed memory update
    ↓
structural / deterministic checks
    ↓
semantic evidence check
    ↓
commit or reject
```

The system should preserve enough history to determine what changed and why.

This principle is inspired by Perplexity's Brain research, which describes a structured Markdown knowledge system with traceable updates and evidence links. Perplexity separately describes Brain as a self-improving agentic memory system. These are precedents, not specifications for Ozymandias. citeturn0search0

---

## 10. Checkpoints and reversibility

Long-running work should not be represented as one irreversible trajectory whenever the underlying operation can be checkpointed.

Preferred future pattern:

```text
checkpoint
   ↓
action
   ↓
outcome
   ├── success → continue
   └── failure → recover / fork / rollback where possible
```

This extends the project's existing principle that **reversibility is a resource**.

A future Veidt runtime should make the reversible boundary explicit before expensive or destructive actions.

---

## 11. Self-improvement must produce evidence

Ozymandias should eventually be able to propose improvements to its own organization, harness, skills, prompts, agents, or resource policy.

The adoption rule should be empirical:

```text
propose change
      ↓
fork / candidate
      ↓
evaluate
      ↓
better evidence?
   ├── no → archive
   └── yes → candidate promotion
```

A model saying "this architecture is better" is not sufficient evidence for changing the architecture.

Historical variants should remain available so that failed branches become evidence rather than disappearing.

---

## 12. Agents are capabilities, not the organization

Multi-agent architecture should not be the default.

Start with:

```text
one executor
+ skills
+ tools
+ memory
+ evaluation
```

Specialized agents should emerge only when repeated work demonstrates a capability boundary that justifies specialization.

An agent can therefore be:

- proposed;
- evaluated;
- promoted;
- demoted;
- retired;
- reconstructed from configuration without falsifying its historical performance.

Retirement should preserve the evidence produced by the agent even when the agent itself is destroyed.

---

## 13. Economic lifecycle

The architecture must work while Ozymandias owns €0 and still make sense when it eventually owns capital.

### Stage 0 — €0 owned capital

```text
local compute
  ↓
human-authorized external capacity
```

No available quota is automatically Ozymandias' budget.

### Stage 1 — revenue

```text
revenue
  ↓
operating costs
  ↓
reserve
```

The first objective is to make the organization self-sustaining.

### Stage 2 — surplus

```text
surplus
  ↓
Ozymandias proposes investment
  ↓
external strategic audit
  ↓
human authorization
  ↓
investment
  ↓
return / loss
  ↓
Karnak
```

### Stage 3 — owned capital

Eventually, Ozymandias may allocate its own earned capital to:

- inference;
- hardware;
- software;
- infrastructure;
- new capabilities;
- experiments;
- other investments.

The requirement remains the same: **capital allocation is a decision backed by a thesis, budget, expected return, reversibility, and evidence.**

---

## 14. The admission layer is the real product boundary

Portable Computer begins after a task already exists. Ozymandias must operate one layer above that.

```text
world
 ↓
signals
 ↓
opportunities
 ↓
evaluation
 ↓
admit / decline
 ↓
work order
```

This is why Ozymandias is not simply a local version of another agent product.

Portable Computer asks:

> How can an agent execute this work efficiently and safely?

Ozymandias asks:

> **Does this deserve to be executed, with whose resources, and how will we know whether it worked?**

Veidt Enterprises is the answer to the first question.

Ozymandias is responsible for the second.

---

## 15. Research precedent: what we are borrowing

The Perplexity precedent validates several architectural ideas relevant to Ozymandias:

- local-first execution;
- deterministic orchestration around probabilistic models;
- on-demand skills rather than permanent context/tool sprawl;
- local task state and durable queues;
- permission-gated cloud escalation;
- isolated tool/code execution;
- self-verification hooks;
- structured, traceable agent memory;
- staged memory evolution;
- external advisor separation from execution authority.

Perplexity's public launch explicitly describes the local orchestrator, planner, tool router, scheduler, durable task queue, local search index, local models, and permission-gated cloud escalation. citeturn0search2

Perplexity's research blog index also identifies Brain, SPACE, and Numbat as separate components for agentic memory, secure long-running runtimes, and endpoint security. citeturn0search0

### What we are not copying

We are not copying:

- the DGX Spark hardware requirement;
- the 27B model requirement;
- Perplexity's proprietary post-training;
- subscription economics;
- its product UI;
- its exact routing implementation;
- any unverified internal mechanism.

The project should steal **principles and harness patterns**, not pretend we have access to proprietary implementation details.

---

## 16. What this thesis does NOT authorize yet

This document is architecture research. It does **not** authorize implementation of:

- a router;
- autonomous finance;
- automatic investment;
- a multi-agent swarm;
- a custom sandbox platform;
- a cloud production environment;
- a hardware purchase;
- a model upgrade;
- autonomous external API spending;
- autonomous modification of the governing experiment.

Those require separate decisions and evidence.

E1 remains an independent experimental instrument. Its results can force architectural changes; architectural enthusiasm must not silently rewrite E1.

---

## 17. Open architectural questions

Before construction, the project still needs evidence or explicit decisions on:

1. How much harness improvement transfers from larger local models to the current 8B/14B endowment?
2. What exact signals should cause a step-level escalation request?
3. How should a Work Order represent budgets and permissions at step level?
4. How should external authorization be represented and audited?
5. What minimum Karnak structure gives useful memory without creating a second self-narrative machine?
6. How should strategic and execution auditors communicate without becoming hidden governance?
7. How should Ozymandias price its own compute, human attention, and external resources while capital is €0?
8. When does a repeated capability gap justify a specialized agent?
9. What evidence is sufficient to promote a self-improvement candidate?
10. Which parts of the architecture should live in Google Cloud versus remain local?

These are **research questions, not implementation tickets**.

---

## 18. Architectural thesis

The current thesis can be stated in one sentence:

> **Ozymandias is a strategic decision organism that admits and budgets work; Veidt Enterprises is its local-first execution organization; Karnak is the evidence-preserving memory; and the harness, not the model alone, is the unit of operational intelligence.**

The intended loop is:

```text
DECISION
   ↓
WORK ORDER
   ↓
EXECUTION
   ↓
EVIDENCE
   ↓
MEMORY
   ↓
SELF-MODEL
   ↓
BETTER DECISION
```

That is the architecture Claude should attack before we build it.
