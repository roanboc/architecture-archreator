# Value proposition canvas

_[← Business design](./README.md) · [Front door](../README.md)_

Who the organization serves, what they are trying to get done, what hurts,
what would delight them, and what the organization offers against each.

**ArchiMate viewpoint:** none; a Strategyzer Value Proposition Canvas, one per
customer segment.

**Status:** ◐ Draft catalogue, not yet approved at Direction.

## Segments

```mermaid
flowchart LR
  p1["▣ archreator, the open method [PROD1]"]:::product
  p2["▣ Consulting [PROD2]"]:::product

  subgraph free["One model, two ways in — and neither of them pays"]
    cs1(["◍ Independent builder, guided [CS1]"]):::segment
    cs2(["◍ Enterprise architect, expert [CS2]"]):::segment
  end

  cs3(["◍ Business owner, served personally [CS3]"]):::segment

  p1 -->|serves| cs1
  p1 -->|serves| cs2
  p2 -->|serves| cs3

  classDef segment fill:#fffbb5,stroke:#c8c04a,color:#333
  classDef product fill:#efe57d,stroke:#b8ad3f,color:#333
```

The method serves two different customers over one model with two ways in:
guided use for the builder, direct navigation for the architect. The product
with two segments earns nothing from either; the one that earns has a single
segment and a single person behind it.

| ID | Segment | How they arrive | Pays |
| -- | ------- | --------------- | ---- |
| `CS1` | **Independent builder.** Builds something real, such as an app, a tool or a business, with a coding agent and no architecture background. The primary guided customer: they explain the business and get only the architecture they need | Finds the method as code or through the site, installs it, uses it on their own project | Nothing; the free tier by design |
| `CS2` | **Enterprise architect.** Architects, business analysts and solution designers who know the discipline. The first-class expert customer: they navigate the standard layered structure directly and use the agent as leverage, not as a doorway | Same channels as `CS1`, already fluent | Nothing |
| `CS3` | **Business owner.** A company with real operational knowledge and no structure a builder can act on, running today or still at the idea stage. The stage changes the price sensitivity, not the segment | Referral and direct approach; served personally by the Requester | Consulting hours |

`CS1` and `CS2` will never pay, and the method is written for them. They
adopt it, exercise it on real problems and are the only plausible source of
the feedback the method improves from. They are not a funnel to a paid tier.

## Jobs to be done

| ID | Job | `CS1` | `CS2` | `CS3` |
| -- | --- | ----- | ----- | ----- |
| `JOB1` | **Understand the problem before answering it.** Solutions rarely fail because they were technically hard; they fail because the problem was misunderstood, and designing is how the understanding happens | Core | Core | Core |
| `JOB2` | **Turn that understanding into a delivered solution**, by building it with an agent or by directing a builder well | Core, builds it | Core, directs and builds | Core, directs a builder |
| `JOB3` | **Keep one shared source others can work from**, so the same explanation is not repeated to every new person or agent | Core | Core | Core |
| `JOB4` | **Get architectural quality without scarce expertise**: without years of seniority and without hiring someone expensive | Core | Secondary; they are the expertise and want their time back | Core |
| `JOB5` | **Change direction without losing the work already designed** | Secondary | Secondary | Core |

## Pains

| ID | Pain | `CS1` | `CS2` | `CS3` |
| -- | ---- | ----- | ----- | ----- |
| `PAIN1` | **The problem is framed wrongly, and nobody finds out until late.** Without a method that forces a complete frame, blind spots stay invisible | Unacceptable | Serious | Unacceptable |
| `PAIN2` | **Design and delivery are separate worlds.** Meaning changes shape at every handover, documentation that drives nothing is a cost, and time to market pays for it | Unacceptable | Unacceptable | Unacceptable |
| `PAIN3` | **Knowledge is scattered, stale, or trapped in one person's head**. When a builder leaves, the owner explains it all again | Unacceptable | Unacceptable | Unacceptable |
| `PAIN4` | **Architectural quality is out of reach**. An architect costs more than these segments can justify, and doing it yourself takes years | Unacceptable | — | Unacceptable |
| `PAIN5` | **AI already does most of this work, but in isolation, with no framework behind it.** The person is the framework, holding it together by hand | Unacceptable | Unacceptable | Serious |
| `PAIN6` | **Token cost compounds as the solution grows.** Building without an architecture is cheap on day one; maintaining is not, because the agent traverses the entire project looking for answers to every question | Unacceptable | Serious | Serious |

