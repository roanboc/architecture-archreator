# Capabilities and Resources — the organization behind archreator

_[← Strategy layer](./README.md) · [EA home](../README.md)_

**ArchiMate elements:** Capability, Resource, Value, Course of Action.

Derived from the value map and the business model canvases, approved at
Gate 0 on 2026-08-08.

## How to read this document

```mermaid
flowchart LR
  res[("«Resource»<br>what it is built with")]:::resource
  cap["«Capability»<br>what we must be able to do"]:::capability
  val[/"«Value»<br>what that is worth to someone"\]:::value
  coa{{"«Course of Action»<br>a direction named,<br>not yet taken"}}:::action
  g("«Goal»<br>what must become true"):::goal

  res -->|assigned to| cap
  cap -->|delivers| val
  cap -->|realizes| g
  coa -.->|would change| res

  classDef resource fill:#faf0d5,stroke:#c8a24a,color:#333
  classDef capability fill:#f5deaa,stroke:#c8a24a,color:#333
  classDef value fill:#e9c987,stroke:#a8813a,color:#333
  classDef action fill:#d9ad5c,stroke:#8a6a2a,color:#333
  classDef goal fill:#c6aae9,stroke:#673ab7,color:#333
```

**Where the strategy layer sits:** resources are what the organization has,
capabilities are what it can therefore do, values are what that is worth to
a stakeholder, and goals — which live in
[the motivation layer](./1_motivation.md) — are what it is all for. Courses
of action are the odd ones out: they are directions named but not taken, so
they attach with a dashed edge to whatever they would change.

| Shape | Element | ID prefix | Reads as |
| ----- | ------- | --------- | -------- |
| Cylinder | «Resource» | `RES` | `RES1` = Resource 1 |
| Rectangle | «Capability» | `CAP` | `CAP1` = Capability 1 |
| Trapezoid | «Value» | `VAL` | `VAL1` = Value 1 |
| Hexagon | «Course of Action» | `COA` | `COA1` = Course of Action 1 |
| Rounded rectangle (violet) | «Goal» — context, from layer 1 | `G` | `G1` = Goal 1 |
| Stadium (violet) | «Stakeholder» — context, from layer 1 | `STK` | `STK1` = Stakeholder 1 |
| Grey, double bars | a **canvas** element from layer 0 — not ArchiMate | `PREL`, `GCRE` | `PREL1` = Pain Reliever 1 |

Four sand tones, running light for what is held to dark for what is only
proposed. Goals keep the Motivation violet and the rounded shape they have in
[1_motivation.md](./1_motivation.md), so an element that appears in two
documents looks the same in both.

**The «stereotype» label appears on the first node of each type in a
diagram** and is dropped on the rest; the legend carries it for the whole
document.

## Capabilities

```mermaid
flowchart LR
  prel1[["PREL1 The gated<br>layer walk"]]:::canvas
  prel2[["PREL2 The method<br>continues into delivery"]]:::canvas
  prel3[["PREL3 One model<br>in one place"]]:::canvas
  prel4[["PREL4 An architect's cost<br>becomes an agent's"]]:::canvas
  gcre1[["GCRE1 Question-driven<br>discovery"]]:::canvas
  gcre2[["GCRE2 Markdown and<br>diagrams for people"]]:::canvas
  gcre3[["GCRE3 Design turns into<br>implementation work"]]:::canvas
  gcre4[["GCRE4 Standardised<br>concepts"]]:::canvas
  gcre5[["GCRE5 The method carries<br>the competence"]]:::canvas
  gcre6[["GCRE6 The layered<br>model"]]:::canvas

  cap1["«Capability»<br>CAP1 Gated discovery"]:::capability
  cap2["CAP2 Design-to-delivery<br>continuity"]:::capability
  cap3["CAP3 One documented<br>model"]:::capability
  cap4["CAP4 A shared<br>architectural language"]:::capability
  cap5["CAP5 Method-carried<br>competence"]:::capability
  cap6["CAP6 Layered change<br>absorption"]:::capability

  prel1 --> cap1
  gcre1 --> cap1
  prel2 --> cap2
  gcre3 --> cap2
  prel3 --> cap3
  gcre2 --> cap3
  gcre4 --> cap4
  prel4 --> cap5
  gcre5 --> cap5
  gcre6 --> cap6

  classDef canvas fill:#eeeeee,stroke:#9e9e9e,color:#333
  classDef capability fill:#f5deaa,stroke:#c8a24a,color:#333
```

