# Project Scope — What belongs at which tier

_[← Scope index](./README.md) · [EA home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** branch `claude/product-1-roadmap-74giay`.

This repository federates three models — the organization, the product, and
the guidance site that implements part of it — and **nothing states how much
design detail belongs at each**. The pattern is already there and already
correct: the organization's layer 4 carries five components for the whole
portfolio, `product-archreator` decomposes three of them into sixteen, and
the site decomposes the fourth. But it is held by nobody. The only place it
is written down is a paragraph inside
[`org-archreator/architecture/4_application/2_application-components.md`](../../../org-archreator/architecture/4_application/2_application-components.md) —
_"the organization's layer 4 names **that** an application exists; a Depth 1
model says **how** it is built. Neither restates the other"_ — a fact
discovered while modeling and never lifted into the method.

The second half of this initiative is the reason the first half is overdue.
[`architecture-first-change`](../../../.claude/skills/architecture-first-change/SKILL.md)
walks a **single** model's layers. Initiative 9 changed two and no step asked
which statements elsewhere it had just falsified, so seven of them shipped
and `RULE2` failed on `main` until [PR #19](https://github.com/roanboc/archreator/pull/19).

## Why now

Both changes come from
[retrospective note 2](../../../org-archreator/architecture/engagements/2_renaming-a-live-model.md),
proposals 1 and 2, and the Requester approved acting on both. Proposal 2 was
requested directly; proposal 1 was raised on one occurrence rather than the
two the mechanism normally asks for, on the grounds that the evidence is a
shipped defect rather than an improvisation that worked.

It also settles [open question 9](./open-questions.md), which initiative 9
answered by adopted interpretation — *the site keeps its own model* — without
being able to say what that model should contain.

## Tier is not depth

The distinction this initiative introduces is **tier**, and it is not the
modeling depth already in `CLAUDE.md`:

| Tree | Depth | Tier |
| ---- | ----- | ---- |
| `org-archreator/` | 2 — Organization | **Enterprise** |
| `product-archreator/` | 1 — Application | **Product** |
| `product-archreator/site/` | 1 — Application | **Implementation** |

Depth says how much of the six layers a model fills in. Tier says how much
**detail** each layer carries, and who it defers to. Two models at the same
depth sit at different tiers, which is exactly the case the repository
already contains and could not previously describe.

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 1_strategy | **No change.** `P3` — each fact in exactly one document — is what the tier rule *applies* across a federation boundary; it is not altered. This is the same reasoning [decision 5](../decisions/5_no-per-product-strategy-folders.md) used to forbid per-product strategy folders, turned ninety degrees |
| 2_business | **`RULE11` and `RULE12` added** to the rules table |
| 3_information | **No change** |
| 4_application | **`ACMP1` and `ACMP6` change behavior** — the process spine gains a step, the notation authority gains a section. Neither changes its realizing artifact |
| 5_technology | **No change** |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — the subject is the method at Depth 1 |
| Gate 1 — Strategy | — | — | **N/A** — no Stakeholder, Driver, Goal or Principle added or modified; `P3` is applied, not changed |
| Gate 2 — Business | _awaiting_ | — | This document, the two rules, and the tier table |
| Gate 3 — Solution design | _to be asked at Gate 2_ | — | The skill edits, if the Requester opts in |

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | Three federated models with an unstated granularity convention, correct by accident and held by nobody. A change touching two models has no step asking what it falsified elsewhere — and has already falsified seven statements once |
| **Target** (delivered) | The convention is stated, with a test that assigns any element to a tier and a requirement that a refining element names its parent. A change that touches more than one model is required to correct what it falsified, in the same change |

## The rule, as proposed

**A tier may refine what the tier above exposed; it may never restate it.
Every refining element names its parent.**

| Layer | Enterprise | Product | Implementation |
| --- | --- | --- | --- |
| 0 business-design | Owned | — | — |
| 1 strategy | Owned | Only goals and principles specific to this product and absent above | Cites its parent; adds nothing |
| 2 business | Owned | Product-specific services and rules | **Cites its parent, and details only what the implementation requires** |
| 3 information | Owned | Product-specific objects | **Cites its parent; representations and implementation-specific objects only** |
| 4 application | Key components and dependencies | Decomposes its enterprise component | Full component, port and interface design |
| 5 technology | Key nodes and dependencies | Product-specific services | Full runtime, deployment and CI design |

The two emphasised cells are the Requester's correction to the first draft,
which had them as "none". An implementation does acquire business and
information elements of its own — the site's Copilot actor, with its autonomy
level and decision rights, is the clearest case in this repository and the
only place an AI actor is modeled in delivery rather than described in the
abstract. What it may not do is *restate* what the tier above already owns.

## Work packages and deliverables

### WP1 — State the rule

- **Deliverables:** a new section in
  [`architecture-doc-style`](../../../.claude/skills/architecture-doc-style/SKILL.md)
  carrying the table above, the refinement rule, the parent-naming
  requirement, and the tier-is-not-depth distinction.
- **Outcome:** an adopter federating a model is told what belongs where,
  instead of rediscovering it and writing it in the wrong file.

### WP2 — Two rules in the model

- **Deliverables:** `RULE11` (a tier refines, never restates; a refining
  element names its parent) and `RULE12` (a change touching more than one
  model corrects every current-state statement it falsifies, in the same
  change) in
  [`2_business-services.md`](../2_business/2_business-services.md) §
  Business rules, each naming the principle it enforces and where it bites.
- **Outcome:** both are model elements that can be cited and traced, not
  just prose inside a skill.

### WP3 — The cross-model step

- **Deliverables:** `architecture-first-change` § Step 7 gains: name every
  other model in the repository whose current state this change falsifies,
  and correct it in the same change.
- **Outcome:** the failure that produced PR #19 has a step that would have
  caught it.

### WP4 — Where an implementation's model lives

- **Deliverables:** `product-archreator/architecture/decisions/8_...md` —
  the choice between keeping an implementation's model in the product's tree
  and giving it a child tree is the **Requester's**, made per implementation,
  and both are legitimate. Refines [decision 7](../decisions/7_one-tree-per-federated-project.md),
  which read as though a tree of its own were the only correct answer.
- **Outcome:** the guidance site and the Pending portal can be answered
  differently without either looking like a mistake, and this repository
  demonstrates both.

### WP5 — Close open question 9

- **Deliverables:** open question 9 moves to Resolved, citing the tier rule
  as what makes "keep its own model" a well-defined answer rather than an
  adopted interpretation.
- **Outcome:** the answer given in initiative 9 now has a rule behind it.

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| The rule, the two model elements, and the process step | **Applying the rule to the site's existing model** — its strategy layer restates the method's drivers, and `DRV1` belongs upstream. That is a migration, and its own initiative |
| The parent-naming requirement, for elements written from now on | Backfilling a parent onto every existing element across three trees |
| The tier-is-not-depth distinction | Any change to the depth ladder itself |
| A decision on where an implementation's model lives | Moving any model as a result of it |

## Gap notes

- **The parent-naming clause is the enforceable half, and nothing enforces
  it yet.** `check_model` could verify that every implementation-tier element
  names a parent — which would be the first mechanical check on `RULE2`'s
  family — but it needs the data to exist first, and the data arrives only as
  elements are written or backfilled. Worth building once one full tier has
  been migrated, not before.
- **`RULE12` is a process rule with no mechanism.** Neither check can catch a
  falsified statement in another model: `check_model` verifies that an element
  *reference* resolves, `check_links` that a *link* resolves, and neither
  reads what a "Realized by" cell claims. This is the same gap `RULE2` already
  admits to, and `RULE12` inherits it — it will be carried by whoever is
  running the process, which is exactly what failed in initiative 9.
- **The rule is asserted, not demonstrated.** Shipping it without migrating
  the site means the one implementation-tier model in existence does not yet
  follow it. That is deliberate — the Requester's calibration is that
  structural churn belongs to a founding phase — but it does mean the first
  adopter to federate a model will be the first real test.

## Open questions

- **Does an implementation tier ever own a Driver?** Adopted interpretation:
  **yes, when the driver is about delivery rather than about the product** —
  the site's `DRV2` (English-only guidance excludes readers) is genuinely its
  own, while `DRV1` (nothing shows the method applied) is the method's. The
  boundary is judgement, and the rule as written does not sharpen it.
  Mirrored to [open questions](./open-questions.md).
