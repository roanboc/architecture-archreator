# Business Services and Rules — archreator

_[← Business layer](./README.md) · [EA home](../README.md)_

**ArchiMate elements:** Business Service, Business Process, Business Rule.

## How to read this document

```mermaid
flowchart LR
  svc(["⬭ «Business Service» what archreator offers"]):::service
  rule[/"❒ «Business Rule» what constrains it"/]:::rule
  p[/"⚑ «Principle» what the rule enforces"/]:::principle
  proc{{"⚙ «Business Process» how it is delivered"}}:::process

  proc -->|realizes| svc
  rule -->|constrains| proc
  rule -->|enforces| p

  classDef service fill:#efe57d,stroke:#8a7a00,color:#333
  classDef rule fill:#e5d95f,stroke:#7a6c00,color:#333
  classDef process fill:#f7f099,stroke:#9a8800,color:#333
  classDef principle fill:#a37cd8,stroke:#4527a0,color:#333
```

| Glyph | Shape | Element | ID prefix | Reads as |
| ----- | ----- | ------- | --------- | -------- |
| `⬭` | Stadium | «Business Service» | `BSVC` | `BSVC1` = Business Service 1 |
| `❒` | Parallelogram | «Business Rule» | `RULE` | `RULE1` = Business Rule 1 |
| `⚙` | Hexagon | «Business Process» | `BPROC` | unnumbered here — the processes are steps of one flow |
| `⚑` | Parallelogram (violet) | «Principle» — context, from [layer 1](../1_strategy/1_motivation.md) | `P` | `P1` = Principle 1 |

**The glyph rides on every node; the «stereotype» word appears once.**

## Business services

```mermaid
flowchart LR
  bsvc1(["⬭ «Business Service» Aligned change [BSVC1]"]):::service
  bsvc2(["⬭ Discovery [BSVC2]"]):::service
  bsvc3(["⬭ Right-sizing [BSVC3]"]):::service
  bsvc4(["⬭ Approval that counts [BSVC4]"]):::service
  bsvc5(["⬭ Federated scale [BSVC5]"]):::service
  bsvc6(["⬭ Staying true [BSVC6]"]):::service
  bsvc7(["⬭ Method upgrade — partially Pending [BSVC7]"]):::service

  stk1(["◍ «Stakeholder» Modeling a company [STK1]"]):::stakeholder
  stk2(["◍ Building one application [STK2]"]):::stakeholder
  stk3(["◍ A non-technical Requester [STK3]"]):::stakeholder
  stk5(["◍ archreator's maintainer [STK5]"]):::stakeholder

  bsvc1 --> stk1
  bsvc1 --> stk2
  bsvc2 --> stk1
  bsvc2 --> stk2
  bsvc3 --> stk1
  bsvc3 --> stk2
  bsvc4 --> stk3
  bsvc5 --> stk1
  bsvc6 --> stk1
  bsvc6 --> stk2
  bsvc7 -.-> stk5

  classDef service fill:#efe57d,stroke:#8a7a00,color:#333
  classDef stakeholder fill:#f4ecfc,stroke:#9575cd,color:#333
```

Every edge reads **serves**. `BSVC5` reaches only `STK1` — federated scale
is the one service a single-application project never needs — and `BSVC7`'s
edge is dashed because no second version has shipped through the mechanism.

What archreator offers whoever adopts it. Each names the document or skill
that realizes it, per `P1`.

