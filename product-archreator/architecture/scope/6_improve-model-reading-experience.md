# Project Scope — Improve the model reading experience

_[← Scope index](./README.md) · [Model home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** [`archreator` PR #40](https://github.com/roanboc/archreator/pull/40).

Feedback from the Bigview enterprise-architecture project showed that the
model remained traceable but made business readers decode identifiers, infer
layer numbers, and reconstruct canvases from tables. This initiative makes
those readings explicit without changing the metamodel or adding a second
source of truth.

## EA alignment

| Layer | Impact |
| ----- | ------ |
| 0_business-design | **Not used** — the subject is the method, not an organization |
| 1_strategy | **No structural change.** The work improves the existing adopter and reviewer outcomes through `RES1` and `RES2` |
| 2_business | **No new service or rule.** Existing subject discovery, model validation and method distribution become easier for human readers to consume |
| 3_information | **No change.** Element IDs, names, canvas blocks and questions already exist; only their presentation changes |
| 4_application | **Changed resources, unchanged components.** `ACMP4` gains clearer document rules and `ACMP10` gains clearer templates |
| 5_technology | **No change.** Markdown and Mermaid remain the portable formats |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — Depth 1; the method has no canvases |
| Gate 1 — Strategy | — | — | **N/A** — no stakeholder, driver, goal, outcome or principle changes |
| Gate 2 — Business | Requester | 2026-08-29 | Visible ID-and-name references, a traditional visual canvas per product, named-layer question groups, and non-real example IDs; comments deferred |
| Gate 3 — Solution design | — | — | **N/A — declined at Gate 2.** The implementation remains portable Markdown and Mermaid |

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** | Cross-references can show bare IDs; business-model canvases are tables only; open questions use numeric layers; examples look like real elements |
| **Target** | Human-readable references retain IDs, every product has a recognizable canvas view, questions are grouped by named layer, and examples cannot pollute real-ID searches |

## Work packages and deliverables

### WP1 — Human-readable references and examples

- **Deliverables:** updated document rulebooks and scaffold examples.
- **Outcome:** references display both stable identity and business meaning;
  illustrative IDs use `#` rather than a number.

### WP2 — Business-facing canvas view

- **Deliverables:** updated canvas rulebook and discovery procedure.
- **Outcome:** the table remains the detailed source while each product also
  has a traditional nine-block visual view.

### WP3 — Named-layer open questions

- **Deliverables:** updated scope-writing guidance and scaffold log.
- **Outcome:** readers browse pending questions by layer name instead of
  translating `0`, `1` and `2` themselves.

## In scope / out of scope

| In scope | Out of scope |
| -------- | ------------ |
| The four approved reading-experience improvements | Page comments and selected-text annotations |
| Portable Markdown and Mermaid behavior | A portal-only representation or client-side model database |

## Gap notes

- Existing adopting projects are not rewritten automatically. They gain the
  behavior when their documents are next restated or regenerated.
- Selected-text annotation remains a separate initiative because it introduces
  identity, storage and hosting decisions that this presentation-only change does not.

## Open questions

None.