Every edge reads **derived into**. The grey nodes are canvas elements from
[layer 0](../0_business-design/1_value-proposition-canvas.md), not ArchiMate
elements — they are drawn only to show the consolidation, which is the one
thing a table cannot show: **ten canvas elements collapsing into six
capabilities**, because most were one ability described twice, once from the
customer's side as a pain being removed and once from the method's side as a
gain being produced.

| ID | Capability | Delivers the value of | Realized by | Source |
| -- | ---------- | --------------------- | ----------- | ------ |
| `CAP1` | **Gated discovery** — question-driven discovery that tests the business rather than recording it, with approval gates forcing a complete frame before anything is built | `VAL1` | The `ea-first-change`, `operating-model-discovery` and `strategy-discovery` skills | `PREL1` Pain Reliever 1, `GCRE1` Gain Creator 1 |
| `CAP2` | **Design-to-delivery continuity** — the approved design is the input an agent builds from, so there is no handover | `VAL2` | The `ea-first-change` skill, Steps 5–7, and the `story-sharding` skill | `PREL2`, `GCRE3` |
| `CAP3` | **One documented model** — markdown in git, catalogues and diagrams, every element naming what realizes it | `VAL3` | The `ea-doc-style` skill, `scripts/check_links.py`, `scripts/check_model.py` | `PREL3`, `GCRE2` |
| `CAP4` | **A shared architectural language** — standardised concepts with defined relationships, which is what makes the model mean the same thing to a person and to an agent | `VAL3` | ArchiMate-on-Mermaid notation, per the `ea-doc-style` skill | `GCRE4` |
| `CAP5` | **Method-carried competence** — the expertise sits in the method, so the price of an architecture drops to the price of an agent | `VAL4` | The skill set as a whole, distributed as a plugin | `PREL4`, `GCRE5` |
| `CAP6` | **Layered change absorption** — strategy can change without redoing technology, and the reverse | `VAL5` | The numbered layers and the per-layer "no change" verdict | `GCRE6` |

**`PREL5` is the eleventh canvas element, and it is absent from the diagram
on purpose.** "The whole thing operating together" is the *aggregate* of
`CAP1`–`CAP6`, not a seventh ability — and it is what the Requester
identified as what archreator essentially is. Modeling it as a peer of the
others would double-count the six and hide the fact that the value is in
their composition.

## Values delivered

```mermaid
flowchart LR
  cap1["«Capability»<br>CAP1 Gated<br>discovery"]:::capability
  cap2["CAP2 Design-to-delivery<br>continuity"]:::capability
  cap3["CAP3 One documented<br>model"]:::capability
  cap4["CAP4 A shared<br>architectural language"]:::capability
  cap5["CAP5 Method-carried<br>competence"]:::capability
  cap6["CAP6 Layered change<br>absorption"]:::capability

  val1[/"«Value»<br>VAL1 The problem is<br>framed completely"\]:::value
  val2[/"VAL2 A working solution,<br>not a document"\]:::value
  val3[/"VAL3 One source that<br>survives people"\]:::value
  val4[/"VAL4 Quality at a price<br>the segment can carry"\]:::value
  val5[/"VAL5 A pivot costs a layer,<br>not the project"\]:::value

  stk1(["«Stakeholder»<br>STK1 Designers"]):::stakeholder
  stk2(["STK2 Established<br>owners"]):::stakeholder
  stk3(["STK3 Founders"]):::stakeholder

  cap1 --> val1
  cap2 --> val2
  cap3 --> val3
  cap4 --> val3
  cap5 --> val4
  cap6 --> val5

  val1 --> stk1
  val1 --> stk2
  val1 --> stk3
  val2 --> stk1
  val2 --> stk2
  val3 --> stk1
  val3 --> stk2
  val4 --> stk2
  val4 --> stk3
  val5 --> stk3

  classDef capability fill:#f5deaa,stroke:#c8a24a,color:#333
  classDef value fill:#e9c987,stroke:#a8813a,color:#333
  classDef stakeholder fill:#f4ecfc,stroke:#9575cd,color:#333
```

Capability edges read **delivers**; value edges read **serves**.

| ID | Value | Delivered to |
| -- | ----- | ------------ |
| `VAL1` | The problem is framed completely before it is answered | `STK1`, `STK2`, `STK3` |
| `VAL2` | The design produces a working solution rather than a document | `STK1`, `STK2` |
| `VAL3` | One source that survives people joining and leaving | `STK1`, `STK2` |
| `VAL4` | Architectural quality at a price the segment can carry | `STK2`, `STK3` |
| `VAL5` | A pivot costs a layer, not the project | `STK3` |

