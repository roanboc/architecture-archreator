# Project Scope — Rebuild the models on method 0.2

_[← Scope index](./README.md) · [Front door](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** the pull request for this initiative, and everything it
contains.

## The problem

Method 0.2 was a foundational reset — three named gates, an eleven-file
scaffold, lazy materialization, name-first references, nothing cached — and
it traversed every document these models are made of. The pre-0.2 corpus
described retired machinery in three layers, spoke the old gate vocabulary
throughout, and carried seventeen initiatives of accumulated history in its
prose. Correcting it in place would have rewritten the whole model twice:
once to cross the version, once to simplify.

So this initiative takes the route `restate-current-state` names for total
drift: the corpus is preserved unchanged at
[`pre-02-2026-08`](https://github.com/roanboc/architecture-archreator/tree/pre-02-2026-08),
treated from here on as reference material, and the models are rebuilt from
scratch on 0.2 — validating the new method with its own.

## The design

- **Two trees, not three.** The guidance site folds into the product as one
  service, one component and one deployment row — it realizes a service of
  the product, and a tree that only restates elements belonging elsewhere is
  a folder pretending to be a project.
- **The two key customers lead the canvases.** The independent builder and
  the enterprise architect are the segments the method is written for, over
  one model with two ways in; the business owner is the consulting segment,
  its two pre-0.2 stages consolidated into one segment with a stage
  distinction.
- **Current state only.** No pending future elements, no roadmap, no carried
  history: the transition layer is a stated gap until a roadmap earns its
  own initiative through Direction, and every document describes its subject
  rather than its own past.
- **The deleted modules are gone from the model** — the SQLite projection,
  the custom portal builder, the PDF exporter and their query tools appear
  nowhere except the preservation ref.
- **Everything lands `◐`.** A rebuild is a new draft, whatever the old
  corpus had passed; the gates below are what turn it back into an approved
  model.

## EA alignment (assessed top-down before recording)

| Tree | Layer | Impact |
| ---- | ----- | ------ |
| org | 0_business-design | **Rebuilt** — segments reframed around the two key customers; portal-era pending elements dropped |
| org | 1_strategy | **Rebuilt** — derived from the new canvases; seven goals, seven principles, one staged course of action, and the capability areas derived from the canvas's key activities |
| org | 2_business | **Rebuilt into one document** — actors with the AI actor's autonomy stated, services, and the organization's own two processes modeled to level 2, with the two empty bands reported as findings |
| org | 3_information | **New** — the two domains the organization masters and the one it defers to the product |
| org | 4–5 | **De-materialized** — stated as external on the front door, per the status-table discipline |
| product | 1_strategy | **Rebuilt** — the three adopting-project roles as stakeholders; goals now serve the organization's by cross-model reference |
| product | 2_business | **Rebuilt** — eight services, the site's folded in |
| product | 3_information | **New** — data domains before data objects, three domains, the leveled identifier carrying the hierarchy |
| product | 4_application | **Rebuilt** — twelve components, all of them shipping code; the deleted modules absent |
| product | 5_technology | **Rebuilt into one document** — five nodes, none operated by this organization, and the deployment table |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Direction, first sitting | — | — | **Pending** — the organization's canvases: the segments, the two products, the fit |
| Direction, second sitting | — | — | **Pending** — the strategy derived from them, both trees' motivation included |
| Understanding | — | — | **Pending** — the business and information layers, and the descriptive application and technology catalogues |
| Design | — | — | **N/A** — a docs-only initiative; the components described are shipped code, not a proposal |

**Where these gates happen:** the pull request for this initiative — each
sitting may be granted as a review reply naming what it covers.

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | Three trees, 105 documents, on method 0.1 — three layers describing deleted machinery, four numbered gates, seventeen initiatives of history in the prose |
| **Target** (this initiative) | Two trees, ~30 documents, on method 0.2 — every element grounded in something that ships, every document `◐` until the gates above are granted |

## Work packages and deliverables

- **WP1 — The organization's model**: canvases, strategy, business and
  information.
- **WP2 — The product's model**: strategy through technology, the site
  folded in, scope and federation.
- **WP3 — The shared machinery**: the 0.2 validators and parse replacing the
  0.1 toolchain at the repository root; the repository's entry points and
  ignore rules rewritten to match.

## In scope / out of scope

| In | Out |
| -- | --- |
| Both trees rebuilt on 0.2, from the preserved corpus as reference | **Any new modeling beyond the subject as it is** — no roadmap, no future elements; a transition layer is its own later initiative |
| The site folded into the product | **Carrying records forward** — the seventeen initiatives, five decisions and four engagement notes are prior art at the ref, by the Requester's explicit choice |
| Honest `◐` on everything, with the gates pending in this document | **Re-validating by assertion** — nothing inherits the old gates' `●`; approval happens again or the mark stays draft |
