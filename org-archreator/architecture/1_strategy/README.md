# Strategy

_[← Front door](../README.md)_

Why the organization exists, what presses on it, what must become true, what
it must be able to do, and how value flows from first contact to a delivered
outcome.

**ArchiMate viewpoint:** Motivation and Strategy: Stakeholder, Driver,
Assessment, Goal, Outcome, Principle, Capability, Resource, Value, Course of
Action, Value Stream. Every element is derived from
[the canvases](../0_business-design/README.md); the `Source` column of each
document says from which block.

## Documents

| # | Document | Elements | Question it answers |
| - | -------- | -------- | ------------------- |
| 1 | [Motivation](./1_motivation.md) | Stakeholders, drivers, assessments, goals, outcomes and the eight principles | Who cares, what presses on them, and what must become true? |
| 2 | [Capabilities and the value stream](./2_capabilities-and-value-stream.md) | Capabilities, resources, values, the course of action and the stream from first contact to a delivered outcome | What can the organization do, and how does value flow? |

## Metamodel

```mermaid
flowchart LR
  %% legend
  subgraph MOT["Motivation"]
    stk(["◍ «Stakeholder» whose interests are at stake [STK#]"]):::stakeholder
    drv{{"✳ «Driver» what presses on them [DRV#]"}}:::driver
    asm>"⌕ «Assessment» what is true today [ASM#]"]:::assessment
    goal("◎ «Goal» what must become true [G#]"):::goal
    out[["◉ «Outcome» how we would know [OUT#]"]]:::outcome
    prin[/"⚑ «Principle» what every change is tested against [P#]"/]:::principle
  end
  subgraph STR["Strategy"]
    cap["✦ «Capability» what it can do [CAP#, CAP#.#]"]:::capability
    res[("▤ «Resource» what it does it with [RES#]")]:::resource
    val[/"◈ «Value» what that is worth [VAL#]"\]:::value
    coa{{"➤ «Course of Action» the course it has taken [COA#]"}}:::coa
    vs[["⇉ «Value Stream» a stage of the stream [VS#.#]"]]:::vsx
  end
  pain>"✖ «Pain» the canvas row a driver is derived from [PAIN#]"]:::pain

  pain -->|is the source of| drv
  stk -->|concerned with| drv
  drv -->|evidenced by| asm
  drv -->|influences| goal
  out -->|measures| goal
  prin -->|constrains| goal
  cap -->|uses| res
  cap -->|delivers| val
  coa -->|shapes| cap
  cap -->|serves| vs
  val -->|strongest for| stk

  classDef stakeholder fill:#f4ecfc,stroke:#9575cd,color:#333
  classDef driver fill:#e6d6f5,stroke:#8e63c8,color:#333
  classDef assessment fill:#d8c3f0,stroke:#7e57c2,color:#333
  classDef goal fill:#c6aae9,stroke:#6f4bb2,color:#333
  classDef outcome fill:#b493e0,stroke:#5f3da0,color:#333
  classDef principle fill:#a37cd8,stroke:#4f318c,color:#333
  classDef capability fill:#f5deaa,stroke:#c8a24a,color:#333
  classDef resource fill:#faf0d5,stroke:#c8a24a,color:#333
  classDef value fill:#e9c987,stroke:#b8873f,color:#333
  classDef coa fill:#d9ad5c,stroke:#a87b2f,color:#333
  classDef vsx fill:#eed4a0,stroke:#c8a24a,color:#333
  classDef pain fill:#ffd6d6,stroke:#c62828,color:#333
```

Purple is motivation and tan is strategy. The pain keeps the canvas rose: it
is a visitor from the value proposition canvas.

## Layer view

```mermaid
flowchart LR
  s3(["◍ Business owners [STK3]"]):::stakeholder
  d1{{"✳ Solutions fail from misunderstanding [DRV1]"}}:::driver
  a1>"⌕ No method, so a wrong frame stays invisible [ASM1]"]:::assessment
  g1("◎ The problem is understood before it is answered [G1]"):::goal
  o1[["◉ Gaps surface during the design work [OUT1]"]]:::outcome
  cap1["✦ Method development [CAP1]"]:::capability
  v1[/"◈ The problem is framed completely first [VAL1]"\]:::value
  vs2[["⇉ Frame [VS1.2]"]]:::vsx

  s3 -->|concerned with| d1
  d1 -->|evidenced by| a1
  o1 -->|measures| g1
  cap1 -->|delivers| v1
  v1 -->|strongest for| s3
  cap1 -->|serves| vs2

  classDef stakeholder fill:#f4ecfc,stroke:#9575cd,color:#333
  classDef driver fill:#e6d6f5,stroke:#8e63c8,color:#333
  classDef assessment fill:#d8c3f0,stroke:#7e57c2,color:#333
  classDef goal fill:#c6aae9,stroke:#6f4bb2,color:#333
  classDef outcome fill:#b493e0,stroke:#5f3da0,color:#333
  classDef principle fill:#a37cd8,stroke:#4f318c,color:#333
  classDef capability fill:#f5deaa,stroke:#c8a24a,color:#333
  classDef resource fill:#faf0d5,stroke:#c8a24a,color:#333
  classDef value fill:#e9c987,stroke:#b8873f,color:#333
  classDef coa fill:#d9ad5c,stroke:#a87b2f,color:#333
  classDef vsx fill:#eed4a0,stroke:#c8a24a,color:#333
```

A business owner's pressure is evidenced by an assessment and answered by a
goal an outcome measures. The capability that builds the method delivers the
value that is strongest for that same owner, and serves the stage where the
problem is framed.
