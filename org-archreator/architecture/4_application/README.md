# Application Layer

_[← EA home](../README.md)_

The software that realizes the
`business services`: application
services, the components providing them, how the components collaborate,
and — at the finest grain — the solution design and the contracts of every
interface/port.

## Analysis order

Files are numbered in the order they are analyzed, from the coarsest view
(services offered to the business) down to the finest (per-method interface
contracts). Not every project needs all five from day one — a small
project may only ever populate 1 and 2; add 3–5 when the component count or
the number of interchangeable adapters justifies the extra grain.

| #   | Document                                                             | Elements                                                     | Question it answers                              |
| --- | -----------------------------------------------------------------------| --------------------------------------------------------------- | --------------------------------------------------- |
| 1   | [1_application-services.md](./1_application-services.md)             | Application Services and the business services they realize | What does the software offer the business layer? |
| 2   | [2_application-components.md](./2_application-components.md)         | Application Components, mapped to source files               | Which components provide those services?          |
| 3   | `3_application-collaborations.md` | Collaborations and interaction sequences                     | How do the components interact?                   |
| 4   | `4_solution-design.md`                       | Overall design, diagrams, patterns, tooling                  | How is the code structured, and why?               |
| 5   | `5_interface-contracts.md`               | Per-interface pre/postconditions, invariants, error behavior | What exactly does each interface promise?          |

[2_application-components.md](./2_application-components.md) is where the **grounding rule** bites
hardest: every component row must point at the module/file that implements
it. `4_solution-design.md` is the natural place to document "how to add a
new X" recipes (a new port, a new adapter, a new platform) once the shape
repeats often enough to be worth writing down once.

## Layer view

```mermaid
flowchart TB
  acmp1["⊞ The skill corpus and plugin manifest [ACMP1]"]:::application
  acmp4["⊞ The scaffold [ACMP4]"]:::application
  acmp3["⊞ The documentation checks [ACMP3]"]:::application
  asvc1(["⬮ Method distribution and update [ASVC1]"]):::application
  bsvc3(["⬭ Advisory and delivery [BSVC3]"]):::business

  acmp1 -->|emits| acmp4
  acmp4 -->|carries| acmp3
  acmp1 -->|provides| asvc1
  bsvc3 -.->|nothing realizes| bsvc3

  classDef application fill:#c2f0ff,stroke:#0288d1,color:#333
  classDef business fill:#efe57d,stroke:#b8ad3f,color:#333
```

The self-loop is the finding: **no application service realizes advisory and
delivery.** It is done by a person, so it scales at the speed of one calendar.

### Relationships

<!-- Transcribed from this document's diagrams. The identifier is
     authoritative; the description beside it is checked against the
     catalogue that defines the element. -->

| From | From element | To | To element | Relationship |
| ---- | ------------ | -- | ---------- | ------------ |
| `ACMP1` | «Application Component» The skill corpus and plugin manifest | `ACMP4` | «Application Component» The scaffold | emits |
| `ACMP4` | «Application Component» The scaffold | `ACMP3` | «Application Component» The documentation checks | carries |
| `BSVC3` | «Business Service» Advisory and delivery with the method | `BSVC3` | «Business Service» Advisory and delivery with the method | nothing realizes |
