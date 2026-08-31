# Motivation

_[← Strategy layer](./README.md) · [Front door](../README.md)_

**ArchiMate viewpoint:** Motivation. Who has a stake in this organization,
what presses on them, what must become true, and the principles every change
is tested against.

**Status:** ◐ Draft catalogue — not yet approved at a gate. **Direction**
covers this document.

## How to read this document

```mermaid
flowchart LR
  stk(["◍ «Stakeholder» whose interests are at stake [STK#]"]):::stakeholder
  drv{{"✳ «Driver» what presses on them [DRV#]"}}:::driver
  asm>"⌕ «Assessment» what is true today [ASM#]"]:::assessment
  goal("◎ «Goal» what must become true [G#]"):::goal
  out[["◉ «Outcome» how we would know [OUT#]"]]:::outcome
  prin[/"⚑ «Principle» what every change is tested against [P#]"/]:::principle

  stk -->|concerned with| drv
  drv -->|evidenced by| asm
  drv -->|influences| goal
  goal -->|measured by| out
  prin -->|constrains| goal

  classDef stakeholder fill:#f4ecfc,stroke:#9575cd,color:#333
  classDef driver fill:#e6d6f5,stroke:#8e63c8,color:#333
  classDef assessment fill:#d8c3f0,stroke:#7e57c2,color:#333
  classDef goal fill:#c6aae9,stroke:#6f4bb2,color:#333
  classDef outcome fill:#b493e0,stroke:#5f3da0,color:#333
  classDef principle fill:#a37cd8,stroke:#4f318c,color:#333
```

## Stakeholders

| ID | Stakeholder | What they want | Concerned with | Source |
| -- | ----------- | -------------- | -------------- | ------ |
| `STK1` | **Independent builders** — building something real with a coding agent and no architecture background | To explain the business once and get from a design to something delivered, without the work outrunning their understanding | `DRV1`, `DRV2`, `DRV5`, `DRV7` | `CS1` |
| `STK2` | **Enterprise architects** — fluent in the discipline, using the method as leverage | A standard model they can navigate directly, with an agent that follows the same rules they do | `DRV2`, `DRV3`, `DRV5` | `CS2` |
| `STK3` | **Business owners** — running a company or forming one, with knowledge but no structure a builder can act on | To have their business understood well enough that what gets built is what they meant | `DRV1`, `DRV3`, `DRV4` | `CS3` |
| `STK4` | **The Requester** — the one person who maintains the method and delivers the consulting | That the method is used, improves through that use, and stops depending on their availability | `DRV5`, `DRV6` | `KR1`, `COST1` |

## Drivers and assessments

| ID | Driver | Source |
| -- | ------ | ------ |
| `DRV1` | **Solutions fail from misunderstanding, not difficulty** — a good answer to the wrong question, discovered late | `PAIN1` |
| `DRV2` | **Design and delivery are separate worlds** — meaning is lost at the handover, and time to market pays for it | `PAIN2` |
| `DRV3` | **Knowledge decays and leaves with people** — the owner explains the business again to every new builder | `PAIN3` |
| `DRV4` | **Architectural expertise is priced out of reach** for the businesses that most need it | `PAIN4` |
| `DRV5` | **AI can now do the work and has no framework behind it** — the capability arrived; the discipline did not | `PAIN5` |
| `DRV6` | **Human knowledge is being delegated rather than improved** — the fastest path with AI is to let it think, and the person ends up understanding their own business less than before | The mission — no canvas block |
| `DRV7` | **Token cost compounds without structure** — building is cheap while the solution is new, and maintaining is not, because an agent with no model traverses the whole project for every answer | `PAIN6` |

**The one driver with no canvas source is the one the organization exists
for.** Nobody lists `DRV6` as a pain, because it does not hurt while it is
happening. It is the driver behind `G6` and behind `P1`.

| ID | Assessment | Evidences | Source |
| -- | ---------- | --------- | ------ |
| `ASM1` | Without a method that forces a complete frame, a wrongly framed problem stays invisible until delivery | `DRV1` | `PAIN1` |
| `ASM2` | Design and delivery being separate is one failure with three faces: slow delivery, documentation that drives nothing, and no path from a canvas to an implementation | `DRV2` | `PAIN2` |
| `ASM3` | Knowledge scattered across documents, meetings, diagrams and wikis is knowledge trapped in whoever last held it | `DRV3` | `PAIN3` |
| `ASM4` | Architectural quality is bought either with years of seniority or with consulting fees, and both are out of reach for the segments that need it most | `DRV4` | `PAIN4` |
| `ASM5` | AI already performs most of this work in isolation, with a person acting as the framework by hand | `DRV5` | `PAIN5` |
| `ASM6` | An agent without a model answers every question by re-reading the codebase, and pays for the traversal in tokens every time | `DRV7` | `PAIN6` |

