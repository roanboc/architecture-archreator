# Project Scope — Element IDs, and the notation standard

_[← Scope index](./README.md) · [EA home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** `site/docs/ea/` on branch
`claude/repo-value-ux-review-3ur5y4`.

The parent template published a
[diagram notation standard](../../../architecture/scope/5_diagram-notation-standard.md)
and recorded that this project was left behind it. Starting the retrofit
surfaced a bigger gap underneath: **this model had almost no element
identifiers.** `scripts/check_model.py` found six, all of them goals and
principles, and reported fourteen tables as unvalidated — so most of this
model could not be referenced from anywhere and could not be checked by
anything.

The notation cannot be applied without identifiers, because a node label is
`<glyph> [«Stereotype»] <ID><br><description>`. So this initiative does both:
assign the missing identifiers, then redraw.

This is a **docs-only initiative**. No page changes; no element's meaning
changes.

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 1_strategy | **Identifiers assigned** — `STK1`–`STK3`, `DRV1`–`DRV2`, `VS1`. `G1`–`G4` and `P1`–`P2` already had them. Two drivers where the table previously listed one driver twice, from two sides |
| 2_business | **Identifiers assigned** — `ACT1`–`ACT3`, `ROLE1`, `BSVC1`, `BPROC1` |
| 3_information | **Identifiers assigned** — `DOBJ1` |
| 4_application | **Identifiers assigned** — `ASVC1`, `ACMP1`–`ACMP6`. The shared stylesheet becomes a component, having previously been mentioned only in prose |
| 5_technology | **Identifiers assigned** — `TSVC1`–`TSVC2`, `NODE1`–`NODE2`, `ART1` |
| domains | **No change** — Depth 1 |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — Depth 1; no business model |
| Gate 1 — Strategy | — | — | **N/A** — no strategy change. Identifiers are assigned to existing elements; the one consolidation (two drivers into one, with two edges) restates what the old table already said twice |
| Gate 2 — Business | Requester | 2026-08-09 | The retrofit, requested directly after the notation standard merged |
| Gate 3 — Solution design | — | — | **N/A** — no solution design |

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | 6 identified elements, 14 unvalidated tables, 9 diagrams — one per document or per layer README, no legends, no glyphs |
| **Target** (delivered) | 30 identified elements, all references validated in CI, 20 diagrams — one per section, each element document self-documenting |

## Work packages and deliverables

### WP1 — Assign element identifiers

- **Deliverables:** identifiers across all eight element documents in
  [`docs/ea/`](../README.md)
- **Outcome:** `scripts/check_model.py` validates this project instead of
  reporting it as uncovered, and any document in the repository can now
  reference an element here by identifier

### WP2 — Redraw to the standard

- **Deliverables:** [`1_motivation.md`](../1_strategy/1_motivation.md),
  [`3_value-stream.md`](../1_strategy/3_value-stream.md),
  [`1_business-actors-and-roles.md`](../2_business/1_business-actors-and-roles.md),
  [`2_business-services.md`](../2_business/2_business-services.md),
  [`1_data-objects.md`](../3_information/1_data-objects.md),
  [`2_application-components.md`](../4_application/2_application-components.md),
  [`1_technology-services.md`](../5_technology/1_technology-services.md),
  [`2_deployment.md`](../5_technology/2_deployment.md)
- **Outcome:** every element document opens with its own legend and every
  section opens with its diagram

### WP3 — Remove the duplicated layer views

- **Deliverables:** the five layer READMEs, each losing its diagram and
  gaining a pointer; [`docs/ea/README.md`](../README.md)'s cross-layer
  overview redrawn to the standard
- **Outcome:** the layer views that restated their own documents' content —
  and had gone stale, still naming `site/index.html` after the move to
  `public/` — are gone rather than maintained in two places

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| The model under `docs/ea/` | The published pages under `public/` — see the gap note |
| Identifiers for every element | Renaming or re-scoping any element |
| Consolidating one driver stated twice | Any other consolidation |

## Gap notes

- **The published architecture page is now a stale derived view.** `ACMP5`
  renders this project's EA layers in hand-written CSS
  ([decision 2](../decisions/2_site-diagram-rendering.md)), and the model it
  renders has just changed shape — identifiers, glyphs, one diagram per
  section. By this project's own `P1` the source wins and the page is
  behind it, which makes this **doc drift of exactly the kind
  `DOBJ1`'s own notes call out**. It affects both language editions. Closing
  it is a content initiative, not a modeling one, and it is not done here.
- **`ACMP6` was invisible before this change.** The shared stylesheet
  carries every diagram on the site and appeared only in a sentence at the
  end of a paragraph. Giving it an identifier made the coupling visible: it
  is the only component the other five depend on.
- **Two drivers where there had been one, listed twice.** The old table gave
  the same driver two rows — the Pilot's side and the reader's side — which
  a diagram cannot draw. It is now one element with two edges, and the
  Spanish-language driver is the genuinely separate second one.
- **Nothing checks that a document opens with a legend.** `RULE10` is carried
  by review in this project as in every other.
