# Project Scope — Rebuild the models on the current method

_[← Scope index](./README.md) · [Model home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** the `rebuild` branch and the pull request replacing `main`.

The models in this repository described a method that no longer exists.
Fifty-eight percent of documents named skills that had been renamed, every one
of the seventeen application components pointed at a path the plugin no longer
has, and the metamodel had moved on to levelled identifiers the model never
used. Restating that document by document would have cost what rebuilding
costs and produced a messier result, so the models are rebuilt from an empty
branch with the current method as the only input.

**This is a rebuild of the models, not of the method.** Nothing in
`archreator` changes because of it.

## What the clean room deliberately dropped

The previous corpus is preserved at the tag `pre-rebuild-2026-08` and is not
carried forward: sixteen scope documents, eight decision records, two reviews
and the engagement notes. They remain citable as prior art and are cited that
way — [decision 1](../decisions/1_the-process-model-stays-with-the-skills.md)
re-derives a question the old corpus had also reasoned about, rather than
inheriting its answer.

Three things were dropped as defects rather than as history:

| Dropped | Why |
| ------- | --- |
| The vendored skill corpus in `.claude/skills/` | It held the previous thirteen skill names and drifted silently from the plugin. The plugin is now enabled through `.claude/settings.json`, so there is no copy to drift |
| The root marketplace manifest | A leftover from when the plugin lived in this repository. It publishes nothing from here |
| Four hundred and thirty-one stereotypes on diagram nodes | The notation dropped them from content diagrams; the sweep was deferred and never ran. Written correctly from the start, the debt does not re-accrue |

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 0_business-design | **Not used** — Depth 1. The canvases describe an organization's customers and economics, and this subject has neither. Stated in [0_business-design/](../0_business-design/README.md) rather than left blank |
| 1_strategy | **Rebuilt.** Four stakeholders, three drivers, four assessments, four goals, three outcomes, five principles; six flat capabilities, five resources; one value stream in five stages. No courses of action — they are an organization's instrument |
| 2_business | **Rebuilt.** Two actors and four roles, with the AI actor's autonomy, decision rights and escalation stated in full; one product, six services, four channels; six business objects; six rules, each naming what enforces it. **No process catalogue** — see decision 1 |
| 3_information | **Rebuilt, and short.** Four data objects. Almost everything the method handles is prose read by people and agents, not a structure parsed by software |
| 4_application | **Rebuilt.** Eight application services and eleven components, skills grouped by the service they provide rather than one component per skill |
| 5_technology | **Rebuilt.** Four nodes, four services, one artifact, and no edge between any of them |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — Depth 1; this tree holds no canvases |
| Gate 1 — Strategy | Requester | 2026-08-22 | [1_motivation.md](../1_strategy/1_motivation.md), [2_capabilities-and-resources.md](../1_strategy/2_capabilities-and-resources.md) and [3_value-stream.md](../1_strategy/3_value-stream.md) — the strategy layer is new in a clean room, so it is approved rather than assumed unchanged |
| Gate 2 — Business | Requester | 2026-08-22 | [1_business-actors-and-roles.md](../2_business/1_business-actors-and-roles.md), [2_business-services.md](../2_business/2_business-services.md), [4_business-objects.md](../2_business/4_business-objects.md), [5_domain-context-and-rules.md](../2_business/5_domain-context-and-rules.md), and [decision 1](../decisions/1_the-process-model-stays-with-the-skills.md) |
| Gate 3 — Solution design | — | — | **N/A — declined at Gate 2.** The layers below the business layer describe an existing method rather than proposing a design; ordinary pull-request review covers them |

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | Three trees describing a superseded method: renamed skills, dead realization paths, no levelled identifiers, a vendored skill copy, and a notation the repository published but did not follow |
| **Target** (delivered) | Three trees describing the method as it is, checked green by both validators, with the plugin consumed rather than copied |

## Work packages and deliverables

### WP1 — The clean room

- **Deliverables:** the tag `pre-rebuild-2026-08` on the previous corpus; an
  orphan `rebuild` branch; the repository's own `CLAUDE.md`, `README.md`,
  `CONTRIBUTING.md`, `.gitignore` and `.claude/settings.json`; one copy of the
  validators and the projection at `scripts/`; `.github/workflows/docs-check.yml`.
- **Outcome:** a repository that checks itself, with the previous corpus
  preserved rather than discarded.

### WP2 — `product-archreator`

- **Deliverables:** the six layer documents named in the EA alignment table,
  plus [decision 1](../decisions/1_the-process-model-stays-with-the-skills.md)
  and this document. One hundred and one elements.
- **Outcome:** the method has a model that describes it.

### WP3 — The scaffold READMEs stopped teaching

- **Deliverables:** `0_business-design/README.md` and `domains/README.md` in
  each Depth 1 tree state that they are unused and why; `1_strategy/README.md`
  drops its `Source` column; `2_business/README.md` carries decision 1; four
  template layer views replaced with real ones.
- **Outcome:** every layer folder states its own declared state, and no
  illustrative identifier is left to dangle.

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| All three trees rebuilt on the current method | **Building the portal.** A published view of these models is a course of action the organization has not taken, and it belongs to that tree |
| The projection shipped and modeled as `ASVC8` | **Giving `ASVC8` a consumer.** It is built, works, and nothing reads it |
| Decision 1 recorded | **Making the cross-repository dependency it creates checkable.** No validator crosses the boundary |
| The notation followed from the first commit | **Any change to the method itself.** Defects found in the scaffold while rebuilding are recorded here and fixed in `archreator` |

## Gap notes

- **The scaffold's layer READMEs carry illustrative identifiers** — `BPROC7.2`,
  `SALES.BSVC3`, `CAP1.2.3` — which are exempt from validation under
  `scaffold/` and become dangling references the moment a real project defines
  its first element. Every project generated from the scaffold will hit this.
  Worked around in all three trees here; the fix belongs in `archreator`.
- **The scaffold ships no `.gitignore`**, so a generated project commits
  bytecode from its own validators, and would commit the projection. Fixed in
  `archreator`; this repository already carries the corrected file.
- **Decision 1's dependency is unenforced in this direction.** If the process
  catalogue is renumbered in `archreator`, nothing here fails. Closing it would
  need a check that crosses repositories, which is more machinery than the risk
  currently justifies.
- **`ASVC8` has no consumer, and that is drawn dashed rather than hidden.** The
  projection was built because a rendered view needs it; the rendered view is a
  later initiative.

## Open questions

- **Should `main` be the default branch again?** This repository's default is
  currently a working branch four commits ahead of `main`, which is why the
  preservation tag was placed on that branch rather than on `main`. Adopted
  interpretation: the pull request targets `main`, and the default should move
  back to it afterwards. Recorded rather than acted on, because it is a
  repository setting rather than a model change.
