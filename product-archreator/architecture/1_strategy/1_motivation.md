# Motivation — archreator

_[← Strategy layer](./README.md) · [EA home](../README.md)_

**ArchiMate elements:** Stakeholder, Driver, Assessment, Goal, Outcome,
Principle.

At Depth 1 there is no `0_business-design/` to derive from, so every element
here was discovered directly rather than mapped from a canvas block.

## How to read this document

```mermaid
flowchart LR
  stk(["◍ «Stakeholder»<br>who cares"]):::stakeholder
  drv{{"✳ «Driver»<br>what pressures them"}}:::driver
  asm>"⌕ «Assessment»<br>what we judge to be true"]:::assessment
  g("◎ «Goal»<br>what must become true"):::goal
  out[["◉ «Outcome»<br>how we would see it"]]:::outcome
  p[/"⚑ «Principle»<br>what must always hold"/]:::principle

  stk -->|concerned with| drv
  drv -->|assessed by| asm
  asm -->|realized by| g
  g -->|realized by| out
  p -->|influences| g

  classDef stakeholder fill:#f4ecfc,stroke:#9575cd,color:#333
  classDef driver fill:#e6d6f5,stroke:#7e57c2,color:#333
  classDef assessment fill:#d8c3f0,stroke:#7e57c2,color:#333
  classDef goal fill:#c6aae9,stroke:#673ab7,color:#333
  classDef outcome fill:#b493e0,stroke:#5e35b1,color:#333
  classDef principle fill:#a37cd8,stroke:#4527a0,color:#333
```

| Glyph | Shape | Element | ID prefix | Reads as |
| ----- | ----- | ------- | --------- | -------- |
| `◍` | Stadium | «Stakeholder» | `STK` | `STK1` = Stakeholder 1 |
| `✳` | Hexagon | «Driver» | `DRV` | `DRV1` = Driver 1 |
| `⌕` | Flag | «Assessment» | `ASM` | `ASM1` = Assessment 1 |
| `◎` | Rounded rectangle | «Goal» | `G` | `G1` = Goal 1 |
| `◉` | Rectangle, double bars | «Outcome» | `OUT` | `OUT1` = Outcome 1 |
| `⚑` | Parallelogram | «Principle» | `P` | `P1` = Principle 1 |

