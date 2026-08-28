# Decision 5 — Folders that are not the architecture, and what moving one costs

_[← Decisions index](./README.md)_

**Status:** Accepted
**Date:** 2026-08-27
**Touches:** [architecture/README.md](../README.md), [roadmap/](../6_transition/README.md),
and the scaffold the method emits

## Context

The Requester looked at a generated project and named something the method has
been carrying without noticing:

> Some of those folders are not really architecture, they should belong to
> another tree and probably also numbered as per logical architectural order

`architecture/` holds nine things, and they are three different kinds:

| | Folders | What they are | Read by the validators? |
| --- | --- | --- | --- |
| **The model** | `0_business-design/` … `5_technology/`, `domains/` | The subject as it is | Yes |
| **Also the model** | `6_transition/` | Where the subject is going — Plateaus and Gaps, which are ArchiMate Implementation & Migration elements | **Yes** |
| **Not the model** | `scope/`, `decisions/`, `reference/`, `reviews/`, `engagements/` | How the model got here: what changed, why, what it was built from | **No** — `model_graph.py` names them `NARRATIVE` and skips them |

**The code already agrees with the Requester.** The parse has a constant listing
the folders that are *about* the model rather than part of it, and it skips
them. They are nested inside `architecture/` anyway, which says the opposite.

And `6_transition/` is the reverse mistake: it holds real elements, it **is** parsed,
and it is the only model folder with no number — so it reads as narrative when
it is the sixth layer.

## What moving them costs, which is the whole difficulty

Renaming or moving a folder breaks every link into it, and some of those links
are in documents the method forbids rewriting:

> A merged scope document is never rewritten, because it is the record of what
> was approved on a date and against what information.

Six merged scope documents link into `6_transition/`. Repairing them is an edit to
an immutable record; not repairing them fails `check_links.py`. **The method
has no story for a structural refactor of its own folders**, which is a real
gap and not a small one.

## Options considered

| Option | Why not (or why) |
| ------ | ---------------- |
| **Move everything now** | Breaks links in six immutable documents, in a repository whose CI fails on a broken link. It is the right end state and it cannot be reached in one step without deciding the question below first |
| **Leave it and document the intent** | The confusion ships into every project the method emits. `6_transition/` in particular is mis-filed in a way that makes a reader treat real elements as narrative |
| **Decide what "never rewritten" protects, then move what is cheap** | A merged record protects **what was claimed and approved**. A path is neither |

## Decision

**A merged document's *claims* are immutable; its *links* may be repaired when
a file moves.** Repairing a path does not change what was approved, by whom, or
against what information — and refusing to repair it means the method can never
reorganise itself without breaking its own checks.

A link repair to a merged document carries no gate and needs no new scope
document. Anything that changes a sentence still does.

**With that settled, `6_transition/` becomes `6_transition/`** — numbered, because
it holds ArchiMate Implementation & Migration elements and belongs in the layer
sequence, and named for the skill that fills it.

**The narrative folders stay where they are for now**, and moving them to a
sibling `record/` is recorded as a gap rather than done here. It touches five
folders across three trees, every skill that writes into one, and the parse
constant that lists them. It is the right shape and it is a separate
initiative — calling it small would be how it arrives half-finished.

## Consequences

- **The method can reorganise itself.** Without the carve-out above, every
  folder name chosen early was permanent, which is a strange property for a
  method about changing things deliberately.
- **`6_transition/` stops looking like narrative.** A reader who sees five numbered
  folders and four unnumbered ones reasonably concludes the numbers mark what
  matters. Now they do.
- **The larger split is written down rather than lost.** `GAP17` on the
  [target state](../6_transition/1_target-state.md) carries it, so the next person
  to notice finds it already reasoned about.
- **`vision/`, and folders like it, have an answer.** A repository-root folder
  that is neither the model nor its record is one of two things: source
  material, which belongs in `reference/`; or somebody's intent, which belongs
  in the strategy layer where it can be approved. The method should say so, and
  that is part of the same gap.
