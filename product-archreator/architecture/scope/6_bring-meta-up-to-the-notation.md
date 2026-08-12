# Project Scope — Bring archreator's own model up to the notation standard

_[← Scope index](./README.md) · [EA home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** `meta/ea/` redrawn, on branch
`claude/repo-value-ux-review-3ur5y4`.

[Scope document 5](./5_diagram-notation-standard.md) wrote the notation
standard and applied it to `organization/`, and recorded the consequence
honestly in its own gap notes: **`meta/` and `site/` were left behind the
standard they document.** archreator's own model disagreeing with
archreator's own `RULE10` is precisely the inconsistency `ASM1` names —
artifacts that describe an architecture without anything having to
correspond to it.

This initiative closes half of that gap. `meta/` is redrawn; `site/` follows
in its own project's scope document, because `site/` is a separate project
and records its own initiatives.

This is a **docs-only initiative**. No element is added, removed or
renamed — only how they are drawn changes, plus one rule whose wording
applying it exposed.

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 1_strategy | **No change to elements.** `1_motivation.md` gains four sectional diagrams and a legend, and loses the single end-of-document view |
| 2_business | **`RULE10` narrowed** to element documents. `1_business-actors-and-roles.md` and `2_business-services.md` gain legends and sectional diagrams |
| 3_information | **No change** — archreator holds no data of its own at Depth 1; the layer has never existed here |
| 4_application | **No change to elements.** `1_application-components.md` gains a legend and a component diagram |
| 5_technology | **No change to elements.** `1_technology-services.md` gains a legend, a node diagram and an artifact diagram |
| domains | **No change** — Depth 1 |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — Depth 1; no business model |
| Gate 1 — Strategy | — | — | **N/A** — no strategy change; the motivation layer's elements are untouched |
| Gate 2 — Business | Requester | 2026-08-09 | The retrofit itself, requested directly after the notation standard merged, and the narrowing of `RULE10` that applying it exposed |
| Gate 3 — Solution design | — | — | **N/A** — no solution design |

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | Five element documents, five diagrams — one per document, at the end, no legends, no glyphs |
| **Target** (delivered) | Five element documents, seventeen diagrams — one per section, at the top, each document self-documenting |

## Work packages and deliverables

### WP1 — Redraw the motivation layer

- **Deliverables:** [`1_strategy/1_motivation.md`](../1_strategy/1_motivation.md)
  — a legend, then stakeholders-to-drivers, assessments-to-goals,
  goals-to-outcomes and principles-to-goals
- **Outcome:** the single view that showed twelve of thirty-six elements is
  gone, replaced by four that between them show all of them

### WP2 — Redraw the business layer

- **Deliverables:** [`1_business-actors-and-roles.md`](../2_business/1_business-actors-and-roles.md),
  [`2_business-services.md`](../2_business/2_business-services.md)
- **Outcome:** the AI actor is drawn in Application cyan here as everywhere
  else, and the rules-to-principles diagram makes `RULE10`'s cost visible
  rather than only stated

### WP3 — Redraw the application and technology layers

- **Deliverables:** [`4_application/1_application-components.md`](../4_application/1_application-components.md),
  [`5_technology/1_technology-services.md`](../5_technology/1_technology-services.md)
- **Outcome:** the one dashed edge in the component view is `ACMP13`
  partially enforcing `RULE2` — the single place this repository asks a
  reader to take grounding on trust, now visible at a glance

### WP4 — Narrow `RULE10`

- **Deliverables:** `RULE10` in
  [`2_business-services.md`](../2_business/2_business-services.md), and
  [`ea-doc-style`](../../../.claude/skills/architecture-doc-style/SKILL.md) § Every
  element document opens with "How to read this document"
- **Outcome:** a layer README that only indexes other documents is exempt,
  which is what applying the rule at scale showed it should always have said

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| `meta/ea/`'s five element documents | `site/docs/ea/` — a separate project, redrawn under its own scope document |
| The `RULE10` narrowing | Enforcing `RULE10` in CI |
| `meta/reviews/` and `meta/decisions/` diagrams | Nothing — they carry no element diagrams |

## Gap notes

- **`RULE10` is still carried by review.** Applying it by hand to five
  documents is exactly the kind of work a check would have caught: a
  `## How to read this document` heading is greppable, and so is a section
  whose first content is a table when a diagram exists further down.
  `scripts/check_model.py` already walks these files.
- **`site/` remains behind the standard until its own initiative runs.** The
  gap is now half as wide and is not closed; saying "brought the trees up to
  the standard" would be false while a whole project still disagrees with it.
- **Nothing verified that the redraw preserved meaning.** The element tables
  are untouched, so no fact moved — but a diagram that draws an edge the
  table does not claim is a new assertion, and only review catches that. Two
  such edges were added deliberately in WP2 and WP3 and are called out in
  the prose beneath them.
