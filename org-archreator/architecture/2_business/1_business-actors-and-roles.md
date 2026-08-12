# Business Actors and Roles — the organization behind archreator

_[← Business layer](./README.md) · [EA home](../README.md)_

**ArchiMate elements:** Business Actor, Business Role, Contract, Business
Collaboration.

Two internal actors, three external. One of the internal two is an AI, and
per [`ea-doc-style` § Actors](../../../.claude/skills/ea-doc-style/SKILL.md)
it carries an autonomy level, concrete decision rights, and a named
escalation path.

## How to read this document

```mermaid
flowchart LR
  act(["⚇ «Business Actor»<br>who acts"]):::actor
  role["⚉ «Business Role»<br>the hat they wear"]:::role
  svc(["⬭ «Business Service»<br>what that produces"]):::service
  ctr[/"❒ «Contract»<br>what binds two parties"/]:::contract
  bcol{{"⧉ «Business Collaboration»<br>parties acting together"}}:::collab

  act -->|assigned to| role
  role -->|realizes| svc
  act -->|party to| ctr
  act -.->|party to| bcol

  classDef actor fill:#fffbb5,stroke:#b8a200,color:#333
  classDef role fill:#f7f099,stroke:#9a8800,color:#333
  classDef service fill:#efe57d,stroke:#8a7a00,color:#333
  classDef contract fill:#e5d95f,stroke:#7a6c00,color:#333
  classDef collab fill:#d9cc4a,stroke:#6b5f00,color:#333
```

| Glyph | Shape | Element | ID prefix | Reads as |
| ----- | ----- | ------- | --------- | -------- |
| `⚇` | Stadium | «Business Actor» | `ACT` | `ACT1` = Business Actor 1 |
| `⚉` | Rectangle | «Business Role» | `ROLE` | `ROLE1` = Business Role 1 |
| `⬭` | Stadium | «Business Service» | `BSVC` | `BSVC1` = Business Service 1 |
| `❒` | Parallelogram | «Contract» | `CTR` | `CTR1` = Contract 1 |
| `⧉` | Hexagon | «Business Collaboration» | `BCOL` | `BCOL1` = Business Collaboration 1 |

**Actor and service share the stadium**, distinguished by glyph and tone —
ArchiMate draws both as rounded shapes, and inventing a difference Mermaid
does not have would be a worse lie than borrowing one shape. The Business
yellow runs light for who acts to dark for what binds them.

**The glyph rides on every node; the «stereotype» word appears once** — on the
first node of each type in a diagram, dropped on the rest.

## Internal actors

```mermaid
flowchart LR
  act1(["⚇ «Business Actor (Human)» ACT1<br>The Requester"]):::actor
  act2(["⚇ «Business Actor (AI)» ACT2<br>The AI agent co-pilot"]):::actorai

  role1["⚉ «Business Role» ROLE1<br>Method maintainer"]:::role
  role2["⚉ ROLE2<br>Consultant"]:::role
  role3["⚉ ROLE3<br>Owner"]:::role

  act1 -->|assigned to| role1
  act1 -->|assigned to| role2
  act1 -->|assigned to| role3
  act2 -.->|assists in| role1
  act2 -.->|assists in| role2
  act2 -->|escalates to| act1

  classDef actor fill:#fffbb5,stroke:#b8a200,color:#333
  classDef actorai fill:#c2f0ff,stroke:#2a8fb0,color:#333
  classDef role fill:#f7f099,stroke:#9a8800,color:#333
```

**`ACT2` is drawn in the Application cyan rather than the Business yellow.**
An AI actor holds a business role and runs as software, and the colour says
so at a glance — which matters more here than palette purity, because the
whole point of naming it is that a reader should never mistake it for a
person. Its edges into roles are dashed: it assists, it does not hold them.

| ID | Actor | Kind | Roles | Autonomy level | Decision rights | Escalation path |
| -- | ----- | ---- | ----- | -------------- | --------------- | --------------- |
| `ACT1` | **The Requester** | Human | `ROLE1`, `ROLE2`, `ROLE3` | — (human) | Everything: what the method becomes, what is delivered to a client, and what is priced. The only actor who can grant a gate | — |
| `ACT2` | **The AI agent** | **AI** | Assists in `ROLE1` and `ROLE2` | **Co-pilot** — it acts, and `ACT1` reviews before the result takes effect | May draft and edit documents, write code, and propose a design within an approved frame. May **not** grant a gate, decide what the business is, or change a Principle | `ACT1`, on anything touching strategy, business, or a gate |

