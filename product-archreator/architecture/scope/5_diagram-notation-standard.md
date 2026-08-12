# Project Scope — The diagram notation standard

_[← Scope index](./README.md) · [EA home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** `docs/ea/README.md` § Notation conventions,
`.claude/skills/ea-doc-style/SKILL.md`, and `RULE10`, on branch
`claude/repo-value-ux-review-3ur5y4`.

Modeling [the organization](../../../org-archreator/README.md) at Depth 2 put the
method's diagrams in front of a Requester for the first time at volume, and
they did not survive it. The notation had one device — a «stereotype» word in
a layer-coloured box — and four separate problems surfaced in one review:

1. A single view per document could only ever be a **selection**, and one
   that looked complete.
2. In a **single-layer** view the layer colour distinguished nothing, so
   every element looked alike.
3. Diagrams sat at the **end** of documents, after the tables they were
   supposed to make readable.
4. Node labels buried the **identifier** mid-label, so scanning a diagram for
   `CAP1` meant reading every node.

This initiative fixes all four and writes the result into the method. It is a
**docs-only initiative**: no code, and the only "implementation" is that
every diagram in `organization/` was redrawn to the new standard as the test.

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 1_strategy | **No change.** No new goal or principle; `P4` and `P3` already covered the ground |
| 2_business | **`RULE10` added** — every EA document opens with its own notation legend, and every section with a diagram opens with it |
| 3_information | **No change** |
| 4_application | **No change.** The notation is carried by `ea-doc-style` and the template README, both already modeled |
| 5_technology | **No change** |
| domains | **No change** |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — no business model change |
| Gate 1 — Strategy | — | — | **N/A** — no strategy change |
| Gate 2 — Business | Requester | 2026-08-09 | The notation itself, approved incrementally as it was tested on `organization/` — diagram-first, one per section, glyphs, tone ramps, identifier-first labels — and then the instruction to write it into the method |
| Gate 3 — Solution design | — | — | **N/A** — no solution design |

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | One notation device: a «stereotype» label and a per-layer fill. One diagram per document, at the end |
| **Target** (delivered) | Four devices — label format, glyph, shape, colour — specified in one place, with diagram-first ordering and a legend in every document |

## Work packages and deliverables

### WP1 — Specify the notation

- **Deliverables:** [`docs/ea/README.md`](../../../.claude/skills/project-bootstrap/templates/architecture/README.md) § Notation
  conventions — the label format, the glyph set for motivation, strategy,
  business and both canvases, the default shape per element, the per-layer
  tone ramps, and the drawing rules
- **Outcome:** one source for four devices, so no document has to invent
  them and none can drift

### WP2 — Put it in the skill

- **Deliverables:** [`ea-doc-style`](../../../.claude/skills/architecture-doc-style/SKILL.md)
  § ArchiMate on Mermaid, § Diagrams come first, § How to read this document,
  and the document skeleton
- **Outcome:** an agent drawing a diagram reaches the rules through the skill
  it already loads, rather than needing to be told

### WP3 — Test it on a real model

- **Deliverables:** all seven documents in
  [`organization/docs/ea/`](../../../org-archreator/architecture/README.md) redrawn —
  33 diagrams where there were 5
- **Outcome:** the standard is evidenced rather than asserted, and the
  failures it was written to fix are visibly gone

### WP4 — Record the rule

- **Deliverables:** `RULE10` in
  [`2_business-services.md`](../2_business/2_business-services.md), and
  [the notation review](../reviews/2_diagram-notation-icons.md) closed with
  its outcome
- **Outcome:** a future document that skips its legend is a rule violation,
  not a matter of taste

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| The notation, and `organization/` redrawn to it | `meta/` and `site/`, whose diagrams still use the old single-view style |
| Unicode glyphs | True ArchiMate icons — tested and recorded as not portable enough |
| A legend per document | Any tooling that checks one exists |

## Gap notes

- **`meta/` and `site/` are now behind the standard they document.** Both
  carry single end-of-document views with no legend and no glyphs. Neither is
  wrong, but archreator's own trees disagreeing with archreator's own rule is
  exactly the inconsistency `ASM1` is about. Bringing them up is a small,
  entirely mechanical initiative that nobody has run.
- **`RULE10` is carried by review, like `RULE2`.** Nothing checks that a
  document opens with a legend or that a section's diagram precedes its
  table. A validator could check the first — a `## How to read this document`
  heading is greppable — and would be a natural extension of
  `scripts/check_model.py`.
- **The per-document legend duplicates the global notation on purpose.** That
  is a cost paid against `P3`, and it is the one place in the method where
  duplication is deliberately accepted. The justification is that these
  documents are read one at a time and out of order; if that ever stops being
  true, the rule should be revisited rather than quietly kept.
- **Shapes are assigned per document, not globally.** Mermaid has about a
  dozen usable shapes and ArchiMate has fifty elements, so collisions across
  documents are unavoidable and are resolved by each document's own legend. A
  reader comparing two documents from different layers can be misled by a
  shape; the glyph and the colour are what stay true.