## Gains

| ID | Gain | Level | Strongest for |
| -- | ---- | ----- | ------------- |
| `GAIN1` | **Understand the business wider and deeper**, with strategic and business gaps surfacing during the work rather than after it | Required | segment `CS3` |
| `GAIN2` | **Documentation ready to put in front of the business** without a rewrite: diagrams over walls of text | Expected | segment `CS2` |
| `GAIN3` | **Build from the design**. The design is the input to delivery, with AI doing the technical work | Delight | segment `CS1` |
| `GAIN4` | **A shared language that keeps working** as people and agents join and leave | Expected | segment `CS2` |
| `GAIN5` | **Speed with structure, at any level of experience**. Competence comes from the method rather than from seniority or budget | Required | segment `CS1` |
| `GAIN6` | **Pivots that cost less**, because the design survives the change instead of being redone | Expected | segment `CS3` |

## Value map

### Products

| ID | Product | For | Price | State |
| -- | ------- | --- | ----- | ----- |
| `PROD1` | **archreator, the open method**: the skills, the scaffold, the documentation, the guidance site | segments `CS1`, `CS2` | Free, open source | Live |
| `PROD2` | **Consulting**: the Requester's time, delivering with archreator | segment `CS3` | Hourly | Live |

### Pain relievers

```mermaid
flowchart LR
  p1["▣ archreator, the open method [PROD1]"]:::product
  p2["▣ Consulting [PROD2]"]:::product

  r1[/"⊖ The gated layer walk [PREL1]"\]:::reliever
  r2[/"⊖ The method continues into delivery [PREL2]"\]:::reliever
  r3[/"⊖ One model in one place [PREL3]"\]:::reliever
  r4[/"⊖ An agent instead of an architect [PREL4]"\]:::reliever
  r5[/"⊖ The whole thing operating together [PREL5]"\]:::reliever
  r6[/"⊖ The model bounds what an agent reads [PREL6]"\]:::reliever

  a1>"✖ Framed wrongly, found out late [PAIN1]"]:::pain
  a2>"✖ Design and delivery are separate worlds [PAIN2]"]:::pain
  a3>"✖ Knowledge scattered, stale or in one head [PAIN3]"]:::pain
  a4>"✖ Architectural quality out of reach [PAIN4]"]:::pain
  a5>"✖ AI works in isolation, with no framework [PAIN5]"]:::pain
  a6>"✖ Token cost compounds as the solution grows [PAIN6]"]:::pain

  p1 -->|offers| r1
  p1 -->|offers| r2
  p1 -->|offers| r3
  p1 -->|offers| r4
  p1 -->|offers| r5
  p1 -->|offers| r6
  p2 -->|offers| r2
  p2 -->|offers| r5

  r1 -->|relieves| a1
  r2 -->|relieves| a2
  r3 -->|relieves| a3
  r4 -->|relieves| a4
  r5 -->|relieves| a5
  r6 -->|relieves| a6

  classDef product fill:#efe57d,stroke:#b8ad3f,color:#333
  classDef reliever fill:#ffe9e9,stroke:#d99b9b,color:#333
  classDef pain fill:#ffd6d6,stroke:#c62828,color:#333
```

The free product carries the whole value map and the paid one borrows two
relievers from it. Nothing in `PROD2` relieves a pain `PROD1` does not
already reach, so the consulting route is a delivery channel for the method
rather than a second offering.

| ID | Pain reliever | Relieves | Offered by |
| -- | ------------- | -------- | ---------- |
| `PREL1` | **The gated layer walk.** Approval gates force a complete frame before anything is built, so a misframed problem surfaces at the gate rather than at delivery | pain `PAIN1` | product `PROD1` |
| `PREL2` | **The method continues past design into delivery.** The design is what an agent builds from, so there is no handover for meaning to change shape in | pain `PAIN2` | products `PROD1`, `PROD2` |
| `PREL3` | **One model in one place**: Markdown in git, catalogues and diagrams, every element naming what realizes it | pain `PAIN3` | product `PROD1` |
| `PREL4` | **The cost of an architect collapses to the cost of an agent**: a subscription instead of consultancy hours, with the adopter's own coding agent doing the work | pain `PAIN4` | product `PROD1` |
| `PREL5` | **The whole thing operating together**: skills holding the method, gates keeping a human in the loop, and a model the solution is built from | pain `PAIN5` | products `PROD1`, `PROD2` |
| `PREL6` | **The model bounds what an agent reads.** A question is answered from the layer that owns it instead of a traversal of the whole project, so token spend falls as the solution grows: somewhat dearer on day one, cheaper every month after. The claim still needs validation in real use | pain `PAIN6` | product `PROD1` |

