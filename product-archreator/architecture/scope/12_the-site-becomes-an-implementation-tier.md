# Project Scope — The site becomes an implementation tier

_[← Scope index](./README.md) · [EA home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** branch `claude/product-1-roadmap-74giay`.

[Initiative 10](./10_what-belongs-at-which-tier.md) stated `RULE11` — a tier
refines what the tier above exposed and never restates it, and every refining
element names its parent — and deliberately shipped it without a worked
example. The guidance site is the only implementation-tier model in existence
and does not follow it: nine of its thirteen elements in layers 1–3 restate
something another model owns.

This initiative migrates it, and to do that it has to answer the question that
blocked it.

## The blocker, and what changed

Nine of those nine parents live in **another model**, and identifiers are
scoped per project — so "names its parent" had no way to be written.
[Initiative 11](./11_referencing-across-models.md) proposed a qualified form
and Gate 2 declined it, correctly, because it arrived as a thirteenth business
rule and twelve already exist.

**The notation survives the objection; the rule does not.** A qualifier is
*addressing*, the same category as the existing `SALES.BSVC3` domain form —
which is not a rule of its own either, but part of how identifiers work under
`RULE5`. Extending § Namespacing to a second axis adds no obligation; it
describes how to write something a federated model already has to write. The
Gate 2 decline on `RULE13` stands and is not revisited.

The alternative — naming parents in prose — was rejected on a sharper ground
than tidiness: prose parents cannot be validated, so the migration would
satisfy the letter of `RULE11` while permanently preventing the parent-naming
check that was the reason for it. Nine unmachine-readable parents are worse
than none, because the model would look migrated.

## A contradiction initiative 10 shipped

`architecture-doc-style` § What belongs at which tier gives the implementation
column of layer 1 as *"cites its parent; adds nothing"*. Open question 10,
merged in the same pull request, records the opposite: an implementation
**does** own a Driver when it is about delivery rather than about the product,
with the site's `DRV2` — English-only guidance excludes readers — as the case.

Both cannot stand. The open question is right and the table is wrong: a site
that publishes in two languages has a driver the method does not have. The
table row is corrected here, before the migration is forced to pick one.

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 1_strategy | **No change to this project's elements.** In the **site's** model, `DRV1` is retired — it states the method's driver, not the site's — see the Gate 1 note below |
| 2_business | **No change to elements.** `RULE11`'s parent-naming clause becomes satisfiable; no rule is added, changed or removed |
| 3_information | **No change** |
| 4_application | **`ACMP6` and `ACMP15` change** — the notation authority gains the second namespacing axis and a corrected layer-1 row; the validator learns to resolve `<model>:ID` and to report an unresolvable-but-declared reference rather than fail it |
| 5_technology | **No change** |

### A Gate 1 judgement to confirm

Retiring the site's `DRV1` modifies a **Driver**, which
`architecture-first-change` Step 1c names as a strategy-discovery trigger.
The interpretation adopted here is that it is **not** one: no strategy is being
decided, and the driver is not disappearing — it is being recognised as
belonging to a model one tier up, where it already exists. A misplaced element
returning to its owner is a correction, not a strategy change.

This is stated rather than assumed because it is exactly the kind of gate that
gets skipped by accident. If the Requester disagrees, the migration becomes a
Gate 1 initiative on the site's model.

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — the subject is the method and one implementation at Depth 1 |
| Gate 1 — Strategy | _to be confirmed at Gate 2_ | — | **Asserted N/A** — retiring the site's `DRV1` is a correction of ownership, not a strategy change. See the note above |
| Gate 2 — Business | _awaiting_ | — | This document, the notation, and the corrected layer-1 row |
| Gate 3 — Solution design | _to be asked at Gate 2_ | — | The validator's resolution and degrade behavior, if the Requester opts in |

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | `RULE11` is asserted with no worked example. The one implementation-tier model restates nine elements it does not own, and has no way to cite them even if it wanted to |
| **Target** (delivered) | The site cites what it refines, in a form a script can check. `RULE11` has a demonstration, and the parent-naming check becomes buildable |

## The notation

| Where the reference is written | How it is written | Example |
| ------------------------------ | ----------------- | ------- |
| Inside the model that owns the element | bare | `RULE11` |
| From another **domain** of the same model | `<DOMAIN>.` prefix | `SALES.BSVC3` |
| From another **model** | `<model>:` prefix | `org-archreator:BSVC2` |

A dot crosses a domain boundary inside one model; a colon crosses a model
boundary. The qualifier is the owning model's directory name, lower case,
exactly as it appears. References are one-directional — a model cites the tier
above, never below — which is what stops any model needing the context of
models that do not exist yet.

## Work packages and deliverables

### WP1 — The notation, and the corrected row

- **Deliverables:** `architecture-doc-style` § Namespacing across domains
  becomes § Namespacing, covering both axes; the layer-1 implementation cell
  in § What belongs at which tier is corrected to *"cites its parent; owns
  only drivers and goals about **delivery** rather than about the product"*.
- **Outcome:** the migration has a form to write parents in, and the rule
  stops contradicting its own open question.

### WP2 — Teach the validator

- **Deliverables:** `check_model` parses `<model>:ID`; resolves it against
  that model when discoverable in the repository; **reports it as
  declared-but-unresolvable when the model is absent**, counted in the summary
  rather than failed; errors when the model is present and the element is not
  defined there.
- **Outcome:** a child repository checked alone does not fail for citing a
  parent it cannot see, and does fail for citing something that does not
  exist.

### WP3 — Migrate the site's model

- **Deliverables:** the nine restating elements gain qualified parents —
  `STK1`/`ACT1` (Pilot), `STK2`/`ACT3` (adopters), `STK3`, `ACT2` (Copilot),
  `BSVC1`, `DOBJ1` — and `DRV1` is retired to the `## Retired` section naming
  the model that owns it. `DRV2`, `DRV3`, `ROLE1` and `BPROC1` stay as the
  site's own, with parents where they have them.
- **Outcome:** `RULE11` has its worked example, and the site's model says what
  is genuinely its own.

### WP4 — Close two open questions

- **Deliverables:** open question 11 resolved by the notation; open question
  10 resolved by the corrected row.
- **Outcome:** both are answered by something that exists rather than by an
  adopted interpretation.

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| The notation as addressing, and validation of it | `RULE13` — the Gate 2 decline stands; no rule is added |
| Migrating the site's layers 1–3 | Its layers 4 and 5, which are already implementation-tier detail and correct |
| Resolving cross-model references within one repository | How a parent model becomes physically available to a *separate* repository — no second repository exists yet |
| The corrected layer-1 row | Any other change to the tier table |

## Gap notes

- **The parent-naming check still is not built.** This initiative makes it
  possible — after it, one full tier carries machine-readable parents — but
  building it is the next step, not this one. Doing both at once would mean
  writing a check against data being written in the same change.
- **One-directional citation remains unenforced.** A parent citing a child
  would look like an unresolvable reference in a model with no parent, which
  WP2 reports rather than fails. Making it an error needs the model to record
  which model is above which; nothing does, except prose.
- **The qualifier is a name, so renaming a model breaks every citation.**
  Greppable and mechanical, and the same exposure the directory names already
  carry — but it is the one property an allocated number would have had, and
  it is given up knowingly.
- **Nine parents is a small sample.** The notation is being proved on one
  implementation whose parents all sit in two models in the same repository.
  A genuinely separate repository will test the degrade path, which nothing
  here exercises beyond a unit-level case.
