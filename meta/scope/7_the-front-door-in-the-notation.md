# Project Scope — The front door, in the notation

_[← Scope index](./README.md) · [EA home](../ea/README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** `README.md`, on branch
`claude/repo-value-ux-review-3ur5y4`.

`README.md` is the first thing anyone sees, and it described the method in
prose while every model in the repository had been redrawn to a notation the
README never showed. A project whose pitch is "your architecture becomes
legible" should demonstrate that in the first screen rather than assert it.

Two diagrams, both drawn to the standard: the change process a requirement
goes through, and the six layers it passes.

This is a **docs-only initiative**. No element changes.

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 1_strategy | **No change** |
| 2_business | **No change.** `RULE10` covers documents that carry elements; `README.md` carries none, so the diagrams are here because they earn their place, not because a rule demands them |
| 3_information | **No change** |
| 4_application | **No change** |
| 5_technology | **No change** |
| domains | **No change** |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — Depth 1 |
| Gate 1 — Strategy | — | — | **N/A** — no strategy change |
| Gate 2 — Business | Requester | 2026-08-09 | Two diagrams at the top of the README, so the documentation visibly uses its own notation |
| Gate 3 — Solution design | — | — | **N/A** |

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | Prose and tables. The notation was specified, applied in four trees, and invisible on the front page |
| **Target** (delivered) | The change process and the layer stack drawn at the top, in the notation, with a pointer to where its values are defined |

## Work packages and deliverables

### WP1 — The two diagrams

- **Deliverables:** [`README.md`](../../README.md) § The shape of it, in two
  diagrams
- **Outcome:** a reader sees the notation working before being asked to adopt
  it, and the AI actor's cyan makes the project's distinguishing bet visible
  rather than only stated

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| `README.md` | `CONTRIBUTING.md`, whose process flow is still in the old style |
| — | The `docs/` scaffold's layer views — see the gap note |

## Gap notes

- **The scaffold is the last tree behind the standard, and it is the one that
  matters most.** Every layer README under `docs/ea/` carries a
  fill-in-the-blank layer view in the pre-standard style, and `docs/` is what
  an adopter copies. A cloner therefore starts from diagrams that disagree
  with the notation section three files away. Mechanical to fix, and worth
  its own initiative because it also means deciding what a *template* diagram
  should look like when its elements are placeholders.
- **`CONTRIBUTING.md` has the same drift** at smaller scale — one process
  flow, still in the old single-colour style.
- **Nothing checks either.** `RULE10` is scoped to element documents, so
  neither file is in its reach even in principle. If the scaffold pass
  happens, that is the moment to decide whether the rule should extend to
  documents that *teach* the notation.
