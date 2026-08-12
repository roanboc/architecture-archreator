# 5 — The strategy layer stays enterprise-wide; products structure layers 0 and 2

_[← Decisions](./README.md)_

**Status:** Accepted
**Date:** 2026-08-09
**Touches:** [`docs/ea/1_strategy/README.md`](../../.claude/skills/project-bootstrap/templates/architecture/1_strategy/README.md),
[`docs/ea/0_business-design/README.md`](../../.claude/skills/project-bootstrap/templates/architecture/0_business-design/README.md),
[`docs/ea/domains/README.md`](../../.claude/skills/project-bootstrap/templates/architecture/domains/README.md)

## Context

The canvases in layer 0 are already per-something: a Value Proposition Canvas
per customer segment, a Business Model Canvas per product. The Requester
asked whether `1_strategy/` should follow — a folder per product or service,
since that is how the canvases decompose.

The question is a good one because the two shapes genuinely differ. Layer 0
is written product by product; layer 1 is written once for the whole
organization.

## Options considered

| Option | Consequence |
| ------ | ----------- |
| **A folder per product inside `1_strategy/`** | Every product gets its own goals, capabilities and value stream. The shape matches layer 0 and the documents stay small |
| **Keep `1_strategy/` enterprise-wide** | One set of capabilities serving three products, with the sharing visible. Documents grow with the organization, not with the catalogue |
| **Split the whole model when products diverge** | Already exists as `domains/` at Depth 3 — the split test, the charter, the federation rule |

## Decision

**The strategy layer stays enterprise-wide.** Products structure layer 0 and
layer 2; when a product genuinely stops sharing the organization's strategy,
the answer is a **domain**, not a folder inside layer 1.

## Why

**The sharing is the finding.** In the organization behind archreator, three
products run on the same three capability areas and the same two resources.
That is the single most useful sentence in its strategy layer, and a
per-product split would delete it — each folder would restate the same
capabilities and no document would show that they are the same ones. `P3`
(each fact in exactly one document) rules this out directly.

**ArchiMate puts these elements at the organization.** Capabilities,
resources, goals and drivers belong to the enterprise; products are what it
offers. Filing a capability under a product asserts an ownership the standard
does not have, and the model stops being checkable against the notation.

**Two competing decomposition rules is one too many.** archreator already
splits by **business line** at Depth 3, with a split test, a charter naming
exposed services, and a federation rule for cross-domain change. Adding a
second axis — by product, inside one layer — would leave a reader with two
questions where there is one: which split applies, and what happens when a
product spans two domains.

**The trigger for splitting is divergence, not size.** A product that has its
own goals, its own people and its own economics has stopped being a product
of this organization and started being a business line. That is exactly what
the split test asks, and it is answered one level up.

## Consequences

- Layer 1 documents grow as the organization's ambitions grow. When one gets
  unreadable, the first question is consolidation (`P5`), the second is
  whether a domain is hiding in it — never "shard by product".
- Layer 2 already keys products, services and interfaces by `PROD`. If
  `2_business-services.md` outgrows one file, sharding **there** by product
  is legitimate, because those elements really do belong to a product.
- Layer 0 is unaffected: one canvas per segment and one per product remains
  the rule.
- If a future adopter's business genuinely needs per-product strategy, the
  model that fits is Depth 3 with each product line as a domain — and that
  path is documented rather than invented on the spot.

## What would reopen this

An organization whose products share **no** capabilities and **no** resources,
and which still does not want domains. That would mean the split test is
mis-drawn, and the fix would be to the test rather than to the folder layout.
