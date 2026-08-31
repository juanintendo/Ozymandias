# Ozymandias — Cognitive Economy v0.1

**Status:** Working architecture decision, pre-construction.
**Date:** 2026-08-31

## Principle

Ozymandias must not run at a negative resource balance. Tokens, local compute, money, and human attention are all resources. Availability is not justification for consumption.

> **Ozy must never spend a resource without sufficient expected information, capability, or economic return to justify its cost.**

A subscription or available quota is capacity, not a spending target.

## Compute hierarchy

### 1. Local compute — default

Ozymandias should prefer existing local Ollama capacity for work that is sufficiently capable there.

Current local capability includes the Ollama models already deployed in Mina's House. Exact model inventory remains an operational input and should be discovered rather than duplicated here.

Local compute is not treated as literally free: CPU/GPU capacity, electricity, latency, thermal limits, and opportunity cost remain resources.

### 2. OpenAI / Google — operational frontier

When local capability is insufficient, Ozymandias may escalate to OpenAI or Google/Gemini, subject to task suitability, available plan/quota, cost, and resource budget.

The system must not consume an available plan merely because capacity exists.

### 3. Claude — strategic reserve

Claude is initially reserved preferentially for deep self-modeling, architecture review, adversarial analysis, and system evolution.

Claude is still budgeted. It is not an unlimited exception.

## Routing principle

Initial routing should be conservative and observable:

`SCHEDULE → CHANGE DETECTION → RESOURCE GATE → LOCAL → OPENAI/GOOGLE IF JUSTIFIED → CLAUDE ONLY WHEN STRATEGIC DEPTH WARRANTS IT`

Most scheduled cycles should terminate before frontier inference when deterministic change detection can establish that nothing requires attention.

No cron should directly assume that an LLM call is necessary.

## Upgrade economy

Local model capacity is itself an asset that Ozymandias may improve when economically justified.

Potential future loop:

`VALUE CREATION → RESOURCE RESERVE → CAPABILITY UPGRADE → GREATER CAPACITY → VALUE CREATION`

An upgrade should be considered only when expected capability/productivity gain justifies its total cost and the upgrade can be responsibly funded from available resources or explicitly authorized capital.

The existence of a better model does not constitute an upgrade case.

## Self-model relationship

The self-model is persistent evidence about system behavior; it is not synonymous with whichever model happens to perform a self-modeling pass.

Workers and models produce observations. Periodic analysis may use a stronger model when justified. The resulting self-model remains persistent state that can be consumed by future workers.

This allows Ozymandias to run local models without making local inference itself the definition of identity or self-modeling.

## Cloud / local split

The eventual deployment target is hybrid:

- **Google Cloud:** persistent Ozymandias control plane, state, memory, self-model, scheduler, resource governance, authenticated console, and public website/publishing layer.
- **Local machine:** cheap/private Ollama inference and other local compute.
- **OpenAI / Google APIs:** paid frontier capacity when justified.
- **Claude:** strategically reserved external reasoning for architecture/self-modeling.

Google Cloud is a preferred candidate, not an irreversible infrastructure commitment.

Local Ollama must not be exposed directly to the public Internet. A secure authenticated bridge may be designed later when an actual cloud-to-local workload requires it.

## Consequence for E1

The discovery of persistent local Ollama capacity is a material change to the project's real endowment. Before E1.1 is frozen, the Cheap/Frontier definition must be reconciled with the E1 protocol rather than silently preserving an obsolete assumption.

The three-provider audit arm remains conceptually separate from the Cheap/Frontier self-model axis.
