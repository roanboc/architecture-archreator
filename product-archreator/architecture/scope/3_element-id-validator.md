# Project Scope — Element-ID validator, and dropping the model database

_[← Scope index](./README.md) · [EA home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** `scripts/check_model.py` on
`claude/repo-value-ux-review-3ur5y4`.

[Initiative 2](./2_archreator-models-itself.md) left `ACMP15` as a Pending
row with two business rules pointing at it: `RULE5` (an ID is assigned once
and never reused) was enforced by nothing at all, and `RULE2` only for links.
The [review](../reviews/1_value-and-ux-review.md) put it first in the
backlog.

`ACMP15` was specified as a `nodes`/`edges` SQLite projection **plus** a
validator. The Requester challenged whether the database earned its place,
and it doesn't — the graph is implicit in the documents, `grep` traverses it,
and an agent reads Markdown natively. What was bundled with it does earn its
place: catching a dangling reference needs a **parse**, not a store. This
initiative builds the parse and drops the store.

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 0_business-design | **Not used** — Depth 1 |
| 1_strategy | **No change.** No stakeholder, driver, goal, or principle moves. `P1` and `P5` are what the validator enforces, not what it changes |
| 2_business | **Changed.** `RULE5` gains an enforcement mechanism; `RULE2` is annotated as carried by review rather than tooling, which was true before and unstated |
| 3_information | **Not started.** Deliberately: the decision not to persist a projection is precisely the decision not to create an information layer yet |
| 4_application | **Changed.** `ACMP15` narrows from "model exporter and validator" to **element-ID validator**, and moves from Pending to realized |
| 5_technology | **Changed.** `TSVC2` broadens from link validation to model validation; `NODE2` and `NODE4` run a second script; `ART3` gains it |
| domains | **Not used** — Depth 1 |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — Depth 1; no canvases |
| Gate 1 — Strategy | — | — | **N/A** — no strategy change |
| Gate 2 — Business | Requester | 2026-08-08 | The validator scoped to dangling and reused IDs only, with the database deferred and the reasoning recorded as a decision record |
| Gate 3 — Solution design | — | — | **N/A** — not requested |

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | `RULE5` unenforced; `RULE2` enforced only for links. `ACMP15` Pending, specified as a database plus a validator. `stack-selection` presented the export as the default |
| **Target** (delivered) | Every element reference under an `ea/` tree resolves, no ID is defined twice, no retired ID reappears as live — checked in CI. No database, with the trigger conditions for reconsidering it written down |

## Work packages and deliverables

### WP1 — The validator

- **Deliverables:** [`scripts/check_model.py`](../../../.claude/skills/project-bootstrap/templates/scripts/check_model.py);
  [`.github/workflows/docs-check.yml`](../../../.github/workflows/docs-check.yml)
  runs both scripts
- **Outcome:** `RULE5` is enforced rather than merely stated

### WP2 — Correct the convention it exposed

- **Deliverables:** `ea-doc-style` § Element IDs — the **two** definition
  shapes (a table's first column, and a bolded `**G1 — Name**` lead-in for
  Goals and Principles), and the scoping rule
- **Outcome:** the convention describes what the repository actually does.
  Initiative 2 wrote Goals as bullets while the convention said "first
  column", so half the elements in `meta/ea` were off-convention as written

### WP3 — Drop the database, and fix the framing that caused it

- **Deliverables:**
  [`meta/decisions/4_defer-the-model-database.md`](../decisions/4_defer-the-model-database.md);
  `stack-selection` § The model as data rewritten so the in-memory validator
  is the default and a projection is an escalation with named triggers
- **Outcome:** the next reader of that section doesn't re-make the same
  over-scoping mistake

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| Dangling references, duplicate definitions, retired-then-live | The grounding check — whether a "Realized by" path exists |
| `ea/` trees only | Scope documents, decision records, reviews |
| The decision record and the corrected `stack-selection` section | The SQLite projection itself |
| | `RULE6` enforcement, still convention-only |

## Gap notes

- **Only `ea/` is checked, and that is a deliberate limit with a real cost.**
  A typo'd element ID in a scope document is not caught. The alternative is
  worse: scope documents cite elements in the same bolded form a motivation
  document uses to define one, so definitions and mentions are
  indistinguishable there — and `RULE6` freezes a merged scope document, so
  as the model moves on it will inevitably reference something retired, with
  no edit permitted to fix it. **Reference-checking an immutable document is
  incoherent, not merely awkward.** That argument is what set the boundary.
- **`RULE2` is still only half-enforced.** Links resolve; realizations are
  not verified to exist. Distinguishing a repository path from a team name
  is fuzzy, and a wrong CI failure teaches people to ignore CI. The grounding
  rule stays carried by review — worth knowing when reading any row in this
  repository that claims a realization.
- **A project whose `ea/` defines no elements is skipped entirely.** That is
  how the blank template scaffold passes: its layer READMEs are full of
  illustrative placeholders (`SALES.BSVC3`) by design. The cost is that a
  project which *should* have elements and has none gets silence rather than
  a warning.

## Open questions

- **Whether the two definition shapes should be reduced to one.** Goals and
  Principles read better as prose bullets than as table rows, which is why
  both exist — but two shapes mean two parsers and two ways to get it wrong.
  Interpretation adopted: keep both, because forcing Goals into a table would
  make the strategy layer worse to read, and the strategy layer is the one
  humans actually read. Revisit if a third shape ever seems necessary.
