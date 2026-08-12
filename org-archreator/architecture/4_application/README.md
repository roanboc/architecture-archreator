# Application Layer — the organization behind archreator

_[← EA home](../README.md)_

The software this organization owns. There is less of it than the products
suggest, and that is the finding rather than an omission.

## Analysis order

| # | Document | Elements | Question it answers | State |
| - | -------- | -------- | ------------------- | ----- |
| 1 | [1_application-services.md](./1_application-services.md) | Application Services and what they realize | What does the software offer the business? | **Filled** — 4 services, 3 live |
| 2 | [2_application-components.md](./2_application-components.md) | Application Components, mapped to files, and the Depth 1 model detailing each | Which components provide them? | **Filled** — 5 components, 4 live |
| 3 | `3_application-collaborations.md` | Collaborations and interaction sequences | How do components interact? | **Not started** — they do not. Four components with no runtime coupling have no interactions to draw |
| 4 | `4_solution-design.md` | Overall design, patterns, tooling | How is the code structured, and why? | **Not started** — belongs to each component's own Depth 1 model, not here |
| 5 | `5_interface-contracts.md` | Per-interface promises | What does each interface promise? | **Not started** — no component exposes an interface to another |

Documents 3 to 5 are empty because this organization's applications do not
call each other, not because the analysis stopped. `COA2` would change that:
a portal has a runtime, callers, and contracts.

## The rule this layer follows

**Name the application; do not restate how it is built.** Each component
points at the Depth 1 model that details it — `product-archreator/` for the method and its
tooling, `product-archreator/site/architecture/` for the guidance site. That link is the whole
relationship between this tree and those, and
[2_application-components.md](./2_application-components.md#how-this-layer-relates-to-meta-and-site)
sets it out.
