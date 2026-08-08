# Business Model Canvas

_[← Business design layer](./README.md) · [EA home](../README.md)_

**Artifact:** Strategyzer Business Model Canvas — one canvas per product.
Not ArchiMate; see [the layer README](../../../../docs/ea/0_business-design/README.md#from-canvas-to-archimate)
for how each block is derived into the strategy and business layers.

Solvara AI sells two things. They share a capability base and every key
partner, and they agree on almost nothing else — different channels,
different relationships, different revenue shape, and opposite dominant
costs. Keeping them as two canvases is what makes that visible; one merged
canvas would have averaged it into nonsense.

## `PROD1` — Advisory engagements

Assess → design → supervised build → handover. Sold to
[`CS1`](./1_value-proposition-canvas.md#cs1--mid-market-operations-lead).

| ID | Block | Element |
| --- | --- | --- |
| `CS1` | Customer segments | Mid-market operations lead |
| `VP1` | Value propositions | A production-ready process in weeks, with a decision trail and a team able to run it — realizing `PREL1`–`PREL4`, `GCRE1`–`GCRE3` |
| `CH1` | Channels | Referral from past engagements |
| `CH2` | Channels | Founder network |
| `CH3` | Channels | Conference talks |
| `CR1` | Customer relationships | Named engagement lead, weekly checkpoint, fixed end date |
| `RS1` | Revenue streams | Fixed fee per phase |
| `RS2` | Revenue streams | Time-and-materials for agreed extensions |
| `RES1` | Key resources | Senior consultants |
| `RES2` | Key resources | Evaluation method IP |
| `RES3` | Key resources | Reference architectures |
| `RES4` | Key resources | Model-provider contracts |
| `KA1` | Key activities | Readiness assessment |
| `KA2` | Key activities | Solution design |
| `KA3` | Key activities | Supervised build |
| `KA4` | Key activities | Handover and enablement |
| `KP1` | Key partners | Model/API providers |
| `KP2` | Key partners | Cloud host |
| `KP3` | Key partners | Implementation partners for work outside our scope |
| `COST1` | Cost structure | Consultant time — **dominant**, and scales linearly with revenue |
| `COST2` | Cost structure | Travel |
| `COST3` | Cost structure | Inference spend during builds (billed through) |

**The structural problem this canvas exposes:** `RS1` and `COST1` grow
together. Every additional unit of revenue costs an additional unit of
consultant time, and `RES1` is the resource we cannot buy quickly. That is
the driver behind `PROD2` and behind
[`COA1`](../1_strategy/2_capabilities-and-resources.md#courses-of-action) —
it is not a growth ambition, it is a structural ceiling.

## `PROD2` — AI product subscription

The productized form of what engagements kept rebuilding. Sold to
[`CS2`](./1_value-proposition-canvas.md#cs2--solo-builder-or-small-team-lead).

| ID | Block | Element |
| --- | --- | --- |
| `CS2` | Customer segments | Solo builder or small team lead |
| `VP2` | Value propositions | Guardrails and architecture discipline out of the box, no engagement needed — realizing `PREL5`–`PREL7`, `GCRE4`–`GCRE5` |
| `CH4` | Channels | Self-serve signup |
| `CH5` | Channels | Product documentation |
| `CH6` | Channels | Content and community |
| `CR2` | Customer relationships | Self-service |
| `CR3` | Customer relationships | Community support |
| `CR4` | Customer relationships | In-product assistant (`ACT4`) |
| `RS3` | Revenue streams | Monthly subscription per seat |
| `RS4` | Revenue streams | Usage tiers above an included allowance |
| `RES2` | Key resources | Evaluation method IP — shared with `PROD1` |
| `RES4` | Key resources | Model-provider contracts — shared with `PROD1` |
| `RES5` | Key resources | The platform codebase |
| `RES6` | Key resources | Engagement archive — the pattern source |
| `KA5` | Key activities | Product engineering |
| `KA6` | Key activities | Evaluation harness upkeep |
| `KA7` | Key activities | Self-serve support |
| `KP1` | Key partners | Model/API providers — shared with `PROD1` |
| `KP2` | Key partners | Cloud host — shared with `PROD1` |
| `KP4` | Key partners | App marketplaces |
| `COST4` | Cost structure | Inference spend — **dominant**, and scales with usage rather than revenue |
| `COST5` | Cost structure | Hosting |
| `COST6` | Cost structure | Product engineering salaries (fixed) |

**The structural risk this canvas exposes:** `COST4` scales with *usage*
while `RS3` scales with *seats*. A heavy user on a flat seat price is sold
at a loss, which is what `RS4` exists to correct — and why the boundary
between the included allowance and the usage tier is a business decision,
not a pricing-page detail.

## What the two share

The shared rows are the operating model. They are why this is one company
and not two.

| Shared | `PROD1` | `PROD2` | Consequence |
| --- | --- | --- | --- |
| `RES2` evaluation method IP | Sold as a deliverable | Shipped as a feature | One method, two packagings — a change to it hits both lines |
| `RES4` model-provider contracts | Build-time inference | Runtime inference | Single negotiating position; `P3` keeps either line from locking in |
| `KP1`, `KP2` | ✅ | ✅ | Concentrated dependency — see the gap note in the [scope document](../../scope/1_model-the-operating-model.md#gap-notes) |
| `CAP1`–`CAP3` | ✅ | ✅ | The capability base both lines draw on |
| `RES6` engagement archive | Produces it | Consumes it | The one-directional link that makes `PROD2` cheaper to build than a standalone product would be |

`RES6` is the load-bearing one: `PROD1` engagements generate the patterns
`PROD2` productizes. If advisory work stopped, `PROD2` would keep running
but would stop learning what to build next.

## Revenue and cost, by element

Revenue and cost have no ArchiMate element (see
[the layer README](../../../../docs/ea/0_business-design/README.md#from-canvas-to-archimate)). They stay here,
keyed to the elements they attach to, so they remain traceable without
being modeled as architecture.

| ID | Revenue stream | Attaches to | Shape |
| --- | --- | --- | --- |
| `RS1` | Fixed fee per engagement phase | `PROD1` | Project, recognized per phase |
| `RS2` | Time-and-materials extension | `PROD1` | Project, hourly |
| `RS3` | Monthly subscription per seat | `PROD2` | Recurring |
| `RS4` | Usage tier above included allowance | `PROD2` | Recurring, variable |

| ID | Cost | Incurred by | Shape |
| --- | --- | --- | --- |
| `COST1` | Consultant time | `RES1` | Variable with `PROD1` revenue — dominant |
| `COST2` | Travel | `RES1` | Variable, small |
| `COST3` | Build-time inference | `RES4` | Variable, billed through |
| `COST4` | Runtime inference | `RES4` | Variable with `PROD2` usage — dominant |
| `COST5` | Hosting | `RES5` | Semi-fixed |
| `COST6` | Product engineering salaries | `RES5` | Fixed |

## Derivation

| These canvases | Derived into |
| --- | --- |
| `VP1`, `VP2`, `PROD1`, `PROD2` | [2_business-services.md](../2_business/2_business-services.md) |
| `CH1`–`CH6` | Business interfaces in [2_business-services.md](../2_business/2_business-services.md) |
| `CR1`–`CR4` | Business services in [2_business-services.md](../2_business/2_business-services.md) |
| Key resources `RES1`–`RES6` | [2_capabilities-and-resources.md](../1_strategy/2_capabilities-and-resources.md) |
| `KA1`–`KA7` | Value stream stages in [3_value-stream.md](../1_strategy/3_value-stream.md); business processes **pending** — see the [scope document](../../scope/1_model-the-operating-model.md) |
| `KP1`–`KP4` | External actors and contracts in [1_business-actors-and-roles.md](../2_business/1_business-actors-and-roles.md) |
| `RS*`, `COST*` | Nowhere — they stay in this document, keyed by element ID |
