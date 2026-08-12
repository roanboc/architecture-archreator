# Project Scope — Take `COA1`, stage one

_[← Scope index](./README.md) · [EA home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** `organization/docs/decisions/`,
`organization/docs/engagements/`, and the layer 1–4 changes, on branch
`claude/repo-value-ux-review-3ur5y4`.

`COA1` — AI agents acting as consultants — has been Pending since Gate 0,
"named as a route, explicitly not a plan". The Requester has now chosen it
over `COA2`. This initiative turns it into something started.

**What it turns out to be** is not a new product. The model already holds the
contradiction: `BSVC3` needs a person in the room, and `CAP9` claims the
expertise sits in the method. Both cannot be fully true, and **nobody has
written down what the person adds.** `COA1` is closing that gap, which makes
it the completion of `CAP9` rather than a new direction — and the reason it
has to precede `COA2`, whose whole value proposition is `CAP9` at scale.

Stage 1 builds the mechanism that captures what the method did not cover.
The reasoning is in [decision 1](../decisions/1_take-coa1-staged.md).

This is a **docs-only initiative**. The one artifact that could be called
code is a skill, which is instructions.

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 0_business-design | **No change.** Neither canvas moves. `RS1` gets its first mechanism, but `RS1` is a Gate 0 element and is not edited — the point is made in layer 1 |
| 1_strategy | **`CAP10` added** under `CAP2` — engagement-to-method learning, the only capability with no canvas source. **`COA1` moves from Pending to taken, staged** |
| 2_business | **`ROLE2` gains `ACT2`** as an assisting actor at co-pilot, behind `ACT1`. `BSVC3` gains `CAP10` and now feeds back into `PROD1` |
| 3_information | **`DOBJ7` added** — engagement pattern notes. The first element that crosses from confidential to public, with the rule governing that crossing |
| 4_application | **No new component.** The skill is part of `ACMP1`, whose count moves from twelve to thirteen |
| 5_technology | **No change.** Nothing new runs anywhere |
| domains | **No change** — Depth 2 |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — no business model change |
| Gate 1 — Strategy | _awaiting_ | — | `CAP10`, `COA1`'s change of state and its four stages, and the reading of `P1` that the later stages depend on |
| Gate 2 — Business | _awaiting_ | — | `ROLE2`'s assisting actor, `DOBJ7` and the confidentiality rule, and the `engagement-retrospective` skill |
| Gate 3 — Solution design | — | — | **N/A** — not requested |

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | `COA1` Pending. `CAP9` claimed method-carried competence with nothing verifying it. What the Requester knows beyond the method lived only in their head, and `RS1` had no mechanism |
| **Target** (delivered) | `COA1` taken and staged. A capability, a data object and a skill that together turn what an engagement taught into method — starting with initiatives, so it works before the next client |

## Work packages and deliverables

### WP1 — The decision

- **Deliverables:** [`docs/decisions/README.md`](../decisions/README.md) and
  [`1_take-coa1-staged.md`](../decisions/1_take-coa1-staged.md) — the first
  decision record in this tree
- **Outcome:** the ordering against `COA2` is settled with its reasoning, the
  four stages are named, and the `P1` argument the later stages depend on is
  written down before anyone objects to it

### WP2 — The capability and the course of action

- **Deliverables:** [`1_strategy/2_capabilities-and-resources.md`](../1_strategy/2_capabilities-and-resources.md)
  — `CAP10` under `CAP2`, `COA1` restated as taken and staged, both diagrams
  updated
- **Outcome:** the strategy layer says the organization can now improve its
  method on purpose, which it previously did only by accident

### WP3 — The data object and its boundary

- **Deliverables:** [`3_information/1_data-objects.md`](../3_information/1_data-objects.md)
  — `DOBJ7`, the edge from `DOBJ4`, and the rule governing it
- **Outcome:** the one place information crosses from confidential to public
  is drawn, named, and governed rather than left to judgement in the moment

### WP4 — The mechanism

- **Deliverables:** `.claude/skills/engagement-retrospective/SKILL.md`
  (recorded in [`meta/scope/8`](../../../product-archreator/architecture/scope/8_the-engagement-retrospective-skill.md)),
  and [`docs/engagements/README.md`](../engagements/README.md)
- **Outcome:** the next initiative or engagement to close produces a note
  instead of nothing

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| Stage 1 — capture | Stages 2, 3 and 4. Each needs the previous one's evidence |
| Widening capture to any initiative, not only paid engagements | Anything that waits for a client |
| The confidentiality rule for `DOBJ7` | Doing anything about `DOBJ4` itself, which still has no system |
| `COA1`'s ordering against `COA2` | Abandoning `COA2` — it is ordered, not dropped |

## Gap notes

- **Nothing has been captured yet.** The mechanism exists; the evidence does
  not. Stage 2 cannot start until several notes exist, and the first useful
  signal — a pattern appearing twice — is by definition two engagements away.
- **The generalization test is unreliable on one case, and the skill says
  so.** That is deliberate, and it means this mechanism is slow on purpose.
  A method that encodes every one-off gets worse, not better.
- **`DOBJ4` is still ungoverned.** `DOBJ7` gives the confidential material a
  supervised exit, which is progress, but the raw client information is still
  held by one person outside any system — open question 2 of
  [initiative 2](./2_complete-layers-3-to-5.md), unchanged.
- **Success has a measure and no baseline.** Hours per engagement is
  observable because clients are known. Nobody recorded what it is today, so
  the first measurement will be a number without a comparison.

## Open questions

| # | Question | State |
| - | -------- | ----- |
| 1 | How does the notation record **one actor at two autonomy levels in two roles**? | Open, and dormant. `ACT2` is co-pilot in both `ROLE1` and `ROLE2` today, so nothing is lost. From stage 3 the actors table's single autonomy column cannot say what the model needs. Deliberately not fixed on a single case — it becomes a real decision, and a change to `ea-doc-style`, when stage 3 is proposed |
| 2 | What is the baseline for hours per engagement? | Open. The measure exists; nobody has recorded where it starts |
