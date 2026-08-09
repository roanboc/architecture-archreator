# Project Scope — Model the operating model

_[← Scope index](./README.md) · [EA home](../ea/README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** `organization/` on branch
`claude/repo-value-ux-review-3ur5y4`.

Every remaining item on archreator's improvement backlog was blocked on the
same missing input: a real organization modeled with the method. Depth 3,
the graph exporter's trigger conditions, multi-agent orchestration, and the
first real use of `restate-current-state` all wait on it.

So this initiative uses the method instead of improving it. The subject is
**the organization that produces archreator**, at Depth 2, modeled in
public. It is not an example — the fictional one was
[removed](../../../meta/scope/4_remove-the-fractal-example.md) precisely
because invented companies prove notation and nothing else.

This is a **docs-only initiative**. No code is delivered.

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 0_business-design | **Filled.** Three customer segments with one consolidated profile, and three business model canvases — one per product |
| 1_strategy | **Not started.** Derived from layer 0 after Gate 0, ending at Gate 1 |
| 2_business | **Not started.** Derived after Gate 0 |
| 3_information | **Not started** |
| 4_application | **Not started.** This is where the method, the site, and the future portal will land |
| 5_technology | **Not started** |
| domains | **Not used** — Depth 2. No business line passes the split test, and inventing one would repeat the mistake this initiative exists to avoid |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | _awaiting_ | — | The two canvases: three segments, one consolidated set of jobs, pains and gains, the value map, and three product business models |
| Gate 1 — Strategy | _pending Gate 0_ | — | The derived strategy and key business elements |
| Gate 2 — Business | — | — | **N/A** — docs-only initiative; no code is delivered |
| Gate 3 — Solution design | — | — | **N/A** — no solution design |

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | archreator had a method, a self-model of the method at Depth 1 (`meta/`), and a published site. The organization producing all of it was unmodeled |
| **Target** (delivered) | The organization modeled at Depth 2: who it serves, what it offers, how each product works economically — including the returns that are not money |

## Work packages and deliverables

### WP1 — Discover and write the value proposition canvas

- **Deliverables:** [`0_business-design/1_value-proposition-canvas.md`](../ea/0_business-design/1_value-proposition-canvas.md)
  — three segments, 6 jobs, 5 pains, 6 gains, 3 products, 5 pain relievers,
  6 gain creators, and the fit check
- **Outcome:** the value proposition is stated in the Requester's own terms
  and can be disagreed with

### WP2 — Write the business model canvases

- **Deliverables:** [`0_business-design/2_business-model-canvas.md`](../ea/0_business-design/2_business-model-canvas.md)
  — nine blocks per product, plus catalogues for channels, relationships,
  resources, activities, revenue and cost
- **Outcome:** the economics are explicit, including that most of the
  return is not monetary

### WP3 — Set up the tree

- **Deliverables:** [`organization/README.md`](../../README.md),
  [`docs/ea/README.md`](../ea/README.md), this scope document and its index
- **Outcome:** a fourth tree that a reader can tell apart from the other
  three at a glance

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| Both canvases, and the fit check between them | Layers 1–5, which are derived after Gate 0 |
| The non-monetary return, named and recorded | Valuing it — Social Return on Investment is named, not applied |
| The single-person concentration, stated as a risk | Doing anything about it |
| Provider neutrality as a posture | The decision record that would fix its limits |

## Gap notes

- **The largest structural risk is `KR1`, and it is a deliberate choice.**
  One person is the key resource behind two of three products and the only
  human in the organization. The Requester has no interest in scaling large,
  so this is chosen rather than accidental — but a choice is not an absence
  of risk, and the model says so rather than implying a resilience it does
  not have. The named route if it ever had to change is AI agents acting as
  consultants carrying the Requester's knowledge, which needs more AI
  maturity than exists today.
- **`RS1` and `RS2` are the primary returns and neither is measured.** The
  organization exists for mission progress and improvement through real
  usage. Both are recorded as non-monetary revenue streams; neither has a
  valuation method. Social Return on Investment is the candidate, and the
  Requester has applied it in governmental work — but naming a framework is
  not applying one.
- **archreator's own canvas guidance has no support for non-monetary
  return.** This model needed a concept the method does not provide, which
  makes it a gap in the method, not only in this model. Any non-profit or
  public-sector organization modeling itself with archreator will hit the
  same wall.
- **`KP3`, the contributor community, does not exist.** `RS1` depends on it.
  A community that never forms would make the primary non-monetary return
  theoretical.
- **Nothing reaches `CS2` or `CS3` who is not already looking.** Every
  channel today (`CH1`–`CH3`) reaches people already close to the tooling.
  `CH5` would change that and is Pending.

## Open questions

Consolidated from both canvases; each is recorded in the canvas that raised
it rather than restated in full here.

| # | Question | Where |
| - | -------- | ----- |
| 1 | How should the non-monetary returns be valued? | [business model canvas](../ea/0_business-design/2_business-model-canvas.md) |
| 2 | How far should provider neutrality go, and what may be provider-specific? | [business model canvas](../ea/0_business-design/2_business-model-canvas.md) |
| 3 | Is the contributor community a partner or an aspiration? | [business model canvas](../ea/0_business-design/2_business-model-canvas.md) |
