# Domain — Advisory

_[← Domains](../README.md) · [EA home](../../README.md)_

**Purpose.** Get a mid-market customer's process into production and leave
behind a team that can run it. It exists to serve `G1` (customers reach
production, not pilots) and `G4` (customers can run it without us) — and,
through `ADVISORY.BSVC9`, to make `G3` reachable by feeding the Product
domain what engagements keep rebuilding.

## Customers

| Customer | Kind | What they need from this domain |
| -------- | ---- | -------------------------------- |
| `STK1` Mid-market operations lead | External | A repeatable process running on real work, defensible afterwards (`JOB1`–`JOB3`) |
| [Product domain](../product/README.md) | Internal | The recurring patterns worth productizing — via `ADVISORY.BSVC9` |

## Exposed services

The interface. Other domains may reference these IDs and nothing else.

| ID | Service | Serves | Realized by |
| -- | ------- | ------ | ----------- |
| `BSVC1` | Readiness assessment | `STK1` | `CAP2`, assessment procedure; stage `VSS2` |
| `BSVC2` | Solution design | `STK1` | `CAP1`, `CAP3`; stage `VSS3` |
| `BSVC3` | Supervised build | `STK1` | `CAP4` (`RES1`, `ACT3`); stage `VSS4` |
| `BSVC4` | Handover and enablement | `STK1` | `CAP2`, `CAP4`; stage `VSS5` |
| `BSVC9` | **Engagement pattern harvest** — after each engagement closes, the reusable pattern is extracted, generalized, and published to `RES6` in a form `PRODUCT.CAP5` can build from | [Product domain](../product/README.md) | **Pending — future initiative.** `RES6` does not exist yet, and no role currently owns the extraction |

`BSVC9` is the contract that turns `COA1` from an intention into a
mechanism. It is deliberately listed while still pending: an exposed service
nobody has built is a commitment with a date attached, whereas the same gap
buried in a resource table was invisible to the domain that depended on it.

## Consumed services

| Qualified ID | From | What this domain relies on it for |
| ------------- | ---- | ---------------------------------- |
| — | — | Nothing. Advisory depends on the shared capability base (`CAP1`–`CAP3`) and on external partners (`ACT8`, `ACT10`), both enterprise-level, not on the Product domain |

The dependency runs one way. That asymmetry is worth stating: Product's
strategy depends on Advisory delivering `BSVC9`, and Advisory's does not
depend on Product at all. If Advisory deprioritizes `BSVC9`, Product's
roadmap stalls and Advisory notices nothing — which is exactly the failure
mode a charter is supposed to make visible.

## Decision rights and escalation

- **Decides alone:** engagement scope and phase completion (`ACT1`), the
  model boundary and evaluation baseline (`ACT2`), whether to subcontract to
  `ACT10`, and how `ACT3` is used within an engagement.
- **Escalates to:** the founders (`STK3`) for anything that changes `P1`–`P3`
  or commits the shared capability base to a change; the
  [Product domain](../product/README.md) before altering `BSVC9`'s shape,
  since Product consumes it.

## Operated by

**Hybrid.** `ACT1` Engagement Lead and `ACT2` Solution Architect are human
and hold every decision right above. `ACT3` Delivery Copilot is an **AI**
actor at **co-pilot** autonomy: it drafts designs, code, evaluation suites,
and documentation, and nothing it produces reaches a customer system without
`ACT1` approving it. It escalates to `ACT1` when a draft would change agreed
scope, cannot meet the evaluation baseline, or would violate `P1` or `P3`.

The autonomy level follows from who bears the consequence — Solvara is
accountable for what it delivers into a customer's production, and a mistake
is expensive and not trivially reversible. See
[the actor rationale](../../2_business/1_business-actors-and-roles.md#internal-actors).
