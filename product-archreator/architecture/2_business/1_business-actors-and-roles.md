# Business Actors and Roles — archreator

_[← Business layer](./README.md) · [EA home](../README.md)_

**ArchiMate elements:** Business Actor, Business Role.

Three actors, one of them an AI. Per
[`architecture-doc-style` § Actors](../../../.claude/skills/architecture-doc-style/SKILL.md),
every AI actor carries an autonomy level, concrete decision rights, and a
named escalation path.

## How to read this document

```mermaid
flowchart LR
  act(["⚇ «Business Actor» who acts"]):::actor
  role["⚉ «Business Role» the hat they wear"]:::role
  svc(["⬭ «Business Service» what that produces"]):::service

  act -->|assigned to| role
  role -->|realizes| svc

  classDef actor fill:#fffbb5,stroke:#b8a200,color:#333
  classDef role fill:#f7f099,stroke:#9a8800,color:#333
  classDef service fill:#efe57d,stroke:#8a7a00,color:#333
```

| Glyph | Shape | Element | ID prefix | Reads as |
| ----- | ----- | ------- | --------- | -------- |
| `⚇` | Stadium | «Business Actor» | `ACT` | `ACT1` = Business Actor 1 |
| `⚉` | Rectangle | «Business Role» | `ROLE` | `ROLE1` = Business Role 1 |
| `⬭` | Stadium | «Business Service» — from [2_business-services.md](./2_business-services.md) | `BSVC` | `BSVC1` = Business Service 1 |

An `(AI)` actor is drawn in the Application cyan even here, so a reader never
mistakes it for a person. **The glyph rides on every node; the «stereotype»
word appears once.**

## Actors

```mermaid
flowchart LR
  act1(["⚇ «Business Actor (Human)» Requester [ACT1]"]):::actor
  act2(["⚇ «Business Actor (AI)» Agent — co-pilot [ACT2]"]):::actorai
  act3(["⚇ «Business Actor (Human)» Reviewer [ACT3]"]):::actor

  role1["⚉ «Business Role» Requesting and approving [ROLE1]"]:::role
  role2["⚉ Executing the method [ROLE2]"]:::role
  role3["⚉ Reviewing and merging [ROLE3]"]:::role

  act1 -->|assigned to| role1
  act2 -->|assigned to| role2
  act3 -->|assigned to| role3
  act2 -.->|escalates to| act1
  act2 -.->|escalates to| act3

  classDef actor fill:#fffbb5,stroke:#b8a200,color:#333
  classDef actorai fill:#c2f0ff,stroke:#2a8fb0,color:#333
  classDef role fill:#f7f099,stroke:#9a8800,color:#333
```

**One actor per role, and the AI holds one of them outright.** `ACT2` is not
drawn assisting `ROLE2` the way an agent assists elsewhere in this
repository — it *is* the executor, and the two dashed escalation edges are
what keep that safe: a human before the work and a human after it.


| ID | Actor | Kind | Role | Autonomy level | Decision rights | Escalation path |
| -- | ----- | ---- | ---- | -------------- | --------------- | --------------- |
| `ACT1` | **Requester** | Human | `ROLE1` Requesting and approving | — (human) | Owns what gets built and why: approves at Gates 0–3, sets the modeling depth, and resolves conflicts with a Principle. The only actor who can approve a gate | — |
| `ACT2` | **Agent** | **AI** | `ROLE2` Executing the method | **Co-pilot** — walks the layers, drafts every document, implements, and opens the PR; nothing reaches `main` without `ACT3` merging it, and nothing is built before `ACT1` grants Gate 2 | May draft and edit any document under `architecture/`, write code, choose an implementation approach within an approved design, declare a modeling depth, and open a PR. May **not** approve its own gate, merge, change a Principle, retire an element during restatement without `ACT1` confirming, or proceed past a Conflict verdict | **`ACT1` Requester** for anything that touches strategy, business, or a gate; **`ACT3` Reviewer** for anything in the diff |
| `ACT3` | **Reviewer** | Human | `ROLE3` Reviewing and merging | — (human) | Approves or rejects the PR, checks that the gates the change required are recorded, and merges. Often the same person as `ACT1` on a small project — but the roles stay distinct because the checks differ | — |

`ACT2` sits at **co-pilot** rather than autonomous-with-checkpoint for the
reason `P2` states: the consequence of a wrong architectural change is
absorbed by whoever maintains the project afterwards, and is not trivially
reversible once other work builds on it. A human gate before code and a
human merge after it are two independent checks, and the method keeps both.
Raising `ACT2`'s autonomy would be exactly the kind of call
[`decision-record`](../../../.claude/skills/decision-record/SKILL.md) exists
for.

## Roles

```mermaid
flowchart LR
  role1["⚉ «Business Role» Requesting and approving [ROLE1]"]:::role
  role2["⚉ Executing the method [ROLE2]"]:::role
  role3["⚉ Reviewing and merging [ROLE3]"]:::role

  bsvc1(["⬭ «Business Service» Aligned change [BSVC1]"]):::service

  role2 -->|realizes| bsvc1
  bsvc1 -->|serves| role1
  role3 -->|gates| bsvc1

  classDef role fill:#f7f099,stroke:#9a8800,color:#333
  classDef service fill:#efe57d,stroke:#8a7a00,color:#333
```


| ID | Role | Filled by | Covers |
| -- | ---- | --------- | ------ |
| `ROLE1` | Requesting and approving | `ACT1` (human) | Presenting a requirement or a problem; granting Gates 0–3 |
| `ROLE2` | Executing the method | `ACT2` (AI), or a person following the same steps | `architecture-first-change` Steps 0–8 |
| `ROLE3` | Reviewing and merging | `ACT3` (human) | PR review, gate-record verification, merge |

`ROLE2` is deliberately written so a human can fill it unchanged. The
process does not branch on who or what is executing it — which is what makes
the AI actor a member of the organization rather than a tool bolted onto it.