Six tones of the Motivation violet, light at the start of the chain and dark
at the end. **The glyph rides on every node; the «stereotype» word appears
once** — on the first node of each type in a diagram, dropped on the rest.
The values come from
[`architecture/README.md` § Notation conventions](../../../.claude/skills/project-bootstrap/templates/architecture/README.md#notation-conventions).

## Stakeholders and drivers

```mermaid
flowchart LR
  stk1(["◍ «Stakeholder» STK1<br>Someone modeling a company"]):::stakeholder
  stk2(["◍ STK2<br>Someone building one application"]):::stakeholder
  stk3(["◍ STK3<br>A non-technical Requester"]):::stakeholder
  stk4(["◍ STK4<br>The AI agent executing the method"]):::stakeholder
  stk5(["◍ STK5<br>archreator's maintainer"]):::stakeholder

  drv1{{"✳ «Driver» DRV1<br>Enterprise architecture is too slow"}}:::driver
  drv2{{"✳ DRV2<br>AI builds faster than oversight"}}:::driver
  drv3{{"✳ DRV3<br>Approvers cannot reach the tools"}}:::driver
  drv4{{"✳ DRV4<br>Agents lose the thread"}}:::driver
  drv5{{"✳ DRV5<br>A copied template cannot improve"}}:::driver

  stk1 --> drv1
  stk2 --> drv2
  stk3 --> drv3
  stk4 --> drv4
  stk5 --> drv5

  classDef stakeholder fill:#f4ecfc,stroke:#9575cd,color:#333
  classDef driver fill:#e6d6f5,stroke:#7e57c2,color:#333
```

Every edge reads **concerned with**. One driver per stakeholder, which is
what a Depth 1 model looks like when it is honest: five constituencies, five
distinct pressures, and no pretence that they overlap.


| ID | Stakeholder | Concern | Driver |
| -- | ----------- | ------- | ------ |
| `STK1` | Someone modeling a company (external, adopts and uses) | Getting their organization into a form AI agents can work from, without a six-month architecture programme | `DRV1` |
| `STK2` | Someone building one application (external, adopts and uses) | The same discipline at a weight a single app can carry | `DRV2` |
| `STK3` | A non-technical Requester (external, approves) | Being able to approve what gets built without learning git | `DRV3` |
| `STK4` | The AI agent executing the method (internal, non-human) | Instructions unambiguous enough to act on without re-deriving intent each session | `DRV4` |
| `STK5` | archreator's maintainer (internal, owner) | A method that improves without every downstream project having to be rebuilt | `DRV5` |

| ID | Driver | What pressures it |
| -- | ------ | ----------------- |
| `DRV1` | **Enterprise architecture is too slow to be useful** — by the time a traditional practice produces a model, the organization has moved |
| `DRV2` | **AI builds faster than humans can keep track** — drift, contradiction, and code nobody can explain a week later |
| `DRV3` | **The people who should approve can't reach the tools** — the person who knows whether the business model is right does not work in a terminal |
| `DRV4` | **Agents lose the thread across sessions** — context that isn't written down is context that doesn't survive |
| `DRV5` | **A copied template cannot be improved** — a method distributed by copy diverges the moment it is used |

## Assessments

```mermaid
flowchart LR
  asm1>"⌕ «Assessment» ASM1<br>Artifacts need not match reality"]:::assessment
  asm2>"⌕ ASM2<br>Confident inconsistency"]:::assessment
  asm3>"⌕ ASM3<br>Approval is unrecorded or unreachable"]:::assessment
  asm4>"⌕ ASM4<br>An agent picks a plausible order"]:::assessment
  asm5>"⌕ ASM5<br>Scaffold and method have opposite lifecycles"]:::assessment

  g1("◎ «Goal» G1<br>A model you can implement against"):::goal
  g2("◎ G2<br>Speed without incoherence"):::goal
  g3("◎ G3<br>The person who should decide, decides"):::goal
  g4("◎ G4<br>The method improves without breaking users"):::goal

  asm1 --> g1
  asm2 --> g2
  asm4 --> g2
  asm3 --> g3
  asm5 --> g4

  classDef assessment fill:#d8c3f0,stroke:#7e57c2,color:#333
  classDef goal fill:#c6aae9,stroke:#673ab7,color:#333
```

Every edge reads **realized by**. `G2` is the only goal two assessments
point at, and that is the shape of the problem archreator exists for:
inconsistency comes both from the agent's speed and from its lack of a fixed
order to work in.


| ID | Assessment | Assesses |
| -- | ---------- | -------- |
| `ASM1` | Documentation frameworks produce artifacts that describe an architecture without anything having to correspond to reality; nothing detects the gap | `DRV1` |
| `ASM2` | The failure mode of AI-assisted building isn't bad code, it's confident inconsistency — each change is locally reasonable and the set is incoherent | `DRV2` |
| `ASM3` | Approval that lives in a chat message is not a record; approval that requires a git client is not accessible | `DRV3` |
| `ASM4` | An agent given a process but not the order to apply it in will pick a plausible order, and a different one next time | `DRV4` |
| `ASM5` | A template's scaffold and its method have opposite lifecycles — one is overwritten on day one, the other should keep improving — and bundling them means neither can be handled correctly | `DRV5` |

## Goals

- **G1 — A model you can implement against.** Every element points at
  something real, so the model is checkable rather than merely written.
  Derived from `ASM1`.
- **G2 — Speed without incoherence.** A change moves as fast as an agent
  can work, and still lands consistent with everything already decided.
  Derived from `ASM2`.
- **G3 — The person who should decide, decides.** Business judgment is
  exercised by whoever holds it, at a surface they can actually use.
  Derived from `ASM3`.
- **G4 — The method improves without breaking its users.** Adopting an
  improvement is an install, not a migration. Derived from `ASM5`.

## Outcomes

```mermaid
flowchart LR
  g1("◎ «Goal» G1<br>A model you can implement against"):::goal
  g2("◎ G2<br>Speed without incoherence"):::goal
  g3("◎ G3<br>The person who should decide, decides"):::goal
  g4("◎ G4<br>The method improves without breaking users"):::goal

  out1[["◉ «Outcome» OUT1<br>Any element checkable in under a minute"]]:::outcome
  out2[["◉ OUT2<br>A conflicting change is stopped before it is built"]]:::outcome
  out3[["◉ OUT3<br>A Requester with no terminal can grant every gate"]]:::outcome
  out4[["◉ OUT4<br>An improvement reaches a project without hand-porting"]]:::outcome

  g1 --> out1
  g2 --> out2
  g3 --> out3
  g4 -.-> out4

  classDef goal fill:#c6aae9,stroke:#673ab7,color:#333
  classDef outcome fill:#b493e0,stroke:#5e35b1,color:#333
```

Every edge reads **realized by**. `OUT4`'s edge is dashed because it is
**Pending**: the plugin mechanism exists and no second version has shipped
through it, so nothing has proved the claim.


| ID | Outcome | Realizes | Measured by |
| -- | ------- | -------- | ----------- |
| `OUT1` | Any element in the model can be checked against the repository or the people doing the work in under a minute | `G1` | A reader picks a row at random and finds the artifact, or an explicit "Pending" |
| `OUT2` | A change that contradicts an existing principle is stopped before it is built, not after | `G2` | `ea-first-change` Step 1c reaches a Conflict verdict rather than proceeding |
| `OUT3` | A Requester with no terminal can grant every gate | `G3` | Gates are granted in conversation or on a PR comment, and transcribed into the Approvals table |
| `OUT4` | A method improvement reaches an existing project without hand-porting | `G4` | `/plugin update`. **Pending** until the plugin has shipped a second version |

## Principles

```mermaid
flowchart LR
  p1[/"⚑ «Principle» P1<br>Every element names what realizes it"/]:::principle
  p2[/"⚑ P2<br>A human approves, and it is recorded"/]:::principle
  p3[/"⚑ P3<br>Each fact in exactly one document"/]:::principle
  p4[/"⚑ P4<br>A skill states the what; the model reasons the how"/]:::principle
  p5[/"⚑ P5<br>History is never rewritten"/]:::principle

  g1("◎ «Goal» G1<br>A model you can implement against"):::goal
  g2("◎ G2<br>Speed without incoherence"):::goal
  g4("◎ G4<br>The method improves without breaking users"):::goal

  p1 --> g1
  p2 --> g2
  p3 --> g1
  p4 --> g4
  p5 --> g2

  classDef principle fill:#a37cd8,stroke:#4527a0,color:#333
  classDef goal fill:#c6aae9,stroke:#673ab7,color:#333
```

Every edge reads **influences**. `G3` has no principle pointing at it — the
person who should decide deciding is a goal the gates deliver structurally,
not something a rule can be checked against.


Few, load-bearing, and testable. These gate every change to the method
itself, and `ea-first-change` Step 1c stops on a conflict with any of them.

| ID | Principle | What it rules out |
| -- | --------- | ----------------- |
| `P1` | **Every element names what realizes it, or is explicitly Pending.** | A model that describes an intention as though it were a fact. This is the grounding rule, and it is the one that makes archreator a modeling-for-implementation method rather than a documentation method |
| `P2` | **A human approves before anything is built, and the approval is recorded where it can be found later.** | Silent agent autonomy; approvals that exist only in a chat scrollback |
| `P3` | **Each fact lives in exactly one document; everything else links to it.** | Drift between two copies of the same table — the failure that makes large models untrustworthy |
| `P4` | **A skill states the *what*; the model reasons the *how*.** | A command catalogue that grows faster than anyone can learn it, and instructions that break when the situation differs slightly from the one anticipated |
| `P5` | **History is never rewritten.** A merged scope document, an assigned element ID, and a granted approval are permanent. | Retroactively making the past agree with the present — which destroys the only evidence that a decision was made against different information |

`P5` is the newest, added when `restate-current-state` made it necessary to
say explicitly what compaction may and may not touch.

## Why there is no single view of this layer

The four diagrams above are the complete view, drawn one link of the chain at
a time. An earlier version of this document ended with one picture of
everything, which showed twelve of thirty-six elements and implied it showed
all of them —
[the notation standard](../../scope/5_diagram-notation-standard.md) exists
because of exactly that.