### Gain creators

```mermaid
flowchart LR
  p1["▣ archreator, the open method [PROD1]"]:::product
  p2["▣ Consulting [PROD2]"]:::product

  c1[/"⊕ Question-driven discovery [GCRE1]"\]:::creator
  c2[/"⊕ Markdown and diagrams, written for people [GCRE2]"\]:::creator
  c3[/"⊕ Skills that turn a design into work [GCRE3]"\]:::creator
  c4[/"⊕ Standardised concepts with defined relationships [GCRE4]"\]:::creator
  c5[/"⊕ The method carries the competence [GCRE5]"\]:::creator
  c6[/"⊕ The layered model [GCRE6]"\]:::creator

  g1[["✔ Understand the business wider and deeper [GAIN1]"]]:::gain
  g2[["✔ Documentation ready for the business [GAIN2]"]]:::gain
  g3[["✔ Build from the design [GAIN3]"]]:::gain
  g4[["✔ A shared language that keeps working [GAIN4]"]]:::gain
  g5[["✔ Speed with structure, at any level [GAIN5]"]]:::gain
  g6[["✔ Pivots that cost less [GAIN6]"]]:::gain

  p1 -->|offers| c1
  p1 -->|offers| c2
  p1 -->|offers| c3
  p1 -->|offers| c4
  p1 -->|offers| c5
  p1 -->|offers| c6
  p2 -->|offers| c1
  p2 -->|offers| c5

  c1 -->|creates| g1
  c2 -->|creates| g2
  c3 -->|creates| g3
  c4 -->|creates| g4
  c5 -->|creates| g5
  c6 -->|creates| g6

  classDef product fill:#efe57d,stroke:#b8ad3f,color:#333
  classDef creator fill:#dcefd0,stroke:#7aa860,color:#333
  classDef gain fill:#c9e7b7,stroke:#558b2f,color:#333
```

`PROD2` adds the two creators a person in the room supplies, the questions
and the competence, and takes the other four from the method it delivers
with.

| ID | Gain creator | Creates | Offered by |
| -- | ------------ | ------- | ---------- |
| `GCRE1` | Question-driven discovery that tests the business rather than recording it | gain `GAIN1` | products `PROD1`, `PROD2` |
| `GCRE2` | Markdown and diagrams as first-class output, written for people | gain `GAIN2` | product `PROD1` |
| `GCRE3` | Skills that turn an approved design into implementation work | gain `GAIN3` | product `PROD1` |
| `GCRE4` | **Standardised concepts with defined relationships**: ArchiMate as the shared vocabulary | gain `GAIN4` | product `PROD1` |
| `GCRE5` | The method carries the competence, so experience level stops being the gate | gain `GAIN5` | products `PROD1`, `PROD2` |
| `GCRE6` | The layered model: strategy can change without redoing technology, and the reverse | gain `GAIN6` | product `PROD1` |

## Fit check

Every pain has a reliever and every gain a creator. Passing the check says
something is pointed at each pain, not that the relief works for every
segment.

| Check | Result |
| ----- | ------ |
| Every pain has at least one pain reliever | Holds. `PAIN1` to `PAIN6` are relieved by `PREL1` to `PREL6`, one each |
| Every gain has at least one gain creator | Holds. `GAIN1` to `GAIN6` are created by `GCRE1` to `GCRE6`, one each |
| Every pain reliever and gain creator traces to a capability | Open. The [capabilities](../1_strategy/2_capabilities-and-value-stream.md) are derived from the key activities, and no row yet names which capability carries each reliever or creator |
| Every product has its own business model canvas | Holds. Two products, two canvases in the [business model canvas](./2_business-model-canvas.md) |
