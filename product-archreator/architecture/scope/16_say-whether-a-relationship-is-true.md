# Project Scope — Say whether a relationship is true

_[← Scope index](./README.md) · [Model home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** [`archreator` PR #46](https://github.com/roanboc/archreator/pull/46),
and the model changes this document holds the gate for.
**Closes:** `GAP4` — reaching `PLAT1` on the
[target state](../6_transition/1_target-state.md).

## The problem

[Initiative 8](./8_declare-the-relationships-and-let-the-graph-be-walked.md)
gave the relationship a home and moved it out of the diagrams. It built the
machinery for saying a relationship is not true yet — `DOBJ4` carries a
`pending` field, `ACMP7` reads a `Pending` marker — and then shipped a corpus
in which **not one relationship used it**. 640 edges, none pending, while 35
were still drawn with the dashed edge the notation reserves for exactly that.

`GAP4` was recorded as closed. It was not. Anything reading the projection as
current state — `trace`, `coverage`, every brief — was wrong about all 35.

## The design

### 1. A pending relationship could not be written down

This is the part that made the initiative bigger than marking rows, and it is
worth stating plainly because it was not obvious until it was measured.

A catalogue cell declares a relationship **only when it holds identifiers and
nothing else**. That rule is what separates a relationship column from an
attribute column, and it is load-bearing. It also means a marker written beside
an identifier does not qualify the relationship:

| cell | read as |
| ---- | ------- |
| `` `BSVC4` `` | declares a relationship |
| `` `BSVC4` — Pending `` | **declares nothing at all** |

So the only surface where a pending relationship could be stated was the
relationship table's notes column — which catalogue columns do not have. Every
relationship declared by an element that does not exist yet was projected as
live, with nowhere to say otherwise. One real row proved it: `CH5`'s Reaches
cell read `` `CS2`, `CS3` — **Pending** ``, and silently declared neither.

### 2. The row says it, once

`ACMP7` reads the marker from the **row**. An element marked
`**Pending — future initiative**` for the grounding rule points at nothing that
is true today, so the marker it already carries marks every relationship the
row declares. No new vocabulary, no new column, nothing restated.

**The rule is anchored to the start of a cell**, and that is the whole design
rather than a detail. A catalogue row is prose as well as data. Matched
anywhere in the row, two real rows in these models match wrongly:

| row | why | pending? |
| --- | --- | -------- |
| `GAP4` — "a **pending** relationship reads as a live one" | the gap entry describing this problem | no |
| `STK4` — "stops de**pending** on their availability" | a substring of another word | no |

Anchored, neither matches and every row that means it does.

### 3. The dashed edge meant four things

Auditing all 35 dashed edges found the device carrying four different claims,
of which the notation defines one:

| meaning | count | what happens to it |
| ------- | ----- | ------------------ |
| **Pending** — not true yet | 14 | stays dashed, and is now declared pending |
| **Optional** — true, but does not always happen | 6 | becomes solid; the label already says *may*, *where wanted* |
| **Not reached** — a roadmap plateau's state | 10 | becomes solid; a plateau's own **Status** carries it |
| **Legend** — a diagram demonstrating the notation | 3 | stays dashed; it is not model content |
| **"Nothing realizes this"** — a self-loop | 2 | removed; it is a grounding fact, and `coverage` reports it |

Optional is not pending. *Sometimes* and *not yet* are different claims, and
collapsing them is what made the projection unable to tell any of them apart.

### 4. Three relationships were drawn and never declared

`PROD3` → `GCRE5`, `BCOL1` → `ACT5`, and `CH5`'s two reaches. Residue of
initiative 8's migration, which compared connections undirectedly and did not
see them. They are declared here, as pending.

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 0_business-design | **Changed** — the products, channels and revenue tables gain a `State` column so the marker leads a cell instead of trailing a sentence |
| 1_strategy | **Changed** — the stakeholder table gains the same column. No stakeholder, driver, goal or principle moves |
| 2_business | **`BOBJ7` restated** — a relationship carries whether it is true today, and where that is stated |
| 3_information | **`DOBJ4` unchanged in structure.** `pending` existed and was never written; what changes is that it now is |
| 4_application | **`ACMP7` restated** — the parse reads a row's Pending marker |
| 5_technology | **No change** |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — the subject is one application |
| Gate 1 — Strategy | — | — | **N/A** — the direction was approved on the [roadmap](../6_transition/README.md) at Gate 1, 2026-08-27 |
| Gate 2 — Business | Requester | 2026-08-29 | The restated `BOBJ7`, the marking of the pending relationships, and taking the dashed style off the ones that were never pending. **Re-presented**: the first presentation said ~13 relationships and a documents-only fix, and both were wrong — see below |
| Gate 3 — Solution design | Requester | 2026-08-29 | § 2, the row-level rule. **Look first at:** the anchoring, because an unanchored match marks rows that are not pending and there are two of those in these models today |

**Gate 2 was granted twice, and the first grant did not count.** It was asked
for on the basis that ~13 relationships needed a marker and no code had to
change. Measuring found ~40 candidates and proved the documents-only fix
impossible — a marker in a relationship cell deletes the relationship. The
Requester was shown the corrected scope and the three options before anything
was built. `P3` says an unrecorded approval did not happen; an approval given
for the wrong scope is the same thing.

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | 640 edges, 0 pending, 35 drawn dashed meaning four different things. `GAP4` recorded as closed and open |
| **Target** (delivered) | `PLAT1`. Every relationship carries whether it is true today; every dashed drawing is backed by a pending declaration; nothing else is dashed but a legend |

## Work packages and deliverables

### WP1 — The row says it

- **Deliverables:** `ACMP7` reads a `Pending` marker anchored to the start of a
  catalogue cell and applies it to that row's relationships;
  `architecture-document-style` states the convention, since the parse now
  depends on it.
- **Outcome:** a pending relationship can be written down at all.

### WP2 — The marker leads a cell

- **Deliverables:** a `State` column on the products, channels, revenue and
  stakeholder tables; the marker moved into it from mid-sentence. `CH5`'s
  Reaches cell becomes a declaration again.
- **Outcome:** the convention is uniform, and two relationships come back.

### WP3 — The dashed edge means one thing

- **Deliverables:** the notes column on seven relationship tables with the
  marker on eleven rows; the optional and roadmap edges redrawn solid; the
  self-loop removed; the three undeclared relationships declared; the prose
  that explained the old drawing repaired in five documents.
- **Outcome:** `GAP4` closed. Every dashed drawing is a pending relationship.

## In scope / out of scope

| In | Out |
| -- | --- |
| Whether a relationship is true today | **A third state.** Optional relationships are drawn solid and say *may* in the label. A `Conditional` marker was considered and declined: it grows the notation for a distinction the words already carry |
| The Pending marker read from a row | **A validator for it.** Nothing checks that a dashed drawing has a pending declaration; the audit that proves it here was written for this initiative and not kept |
| Catalogue and relationship-table declarations | **94 catalogue cells that name an element in prose** — `` `CS1` — designers find it as code `` — and so declare nothing. A sibling of `GAP2`, found while measuring this one, and its own initiative |
