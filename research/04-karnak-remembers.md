# OZYMANDIAS — Karnak Remembers (Round 2 continued)

Full document: https://claude.ai/code/artifact/eaba1441-4742-48e4-91ed-9d56dfa5bc3a
Prepared 31 August 2026. Covers: character model, continuity matrix, Karnak, organizational memory,
agent lifecycle, opportunity engine additions, self-model additions, auditor concealment, capital,
attention filtering, UI direction, the Karnak/VE split, architecture, counterarguments, experiments,
20 questions answered.

Provenance tags used throughout: SOURCE / FINDING / INFERENCE / DESIGN HYPOTHESIS / INVENTION.

## THE CENTRAL FINDING

**"Karnak remembers" is not canon. It is precisely inverted canon.**
SOURCE: Karnak is where Adrian tells three Vietnamese servants the truth about himself and then
**poisons all three**; where he opens the vivarium dome to Antarctic air, killing everything inside;
downstream of killing the island artists/writers/scientists by bomb. Karnak is the machine by which
knowledge stops existing anywhere except inside Adrian's head. **Karnak forgets, deliberately, as
policy** — and that memory policy is the direct cause of his central defect: a plan nobody could
audit, never falsifiable, executed once.

**Adopt the principle anyway — as an INVENTION that corrects the character**, exactly like
"reversibility is a resource" in Round 1. Calling it canon would be the failure.

**The referent validates what the fiction contradicts.** FINDING: the real Karnak was built across
~1,300 years by successive rulers who *added rather than replaced* (Amenhotep I's barque shrine,
Thutmose I's enclosure walls, Thutmose III's Akh-menu extending the temple ~50%). Veidt named his
retreat after the most accretive structure in the ancient world and ran it as an incinerator.
**The Hatshepsut clause:** FINDING — Thutmose III walled off Hatshepsut's obelisks to hide them.
Even at Karnak, what is forgotten is a political act. Therefore: **every deletion writes a
tombstone** (what class, when, under which rule, by whom).

## AGENT LIFECYCLE — canon supplies the ANTI-pattern

SOURCE (HBO): Mr Phillips and Ms Crookshanks are manufactured clones, harvested as fetuses from a
lake, used, destroyed in batches, replaced with fresh identical copies that know nothing. **A
stateless disposable worker pool with zero knowledge transfer** — the canonical Veidt approach to
personnel, and exactly what an organisation meant to learn must avoid. He pays total institutional
amnesia continuously and never notices because his servants only ever do the same task.

**Principle: the cost of retiring an agent is not the replacement — it is the loss of everything it
learned.** Invisible unless the learning was stored outside the agent.

**What survives retirement: not the agent, its evidence** — predictions, errors, calibration curve.
An agent leaving behind completed tasks contributed nothing; one leaving a calibration history
contributed permanently.

