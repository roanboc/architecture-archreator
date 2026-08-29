# Project Scope — Focus the question

_[← Scope index](./README.md) · [Model home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** the corresponding change in `archreator` and this model alignment.
**Extends:** [initiative 13](./13_answer-one-question.md).

Initiative 13 let a reader name a graph scope, but the command still asked in
the model's vocabulary: element, layer, type and depth. A person normally
arrives with a different choice — whether they need to understand the
business, the information, the solution, an end-to-end impact or a decision.
Selecting every layer just in case recreates the unreadable graph the brief
replaced.

## The design

### 1. Confirm the reader's question before selecting layers

The new `answer-architecture-question` skill recommends and confirms one of
five human-facing viewpoints. It asks what the view should help the reader
understand, not which ArchiMate layers they know how to select:

| Focus | Primary content | Supporting context |
| ----- | --------------- | ------------------ |
| Business and operations | Motivation, Strategy, Business | Directly connected Information and Application |
| Information and data | Business, Information, Application | Directly connected Strategy and Technology |
| Solution and technology | Application, Technology | Directly connected Business and Information |
| End-to-end impact | Every reached layer | None omitted by focus |
| Decision overview | Motivation, Strategy, Business, Implementation & Migration | Directly affected Information, Application and Technology |

The agent infers a recommendation, confirms it, and resolves an actual model
anchor. `impact` is the recommendation for a change unless the request clearly
centres another question.

### 2. The conversation and command express the same choice

`build_brief.py` gains `--focus business|information|solution|impact|decision`.
Focus runs after the existing scope traversal: every reached primary-layer
element stays; supporting-layer elements stay only when directly related to a
retained primary element; the named anchor always stays. What focus removes is
listed in the boundary section rather than disappearing silently.

The option is deliberately optional. Existing callers without `--focus`
retain the current all-elements behavior, while the skill always passes the
focus the reader confirmed.

### 3. The brief declares its editorial boundary

The generated header states the focus, anchor or scope, traversal depth,
emphasis and de-emphasized context. Its leading diagram heading follows the
question. Catalogue facts, relationship declarations and excerpts remain
unchanged and verbatim; the projection schema does not move.

## EA alignment

| Layer | Impact |
| ----- | ------ |
| 0_business-design | **Not used** — Depth 1 |
| 1_strategy | **No change.** The reader-first brief serves existing `G1` and capabilities |
| 2_business | **`BSVC8` and `BOBJ10` restated.** Interrogation confirms one viewpoint; the brief records that focus and what it de-emphasized |
| 3_information | **No change.** `DOBJ4` and its projection schema are unchanged |
| 4_application | **`ASVC10`, `ACMP3` and `ACMP17` restated.** A portable skill owns the conversation and the generator owns deterministic selection |
| 5_technology | **No change.** No runtime, renderer or network dependency is added |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — Depth 1 |
| Gate 1 — Strategy | Requester | 2026-08-29 | No strategy change; improve human visualization while preserving agent-readable Markdown |
| Gate 2 — Business | Requester | 2026-08-29 | Generated briefs only; five predefined focuses; the agent confirms the reader's question before generation |
| Gate 3 — Solution design | Requester | 2026-08-29 | Agent plus CLI; optional `--focus` for compatibility; deterministic primary/supporting-layer selection and explicit exclusions |

## Work packages

1. Add the five focus presets, metadata and boundary reporting to `build_brief.py`.
2. Add `answer-architecture-question` as `BPROC3.3` and bind it into the portable skill corpus.
3. Update the process model, catalogue, scaffold guidance and publishing documentation.
4. Add synthetic graph tests and verify five worked-model briefs.

## In scope / out of scope

| In scope | Out of scope |
| -------- | ------------ |
| One confirmed focus per generated brief | Combined viewpoints |
| Deterministic selection and headings | AI-authored summaries or inferred facts |
| Backward-compatible CLI | Changing authored diagrams |
| Explicit focus exclusions | Adaptive complexity scoring and primary-path emphasis |
