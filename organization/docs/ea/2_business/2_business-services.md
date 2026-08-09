# Products, Services and Channels — the organization behind archreator

_[← Business layer](./README.md) · [EA home](../README.md)_

**ArchiMate elements:** Product, Business Service, Business Interface.

Derived from the three products, five channels and three customer
relationships on the
[business model canvas](../0_business-design/2_business-model-canvas.md),
approved at Gate 0.

## How to read this document

```mermaid
flowchart LR
  prod["▣ «Product»<br>what a customer buys"]:::product
  svc(["⬭ «Business Service»<br>what it actually does for them"]):::service
  bif["⊸ «Business Interface»<br>where they meet it"]:::interface
  stk(["◍ «Stakeholder»<br>who they are"]):::stakeholder

  prod -->|aggregates| svc
  svc -->|assigned to| bif
  bif -->|serves| stk

  classDef product fill:#fffbb5,stroke:#b8a200,color:#333
  classDef service fill:#efe57d,stroke:#8a7a00,color:#333
  classDef interface fill:#e5d95f,stroke:#7a6c00,color:#333
  classDef stakeholder fill:#f4ecfc,stroke:#9575cd,color:#333
```

**A product is not a service.** The product is what a customer names and
pays for; the services are what it does for them; the interface is where
they touch it. Keeping the three separate is what lets one service belong to
two products, and one interface carry two services.

| Glyph | Shape | Element | ID prefix | Reads as |
| ----- | ----- | ------- | --------- | -------- |
| `▣` | Rectangle | «Product» | `PROD` | `PROD1` = Product 1 |
| `⬭` | Stadium | «Business Service» | `BSVC` | `BSVC1` = Business Service 1 |
| `⊸` | Rectangle | «Business Interface» — the channel | `BIF` | `BIF1` = Business Interface 1 |
| `◍` | Stadium (violet) | «Stakeholder» — context, from [layer 1](../1_strategy/1_motivation.md) | `STK` | `STK1` = Stakeholder 1 |
| `✦` | Rectangle (sand) | «Capability» — context, from [layer 1](../1_strategy/2_capabilities-and-resources.md) | `CAP` | `CAP1` = Capability 1 |

`⊸` is ArchiMate's interface lollipop, the one glyph in this document that
depicts rather than merely distinguishes.

**The glyph rides on every node; the «stereotype» word appears once** — on the
first node of each type in a diagram, dropped on the rest.

## Products and the services they aggregate

```mermaid
flowchart LR
  prod1["▣ «Product» PROD1<br>The open method"]:::product
  prod2["▣ PROD2<br>Consulting"]:::product
  prod3["▣ PROD3<br>The portal — Pending"]:::product

  bsvc1(["⬭ «Business Service» BSVC1<br>The method, published"]):::service
  bsvc2(["⬭ BSVC2<br>Guidance and worked reference"]):::service
  bsvc3(["⬭ BSVC3<br>Advisory and delivery"]):::service
  bsvc4(["⬭ BSVC4<br>Architecture as a service — Pending"]):::service

  cap1["✦ «Capability» CAP1<br>Business understanding"]:::capability
  cap2["✦ CAP2<br>Model stewardship"]:::capability
  cap3["✦ CAP3<br>Delivery from design"]:::capability

  prod1 --> bsvc1
  prod1 --> bsvc2
  prod2 --> bsvc3
  prod3 -.-> bsvc4

  bsvc1 --> cap1
  bsvc1 --> cap2
  bsvc1 --> cap3
  bsvc2 --> cap3
  bsvc3 --> cap1
  bsvc3 --> cap3
  bsvc4 -.-> cap1
  bsvc4 -.-> cap3

  classDef product fill:#fffbb5,stroke:#b8a200,color:#333
  classDef service fill:#efe57d,stroke:#8a7a00,color:#333
  classDef capability fill:#f5deaa,stroke:#c8a24a,color:#333
```

