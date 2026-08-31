# Project Scope — Reset the method, and keep the kernel

_[← Scope index](./README.md) · [Model home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** [`archreator` PR #49](https://github.com/roanboc/archreator/pull/49),
merged 2026-08-31 as method version 0.2.0. This document holds the gate for
the initiative that PR delivered, recorded here after the fact by the
Requester's explicit choice — see § Approvals.

## The problem

The method had grown costs nobody had measured against its own first
principle. A new project's first commit was 44 files and 6,626 lines, of
which nothing was about the project. The rulebook every model-writing skill
consults cost roughly 10,000 tokens on almost every activation. The reading
tools trusted a persisted SQLite projection that was rebuilt only when its
file was missing — verified on the largest real model on this method: a
renamed element was served under its old name with no warning, a new element
answered "no such element", and the generated brief stamped a revision hash
implying a currency its content did not have.

The Requester commissioned a reset: assess archreator as a customer who
understands their business but not enterprise architecture, and make the
method simpler without losing the rigor that makes it more than a prompt.

## The design

### 1. Two independent resets, then a comparison

The same request was answered twice, by two agents working independently.
One rebuilt the method — ten skills, a new runtime, conditional gates. The
other kept the eighteen-skill kernel and cut what a customer carries: the
scaffold to eleven files, the rulebook split so lookup tables load only when
reached for, the projection deleted in favor of a fresh parse, the portal
reduced to a generated stock configuration. The second was kept; the first
was mined for what the second lacked and closed. The comparison itself became
a third layer of work: the defects neither run's checks could see, the
records neither run wrote, and the migration path the breaking version bump
never shipped.

### 2. What 0.2 is, in one paragraph

Eighteen skills, three named gates — Direction, Understanding, Design — an
eleven-file scaffold whose front page carries a status row per layer instead
of empty folders, templates emitted by the skill that first has content for
them, one fresh parse with nothing cached, references written name-first
(`Name [ID]`), and a migration page for every project that adopted earlier.
The full account is the PR's own body and the engagement note this initiative
files — see § Work packages.

## EA alignment (assessed top-down before recording)

| Layer | Impact |
| ----- | ------ |
| 1_strategy | **No change.** The method's purpose, customers and principles are what the reset was judged against, not what it moved |
| 2_business | **No change to the elements.** The service the method delivers is the same; what changed is its cost |
| 3_information | **Falsified in places** — documents that describe the projection and its readers describe tools 0.2 deleted. Realigning them is the migration, named below |
| 4_application | **Falsified in places** — the application components include the SQLite projection, the portal builder and the PDF export, all removed in 0.2 |
| 5_technology | **Falsified in places** — deployment documents name workflows and publishing paths the reset replaced |

**The falsified documents stay as they are in this initiative.** This model
still runs on the 0.1 method; crossing it to 0.2 — scripts, gate vocabulary,
and the element catalogue realignment above — is
[`archreator` `docs/migrating.md`](https://github.com/roanboc/archreator/blob/main/docs/migrating.md)
applied here, and it is the next initiative, not a rider on this record.
Precedent: initiative 1 was exactly such a whole-model refresh, run on its
own.

## Approvals

Written with 0.2's named gates — a new document uses the current vocabulary;
the frozen documents above it keep theirs.

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Direction | — | — | **N/A** — the method's purpose and customers did not move; the reset changed what a customer carries, not why the method exists |
| Understanding | Requester | 2026-08-31 | The reset itself, granted in the delivering repository: the comparison reviewed, four review threads answered and acted on, and [`archreator` PR #49](https://github.com/roanboc/archreator/pull/49) merged by the Requester's instruction. This row records where that approval lives |
| Design | — | — | **N/A** — no solution design in this repository; the delivering PR's review covered the method's own code |

**Recorded after the fact, on purpose.** The Requester chose to leave this
repository untouched until the reset method was validated, so the initiative
that would ordinarily open before implementation opens here after the merge,
citing the approval where it actually happened. The gap between the rule and
this record is itself recorded — nothing here pretends the gate was shown a
draft.

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | Method 0.1: 44-file scaffold, four numbered gates, a persisted projection two readers trusted stale, a 500-line portal theme, whole-model PDF |
| **Target** (delivered) | Method 0.2 on `archreator` main. This model's own crossing to it is the remaining distance, held by the migration initiative |

## Work packages and deliverables

### WP1 — The comparison (delivered)

Two independent resets judged against the Requester's recorded principles,
the losing run mined, the stale-cache defect reproduced and measured, and the
winning branch's own defects found and fixed before merge.

### WP2 — The record (this initiative)

- This scope document, and its row in the [index](./README.md).
- [Engagement note 4](../../../org-archreator/architecture/engagements/4_the-method-reset-run-twice.md)
  — what the method did not cover, and the corrections that survive the
  closed branches.

### WP3 — The migration (out of scope, next)

Crossing this repository to 0.2 per the method's migration page: the shared
`scripts/`, the gate vocabulary in living documents, and the realignment of
the falsified layer documents above.

## In scope / out of scope

| In | Out |
| -- | --- |
| Recording the reset as an initiative, with its approval cited where it happened | **Migrating this repository to 0.2** — its own initiative, WP3 above |
| The engagement note carrying the corrections | **Re-litigating the comparison** — the closed PRs #47 and #48 remain readable history |
| Honest falsification verdicts per layer | **Realigning the falsified documents now** — they move with the migration, so the model changes once, not twice |
