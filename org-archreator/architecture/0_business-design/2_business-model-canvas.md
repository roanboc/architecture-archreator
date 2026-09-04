# Business model canvas

_[← Business design](./README.md) · [Front door](../README.md)_

**Not an ArchiMate layer.** How the organization around
[archreator, the open method [PROD1]](./1_value-proposition-canvas.md) and
[Consulting [PROD2]](./1_value-proposition-canvas.md) actually operates and
pays for itself.

**Status:** ◐ Draft catalogue — not yet approved at a gate. **Direction**
covers this document.

## How to read this document

```mermaid
flowchart LR
  kp{{"⧉ «Key Partner» who is depended on [KP#]"}}:::partner
  ka{{"⚙ «Key Activity» what must be done [KA#]"}}:::activity
  kr[("▤ «Key Resource» what it takes [KR#]")]:::resource
  ch["⊸ «Channel» how it reaches someone [CH#]"]:::channel
  cr["⇄ «Customer Relationship» what kind of contact [CR#]"]:::relationship
  rs[/"▲ «Revenue Stream» what comes in [RS#]"\]:::revenue
  cost[\"▼ «Cost» what goes out [COST#]"/]:::cost
  prod["▣ «Product» what is offered — defined in the value proposition canvas [PROD#]"]:::product
  cs(["◍ «Customer Segment» who is served — defined there too [CS#]"]):::segment

  kp -->|enables| ka
  kr -->|enables| ka
  ka -->|delivers| prod
  prod -->|carried by| ch
  ch -->|establishes| cr
  ch -->|reaches| cs
  cr -->|produces| rs
  ka -->|incurs| cost

  classDef partner fill:#f7f099,stroke:#b8ad3f,color:#333
  classDef activity fill:#f7f099,stroke:#b8ad3f,color:#333
  classDef resource fill:#faf0d5,stroke:#d4b96a,color:#333
  classDef channel fill:#e5d95f,stroke:#a89a34,color:#333
  classDef relationship fill:#efe57d,stroke:#b8ad3f,color:#333
  classDef revenue fill:#c9e7b7,stroke:#558b2f,color:#333
  classDef cost fill:#ffd6d6,stroke:#c62828,color:#333
  classDef product fill:#efe57d,stroke:#b8ad3f,color:#333
  classDef segment fill:#fffbb5,stroke:#c8c04a,color:#333
```

Revenue is green and cost is rose, so the arithmetic is visible without
reading a label. The segments and products keep the identifiers
[the value proposition canvas](./1_value-proposition-canvas.md) defines.

## The products at a glance

```mermaid
flowchart LR
  ka1{{"⚙ Developing and improving the method [KA1]"}}:::activity
  ka2{{"⚙ Publishing guidance [KA2]"}}:::activity
  ka3{{"⚙ Running discovery and delivery with clients [KA3]"}}:::activity

  p1["▣ archreator, the open method [PROD1]"]:::product
  p2["▣ Consulting [PROD2]"]:::product

  ch1["⊸ The public repository [CH1]"]:::channel
  ch2["⊸ The guidance site [CH2]"]:::channel
  ch3["⊸ The plugin marketplace [CH3]"]:::channel
  ch4["⊸ Referral and direct approach [CH4]"]:::channel

  cr1["⇄ Self-service [CR1]"]:::relationship
  cr2["⇄ Personal and direct [CR2]"]:::relationship

  cs1(["◍ Independent builder [CS1]"]):::segment
  cs2(["◍ Enterprise architect [CS2]"]):::segment
  cs3(["◍ Business owner [CS3]"]):::segment

  ka1 -->|delivers| p1
  ka2 -->|delivers| p1
  ka3 -->|delivers| p2

  p1 -->|carried by| ch1
  p1 -->|carried by| ch2
  p1 -->|carried by| ch3
  p2 -->|carried by| ch4

  p1 -->|contact is| cr1
  p2 -->|contact is| cr2

  ch1 -->|reaches| cs1
  ch1 -->|reaches| cs2
  ch2 -->|reaches| cs1
  ch2 -->|reaches| cs2
  ch3 -->|reaches| cs1
  ch3 -->|reaches| cs2
  ch4 -->|reaches| cs3

  classDef activity fill:#f7f099,stroke:#b8ad3f,color:#333
  classDef product fill:#efe57d,stroke:#b8ad3f,color:#333
  classDef channel fill:#e5d95f,stroke:#a89a34,color:#333
  classDef relationship fill:#efe57d,stroke:#b8ad3f,color:#333
  classDef segment fill:#fffbb5,stroke:#c8c04a,color:#333
```