| ID | Service | Serves | Realized by |
| -- | ------- | ------ | ----------- |
| `BSVC1` | **Aligned change** — a requirement becomes a change that is consistent with everything already decided | `STK1`, `STK2` | [`architecture-first-change`](../../../.claude/skills/architecture-first-change/SKILL.md) |
| `BSVC2` | **Discovery** — an unstated strategy or business model becomes a documented one, by asking rather than assuming | `STK1`, `STK2` | [`operating-model-discovery`](../../../.claude/skills/operating-model-discovery/SKILL.md), [`strategy-discovery`](../../../.claude/skills/strategy-discovery/SKILL.md) |
| `BSVC3` | **Right-sizing** — the method costs what the subject is worth, and says which weight it picked | `STK1`, `STK2` | The depth ladder in [`architecture/README.md`](../../../.claude/skills/project-bootstrap/templates/architecture/README.md#modeling-depth); [`project-bootstrap`](../../../.claude/skills/project-bootstrap/SKILL.md) |
| `BSVC4` | **Approval that counts** — a business judgment is exercised by whoever holds it and survives in the record | `STK3` | `architecture-first-change` § The gates and § Where a gate happens; the Approvals table in [`scope-doc`](../../../.claude/skills/scope-doc/SKILL.md) |
| `BSVC5` | **Federated scale** — a business line is modeled on its own terms without being flattened into the enterprise | `STK1` | [`domain-modeling`](../../../.claude/skills/domain-modeling/SKILL.md); [`architecture/domains/`](../../../.claude/skills/project-bootstrap/templates/architecture/domains/README.md) |
| `BSVC6` | **Staying true** — the model keeps describing today, and the method keeps up with what using it actually teaches | `STK1`, `STK2` | [`restate-current-state`](../../../.claude/skills/restate-current-state/SKILL.md) for the model; [`engagement-retrospective`](../../../.claude/skills/engagement-retrospective/SKILL.md) for the method |
| `BSVC7` | **Method upgrade** — an improvement to the method reaches an existing project without a migration | `STK5` | The plugin manifest at `.claude/.claude-plugin/plugin.json`; **partially Pending** — the mechanism exists, no second version has shipped through it yet |

## Business rules


```mermaid
flowchart LR
  rule1[/"❒ «Business Rule» No code before Gate 2 [RULE1]"/]:::rule
  rule2[/"❒ Every element names what realizes it [RULE2]"/]:::rule
  rule5[/"❒ IDs are never reused [RULE5]"/]:::rule
  rule6[/"❒ Merged scope documents are never rewritten [RULE6]"/]:::rule
  rule10[/"❒ Every element document opens with its legend [RULE10]"/]:::rule

  p1[/"⚑ «Principle» Every element names what realizes it [P1]"/]:::principle
  p2[/"⚑ A human approves, recorded [P2]"/]:::principle
  p5[/"⚑ History is never rewritten [P5]"/]:::principle
  p3[/"⚑ Each fact in one document [P3]"/]:::principle

  rule1 --> p2
  rule2 --> p1
  rule5 --> p5
  rule6 --> p5
  rule10 -.->|costs| p3

  classDef rule fill:#e5d95f,stroke:#7a6c00,color:#333
  classDef principle fill:#a37cd8,stroke:#4527a0,color:#333
```

Solid edges read **enforces**. `RULE10`'s edge is dashed and points the other
way: it is the one rule that **costs** a principle rather than serving one,
and the table below says why that is accepted. Five of the twelve rules are
shown; the rest follow the same pattern.

The rules that constrain how the services are delivered. Each traces to the
principle it enforces.

| ID | Rule | Enforces | Where it bites |
| -- | ---- | -------- | -------------- |
| `RULE1` | No code is written before the Requester grants Gate 2 | `P2` | `architecture-first-change` Step 4 |
| `RULE2` | Every EA element names its realizing artifact, or is explicitly "Pending — future initiative" | `P1` | `architecture-doc-style` § Grounding rule; `architecture-first-change` Step 7. Carried by **review**, not tooling — see `ACMP13` |
| `RULE3` | Every layer gets an explicit verdict in a scope document, including "no change" | `P2` | `scope-doc` § Rules |
| `RULE4` | An approval that isn't recorded didn't happen; a gate that didn't apply is written `N/A — <why>` rather than deleted | `P2` | The Approvals table |
| `RULE5` | An element ID is assigned once and never reused, even after the element is retired | `P5` | `architecture-doc-style` § Element IDs; `restate-current-state`. Enforced in CI by `ACMP15` |
| `RULE6` | A merged scope document is never rewritten — follow-up work gets a new numbered document | `P5` | `scope-doc`; `restate-current-state` § The one rule |
| `RULE7` | A change that contradicts an existing Principle stops and goes back to the Requester | `P2` | `architecture-first-change` Step 1c, Conflict verdict |
| `RULE8` | Changing a domain's exposed service requires the consuming domains' Requesters at Gate 2 | `P2` | `domain-modeling` § Cross-domain changes |
| `RULE9` | A skill links only within `.claude/skills/`; it names a project's documents in code spans | `P3` | `architecture-doc-style` § Links. Added when packaging as a plugin made outbound links resolve to nothing |
| `RULE10` | Every EA document **that carries elements** opens with its own notation legend, and every section that has a diagram opens with it | **none — it costs `P3`** | `architecture-doc-style` § Diagrams come first; `architecture/README.md` § Notation conventions. The per-document legend is a deliberate, bounded copy of the global notation — duplication `P3` would normally forbid — accepted because these documents are read one at a time and out of order, by people and agents who will not open a second file. Narrowed to element documents when the rule was first applied at scale: a layer README that only indexes other documents has no elements to legend, and giving it one would be ceremony. Carried by **review**; nothing checks that a diagram was drawn |
| `RULE11` | A tier refines what the tier above exposed and never restates it; every refining element names its parent | `P3` | `architecture-doc-style` § What belongs at which tier. Carried by **review** — nothing checks that a parent is named, and nothing could until enough elements carry one to make the absence meaningful. See [scope document 10](../scope/10_what-belongs-at-which-tier.md) |
| `RULE12` | A change that touches more than one model corrects every current-state statement it falsifies, in the same change | `P1` | `architecture-first-change` Step 7. Carried by **review**, and it has already failed once: initiative 9 falsified seven statements in the organization's model and shipped them, because the process walks one model's layers and asks nothing about the others |

## The process, in one view

```mermaid
flowchart LR
  req(["Requirement or problem"]):::start
  depth{{"⚙ «Business Process» Confirm depth, locate domain"}}:::process
  align{{"⚙ Align layers 1–3"}}:::process
  gate[/"❒ Gate 2 granted? [RULE1]"/]:::rule
  build{{"⚙ Align 4–5, implement"}}:::process
  verify{{"⚙ Verify RULE2, open PR"}}:::process
  merged(["Merged"]):::start

  req --> depth --> align --> gate
  gate -- no --> align
  gate -- yes --> build --> verify --> merged

  classDef start fill:#fffbb5,stroke:#b8a200,color:#333
  classDef process fill:#f7f099,stroke:#9a8800,color:#333
  classDef rule fill:#e5d95f,stroke:#7a6c00,color:#333
```

The full version, including the discovery branches and all four gates, is
the process flow in [CONTRIBUTING.md](../../../CONTRIBUTING.md) — not
restated here, per `P3`.
