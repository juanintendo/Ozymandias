# Claude Code Handoff Addendum — Cognitive Economy

**Date:** 2026-08-31
**Status:** Working architecture decision; E1.1 must reconcile this before freeze.

## New material fact

The project's actual endowment includes persistent local Ollama inference already operating in Mina's House. Current House configuration includes local Qwen-based workloads, including a Qwen 8B abliterated profile used for scheduled autonomy. This means local inference is an available resource, not a hypothetical future capability.

## Economic rule

Ozymandias must not run at a negative resource balance.

Tokens, local compute, money and human attention are resources. An available subscription/quota is capacity, not a spending target.

Working rule:

> Ozy must never spend a resource without sufficient expected information, capability, or economic return to justify its cost.

## Initial model hierarchy

1. **Local Ollama — default/cheap layer.** Use existing local models whenever capability is sufficient. Local is not literally free: compute, electricity, latency and opportunity cost remain resources.
2. **OpenAI / Google — operational frontier.** Escalate when local capability is insufficient and expected value justifies the external resource cost. Prefer these operationally because they have broad capabilities/plans available to the project.
3. **Claude — strategic reserve.** Preferentially reserve for deep self-modeling, architecture review, adversarial analysis and system evolution. Claude remains budgeted; it is not unlimited.

Do not burn a plan/quota merely because capacity exists.

## Scheduled autonomy / crons

A cron must not imply an LLM call.

Preferred eventual flow:

`SCHEDULE → CHANGE DETECTION → RESOURCE GATE → LOCAL → OPENAI/GOOGLE IF JUSTIFIED → CLAUDE ONLY WHEN STRATEGIC DEPTH WARRANTS IT`

Most scheduled cycles should terminate before frontier inference when deterministic checks establish that nothing changed.

The scheduler/resource governor should eventually account for both monetary API budgets and local compute availability.

## Local upgrades

Ozymandias may eventually reinvest generated resources into better local compute/model capability.

Conceptual loop:

`VALUE CREATION → RESOURCE RESERVE → CAPABILITY UPGRADE → GREATER CAPACITY → VALUE CREATION`

An upgrade requires sufficient expected capability/productivity gain relative to total cost. The existence of a better model is not itself a justification.

## Self-model

The self-model is persistent evidence about system behavior, not the identity of a particular model.

Local workers, OpenAI, Google and Claude can all generate observations. A stronger model may periodically interpret them. The resulting self-model persists independently and can be consumed by future workers.

## Cloud/local deployment direction

Eventual architecture is hybrid:

- **Google Cloud:** persistent Ozymandias control plane, state, memory, self-model, scheduler, resource governance, authenticated console and public website/publishing.
- **Local machine:** private/cheap Ollama compute.
- **OpenAI/Google APIs:** paid frontier escalation.
- **Claude:** strategic external reasoning reserve.

Google Cloud is preferred but not frozen.

Do not expose Ollama directly to the public Internet. A secure authenticated bridge can be designed only when an actual workload requires it.

## E1 consequence

This changes the real endowment before E1.1 freeze.

Do not silently preserve an API-only Cheap condition.

The three-provider audit arm remains separate from the Cheap/Frontier self-model axis.

Before freezing E1.1, reconcile the protocol with local Ollama and document the final definition explicitly. If the protocol must change, version the change rather than editing silently.

## Current implementation status

Nothing in this addendum authorizes construction of the full Ozymandias application, cloud infrastructure, model router, cron system, agent ecology or financial automation.

The immediate engineering posture remains:

**If E1 can run without new infrastructure, do not code.**
