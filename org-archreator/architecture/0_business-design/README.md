# Business Design Layer

_[← EA home](../README.md)_

The business model itself, in the language the business uses: who the
customers are, what they are trying to get done, what hurts today, and which
product or service relieves it — plus, for each product, how it is delivered
and paid for.

This folder is **not an ArchiMate layer**. Its two documents are
[Value Proposition Canvas](https://www.strategyzer.com/library/the-value-proposition-canvas)
and [Business Model Canvas](https://www.strategyzer.com/library/the-business-model-canvas)
artifacts — business design tools that sit *upstream* of the architecture.
They are the input the [strategy layer](../1_strategy/README.md) is derived
from, which is why they carry the number `0`: everything in layers 1–5
should be traceable back to a block on one of these canvases.

**This folder is filled only when the initiative is modeling an
organization** — a company, a department, a service line. A project that is
building a single application skips it entirely and starts at the
[strategy layer](../1_strategy/README.md), driven by the
`discover-strategy` skill. The company track is driven by the
`discover-business-model` skill instead, and ends at **Gate 0 — Business
model**, where the Requester approves these canvases before anything is
derived from them.

## Analysis order

Files are numbered in the order they are analyzed: first _who we serve and
what they need_, then _how each offering is delivered and paid for_. The
value proposition comes first because the business model is built per
product, and the products are named by the value proposition.

| #   | Document                                                             | Elements                                                                          | Question it answers                                     |
| --- | -------------------------------------------------------------------- | --------------------------------------------------------------------------------- | -------------------------------------------------------- |
| 1   | [1_value-proposition-canvas.md](./1_value-proposition-canvas.md)     | Customer Segments, Jobs, Pains, Gains, Products & Services, Pain Relievers, Gain Creators | Who do we serve, what do they need, and what do we offer? |
| 2   | [2_business-model-canvas.md](./2_business-model-canvas.md)           | The nine BMC blocks, one canvas per product or service                            | How is each offering delivered, and how does it pay?     |

[1_value-proposition-canvas.md](./1_value-proposition-canvas.md) carries one canvas **per customer segment**;
[2_business-model-canvas.md](./2_business-model-canvas.md) carries one canvas **per product or service**.
A company with two product lines serving two different segments therefore
has two of each — and the interesting architecture is usually in what they
_share_ (capabilities, resources, partners) versus what they don't (channels,
revenue, cost).

### Fit is a rule, not a comment

A value proposition canvas only means something if it *fits*. Checked at
Gate 0, and re-checked whenever either canvas changes:

- every **Pain** is addressed by at least one **Pain Reliever**;
- every **Gain** is produced by at least one **Gain Creator**;
- every Pain Reliever and Gain Creator traces to a **Capability** in
  `2_capabilities-and-resources.md`;
- every **Product & Service** has its own business model canvas.

An unaddressed Pain is not a documentation gap — it is either a missing
capability or a customer you have decided not to serve. Say which.

## From canvas to ArchiMate

This is the load-bearing part of this folder: the canvases are only worth
filling in if the architecture is *derived* from them. Each block below has
a defined destination, and the receiving document records where the element
came from. This table is the **single source** for the mapping; other
documents and skills link here rather than restating it.

### Value Proposition Canvas

| Canvas block         | ArchiMate element                                         | Derived into                                                                                                          |
| -------------------- | --------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Customer Segment     | «Stakeholder», and a «Business Actor» / «Business Role»   | `1_motivation.md`, `1_business-actors-and-roles.md` |
| Customer Job         | «Goal» of that Stakeholder (a «Business Process» they perform) | `1_motivation.md`                                                                   |
| Pain                 | «Assessment», attached to the «Driver» it assesses        | `1_motivation.md`                                                                       |
| Gain                 | «Outcome»                                                 | `1_motivation.md`                                                                       |
| Products & Services  | «Product», aggregating «Business Service»s                | `2_business-services.md`                                                         |
| Pain Reliever        | «Capability», with a «Course of Action» where a choice was made | `2_capabilities-and-resources.md`                                  |
| Gain Creator         | «Capability» delivering a «Value»                         | `2_capabilities-and-resources.md`                                       |

### Business Model Canvas

| Canvas block           | ArchiMate element                                            | Derived into                                                                          |
| ---------------------- | ------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| Customer Segments      | «Stakeholder» / «Business Actor»                             | `1_motivation.md`, `1_business-actors-and-roles.md` |
| Value Propositions     | «Value», attached to the «Product»                           | `2_business-services.md`                           |
| Channels               | «Business Interface», plus the «Business Service» delivering through it | `2_business-services.md`                 |
| Customer Relationships | «Business Service» (onboarding, support, account management) | `2_business-services.md`                           |
| Key Activities         | «Business Process», realizing a «Capability»                 | `3_business-processes.md`                         |
| Key Resources          | «Resource»                                                   | `2_capabilities-and-resources.md`         |
| Key Partners           | external «Business Actor», with a «Contract» or «Business Collaboration» | `1_business-actors-and-roles.md` |
| Revenue Streams        | **no native element** — «Value» in the monetary sense        | stays a table here, keyed to the `PROD` it belongs to                                    |
| Cost Structure         | **no native element**                                        | stays a table here, keyed to the `RES` or `CAP` that incurs it                           |

Revenue and cost have no first-class ArchiMate element, and inventing a
stereotype for them would put the model out of step with the standard. They
stay as tables in [2_business-model-canvas.md](./2_business-model-canvas.md), keyed by element ID to the
Product, Resource, or Capability they attach to — which keeps them
traceable without pretending they are architecture.

## Layer view

```mermaid
flowchart LR
  cs2(["◍ Established business owners [CS2]"]):::segment
  pain4>"✖ Architectural quality is out of reach [PAIN4]"]:::pain
  prel4[/"⊖ The cost of an architect collapses [PREL4]"\]:::reliever
  prod3["▣ The archreator portal [PROD3]"]:::pending

  cs2 -->|suffers| pain4
  prel4 -->|relieves| pain4
  prod3 -.->|would offer| prel4

  classDef segment fill:#fffbb5,stroke:#c8c04a,color:#333
  classDef pain fill:#ffd6d6,stroke:#c62828,color:#333
  classDef reliever fill:#ffe9e9,stroke:#d99b9b,color:#333
  classDef pending fill:#efe57d,stroke:#b8ad3f,color:#333,stroke-dasharray: 4 3
```

One chain of the canvas, and the dashed edge is the organization's central
gap: the reliever exists, and the product that would carry it to this segment
does not.

The canvas blocks are drawn with the Motivation and Strategy fills because
that is where they land once derived — the customer profile becomes
motivation elements, the value map becomes strategy elements. The fills come
from [`architecture/README.md` § Notation conventions](../README.md#notation-conventions),
which stays the single source for the palette.