**One person holds all three roles**, which the diagram shows as three solid
edges from a single node. That is `RES1`
([the binding constraint](../1_strategy/2_capabilities-and-resources.md#resources))
seen from the business layer: not a staffing gap to be filled, but a
deliberate shape the model states plainly instead of implying a resilience it
does not have.

`ACT2` sits at co-pilot because of `P1` — humans hold strategy and business
judgment. Raising its autonomy is exactly the call the `decision-record`
skill exists for, and it would need `P1` revisited first.

## Roles

| ID | Role | Filled by | Covers | Source |
| -- | ---- | --------- | ------ | ------ |
| `ROLE1` | **Method maintainer** | `ACT1`, assisted by `ACT2` | Developing the method, publishing guidance — `KA1` Key Activity 1 and `KA2` | `KA1`, `KA2` |
| `ROLE2` | **Consultant** | `ACT1`, assisted by `ACT2` | Running discovery and delivery with clients — `KA3` — and capturing afterwards what the method did not cover (`CAP10`) | `KA3` |
| `ROLE3` | **Owner** | `ACT1` | Deciding direction, pricing, and what the organization is for | `KR1` Key Resource 1 |

`ROLE1` is written so a contributor could fill it unchanged — the method does
not branch on who maintains it. That is what would make `STK5`, the
contributor community, a real partner rather than an aspiration.

**`ROLE2` gained an assisting actor, and that is `COA1` starting.**
[Decision 1](../decisions/1_take-coa1-staged.md) takes the course of
action in four stages; stage 1 keeps `ACT2` at co-pilot and behind `ACT1` —
the Requester is still the person in the room. Stage 3 would raise it inside
this role, and stage 4 would put an agent in front of a client. Both need
their own decision records.

**A notation limit the model has now hit.** `ACT2` will eventually hold one
autonomy level in `ROLE1` and a different one in `ROLE2`, and the actors
table above has a single autonomy column. Today both are co-pilot, so nothing
is lost — but from stage 3 the notation cannot say what the model needs to
say. Recorded as an open question in
[scope document 3](../scope/3_take-coa1-stage-one.md) rather than fixed on
a single case.

## External actors, and what binds them

```mermaid
flowchart LR
  act1(["⚇ «Business Actor» ACT1<br>The Requester"]):::actor
  act3(["⚇ ACT3<br>AI model providers"]):::actor
  act4(["⚇ ACT4<br>GitHub"]):::actor
  act5(["⚇ ACT5<br>Contributor community — Pending"]):::actor

  ctr1[/"❒ «Contract» CTR1<br>Provider subscription terms"/]:::contract
  ctr2[/"❒ CTR2<br>Platform terms"/]:::contract
  bcol1{{"⧉ «Business Collaboration» BCOL1<br>Open-source collaboration — Pending"}}:::collab

  act1 --> ctr1
  act3 --> ctr1
  act1 --> ctr2
  act4 --> ctr2
  act1 -.-> bcol1
  act5 -.-> bcol1

  classDef actor fill:#fffbb5,stroke:#b8a200,color:#333
  classDef contract fill:#e5d95f,stroke:#7a6c00,color:#333
  classDef collab fill:#d9cc4a,stroke:#6b5f00,color:#333
```

Every edge reads **party to**. Two of the three relationships are contracts
that exist; the third is a collaboration that does not.

| ID | Actor | Provides | Bound by | Dependency | Source |
| -- | ----- | -------- | -------- | ---------- | ------ |
| `ACT3` | **AI model providers** | The inference every product ultimately runs on | `CTR1` | **Substitutable by design**, per `P6`. The method is transferable instructions; only the packaging is provider-specific | `KP1` Key Partner 1 |
| `ACT4` | **GitHub** | Repository, plugin distribution, site hosting | `CTR2` | Replaceable, and free at this scale — but `BIF1`–`BIF3` all run through it, so replacing it would mean rebuilding every channel at once | `KP2` |
| `ACT5` | **Contributor community** | Feedback and real-world use, which is `RS1` | `BCOL1` | **Pending** — no contributor base exists yet | `KP3` |

| ID | Contract or collaboration | Between | State |
| -- | ------------------------- | ------- | ----- |
| `CTR1` | Model provider subscription and usage terms | `ACT1` (and every adopter, separately) with `ACT3` | Live. Each adopter holds their own — this organization does not resell inference for `PROD1` |
| `CTR2` | Platform terms | `ACT1` with `ACT4` | Live |
| `BCOL1` | Open-source collaboration around the method | `ACT1` with `ACT5` | **Pending — future initiative.** `RS1` and `STK5` both depend on it |

`CTR1` being held separately by each adopter is what makes `P7` — priced at
the cost of running it — hold for `PROD1` without any billing at all: the
adopter pays their own provider, and this organization charges nothing.
`PROD3` is where that changes, because the portal would run the inference
itself.
