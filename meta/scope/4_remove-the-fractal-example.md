# Project Scope — Remove the fictional worked example

_[← Scope index](./README.md) · [EA home](../ea/README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** deletion of `example-company/` on
`claude/repo-value-ux-review-3ur5y4`.

[Initiative 1](./1_repo-value-and-fractal-domains.md) built `example-company/`
— Solvara, a fictional AI consultancy — to prove the fractal-domain design
against a concrete model rather than assert it. It did that job: writing it
is what turned `COA1`'s blocker from a pending resource nobody owned into an
exposed service with an owner.

The Requester's judgement is that a fictional company is the wrong ongoing
investment: it demonstrates the notation but proves nothing about whether the
method survives contact with a real business, and it has to be maintained
alongside every change to the method. Real projects are the test.

`example/` is **kept**, and is not an example in the same sense — it is this
project's own published documentation, built with the method and deployed to
GitHub Pages from this repository. Updating it to match the current method is
the next initiative, in its own scope folder.

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 0_business-design | **Not used** — Depth 1 |
| 1_strategy | **No change.** No stakeholder, driver, goal, or principle moves |
| 2_business | **No change.** `BSVC5` (federated scale) is still offered by `domain-modeling` and `docs/ea/domains/`; what is lost is a demonstration of it, not the capability |
| 3_information | **Not started** |
| 4_application | **No change** |
| 5_technology | **No change** |
| domains | **Not used** — Depth 1. archreator has never had domains of its own |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — Depth 1 |
| Gate 1 — Strategy | — | — | **N/A** — no strategy change |
| Gate 2 — Business | Requester | 2026-08-08 | Removing the fictional example and keeping `example/`, on the reasoning that real projects are better evidence than a maintained fiction |
| Gate 3 — Solution design | — | — | **N/A** — no code |

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | Two worked examples: an application (`example/`) and a fictional company (`example-company/`) carrying canvases, Gate 0, two domains, charters, and namespaced IDs |
| **Target** (delivered) | One worked application, plus `meta/` — archreator modeled with archreator, which is a real model of a real thing. Depth 3 documented and undemonstrated |

## Work packages and deliverables

### WP1 — Delete, and repair what pointed at it

- **Deliverables:** `example-company/` removed; links fixed in
  [`README.md`](../../README.md) (3), [`meta/README.md`](../README.md),
  [`meta/reviews/1_value-and-ux-review.md`](../reviews/1_value-and-ux-review.md),
  and `project-bootstrap`'s delete-on-clone list
- **Outcome:** `check_links.py` and `check_model.py` both pass

### WP2 — Retire the question it raised

- **Deliverables:** [`meta/open-questions.md`](../open-questions.md) — the
  shared-capability-base question moves to Resolved as **withdrawn, not
  answered**
- **Outcome:** the log doesn't carry a question whose entire evidence base
  was invented and has been deleted. Answering it from a fiction would have
  been worse than admitting it is unasked

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| Deleting `example-company/` and repairing references | `example/`, which stays and gets updated next |
| Withdrawing the question it raised | Rewriting `meta/scope/1_*.md`, which is merged and immutable |
| Recording what the removal costs | Replacing the Depth 3 demonstration |

## Gap notes

- **Depth 3 is now documented and undemonstrated.** `docs/ea/domains/`, the
  `domain-modeling` skill, the split test, the charter shape, and the
  federation rule all exist as instructions with nothing showing them
  applied. The same is true of the canvases and Gate 0 — the
  `operating-model-discovery` track no longer has a worked result. A reader
  who wants to see what these produce has only the skill files. Closing this
  means a real project reaching that size, which is the point of removing
  the fiction rather than a reason not to.
- **The validator lost coverage.** `example-company/` held 161 of the
  repository's 245 defined elements, and it was the only model exercising
  namespaced cross-domain references. `check_model.py`'s domain-qualification
  path is now tested by nothing in this repository. That code is still
  correct — it found five real errors in `example-company` before deletion,
  including a bare `BSVC9` used from inside the `PRODUCT` domain where it
  would have resolved to `PRODUCT.BSVC9` — but nothing regression-tests it
  from here.
- **`meta/scope/1_*.md` still describes building it.** That document is
  merged and immutable under `RULE6`, so it goes on recording that initiative
  1 delivered a domain split, in a repository where that folder no longer
  exists. This is correct behaviour, not an oversight: the document records
  what was approved on a date, and the model moving on afterwards is exactly
  what a historical record is for. Its two references are code spans rather
  than links, so nothing breaks.

## Open questions

None. The one this initiative touched was withdrawn rather than answered —
see [`meta/open-questions.md`](../open-questions.md) row 2.
