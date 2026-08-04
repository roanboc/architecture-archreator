---
name: scope-doc
description: Use when creating or updating a project scope document in docs/scope/ — one per initiative, drafted before the pre-implementation gate as step 3 of the ea-first-change process, and the durable record of gate approvals.
---

# Writing a scope document

One file per initiative in `docs/scope/`, named `<n>_<kebab-case-name>.md`
where `<n>` is the next number in the chronological sequence (check the
index table in `docs/scope/README.md`, and add the new document to it).

## Template

```markdown
# Project Scope — <Initiative Name>

_[← Scope index](./README.md) · [EA home](../ea/README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** <branch and/or PR reference>.

<One paragraph: what this initiative changes and why now.>

## EA alignment (assessed top-down before implementing)

| Layer         | Impact                                              |
| ------------- | ---------------------------------------------------- |
| 0_business-design | <canvases added/changed — or "not used" for an application project> |
| 1_strategy    | <new/changed goals, drivers — or "no change" + why> |
| 2_business    | <services, processes, rules, glossary>              |
| 3_information | <data objects, flows, storage, classification>      |
| 4_application | <services, components, ports>                       |
| 5_technology  | <runtimes, build, CI, hosting>                      |

## Approvals

| Gate                     | Approved by | Date         | What was approved                          |
| ------------------------ | ----------- | ------------ | ------------------------------------------- |
| Gate 2 — Business        | <Requester> | <YYYY-MM-DD> | <the docs/sections presented at the gate>  |

## Plateaus

| Plateau                | State                     |
| ----------------------- | ------------------------- |
| **Baseline** (before)  | <state before the change> |
| **Target** (delivered) | <state after the change>  |

## Work packages and deliverables

### WP1 — <name>

- **Deliverables:** <files, modules, docs — concrete artifacts>
- **Outcome:** <the capability gained>

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| …        | …                                           |

## Gap notes

- <Each out-of-scope item that leaves a real gap: what closing it would
  take, and what makes it easy or hard.>

## Open questions

- <Only if there are any: adopted interpretations that the product owner
  or stakeholders still need to confirm, each linked to the document where
  the interpretation was applied.>
```

## Rules

- **Every layer gets a verdict** in the EA-alignment table, including
  explicit "no change" — silence is not a decision.
- **Gates are recorded in the Approvals table** — which gate, who
  approved, when, and what was shown (see `ea-first-change` § The gates).
  Any initiative that changes documented behavior carries at least a
  **Gate 2 — Business** row before implementation starts; a
  strategy-discovery initiative carries **Gate 1 — Strategy**; an
  operating-model discovery carries **Gate 0 — Business model** and then
  **Gate 1**; a **Gate 3 — Solution design** row appears only if the
  Requester opted in at Gate 2. An approval that isn't recorded didn't happen; a scope
  document is a historical record, so the table shows who accepted what,
  durably.
- **Deliverables are concrete artifacts** (file paths, page/screen names),
  never vague ("improved UX").
- **Out of scope is as important as in scope**: it is where the next
  initiative's backlog lives. Pair each meaningful exclusion with a gap
  note.
- A merged initiative's scope document is a **historical record** — do not
  rewrite it later; follow-up work gets a new numbered document.
- Optionally include a small Mermaid plateau diagram using the
  `implementation` classDef from the EA notation conventions
  (`docs/ea/README.md`).

## Optional: the open-questions log

Projects with an external stakeholder or governing body who cannot be
consulted synchronously (a board, a client, a compliance owner) benefit
from a single living index, `docs/scope/open-questions.md`, listing every
adopted interpretation across all scope documents that still needs
confirmation. If the project keeps one:

- **Every new (or resolved) "Open questions" row is mirrored there** in the
  same change — it is the consolidated index reviewed between initiatives
  so questions don't get lost in old scope documents.
- Step 0 of `ea-first-change` reads it before starting a new change.

Projects without an external stakeholder to reconcile with can skip this
file entirely — the "Open questions" section within each scope document is
enough.