Product edges read **aggregates**; service edges read **realizes**. The
products are defined on the
[value proposition canvas](../0_business-design/1_value-proposition-canvas.md#products);
this table records what each one aggregates and returns.

| Product | Aggregates | Delivered through | Returns |
| ------- | ---------- | ----------------- | ------- |
| `PROD1` archreator, the open method | `BSVC1`, `BSVC2` | `BIF1`, `BIF2`, `BIF3` | `RS1`, `RS2` — both non-monetary |
| `PROD2` Consulting | `BSVC3` | `BIF4` | `RS3` — monetary, hourly |
| `PROD3` The archreator portal — **Pending** | `BSVC4` | `BIF5` | `RS4` — monetary, per use |

| ID | Business service | Realizes | Product | Realized by | Source |
| -- | ---------------- | -------- | ------- | ----------- | ------ |
| `BSVC1` | **The method, published and installable** — the skills, the conventions, the gates, obtainable and usable without asking anyone | `CAP1`, `CAP2`, `CAP3` — all three areas | `PROD1` | `.claude/skills/`, the plugin manifest, `docs/` | Value propositions of `PROD1` |
| `BSVC2` | **Guidance and worked reference** — how to start, what the method is for, and a model built with it that a reader can inspect | `CAP3` | `PROD1` | `site/`, `meta/`, and this tree | Value propositions of `PROD1` |
| `BSVC3` | **Advisory and delivery with the method** — the Requester runs discovery and delivery personally | `CAP1`, `CAP3` | `PROD2` | `ROLE2`, in person | Value propositions of `PROD2` |
| `BSVC4` | **Architecture as a service** — an owner supplies what they have and receives a working architecture repository | `CAP1`, `CAP3` | `PROD3` | **Pending — future initiative** (`COA2`) | Value propositions of `PROD3` |

**`BSVC1` is the only service touching all three capability areas**, which is
what makes the free product the load-bearing one: everything the organization
can do is reachable through it. `BSVC2` is realized partly by **this
document's own tree** — the organization modeling itself in public is not a
side project, it is what makes the guidance inspectable, which is the
service.

## Business interfaces — the channels

```mermaid
flowchart LR
  bif1["⊸ «Business Interface» BIF1<br>Public repository"]:::interface
  bif2["⊸ BIF2<br>The guidance site"]:::interface
  bif3["⊸ BIF3<br>Plugin marketplace"]:::interface
  bif4["⊸ BIF4<br>Referral and direct approach"]:::interface
  bif5["⊸ BIF5<br>The web, self-serve — Pending"]:::interface

  stk1(["◍ «Stakeholder» STK1<br>Designers"]):::stakeholder
  stk2(["◍ STK2<br>Established owners"]):::stakeholder
  stk3(["◍ STK3<br>Founders"]):::stakeholder

  bif1 --> stk1
  bif2 --> stk1
  bif2 --> stk2
  bif3 --> stk1
  bif4 --> stk2
  bif5 -.-> stk2
  bif5 -.-> stk3

  classDef interface fill:#e5d95f,stroke:#7a6c00,color:#333
  classDef stakeholder fill:#f4ecfc,stroke:#9575cd,color:#333
```

Every edge reads **serves**. **`STK3` has exactly one edge, and it is
dashed** — nothing in operation today reaches a founder at the idea stage.

| ID | Interface | Serves | Relationship | Cost to operate | Source |
| -- | --------- | ------ | ------------ | --------------- | ------ |
| `BIF1` | The public repository | `STK1` | Self-service | Zero | `CH1` Channel 1 |
| `BIF2` | The guidance site | `STK1`, and any owner evaluating the method | Self-service | Zero — free hosting | `CH2` |
| `BIF3` | The plugin marketplace | `STK1`, already working in an agent | Self-service | Zero | `CH3` |
| `BIF4` | Referral and direct approach | `STK2` | Personal and direct — the Requester individually | The Requester's whole available time | `CH4` |
| `BIF5` | The web, self-serve | `STK2`, `STK3` | Self-service | **Pending** — inference dominates, and it scales with use | `CH5` |

**Four of five interfaces reach only people already looking.** `BIF1`–`BIF3`
find those close to the tooling and `BIF4` needs someone to make an
introduction. `BIF5` is the only one that would reach an owner who is not
already searching, and it is Pending on `COA2` — which is the same gap the
[value stream](../1_strategy/3_value-stream.md#where-the-stream-is-weak)
records at stage 1, seen from the interface side.