`VAL1` is the only value every stakeholder receives, and `CAP1` is the only
capability that produces it. That makes gated discovery the one ability this
organization cannot drop without changing who it serves.

## Resources

```mermaid
flowchart LR
  res1[("«Resource»<br>RES1 The Requester's<br>knowledge and time")]:::resource
  res2[("RES2 The method")]:::resource
  res3[("RES3 The published<br>guidance site")]:::resource
  res4[("RES4 The portal<br>— Pending")]:::resource

  cap1["«Capability»<br>CAP1 Gated<br>discovery"]:::capability
  cap2["CAP2 Design-to-delivery<br>continuity"]:::capability
  cap3["CAP3 One documented<br>model"]:::capability
  cap4["CAP4 A shared<br>architectural language"]:::capability
  cap5["CAP5 Method-carried<br>competence"]:::capability
  cap6["CAP6 Layered change<br>absorption"]:::capability

  res1 --> res2
  res1 --> res3
  res2 --> cap1
  res2 --> cap2
  res2 --> cap3
  res2 --> cap4
  res2 --> cap5
  res2 --> cap6
  res3 --> cap5
  res4 -.-> cap5

  classDef resource fill:#faf0d5,stroke:#c8a24a,color:#333
  classDef capability fill:#f5deaa,stroke:#c8a24a,color:#333
```

Every edge reads **assigned to**. **This diagram is the risk, drawn.** One
resource authors the method, the method realizes all six capabilities, and
so one person's availability sits behind everything the organization can do.
The [business model canvas](../0_business-design/2_business-model-canvas.md#what-the-three-share-and-where-they-diverge)
records that as a concentration; here it is in the layer where something
could be done about it.

| ID | Resource | Kind | State | Source |
| -- | -------- | ---- | ----- | ------ |
| `RES1` | **The Requester's knowledge and time** | People | **Constrained — the binding limit on the whole organization** | `KR1` Key Resource 1 |
| `RES2` | **The method** — skills, conventions, gates | Knowledge | Held, and improving. Every capability depends on it | `KR2` |
| `RES3` | **The published guidance site** | Asset | Held — realized by `site/` | `KR3` |
| `RES4` | **The portal** | Asset | **Pending — future initiative** (`COA2`) | `KR4` |

## Courses of action

```mermaid
flowchart LR
  coa1{{"«Course of Action»<br>COA1 AI agents as<br>consultants"}}:::action
  coa2{{"COA2 Build<br>the portal"}}:::action
  coa3{{"COA3 Instrument the<br>adoption measure"}}:::action

  res1[("«Resource»<br>RES1 The Requester's<br>knowledge and time")]:::resource
  res4[("RES4 The portal<br>— Pending")]:::resource

  coa1 -.->|would relieve| res1
  coa2 -.->|would create| res4
  coa2 -.->|would consume| res1
  coa3 -.->|would make the<br>outcomes measurable| res1

  classDef action fill:#d9ad5c,stroke:#8a6a2a,color:#333
  classDef resource fill:#faf0d5,stroke:#c8a24a,color:#333
```

Choices the organization has named but not taken. Each is Pending, and each
is a candidate initiative rather than a plan — which is why every edge is
dashed.

| ID | Course of action | Addresses | Requires | State |
| -- | ---------------- | --------- | -------- | ----- |
| `COA1` | **AI agents acting as consultants**, carrying the Requester's knowledge | The `RES1` concentration, if `PROD2` ever had to scale | More AI maturity than exists today | **Pending** — named at Gate 0 as a route, explicitly not a plan |
| `COA2` | **Build the portal** (`PROD3`) | `STK2` and `STK3` are reachable today only through a coding agent, and nothing reaches an owner who is not already looking | An application and technology layer this model does not yet have | **Pending — target state** |
| `COA3` | **Instrument the adoption measure** | Only three of seven outcomes are checkable today; one is observable but never counted, and three have no collection method at all | A way for adopters to report use — self-reporting is the obvious candidate | **Pending.** Prerequisite for any Social Return on Investment valuation |

**All three edges land on `RES1`, and two of them pull opposite ways.** `COA1`
would relieve the Requester's time; `COA2` would spend a great deal of it
first, and `COA3` spends some too. Which comes first is a strategy decision,
not a sequencing detail, and it is not settled here.
