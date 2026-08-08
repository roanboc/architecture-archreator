# Project Scope — Split the operating model into domains

_[← Scope index](./README.md) · [EA home](../ea/README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** `example-company/docs/ea/domains/` on
`claude/repo-value-ux-review-3ur5y4`.

[Initiative 1](./1_model-the-operating-model.md) modeled Solvara as one
organization and ended by noting that `PROD1` and `PROD2` "agree on nothing
except a shared capability base". This initiative acts on that: each product
line becomes a **domain** with its own charter, and the dependency between
them — previously the pending resource `RES6`, owned by nobody — becomes an
exposed service with an owner, `ADVISORY.BSVC9`.

The subject is still the organization, so no software is delivered here
either. What changes is the *shape* of the model, not its content.

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 0_business-design | **No change.** The canvases are what justified the split; nothing about them moved |
| 1_strategy | **No change to elements**, but `COA1` is no longer blocked on an unowned resource — it is realized by `ADVISORY.BSVC9`, which has an owning domain and an escalation path |
| 2_business | **Changed.** Products, services, actors, and roles are now partitioned between two domains; `ADVISORY.BSVC9` is added as the one cross-domain service. Existing IDs are unchanged and now qualified |
| 3_information | **Not started** — unchanged |
| 4_application | **Not started** — unchanged |
| 5_technology | **Not started** — unchanged |
| domains | **New.** [`domains/README.md`](../ea/domains/README.md) with the split test verdict, plus a charter each for [Advisory](../ea/domains/advisory/README.md) and [Product](../ea/domains/product/README.md) |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — the canvases are unchanged; Gate 0 was passed in initiative 1 |
| Gate 1 — Strategy | — | — | **N/A** — no stakeholder, driver, goal, or principle changes |
| Gate 2 — Business | Requester | 2026-08-08 | The split into Advisory and Product, both charters, and `ADVISORY.BSVC9` as the contract between them. Both domains' Requesters are the same person at this size, which is itself a reason the split is about clarity rather than governance today |
| Gate 3 — Solution design | — | — | **N/A** — no solution design; nothing is built |

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | One flat model. Two product lines visible only as a `Part of` column and a shared-versus-different table. `COA1` — the strategic bet behind `G3` — depended on `RES6`, which was pending and owned by nobody |
| **Target** (delivered) | Two domains with charters. Each names what it exposes, what it consumes, what it decides alone, and whether a human or an AI operates it. The Advisory → Product dependency is a named service with an owner |

## Work packages and deliverables

### WP1 — Apply the split test and record the verdict

- **Deliverables:** [`domains/README.md`](../ea/domains/README.md) — the
  five-part test scored against Solvara, what stays at the enterprise level,
  and the cross-domain diagram
- **Outcome:** the split is justified in the model rather than asserted; a
  reader can check the reasoning and disagree with it

### WP2 — Write both charters

- **Deliverables:** [`domains/advisory/README.md`](../ea/domains/advisory/README.md),
  [`domains/product/README.md`](../ea/domains/product/README.md)
- **Outcome:** each domain's interface, dependencies, decision rights, and
  operating mode (including its AI actor's autonomy level) are stated where
  the other domain can read them

### WP3 — Turn `RES6` into a contract

- **Deliverables:** `ADVISORY.BSVC9` in the Advisory charter's exposed
  services; the matching row in Product's consumed services
- **Outcome:** `COA1` has a mechanism. The service is still **Pending**, but
  it is now pending *against a named owner and a domain that depends on it*
  rather than sitting in a resource table

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| The split test, both charters, the cross-domain contract | Moving elements out of the enterprise layers into per-domain layer folders |
| Declaring Depth 3 in `CLAUDE.md` and the EA README | Building `RES6` or staffing `ADVISORY.BSVC9` |
| Qualified element IDs at the boundary | A third domain for the shared capability base — `CAP1`–`CAP3` stay enterprise-level deliberately |

## Gap notes

- **Both domains have charters and no layer folders.** This is the
  prescribed order — `domain-modeling` writes the charter first, because
  that is what catches a domain with nothing to expose — but it means the
  domain-level `1_strategy/` through `5_technology/` are Pending. Closing it
  is cheap and incremental: each folder is created by the first initiative
  that touches it, and until then the elements live in the enterprise layers
  where they already are. Pre-creating six empty folders per domain would
  add twelve READMEs saying "not started" and nothing else.
- **`ADVISORY.BSVC9` is exposed but unbuilt**, which is the point of listing
  it. A commitment with a consumer attached gets prioritized; a pending
  resource in a table owned by nobody does not. It stays the largest gap in
  the model, now with an address.
- **The dependency is one-way and unbalanced.** Product's strategy depends
  on Advisory delivering `BSVC9`; Advisory depends on Product for nothing.
  If Advisory deprioritizes it, Product stalls and Advisory feels no
  consequence. At Solvara's size the same person owns both, so this is a
  documented hazard rather than a live problem — but it is exactly the
  failure mode that would bite at fifty people, and no structure here
  prevents it.

## Open questions

- **Whether the shared capability base should itself become a domain.**
  `CAP1`–`CAP3` are consumed by both lines and owned by neither, which fits
  three of the five split tests. Interpretation adopted: leave it at the
  enterprise level, because a domain with no customers of its own and no
  distinct economics is a shared service, not an organization. Worth
  revisiting if a third product line appears.