**Reconstruction:** the *configuration* reconstructs trivially (it's a file); the *performance
record* never does. A reconstructed agent resumes at `claimed`, never `demonstrated` — otherwise
**resurrection laundering**: retire an underperformer, rebuild it, bad record evaporates. This is
the single exploitable path in the design and must be closed by rule. Agents use the same graveyard
+ revival-trigger mechanism as theses — one mechanism, two populations.

**Should Ozy know archived agents existed? Yes** — an unremembered retirement is a repeatable
failure. It sees what and why and the evidence, *not* the retired agent's reasoning prose.

## MEMORY: what to remember / forget

REMEMBER (permanent, uncompressed): every prediction + resolution · every kill + reason · every
buyer rejection verbatim · every endowment version + diff · every discovered constraint.

FORGET: outputs compressed to a reference/hash · **its own reasoning prose once the prediction
resolves** (counterintuitive, and the key one — a growing archive of the system's own rationales
becomes a corpus it can pattern-match to generate more plausible-sounding rationales, i.e. the
self-narrative failure mode with a training set; keep prediction, outcome, and the rationale
compressed to its single falsifiable claim) · third-party personal data beyond the minimum ·
all on a schedule set at write time, never on request.

## CHARACTER — the self-made man, and its dangerous import

SOURCE: he renounces the inheritance explicitly so what follows is unambiguously his.
INFERENCE: **he treats his own success as evidence for his method** — one life, no control
condition, no accounting for timing or for the education the inheritance bought before he renounced
it. **The single most dangerous import: the belief that success validates the reasoning that
produced it.** Concretely: after any success, the system must state what *else* could explain it
before it may update its policy. A field in the decision journal, not an aspiration.

Import: preparation as a first-class expense · long horizons · discipline · being uninterested in
his own past achievements. Do not import: authorship as terminal value · secrecy from stakeholders ·
comprehensiveness mistaken for correctness · people as instruments · the self-made narrative itself.

**How his intelligence fails:** it is anticipatory breadth with **no mechanism for encountering the
unanticipated**. The model is closed. Software translation: the architecture's value is not modelling
more, it is detecting that the model has broken — Round 2 §12's reframed Mirror is the most
character-faithful component precisely because Veidt lacks it.

## CONTINUITY MATRIX (weighted)

Watchmen (Moore/Gibbons) = Primary, sole authority for voice · Supplementary in-world material =
Primary and richest source on the self-made philosophy, but it is marketing copy Adrian wrote, so
read it as a source about his *persona* not his psychology · HBO = sanctioned sequel, supplies the
agent lifecycle, tonally distant · Before Watchmen = apocrypha, only concrete business origin detail ·
Doomsday Clock = heavily contested, use for failure modes only, never voice · Snyder/motion/animated =
adaptation, visual reference only · New 52/wider DC = tertiary, ignore.
**Rule: the persona layer reads Primary only.** A persona averaged across seven continuities produces
a fan-wiki composite — still the most likely aesthetic failure of this project.

## OPPORTUNITY ENGINE — what the taxonomy misses

The registry is organised by *market category*; its blind spot is anything defined by a
**relationship, a moment, or an asymmetry**: a *buyer* not a market (Circadian's 3 wins = 1
requester; needs a buyer table) · a *window* (regulation changed, competitor failed, API opened —
events, and they expire) · *cross-market arbitrage* (award-notice data is unusually good at this) ·
*being paid for the by-product* (the reproducible-measurement thesis is this shape: the calibration
machinery is required for research and saleable as product).
**Add a fifth register: ASYMMETRIES.** Artifact attaches to a party or an event, not a category.
**Also: a kill without a revival trigger is not a kill, it is a shrug** — reject it at review.

## SELF-MODEL — the pre-task prediction block (most actionable item)

Before every task, four binaries + one quantity, all resolving same-day:
`predicted_juan_minutes` · `predicted_self_sufficiency` (finish without asking?) ·
`predicted_model_adequacy` (will the cheap model do?) · `predicted_first_pass` (right first time?).
Dozens per week, all claims about the system's own boundary. **This block alone can produce enough
resolved predictions inside 90 days to run the §9 baseline comparison, which the market-outcome
track cannot do inside nine months.**
Predicting when to create/retire an agent: not yet — rarest events, longest horizon, weakest ground
truth. Year two.

## AUDITOR — you cannot have both

Critiques reaching Ozy **and** Ozy not knowing an evaluator exists are incompatible. What you can
have is **unattributed critique**: the challenge arrives as a required adversarial pass without being
labelled as external. Conceals *identity*, not *existence* — and it makes the Mirror hypothesis
clean: the observable regularity becomes the critique's *statistical signature* (timing, blind spots,
category-dependent accuracy), and correct detection means naming that structure, not noticing that
critiques exist.

## HUMAN ATTENTION — the filter is a falsifiable claim

"One matter warrants your attention" is a claim and must be testable. Every surfaced matter carries
a prediction (*this will change your decision*); every **withheld** matter is also a prediction
(*this would not have*). **Sample the withheld set.** If suppressed matters would have changed Juan's
decisions, the filter is miscalibrated. Without this, "I have already filtered the world for you" is
an aesthetic promise; with it, it is a capability with an error rate — probably the most valuable
single function in the system.

## CAPITAL

Unchanged from Round 2 §13, plus: **every allocation that increases the size of the system must be a
thesis with a kill condition.** Growth financed without a kill condition is not capital allocation,
it is spending. First correct use of surplus remains: buy back Juan's hours.

## UI DIRECTION — derived from how he handles information

**The monitor wall is the most useful object in the corpus.** SOURCE: many simultaneous global
broadcasts, read as a *field*, synthesised for commercial intelligence. His advantage is not watching
more — it is an environment where **pattern across sources is visible without sequential reading**.
A queue destroys that property. A feed destroys that property.

Six principles:
1. **The field, not the queue.** Composed state read at once. No feed, no inbox, no notification count.
2. **Show the difference, not the events.** INVENTION — a diff is bounded and shrinks when the world
   is quiet; a feed is unbounded and grows when it is noisy, which is backwards.
