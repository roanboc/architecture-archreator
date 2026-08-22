# Project Scope — Rebuild the models on the current method

_[← Scope index](./README.md) · [Model home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** the `rebuild` branch and the pull request replacing `main`.

The organization's half of the clean-room rebuild recorded in the method's own
[scope document 1](../../../product-archreator/architecture/scope/1_rebuild-the-models-on-the-current-method.md).
The models described a method that no longer exists — renamed skills, dead
realization paths, and a metamodel that had moved on — so all three trees were
rebuilt from an empty branch with the current method as the only input.

**This tree is the exception to "the current method as the only input".** The
organization's stakeholders, canvases, capabilities and courses of action are
not derivable from the `archreator` repository; they came from discovery with
the Requester. The previous tree's element layers were therefore treated as
the **discovery record** and re-expressed in current notation, rather than
re-derived from a blank page. The alternative — re-running Gate 0 and Gate 1
from nothing — would have discarded business facts with no other source.

## What changed in the re-expression

| Change | Why |
| ------ | --- |
| **Capabilities became levelled** — three areas at level 1 with `CAP1.1` … `CAP3.2` beneath them, replacing ten flat identifiers with a `Level` and a `Composed of` column | The metamodel now carries the hierarchy in the identifier, so the parent column is redundant. The old model predates that and said so at the time |
| **Value stream stages became levelled** — `VS1.1` … `VS1.6` rather than a numbered column inside one element | Same reason |
| **Processes gained the four bands** — strategic, operational, support, evaluation, with a focus table per branch | The method now requires the classification, and applying it surfaced that two of four bands are empty |
| **Skill names and paths corrected throughout** | Eleven skills were renamed and the scaffold moved; every realization path in the old tree pointed at something that no longer exists |

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 0_business-design | **Rebuilt.** Three segments, six jobs, five pains, six gains, three products, five pain relievers, six gain creators; the nine business-model blocks, and the canvas-to-ArchiMate mapping |
| 1_strategy | **Rebuilt and re-levelled.** Five stakeholders, six drivers, five assessments, six goals, seven outcomes, seven principles; three capability areas over seven capabilities, five values, four resources, three courses of action; one value stream in six stages |
| 2_business | **Rebuilt.** Five actors, three roles, two contracts, one collaboration; three products referenced from the canvas, four services, five interfaces; six processes in two of four bands; seven business objects; no rules, with a verdict |
| 3_information | **Rebuilt.** Seven data objects, three of which this organization does not hold |
| 4_application | **Rebuilt.** Four services and five components, with the empty cell under advisory left visible |
| 5_technology | **Rebuilt.** Five services over four nodes, none operated by this organization |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | Requester | 2026-08-22 | [1_value-proposition-canvas.md](../0_business-design/1_value-proposition-canvas.md) and [2_business-model-canvas.md](../0_business-design/2_business-model-canvas.md), re-expressed from the previous tree as the discovery record |
| Gate 1 — Strategy | Requester | 2026-08-22 | [1_motivation.md](../1_strategy/1_motivation.md), [2_capabilities-and-resources.md](../1_strategy/2_capabilities-and-resources.md) and [3_value-stream.md](../1_strategy/3_value-stream.md), including the re-levelling of capabilities and stream stages |
| Gate 2 — Business | Requester | 2026-08-22 | The five business-layer documents, and [decision 1](../decisions/1_take-coa1-staged.md) re-expressed with the new capability identifiers |
| Gate 3 — Solution design | — | — | **N/A — declined at Gate 2.** Layers 3 to 5 describe what exists rather than proposing a design |

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | An organization model naming skills that had been renamed, realization paths that no longer resolved, and flat identifiers for catalogues the metamodel can now level |
| **Target** (delivered) | The same organization, described accurately, with the hierarchy in the identifiers and the process bands applied |

## Work packages and deliverables

### WP1 — The canvases

- **Deliverables:**
  [1_value-proposition-canvas.md](../0_business-design/1_value-proposition-canvas.md),
  [2_business-model-canvas.md](../0_business-design/2_business-model-canvas.md),
  including the canvas-to-ArchiMate mapping that every `Source` column points at.
- **Outcome:** Gate 0's subject exists again, and the strategy layer has
  something to be derived from.

### WP2 — The strategy layer, re-levelled

- **Deliverables:** the three strategy documents, with capabilities as three
  areas over seven, and the stream as six levelled stages.
- **Outcome:** the catalogues carry their hierarchy in the identifier, and no
  table needs a parent column.

### WP3 — The business layer, with the bands applied

- **Deliverables:** the five business documents, and
  [decision 1](../decisions/1_take-coa1-staged.md).
- **Outcome:** the process map is classified, and the two empty bands are
  visible as a finding rather than hidden by a flat list.

### WP4 — Layers 3 to 5

- **Deliverables:** the data objects, the application services and components,
  and the technology services.
- **Outcome:** the three facts this organization most needs stated — it holds
  almost nothing, one business service has no software, and it operates no
  infrastructure — are each stated once, in the layer that owns them.

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| Re-expressing the organization's model on the current method | **Changing what the organization is.** No segment, product, course of action or principle is added, removed or reinterpreted |
| Re-levelling capabilities and stream stages | Decomposing anything to a third level. No named pain justifies one |
| Applying the four process bands | **Filling the two empty bands.** That would mean documenting how direction is set, which is real work and a different initiative |
| Carrying decision 1 forward, re-expressed | The three engagement notes, which were not carried — see the gap notes |

## Gap notes

- **The engagement notes were not carried, and they are the one loss with no
  other source.** Three notes recorded what the method failed to cover during
  real work, generalized past recognition of the client. Everything else in
  this tree was derivable or re-expressible; those were field observations.
  `CAP2.3` is consequently described as having no evidence today — the
  mechanism is intact, the record of having exercised it is gone. Recovering
  them means reading them at the tag and deciding, note by note, whether each
  still holds.
- **Two of four process bands are empty.** `ROLE3` decides direction, pricing
  and what the organization is for, and no process describes how. Documenting
  it is a normal initiative, and until then the model says the gap exists
  rather than implying the six operational processes are the whole business.
- **Three of seven outcomes have no collection method.** `COA3` is the course
  of action pointed at this, and it is Pending. Until it is taken, the
  organization cannot evidence its own main claim.
- **Rules from the tier below cannot be cited by identifier.** The business
  layer states that this organization adds no rules of its own and follows the
  method's — and cannot name them, because identifiers are scoped per tree.
  This is the third occurrence of that limitation in this repository.

## Open questions

- **Should the engagement notes be recovered from the tag?** Adopted
  interpretation: **not automatically.** They are historical records of what
  the method lacked at a moment, and several of those lacks have since been
  fixed — carrying them forward unread would restate stale findings as
  current. Recovering them is a judgement per note, and belongs to whoever
  next runs `run-retrospective`. Recorded here so the loss is visible rather
  than silent.
