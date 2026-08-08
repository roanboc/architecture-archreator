# Domain — Product

_[← Domains](../README.md) · [EA home](../../README.md)_

**Purpose.** Sell the same discipline Advisory delivers by hand, at a price
a solo builder can pay and with nobody on our side in the loop. It exists to
serve `G3` (revenue that does not scale with consultant hours) and to
extend `G2` (every decision we ship is reviewable) to customers who could
never afford an engagement.

## Customers

| Customer | Kind | What they need from this domain |
| -------- | ---- | -------------------------------- |
| `STK2` Solo builder / small team lead | External | Guardrails and architecture discipline out of the box, without buying consulting (`JOB4`, `JOB5`) |
| `ACT7` Builder, in role `ROLE4` | External | A named administrator per project — a subscription without one is not provisioned |

## Exposed services

| ID | Service | Serves | Realized by |
| -- | ------- | ------ | ----------- |
| `BSVC5` | Platform access | `STK2` | `CAP5`, `RES5`; stages `VSS8`–`VSS9` |
| `BSVC6` | Drift monitoring | `STK2` | `CAP3`, `CAP5`; stage `VSS10` |
| `BSVC7` | Self-serve onboarding | `STK2` | `CAP6`; stage `VSS8` |
| `BSVC8` | Community support | `STK2` | `CAP6`; stage `VSS11` |

All four are sold to external customers; **no other domain consumes this
one**. Product is a leaf in the internal service graph, which is why it can
ship on its own cadence.

## Consumed services

| Qualified ID | From | What this domain relies on it for |
| ------------- | ---- | ---------------------------------- |
| `ADVISORY.BSVC9` | [Advisory](../advisory/README.md) | The engagement patterns that populate `RES6` and become the `PROD2` roadmap. `CAP5` builds from them; `COA1` is the strategy that depends on it |

**This is the domain's single external dependency and its single largest
risk.** `ADVISORY.BSVC9` is Pending, so today `CAP5` decides what to build
from intuition rather than from harvested evidence. The charter makes that
visible to the domain that suffers from it — previously it was recorded only
as `RES6`'s state in a resource table owned by nobody.

## Decision rights and escalation

- **Decides alone:** the platform codebase and release cadence (`ACT5`),
  the evaluation harness, what `ACT4` is permitted to do inside a
  subscriber's project, and pricing within `RS3`/`RS4`.
- **Escalates to:** the founders (`STK3`) for changes to `P1`–`P3` or to
  `ACT4`'s autonomy level — the latter also requires a `decision-record`;
  the [Advisory domain](../advisory/README.md) when the roadmap needs a
  pattern `BSVC9` has not delivered.

## Operated by

**Hybrid.** `ACT5` Product Engineer is human and owns the platform (`RES5`),
the evaluation harness, and `ACT4`'s permitted actions. `ACT4` Product Agent
is an **AI** actor at **autonomous with checkpoint**: it acts inside a
subscriber's project without prior approval — applying guardrail templates,
flagging drift, opening change proposals, answering product questions — and
the customer is notified and can revert. It may not modify billing, delete
customer work, or act outside the project that invoked it. It escalates to
`ROLE4`, the named human on the customer's side, and internally to `ROLE3`
for drift it cannot resolve.

The higher autonomy than Advisory's `ACT3` follows from who can undo the
work: the customer owns the project, sees every action, and can revert it.
See [the actor rationale](../../2_business/1_business-actors-and-roles.md#internal-actors).
