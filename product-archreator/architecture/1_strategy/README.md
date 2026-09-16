# Strategy

_[← Front door](../README.md)_

Why the method exists and what must be true of it, light enough to judge a
change against and nothing more.

**ArchiMate viewpoint:** Motivation: Stakeholder, Driver, Assessment, Goal,
Outcome. An element of the organization's is cited as `ORG.<ID>`, never
restated.

## Documents

| # | Document | Elements | Question it answers |
| - | -------- | -------- | ------------------- |
| 1 | [Motivation](./1_motivation.md) | The three roles of an adopting project and two readers, what presses on them, seven goals and how each is checked | Who has a stake in the method, and what must be true of it? |

## Metamodel

```mermaid
flowchart LR
  %% legend
  stk(["◍ «Stakeholder» whose interests are at stake [STK#]"]):::stakeholder
  drv{{"✳ «Driver» what presses on them [DRV#]"}}:::driver
  asm>"⌕ «Assessment» what is true today [ASM#]"]:::assessment
  goal("◎ «Goal» what must become true [G#]"):::goal
  out[["◉ «Outcome» how we would know [OUT#]"]]:::outcome
  parent("◎ the organization's own element, cited and never restated [ORG.CS#, ORG.DRV#, ORG.G#]"):::parent

  stk -->|refines| parent
  drv -->|pressing on| stk
  asm -->|evidences| drv
  drv -->|sharpens| parent
  goal -->|against| asm
  goal -->|serves| parent
  goal -->|measured by| out

  classDef stakeholder fill:#f4ecfc,stroke:#9575cd,color:#333
  classDef driver fill:#e6d6f5,stroke:#8e63c8,color:#333
  classDef assessment fill:#d8c3f0,stroke:#7e57c2,color:#333
  classDef goal fill:#c6aae9,stroke:#6f4bb2,color:#333
  classDef outcome fill:#b493e0,stroke:#5f3da0,color:#333
  classDef principle fill:#a37cd8,stroke:#4f318c,color:#333
  classDef parent fill:#ede4f8,stroke:#6f4bb2,color:#333,stroke-dasharray: 4 3
```

An element of the organization's keeps its own shape and glyph and is drawn
dashed.

## Layer view

```mermaid
flowchart LR
  s1(["◍ Requester in an adopting project [STK1]"]):::stakeholder
  d1{{"✳ Agents build faster than anyone can specify [DRV1]"}}:::driver
  a1>"⌕ Requirements reach code without passing through architecture [ASM1]"]:::assessment
  g2("◎ A person approves before code exists [G2]"):::goal
  o1(["◍ Independent builder [ORG.CS1]"]):::parent
  o5{{"✳ AI can do the work, with no framework [ORG.DRV5]"}}:::parent
  og1("◎ The problem is understood before it is answered [ORG.G1]"):::parent

  s1 -->|refines| o1
  d1 -->|pressing on| s1
  a1 -->|evidences| d1
  d1 -->|sharpens| o5
  g2 -->|against| a1
  g2 -->|serves| og1

  classDef stakeholder fill:#f4ecfc,stroke:#9575cd,color:#333
  classDef driver fill:#e6d6f5,stroke:#8e63c8,color:#333
  classDef assessment fill:#d8c3f0,stroke:#7e57c2,color:#333
  classDef goal fill:#c6aae9,stroke:#6f4bb2,color:#333
  classDef outcome fill:#b493e0,stroke:#5f3da0,color:#333
  classDef principle fill:#a37cd8,stroke:#4f318c,color:#333
  classDef parent fill:#ede4f8,stroke:#6f4bb2,color:#333,stroke-dasharray: 4 3
```

A requester in an adopting project refines the organization's independent
builder; the pressure on them sharpens a driver of the organization's, and the
goal that answers it serves a goal of the organization's.
