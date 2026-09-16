# Business design

_[← Front door](../README.md)_

Who the organization serves, what hurts them, what is offered against it, and
how the whole thing pays for itself.

**ArchiMate viewpoint:** none. Two Strategyzer canvases: a Value Proposition
Canvas per customer segment and a Business Model Canvas per product. The
[strategy layer](../1_strategy/README.md) is derived from their blocks.

## Documents

| # | Document | Elements | Question it answers |
| - | -------- | -------- | ------------------- |
| 1 | [Value proposition canvas](./1_value-proposition-canvas.md) | Segments, jobs, pains, gains; the products, pain relievers and gain creators offered against them | Who do we serve, what do they need, and what do we offer? |
| 2 | [Business model canvas](./2_business-model-canvas.md) | Channels, customer relationships, key activities, key resources, key partners, revenue streams and costs | How is each product delivered, and how does it pay? |

## Metamodel

```mermaid
flowchart LR
  %% legend
  subgraph VPC["Value proposition canvas"]
    cs(["◍ «Customer Segment» who is served [CS#]"]):::segment
    job{{"⚙ «Customer Job» what they are trying to do [JOB#]"}}:::job
    pain>"✖ «Pain» what hurts on the way [PAIN#]"]:::pain
    gain[["✔ «Gain» what would be better than fine [GAIN#]"]]:::gain
    prod["▣ «Product» what is offered [PROD#]"]:::product
    prel[/"⊖ «Pain Reliever» it subtracts [PREL#]"\]:::reliever
    gcre[/"⊕ «Gain Creator» it adds [GCRE#]"\]:::creator
  end
  subgraph BMC["Business model canvas"]
    kp{{"⧉ «Key Partner» who is depended on [KP#]"}}:::partner
    ka{{"⚙ «Key Activity» what must be done [KA#]"}}:::activity
    kr[("▤ «Key Resource» what it takes [KR#]")]:::kresource
    ch["⊸ «Channel» how it reaches someone [CH#]"]:::channel
    cr["⇄ «Customer Relationship» what kind of contact [CR#]"]:::relationship
    rs[/"▲ «Revenue Stream» what comes in [RS#]"\]:::revenue
    cost[\"▼ «Cost» what goes out [COST#]"/]:::cost
  end

  cs -->|has| job
  job -->|obstructed by| pain
  job -->|improved by| gain
  prod -->|offers| prel
  prod -->|offers| gcre
  prel -->|relieves| pain
  gcre -->|creates| gain
  prod -->|serves| cs
  kp -->|enables| ka
  kr -->|enables| ka
  ka -->|delivers| prod
  prod -->|carried by| ch
  ch -->|reaches| cs
  prod -->|contact is| cr
  prod -->|produces| rs
  cost -->|is spent on| prod

  classDef segment fill:#fffbb5,stroke:#c8c04a,color:#333
  classDef job fill:#f7f099,stroke:#b8ad3f,color:#333
  classDef pain fill:#ffd6d6,stroke:#c62828,color:#333
  classDef gain fill:#c9e7b7,stroke:#558b2f,color:#333
  classDef product fill:#efe57d,stroke:#b8ad3f,color:#333
  classDef reliever fill:#ffe9e9,stroke:#d99b9b,color:#333
  classDef creator fill:#dcefd0,stroke:#7aa860,color:#333
  classDef partner fill:#f7f099,stroke:#b8ad3f,color:#333
  classDef activity fill:#f7f099,stroke:#b8ad3f,color:#333
  classDef kresource fill:#faf0d5,stroke:#d4b96a,color:#333
  classDef channel fill:#e5d95f,stroke:#a89a34,color:#333
  classDef relationship fill:#efe57d,stroke:#b8ad3f,color:#333
  classDef revenue fill:#c9e7b7,stroke:#558b2f,color:#333
  classDef cost fill:#ffd6d6,stroke:#c62828,color:#333
```

Revenue is green and cost is rose, so the arithmetic is visible without
reading a label. The segments and the products appear on both canvases and
keep the identifiers the value proposition canvas gives them.

## Layer view

```mermaid
flowchart LR
  cs1(["◍ Independent builder [CS1]"]):::segment
  cs2(["◍ Enterprise architect [CS2]"]):::segment
  cs3(["◍ Business owner [CS3]"]):::segment
  p1["▣ archreator, the open method [PROD1]"]:::product
  p2["▣ Consulting [PROD2]"]:::product
  rs1[/"▲ Continuous improvement, non-monetary [RS1]"\]:::revenue
  rs3[/"▲ Consulting fees [RS3]"\]:::revenue
  c1[\"▼ The Requester's time [COST1]"/]:::cost

  p1 -->|serves| cs1
  p1 -->|serves| cs2
  p2 -->|serves| cs3
  p1 -->|produces| rs1
  p2 -->|produces| rs3
  c1 -->|is spent on| p1
  c1 -->|is spent on| p2

  classDef segment fill:#fffbb5,stroke:#c8c04a,color:#333
  classDef job fill:#f7f099,stroke:#b8ad3f,color:#333
  classDef pain fill:#ffd6d6,stroke:#c62828,color:#333
  classDef gain fill:#c9e7b7,stroke:#558b2f,color:#333
  classDef product fill:#efe57d,stroke:#b8ad3f,color:#333
  classDef reliever fill:#ffe9e9,stroke:#d99b9b,color:#333
  classDef creator fill:#dcefd0,stroke:#7aa860,color:#333
  classDef partner fill:#f7f099,stroke:#b8ad3f,color:#333
  classDef activity fill:#f7f099,stroke:#b8ad3f,color:#333
  classDef kresource fill:#faf0d5,stroke:#d4b96a,color:#333
  classDef channel fill:#e5d95f,stroke:#a89a34,color:#333
  classDef relationship fill:#efe57d,stroke:#b8ad3f,color:#333
  classDef revenue fill:#c9e7b7,stroke:#558b2f,color:#333
  classDef cost fill:#ffd6d6,stroke:#c62828,color:#333
```

The product with two segments earns feedback rather than money; the product
that earns money has one segment and one person's time behind it.
