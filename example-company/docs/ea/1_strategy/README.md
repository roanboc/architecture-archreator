# Strategy & Motivation Layer — Solvara AI

_[← EA home](../README.md)_

Who has a stake in Solvara AI, why it exists, which capabilities it needs,
and how value flows through its two product lines.

**This layer is derived**, not invented: every element traces back to a
block in [0_business-design/](../0_business-design/README.md), approved at
Gate 0 before any of this was written. The one exception is the
**Principles**, which have no canvas source and were discovered directly
with the Requester.

## Analysis order

| #   | Document                                                             | Elements                                                        | Question it answers                                | Source                                                       |
| --- | ---------------------------------------------------------------------| ------------------------------------------------------------------ | ---------------------------------------------------- | -------------------------------------------------------------- |
| 1   | [1_motivation.md](./1_motivation.md)                                 | Stakeholders, Drivers, Assessments, Goals, Outcomes, Principles | Who cares, what pressures them, what must be true?  | `CS1`, `CS2`, `JOB*`, `PAIN*`, `GAIN*` — Principles: none    |
| 2   | [2_capabilities-and-resources.md](./2_capabilities-and-resources.md) | Capabilities, Resources, Courses of Action                      | What must we be able to do, and with what?          | `PREL*`, `GCRE*`, `KR*`, `KA*`                               |
| 3   | [3_value-stream.md](./3_value-stream.md)                             | Value Streams and their stage mapping                            | How does value flow end-to-end?                     | `KA*`, `CH*`                                                 |

## Layer view

```mermaid
flowchart TB
  stk3["«Stakeholder»<br>STK3 Founders"]:::motivation
  drv3["«Driver»<br>DRV3 Revenue concentration<br>in consultant time"]:::motivation
  asm5["«Assessment»<br>ASM5 The smallest builders<br>cannot buy consulting"]:::motivation
  g3["«Goal»<br>G3 Revenue that does not scale<br>with consultant hours"]:::motivation

  coa1["«Course of Action»<br>COA1 Productize the<br>recurring pattern"]:::strategy
  vs2["«Value Stream»<br>VS2 Signup → Sustain"]:::strategy
  cap5["«Capability»<br>CAP5 Product engineering"]:::strategy
  res6["«Resource»<br>RES6 Engagement archive<br>(Pending)"]:::strategy

  stk3 -->|concerned with| drv3
  drv3 -->|assessed by| asm5
  asm5 -->|influences| g3
  g3 -->|realized by| coa1
  coa1 -->|realized by| vs2
  vs2 -->|requires| cap5
  cap5 -->|uses| res6

  classDef motivation fill:#e6d6f5,stroke:#7e57c2,color:#333
  classDef strategy fill:#f5deaa,stroke:#c8a24a,color:#333
```

The chain from `STK3` to `RES6` is the strategic spine of this business: the
founders' concern about revenue shape produces the product line, and the
product line depends on a resource that does not exist yet. Reading it
top-to-bottom is the fastest way to understand what Solvara AI is betting on
and what could stop it.