**Three channels converge on two segments and one product; one channel is a
person.** That is the same asymmetry the table below states in its last row,
drawn: everything on the `PROD1` side fans out and costs nothing per user,
and everything on the `PROD2` side passes through a single line.

| | archreator, the open method [`PROD1`] | Consulting [`PROD2`] |
| --- | --- | --- |
| **Segments** | `CS1`, `CS2` | `CS3` |
| **Channels** | `CH1`, `CH2`, `CH3` | `CH4` |
| **Relationship** | `CR1` | `CR2` |
| **Revenue** | `RS1`, `RS2` — non-monetary | `RS3` |
| **Dominant cost** | `COST1` | `COST1` |
| **Scales?** | Yes, freely | **No** — bounded by one person's hours |

**The last row is the model's central tension.** The product that earns
money cannot grow, and the product that grows earns feedback and mission
progress rather than money — deliberately, per
[Priced at the cost of running it [P7]](../1_strategy/1_motivation.md#principles).

A third product — **a self-service portal**, everything the consulting
route does but self-served — is deliberately absent: it waits on the method
proving itself, and enters the model when an initiative through Direction
makes it real.

## Channels

| ID | Channel | Carries | Reaches | State |
| -- | ------- | ------- | ------- | ----- |
| `CH1` | The public repository — they find it as code, not as marketing | `PROD1` | `CS1`, `CS2` | Live |
| `CH2` | The guidance site — also where an owner evaluates the method before adopting | `PROD1` | `CS1`, `CS2` | Live |
| `CH3` | The plugin marketplace — reaching them already working inside an agent | `PROD1` | `CS1`, `CS2` | Live |
| `CH4` | Referral and direct approach | `PROD2` | `CS3` | Live |

## Customer relationships

| ID | Relationship | For | Costs |
| -- | ------------ | --- | ----- |
| `CR1` | Self-service | `PROD1` | Near zero per user |
| `CR2` | Personal and direct — the Requester individually | `PROD2` | Their whole available time |

## Key activities

| ID | Activity | For | Performed by |
| -- | -------- | --- | ------------ |
| `KA1` | Developing and improving the method | `PROD1` | The Requester, with an AI agent at co-pilot autonomy |
| `KA2` | Publishing guidance | `PROD1` | The Requester, with an AI agent |
| `KA3` | Running discovery and delivery with clients | `PROD2` | The Requester |

## Key resources

| ID | Resource | Kind | State |
| -- | -------- | ---- | ----- |
| `KR1` | The Requester's knowledge and time | People | **Constrained — the binding limit on the whole organization** |
| `KR2` | The method: skills, conventions, gates | Knowledge | Held, and improving |
| `KR3` | The published guidance site | Asset | Held |

## Key partners

| ID | Partner | Provides | Note |
| -- | ------- | -------- | ---- |
| `KP1` | AI model providers | The inference every product ultimately runs on | **Substitutable by design.** The method is provider-agnostic prose; only the packaging names a platform |
| `KP2` | The code host | Repository, plugin distribution, site hosting | Replaceable, and free at this scale |

## Revenue streams and cost structure

```mermaid
flowchart TB
  rs1[/"▲ Continuous improvement — non-monetary [RS1]"\]:::revenue
  rs2[/"▲ Mission progress — non-monetary [RS2]"\]:::revenue
  rs3[/"▲ Consulting fees — the only money in [RS3]"\]:::revenue

  p1["▣ archreator, the open method [PROD1]"]:::product
  p2["▣ Consulting [PROD2]"]:::product

  c1[\"▼ The Requester's time — dominant [COST1]"/]:::cost
  c2[\"▼ AI inference [COST2]"/]:::cost
  c3[\"▼ Hosting the repository and site [COST3]"/]:::cost

  p1 -->|produces| rs1
  p1 -->|produces| rs2
  p2 -->|produces| rs3

  c1 -->|is spent on| p1
  c1 -->|is spent on| p2
  c2 -->|is spent on| p1
  c2 -->|is spent on| p2
  c3 -->|is spent on| p1

  classDef revenue fill:#c9e7b7,stroke:#558b2f,color:#333
  classDef product fill:#efe57d,stroke:#b8ad3f,color:#333
  classDef cost fill:#ffd6d6,stroke:#c62828,color:#333
```

**Only one green box is money, and it hangs off the product that cannot
grow.** The product carrying every cost returns feedback and mission
progress instead of revenue, which is the arithmetic
[Priced at the cost of running it [P7]](../1_strategy/1_motivation.md#principles)
accepts on purpose rather than a shortfall to fix.

| ID | Revenue stream | Kind | From | Note |
| -- | -------------- | ---- | ---- | ---- |
| `RS1` | **Continuous improvement** — feedback and real usage flowing back into the method | Non-monetary | `PROD1` | Grows with adoption; the method improves because people use it where the Requester is not |
| `RS2` | **Mission progress** — people building better things with AI while human knowledge improves rather than being delegated away | Non-monetary | `PROD1` | The reason the organization exists |
| `RS3` | Consulting fees | Monetary | `PROD2` | Hourly; bounded by one person's available time |

| ID | Cost | For | Note |
| -- | ---- | --- | ---- |
| `COST1` | **The Requester's time** | `PROD1`, `PROD2` | **Dominant, and the binding constraint on everything** |
| `COST2` | AI inference | `PROD1`, `PROD2` | Each adopter carries their own; the organization pays only for its own use |
| `COST3` | Hosting the repository and site | `PROD1` | Effectively zero — free tiers |

**The Requester appears three times** — a key resource, the dominant cost,
and a stakeholder with wants of their own. That triple entry is the
organization's central fact, not a modelling accident.

## From canvas to ArchiMate

```mermaid
flowchart LR
  subgraph canvas["0_business-design — the canvases"]
    cs(["◍ «Customer Segment» [CS#]"]):::segment
    pain>"✖ «Pain» [PAIN#]"]:::pain
    jobgain{{"⚙ «Job» and ✔ «Gain» [JOB#, GAIN#]"}}:::activity
    kavalue{{"⚙ «Key Activity», ⊖ «Pain Reliever», ⊕ «Gain Creator» [KA#, PREL#, GCRE#]"}}:::activity
    kr[("▤ «Key Resource» [KR#]")]:::kres
    chcr["⊸ «Channel» and ⇄ «Customer Relationship» [CH#, CR#]"]:::channel
  end

  subgraph motivation["1_strategy — motivation"]
    stk(["◍ «Stakeholder» [STK#]"]):::stakeholder
    drv{{"✳ «Driver» with its ⌕ «Assessment» [DRV#, ASM#]"}}:::driver
    goal("◎ «Goal» with its ◉ «Outcome» [G#, OUT#]"):::goal
  end

  subgraph strategy["1_strategy — capabilities"]
    cap["✦ «Capability» [CAP#]"]:::capability
    res[("▤ «Resource» [RES#]")]:::sres
  end

  subgraph business["2_business"]
    bsvc(["⬭ «Business Service» and how it is reached [BSVC#]"]):::bservice
  end

  cs -->|becomes| stk
  pain -->|becomes| drv
  jobgain -->|becomes| goal
  kavalue -->|becomes| cap
  kr -->|becomes| res
  chcr -->|becomes| bsvc

  classDef segment fill:#fffbb5,stroke:#c8c04a,color:#333
  classDef pain fill:#ffd6d6,stroke:#c62828,color:#333
  classDef activity fill:#f7f099,stroke:#b8ad3f,color:#333
  classDef kres fill:#faf0d5,stroke:#d4b96a,color:#333
  classDef channel fill:#e5d95f,stroke:#a89a34,color:#333
  classDef stakeholder fill:#f4ecfc,stroke:#9575cd,color:#333
  classDef driver fill:#e6d6f5,stroke:#8e63c8,color:#333
  classDef goal fill:#c6aae9,stroke:#6f4bb2,color:#333
  classDef capability fill:#f5deaa,stroke:#c8a24a,color:#333
  classDef sres fill:#faf0d5,stroke:#c8a24a,color:#333
  classDef bservice fill:#efe57d,stroke:#b8ad3f,color:#333
```

**This is the one diagram in the model whose subject is the notation**, so
its nodes carry stereotypes where every other diagram drops them. Stated
once, here; the [strategy layer](../1_strategy/README.md) cites it per
element rather than restating it.

| Canvas block | Becomes | In |
| ------------ | ------- | -- |
| Customer segment | «Stakeholder» | [Motivation](../1_strategy/1_motivation.md) |
| Pain | «Driver» and its «Assessment» | Motivation |
| Job, gain | «Goal» and its «Outcome» | Motivation |
| Key activity, pain reliever, gain creator | «Capability» | [Capabilities](../1_strategy/2_capabilities-and-value-stream.md) |
| Key resource | «Resource» | Capabilities |
| Channel, relationship | The service's access, on the business layer | [Business](../2_business/README.md) |
