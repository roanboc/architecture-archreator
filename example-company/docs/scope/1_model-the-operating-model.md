# Project Scope — Model the Solvara AI operating model

_[← Scope index](./README.md) · [EA home](../ea/README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** `example-company/` on
`claude/archreator-operative-model-scaling-0aw3cs`.

Solvara AI had two product lines, a shared team, and no written model of
either. This initiative documents the business model as two value
proposition canvases and two business model canvases, and derives the
strategy and key business layers from them. It delivers **no software** —
the architecture is the deliverable, and any system built later is a
separate initiative that will find this model already in place.

## EA alignment (assessed top-down before implementing)

| Layer         | Impact                                                                                                     |
| ------------- | ------------------------------------------------------------------------------------------------------------ |
| 0_business-design | **New.** Two value proposition canvases (`CS1`, `CS2`) and two business model canvases (`PROD1`, `PROD2`) |
| 1_strategy    | **New**, derived from layer 0: 5 stakeholders, 4 drivers, 5 assessments, 4 goals, 5 outcomes, 3 principles, 6 capabilities, 6 resources, 2 courses of action, 2 value streams |
| 2_business    | **Partially new.** Actors (including two AI actors), roles, contracts, products, services, channels. Processes, objects, and rules deliberately deferred |
| 3_information | **No change** — not started. No application exists, so there is no data architecture to describe            |
| 4_application | **No change** — not started. Nothing has been built                                                         |
| 5_technology  | **No change** — not started                                                                                 |

## Approvals

| Gate                        | Approved by | Date         | What was approved                                                                                                     |
| --------------------------- | ----------- | ------------ | ----------------------------------------------------------------------------------------------------------------------- |
| Gate 0 — Business model     | Requester   | 2026-08-04   | Both value proposition canvases and both business model canvases, with the fit check and the deliberate non-service of `JOB2` |
| Gate 1 — Strategy           | Requester   | 2026-08-04   | The derived strategy layer and the key business elements — in particular the two AI actors' autonomy levels and escalation paths |

Gate 2 does not apply: no code is delivered, so there is no
pre-implementation gate to pass. Gate 3 was not requested — there is no
solution design in this initiative.

## Plateaus

| Plateau                | State                                                                                                      |
| ----------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Baseline** (before)  | Two product lines run from shared understanding held in people's heads. No written business model, no stated principles, no record of why the two AI actors have the autonomy they do |
| **Target** (delivered) | A canvas-derived operating model: what is sold, to whom, at what economics, realized by which capabilities and roles — with every element traceable to a customer statement |

## Work packages and deliverables

### WP1 — Business design

- **Deliverables:**
  [`docs/ea/0_business-design/1_value-proposition-canvas.md`](../ea/0_business-design/1_value-proposition-canvas.md),
  [`docs/ea/0_business-design/2_business-model-canvas.md`](../ea/0_business-design/2_business-model-canvas.md),
  [`docs/ea/0_business-design/README.md`](../ea/0_business-design/README.md)
- **Outcome:** The business model is stated, fit-checked, and approved —
  including the two structural problems it exposed (`PROD1`'s cost and
  revenue scaling together; `PROD2` priced per seat but costed per use).

### WP2 — Derived strategy layer

- **Deliverables:**
  [`docs/ea/1_strategy/1_motivation.md`](../ea/1_strategy/1_motivation.md),
  [`docs/ea/1_strategy/2_capabilities-and-resources.md`](../ea/1_strategy/2_capabilities-and-resources.md),
  [`docs/ea/1_strategy/3_value-stream.md`](../ea/1_strategy/3_value-stream.md),
  [`docs/ea/1_strategy/README.md`](../ea/1_strategy/README.md)
- **Outcome:** Every strategy element carries the canvas block it came from;
  the three Principles, which have no canvas source, are stated explicitly
  as discovered directly with the Requester.

### WP3 — Key business elements

- **Deliverables:**
  [`docs/ea/2_business/1_business-actors-and-roles.md`](../ea/2_business/1_business-actors-and-roles.md),
  [`docs/ea/2_business/2_business-services.md`](../ea/2_business/2_business-services.md),
  [`docs/ea/2_business/README.md`](../ea/2_business/README.md)
- **Outcome:** Who does the work — including two AI actors at deliberately
  different autonomy levels, each escalating to a named role per `P2` — and
  what is offered through which channels.

## In scope / out of scope

| In scope                                                        | Out of scope (gaps, candidate future work)                                     |
| ---------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Value proposition canvases for both customer segments           | Business processes decomposing `KA1`–`KA7` (`3_business-processes.md`)          |
| Business model canvases for both products                       | Business objects (`4_business-objects.md`)                                       |
| Derived motivation, capabilities, resources, value streams      | Glossary and business rules (`5_domain-context-and-rules.md`)                    |
| Actors, roles, contracts, products, services, channels          | Layers 3–5 entirely — no application exists to describe                          |
| The `RES6` gap, stated rather than papered over                 | Building `RES6` (the engagement archive) — the initiative `COA1` depends on      |
| Revenue and cost tables keyed to element IDs                    | Any financial model, forecast, or unit-economics analysis built on them          |

## Gap notes

- **`RES6` — the engagement archive — does not exist.** `COA1`, the
  strategic bet behind `G3`, depends on it entirely, and so do the only two
  edges connecting `VS1` to `VS2`. Until it exists, "engagements feed the
  product" is an intention, not a mechanism. Closing it means a deliberate
  harvesting step at `VSS6` and somewhere for the output to live — small in
  effort, but it needs someone to own it, which is a decision this
  initiative did not have the authority to make.
- **`KP1` and `KP2` serve both product lines.** A model-provider or cloud
  failure hits advisory delivery and the subscription simultaneously.
  `COA2` keeps `CTR1` substitutable; there is no equivalent mitigation for
  `CTR2` today, and adding one means either a second host or accepting the
  concentration explicitly.
- **`JOB2` is deliberately unserved.** `CS1` wants to show the board that
  something happened, and no pain reliever or gain creator addresses it.
  Recorded in the [fit check](../ea/0_business-design/1_value-proposition-canvas.md#fit-check)
  so a future initiative revisits it as a choice rather than rediscovering
  it as an oversight.
- **Business processes are unmodeled**, so `KA1`–`KA7` map to value-stream
  stages but nothing decomposes them. Any initiative that automates part of
  an activity will need that decomposition first.

## Open questions

- **Is the `PROD2` included-usage allowance a business decision or a
  pricing-page detail?** The model treats it as the former (`RS4` exists
  specifically to correct the seat-vs-usage mismatch). If the Requester
  intends it as a tunable marketing parameter instead, `RS4`'s description
  in [2_business-model-canvas.md](../ea/0_business-design/2_business-model-canvas.md#revenue-and-cost-by-element)
  needs revising.
- **Who owns `RES6` once it exists?** The model assigns it to `CAP5`
  (product engineering), but harvesting happens at `VSS6` inside `ROLE1`
  (engagement delivery). Adopted interpretation: `ROLE1` produces, `CAP5`
  consumes — unconfirmed.