## Goals and outcomes

- **G1 — The problem is understood before it is answered.** Designing is how
  the understanding happens, not a record of understanding already had. From
  `JOB1`, against `ASM1`.
- **G2 — The design is what gets built.** An approved design flows into
  delivery without a handover for meaning to be lost in. From `JOB2`, against
  `ASM2`.
- **G3 — One shared source that outlives the people.** The same explanation
  is not repeated to every new person or agent, and a departure does not take
  the model with it. From `JOB3`, against `ASM3`.
- **G4 — Architectural quality without scarce expertise.** Competence comes
  from the method rather than from seniority or budget. From `JOB4`, against
  `ASM4`.
- **G5 — A change of direction does not discard the work.** A pivot changes
  the layers it reaches and leaves the rest standing. From `JOB5`.
- **G6 — Human knowledge improves while AI builds.** The person understands
  their own business more after the work than before it. From `DRV6`, and
  held for its own sake rather than because a customer asked.
- **G7 — Cheaper to run the longer it runs.** The model bounds what an agent
  reads, so token spend falls over the life of a solution instead of rising
  with its size — somewhat dearer on day one, cheaper every month after.
  From `PAIN6`, against `ASM6`, and still to be validated in real use.

| ID | Outcome | For | How it is checked | Source |
| -- | ------- | --- | ----------------- | ------ |
| `OUT1` | Strategic and business gaps surface **during** the design work rather than after delivery | `G1` | **No method** — a gate presentation naming a gap the owner had not stated is the evidence, and nothing records it | `GAIN1` |
| `OUT2` | Documentation goes in front of the business without a rewrite | `G1`, `G3` | **Checkable** — the document shown at a gate is the document in the repository; no separate deck exists | `GAIN2` |
| `OUT3` | Delivery starts from the approved design, with AI doing the technical work | `G2` | **Checkable** — an implementation initiative names the scope document and the elements it builds | `GAIN3` |
| `OUT4` | A new person or agent works from the model instead of being briefed | `G3` | **Observable, never counted** | `GAIN4` |
| `OUT5` | Someone without years of seniority produces an architecture that holds | `G4` | **No method** — only real adoption would evidence it | `GAIN5` |
| `OUT6` | A pivot changes some layers and leaves the rest standing | `G5` | **Checkable** — a scope document records "no change" verdicts for the layers the pivot did not reach | `GAIN6` |
| `OUT7` | Token spend per change falls once the model exists | `G7` | **No method yet** — the claim needs measuring in a real adoption before anyone repeats it | `PREL6` |

**Three of seven outcomes are checkable, one is observed and never counted,
and three have no method at all.** That distribution is the honest state of
this organization's ability to know whether it is working.

## Principles

- **P1 — Humans hold strategy and business judgement; AI assists and
  executes.** The gates make that structural rather than aspirational. Rules
  out an agent deciding what the business is — and the convenience path,
  letting AI think so the person does not have to, which is `DRV6` arriving
  from the inside.
- **P2 — Everything is in the repository, as text.** Model, method, decisions
  and approvals. Rules out a modeling tool, a wiki or a database as the
  source of truth — and any cache the model could go stale behind.
- **P3 — Better language, never simpler language.** Standardised concepts
  with defined relationships, expanded on first use, the name leading and the
  identifier riding along. Rules out hiding the model from the owner to
  spare them.
- **P4 — A design that delivers nothing is a cost.** Every element earns its
  place by leading to an outcome. Rules out documentation as the
  deliverable, and modeling an intention nobody committed to.
- **P5 — Well-done less is more.** Consolidate before enumerating; nothing
  lands that the project does not use; when in doubt, stop a level earlier.
  Rules out a catalogue nobody can hold in their head.
- **P6 — Generic by design, one implementation at a time.** The method is
  transferable instructions; the packaging is provider-specific and
  disposable.
- **P7 — Priced at the cost of running it.** Even at scale, the intent is
  not to charge much beyond operational cost. Rules out value-based pricing
  without revisiting this principle first.

**`P1` and `P4` are the two that stop work.** A change that would let an
agent decide what the business is, or that adds an element leading nowhere,
is refused at the first step rather than argued about later.