3. **Symmetry is the default; asymmetry is a signal**, reserved for the anomaly.
4. **Concentric geometry = distance from reversibility.** Centre: standing state (reversible, Ozy's).
   Ring I: the difference. Ring II: the one matter (requires Juan). Ring III: commitments
   (irreversible, Juan authorises). The Karnak/VE boundary made spatial.
5. **No number without its interval and its date.**
6. **Keep one place alive and unoptimised** — the Observatory is the vivarium. Canon warning: he
   destroyed it the moment it was inconvenient; protect it from the efficiency logic.

Three objects: **Terminal** (ask) · **Observatory** (see — a physical instrument, raw material, no
metrics on it) · **the state** (know — dense, symmetric, numeric).

**Materials, not a palette.** SOURCE: dark marble obelisks *with purple accents*; gold as leaf.
So: **ground is stone, purple is a classification stain, gold is an edge.** Purple as fill or
gradient = crypto dashboard.

**Would not show:** activity (counts of tasks/tokens/agents — motion is not state) · anything already
decided (surfacing it confesses the filter failed) · progress bars on untested theses · his own
reasoning unasked.
**The one deliberate disobedience: the calibration curve belongs at the centre, next to the runway.**
An interface faithful to him on this point would reproduce the defect that made him unfalsifiable.

**BUILD GATES (the real UI risk is building the room before the contents):** design system now (one
day) · one screen at ≥40 resolved decisions · Observatory at ≥100 stored artifacts · environment/
rooms/spatial metaphor at ≥3 resolved theses.

## KARNAK vs VEIDT ENTERPRISES

**Against:** it reproduces Veidt's pathology as architecture — reasoning where nobody can reach it,
consequences visible only as output. Also currently dishonest: VE would be an empty room.
**For:** the halves genuinely differ in cadence and authority, and that boundary already governs
every design in these documents.
**Recommendation: keep the split, redraw the axis from "thinking vs organisation" to "reversible and
mine vs irreversible and Juan's" — and make Veidt Enterprises a THRESHOLD, not a place.** You don't
navigate into it; something *crosses into* it. Honest about the current state, needs no interface
until the first crossing.

## ARCHITECTURE — additions only

MUST NOW: the pre-task prediction block · tombstones on deletion · revival triggers required on every
kill (all write-time rules, all unrecoverable if added later).
SHOULD LATER: buyer table + ASYMMETRIES register · withheld-matter sampling.
ONLY IF JUSTIFIED: persistent specialists · learned routing · the Karnak environment (numeric gates).
DO NOT BUILD: rooms · spatial navigation · a VE view · agent visualisation · self-modification.

## STRONGEST COUNTERARGUMENTS

1. The memory apparatus may be premature — at one orchestrator and zero agents there is nothing to
   remember *from*. Only the prediction record is defensible now.
2. **The character work may be doing no load-bearing work.** Every useful conclusion across four
   documents is derivable from decision theory without Watchmen. The character supplies identity and
   motivation — real, and possibly nothing else.
3. Decision frequency, still unfixed: the pre-task block raises *self*-prediction frequency, not
   *strategic* prediction frequency, and the strategic ones are what the project is about.
4. **"Karnak remembers" may be too good a phrase** — memorable phrases survive their evidence. Watch
   for it being cited as a reason rather than a label.
5. The interface may be what keeps the project alive; gating it optimises a metric at the expense of
   the project. Not resolvable analytically.

## EXPERIMENTS ADDED (6 and 7; 1–5 from Round 2 stand)

6. **Withheld-matter audit** — 4 weeks, ~0 cost: log everything suppressed, then count how many
   would have changed a decision. Tests whether filtering is a capability or a slogan.
7. **Persona calibration test** — ~€15, 2 h: same decisions persona-on / persona-off, compare log
   score and calibration slope. Makes the aesthetic commitment falsifiable.
The organisational-memory question cannot be tested this quarter; its smallest honest form (decide
20 decisions twice, with and without archive, blind) needs a year of record.

## WHAT TO BUILD NEXT (superseded by the Journal Instrument and E1 — see /journal and /experiments)

Add three fields — `predicted_self_sufficiency`, `predicted_model_adequacy`, `predicted_first_pass`
— which turn the journal from a strategic log resolving in months into a self-model instrument
resolving in hours. Then the design system (one day). Then stop and let the gates decide.

## THE STANDING JUDGEMENT

Four documents in, the project's ideas had improved substantially and its evidence had not moved at
all. That asymmetry is the finding — and it is precisely the six-month failure mode of Round 1 §22,
describing our own process rather than the system's. This is what triggered the pivot to the
Journal Instrument and Experiment E1.

## FALSIFICATION OF THE WHOLE PROJECT

At 90 days: predictions indistinguishable from base rate, **and** no thesis has produced a Class A
artifact, **and** the only input producing value is Juan's own hours. Then this is a consulting
practice with an expensive research hobby attached, and the correct response is to name it that.
