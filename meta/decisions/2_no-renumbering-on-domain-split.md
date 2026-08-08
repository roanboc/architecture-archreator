# 2 — Element IDs are not renumbered when a model splits into domains

_[← Decisions](./README.md)_

**Status:** Accepted
**Date:** 2026-08-08
**Touches:** [`RULE5`](../ea/2_business/2_business-services.md),
[`P5`](../ea/1_strategy/1_motivation.md)

## Context

Namespaced IDs (`SALES.BSVC3`) number per prefix **per domain**, so two
domains may each own a `BSVC3`. When an existing flat model is split, its
IDs were assigned globally — in `example-company`, Advisory happened to hold
`BSVC1`–`BSVC4` and Product `BSVC5`–`BSVC8`.

Leaving them produces a model where Product's services start at 5 for no
visible reason. Renumbering produces a tidy model and breaks every reference
written before the split.

## Options considered

| Option | Consequence |
| ------ | ----------- |
| **Renumber each domain from 1** | Tidy. Violates `RULE5` and `P5`: an ID would change, and every scope document, decision record, and diagram citing the old one silently points somewhere else — or worse, at a *different live element* that now holds the number |
| **Renumber, and add a migration table** | The references still break; the table only documents that they did. And the table has to be consulted forever |
| **Keep existing IDs; number new elements per domain** | Product's IDs start at 5. Nothing breaks. The gap is visible and explainable |

## Decision

Existing IDs keep their numbers. Per-domain numbering applies to elements
created after the split.

## Consequences

- **A split model has visibly non-contiguous IDs**, which looks like an
  error until you know why. `docs/ea/domains/README.md` § Element IDs says
  so explicitly, and `example-company`'s domains README repeats the specific
  case — the only permitted duplication of this fact, because a reader
  hitting `BSVC5` as Product's first service will not go looking for the
  general rule.
- **The tidiness cost is permanent and the correctness benefit is
  permanent.** This trade only gets more favourable as a model ages: the
  number of stale references a renumber would break grows monotonically.
- **`P5` was written partly to settle this class of question.** Renumbering
  is a form of rewriting history, and treating it as one makes the answer
  fall out of an existing principle rather than needing a new judgment each
  time.
