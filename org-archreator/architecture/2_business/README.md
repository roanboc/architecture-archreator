# Business Layer

_[← EA home](../README.md)_

Who interacts with the system, the services it offers them, the processes
those services run through, the business objects they handle, and the
domain vocabulary and rules that constrain all of it.

## Analysis order

Files are numbered in the order they are analyzed: identify _who_ first,
then _what they are offered_, then _how it is delivered_, then _what is
handled_, and finally the domain vocabulary and rules.

| #   | Document                                                          | Elements                                           | Question it answers                              |
| --- | -------------------------------------------------------------------| ---------------------------------------------------- | --------------------------------------------------- |
| 1   | [1_business-actors-and-roles.md](./1_business-actors-and-roles.md) | Business Actors and Roles, organizational units, external partners (Contracts, Collaborations) | Who interacts with the system, and who do we depend on? |
| 2   | [2_business-services.md](./2_business-services.md)                | Products, Business Services, Business Interfaces (channels) | What is offered to them, and through which channels? |
| 3   | [3_business-processes.md](./3_business-processes.md) — or a folder of the same name, one document per level, once leveled | Business Processes | How are those services delivered, and at what level of detail? |
| 4   | [4_business-objects.md](./4_business-objects.md)                  | Business Objects                                   | What things do the processes handle?              |
| 5   | [5_domain-context-and-rules.md](./5_domain-context-and-rules.md)  | Problem statement, system context, glossary, rules | What vocabulary and constraints bind everything?  |

[3_business-processes.md](./3_business-processes.md) holds the **macro process
map**: six processes at level 1, classified into the four bands — strategic,
operational, support and evaluation. **Nothing is decomposed to level 2**, and
the focus table there records that decision per branch, which is what
separates a scoped model from an unfinished one.

Two of the four bands are empty, and the document treats that as a finding
about the organization rather than a hole in the model.

[5_domain-context-and-rules.md](./5_domain-context-and-rules.md) carries the project's **glossary** (reuse
its terms in code and commits) and its **business rules table** — every new
rule gets a row there, with its rationale, before it gets a line of code.
It is also the natural home for a role × operation access matrix if the
project has segregated roles.

[2_business-services.md](./2_business-services.md) is where a **«Product»** aggregates the services
that make it up. A single-application project usually has one implicit
product and can leave it out; an organization sells several, and the
portfolio is what makes the rest of the model make sense — two products may
share every capability and still need entirely different channels and
processes. On the company track the products, channels, and customer
relationships are derived from the business model canvases (see
[0_business-design/](../0_business-design/README.md#from-canvas-to-archimate)),
and Key Partners land in [1_business-actors-and-roles.md](./1_business-actors-and-roles.md) as external
actors, each with the «Contract» or «Business Collaboration» that binds
them.

[1_business-actors-and-roles.md](./1_business-actors-and-roles.md) states each actor's **kind** — human, AI,
or hybrid — and, for AI/hybrid actors, its autonomy level, decision
rights, and escalation path (see the `architecture-document-style` skill's actor
notation). This is where an AI system's role **in the business being
modeled** gets stated explicitly — not just its role in how this repo is
developed (see `CONTRIBUTING.md`). If an initiative changes one of those
values, consider a `record-decision` alongside the scope document.

## Layer view

```mermaid
flowchart TB
  act1(["⚇ The Requester (Human) [ACT1]"]):::business
  act2(["⚇ The AI agent, co-pilot (AI) [ACT2]"]):::application
  role2["⚉ Consultant [ROLE2]"]:::business
  svc(["⬭ Advisory and delivery [BSVC3]"]):::business
  proc{{"⚙ Frame [BPROC2]"}}:::business
  obj["▧ An engagement [BOBJ5]"]:::external

  act1 -->|assigned to| role2
  act2 -->|assists in| role2
  role2 -->|delivers| svc
  proc -->|realizes| svc
  proc -->|accesses, never keeps| obj

  classDef business fill:#fffbb5,stroke:#b8a200,color:#333
  classDef application fill:#c2f0ff,stroke:#0288d1,color:#333
  classDef external fill:#eeeeee,stroke:#999999,color:#333
```

The AI actor is drawn in the Application cyan even inside a business diagram,
so a reader never mistakes it for a person — and it **assists in** the role
rather than being assigned to it, which is `P1` drawn rather than asserted.
The grey object belongs to the client.

The AI actor is drawn in the Application cyan even though it sits in a
business diagram — one of the two colour overrides in
[README.md § Notation conventions](../README.md#notation-conventions), so a
reader never mistakes it for a person.

Every business service is realized by application services — the mapping is
in `4_application/1_application-services.md`.

## Relationships

<!-- Transcribed from this document's diagrams. The identifier is
     authoritative; the description beside it is checked against the
     catalogue that defines the element. -->

| From | From element | To | To element | Relationship |
| ---- | ------------ | -- | ---------- | ------------ |
| `ACT2` | «Actor» The AI agent | `ROLE2` | «Role» Consultant | assists in |
| `ROLE2` | «Role» Consultant | `BSVC3` | «Business Service» Advisory and delivery with the method | delivers |
