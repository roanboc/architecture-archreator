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
| 1_strategy | **Filled.** Motivation and strategy derived from layer 0; Principles discovered directly, since no canvas block feeds them |
| 2_business | **Key elements filled.** Actors, roles, external partners, products, services and channels. Processes, objects, glossary and rules are left to the initiatives that touch them |
| 3_information | **Not started.** No initiative has handled data yet |
| 4_application | **Not started.** The method, the site and the future portal are modeled as *products* in layer 2; they become components when an initiative builds against them |
| 5_technology | **Not started** |
| domains | **Not used** — Depth 2. No business line passes the split test, and inventing one would repeat the mistake this initiative exists to avoid |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | Requester | 2026-08-08 | The two canvases: three segments, one consolidated set of jobs, pains and gains, the value map, and three product business models. Presented in the session, with the branch links to both canvas documents. Granted with one addition — the Social Return on Investment measures now recorded against `RS1` and `RS2` |
| Gate 1 — Strategy | _awaiting_ | — | The derived strategy — stakeholders, drivers, assessments, goals, outcomes, principles, capabilities, resources, courses of action, the value stream — and the key business elements: actors, roles, partners, products, services and channels |
| Gate 2 — Business | — | — | **N/A** — docs-only initiative; no code is delivered |
| Gate 3 — Solution design | — | — | **N/A** — no solution design |

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | archreator had a method, a self-model of the method at Depth 1 (`meta/`), and a published site. The organization producing all of it was unmodeled |
| **Target** (delivered) | The organization modeled at Depth 2 through layer 2: who it serves, what it offers, how each product works economically — including the returns that are not money — and what it must be able to do, with what, and by whose hands |

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

### WP3 — Derive the strategy layer

- **Deliverables:** [`1_strategy/README.md`](../ea/1_strategy/README.md),
  [`1_motivation.md`](../ea/1_strategy/1_motivation.md),
  [`2_capabilities-and-resources.md`](../ea/1_strategy/2_capabilities-and-resources.md),
  [`3_value-stream.md`](../ea/1_strategy/3_value-stream.md) — 5 stakeholders,
  6 drivers, 5 assessments, 6 goals, 7 outcomes, 7 principles, 6
  capabilities, 5 values, 4 resources, 3 courses of action, 1 value stream
- **Outcome:** every canvas element either has a strategic consequence or is
  shown not to need one, and the seven principles are written down where a
  future change gets checked against them

### WP4 — Derive the key business elements

- **Deliverables:** [`2_business/README.md`](../ea/2_business/README.md),
  [`1_business-actors-and-roles.md`](../ea/2_business/1_business-actors-and-roles.md),
  [`2_business-services.md`](../ea/2_business/2_business-services.md)
- **Outcome:** who acts is explicit — including the AI actor's autonomy — and
  every product names the services and channels that deliver it

### WP5 — Set up the tree

- **Deliverables:** [`organization/README.md`](../../README.md),
  [`docs/ea/README.md`](../ea/README.md), this scope document and its index
- **Outcome:** a fourth tree that a reader can tell apart from the other
  three at a glance

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| Both canvases, and the fit check between them | — |
| Layers 1 and 2 derived from them, plus the Principles discovered directly | Layers 3–5, and the business processes, objects and rules inside layer 2 — filled by the initiatives that touch them, not invented here |
| The non-monetary return, named, recorded, and given a measure | Instrumenting that measure (`COA3`), and valuing it — Social Return on Investment is named, not applied |
| The single-person concentration, stated as a risk and carried into `RES1` | Doing anything about it. `COA1` names a route and nothing more |
| Provider neutrality, promoted from a posture to `P6` | The decision record that would fix its limits |

## Gap notes

- **The largest structural risk is `KR1`, and it is a deliberate choice.**
  One person is the key resource behind two of three products and the only
  human in the organization. The Requester has no interest in scaling large,
  so this is chosen rather than accidental — but a choice is not an absence
  of risk, and the model says so rather than implying a resilience it does
  not have. The named route if it ever had to change is AI agents acting as
  consultants carrying the Requester's knowledge, which needs more AI
  maturity than exists today.
- **`RS1` and `RS2` now have a measure, and no instrumentation.** Both
  primary returns are measured by adoption in two bands — pre-engagement
  (stars, forks, contributions, discussions) and real (enterprises and
  initiatives actually designed and built). The pre-engagement band is
  readable from GitHub today; the real band has no collection method, and
  only the real band evidences mission progress. Valuation is a further step
  again: Social Return on Investment is the candidate framework, and the
  Requester has applied it in governmental work — but naming a framework is
  not applying one, and it needs quantities first.
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
  `CH5` would change that and is Pending. Deriving layer 2 made this worse
  rather than better: it is now visible in three places at once — the channel
  catalogue, the value stream's first stage, and the business interfaces —
  which is what a model is for.
- **Four of the seven Outcomes have no working measure.** Three (`OUT2`,
  `OUT3`, `OUT6`) are checkable by reading a document the method itself
  produces. The other four are about what happened to a *person*, and the
  organization can observe that people star the repository while being
  unable to observe whether anyone finished an architecture with it. `COA3`
  is the named response and it is Pending.
- **`COA1` and `COA2` pull against each other on `RES1`.** One reduces the
  dependency on the Requester's time, the other spends a great deal of it
  first. Which comes first is a strategy decision this initiative
  deliberately does not take — it belongs to whoever opens that initiative,
  with this model in front of them.
- **The Principles were drafted from the Requester's own stated positions,
  not asked as fresh questions.** Every one of `P1`–`P7` traces to something
  the Requester said while the method was being built, which is why they
  could be written at all — but they were assembled by an agent and are
  approved at Gate 1 rather than discovered at it. `P7` in particular fixes a
  pricing posture that no initiative has yet tested.

## Open questions

Consolidated from both canvases; each is recorded in the canvas that raised
it rather than restated in full here.

| # | Question | State | Where |
| - | -------- | ----- | ----- |
| 1 | How should the non-monetary returns be valued? | Measure answered at Gate 0; valuation still open | [business model canvas](../ea/0_business-design/2_business-model-canvas.md) |
| 2 | How far should provider neutrality go, and what may be provider-specific? | Open. `P6` states the posture; its boundary needs a decision record | [business model canvas](../ea/0_business-design/2_business-model-canvas.md) |
| 3 | Is the contributor community a partner or an aspiration? | Open. Modeled as `ACT5` with `BCOL1` marked Pending | [business model canvas](../ea/0_business-design/2_business-model-canvas.md) |
| 4 | Does `COA1` or `COA2` come first? | Raised by this derivation; not taken here | [capabilities and resources](../ea/1_strategy/2_capabilities-and-resources.md) |
