# Enterprise Architecture — the organization behind archreator

_[← Project README](../README.md) · [Scope documents](./scope/README.md)_

**Modeling depth: 2 — Organization.** The subject is the organization that
produces archreator, not the method itself. The method is one of the things
this organization makes, and appears in layer 4 as a product rather than as
the subject.

**Status: all six layers modeled.** The canvases were approved at **Gate 0**
on 2026-08-08, the strategy and key business elements were derived at
**Gate 1** on 2026-08-09, and layers 3–5 describe what exists today rather
than what is intended.

## Layers, in assessment order

| # | Layer | ArchiMate viewpoint | State |
| - | ----- | ------------------- | ----- |
| 0 | [0_business-design/](./0_business-design/README.md) | _none — business design input_ | **Filled** — three segments with one consolidated profile, and three product business models. **Approved at Gate 0** |
| 1 | [1_strategy/](./1_strategy/README.md) | Motivation + Strategy | **Filled** — derived from layer 0, plus the Principles discovered directly |
| 2 | [2_business/](./2_business/README.md) | Business layer | **Key elements filled** — actors, roles, partners, products, services and channels. Processes, objects and rules follow per initiative |
| 3 | [3_information/](./3_information/README.md) | Passive structure (data) | **Filled** — 6 data objects, 3 of which this organization does not hold |
| 4 | [4_application/](./4_application/README.md) | Application layer | **Filled** — 4 services, 5 components, each pointing at the Depth 1 model that details it |
| 5 | [5_technology/](./5_technology/README.md) | Technology layer | **Filled** — 5 services, 4 nodes, none operated by this organization |
| — | `domains/` | _the same layers, nested_ | **Not used** — Depth 2. Revisit only if the organization grows business lines that pass the split test |

**Two findings run through the bottom three layers, and they agree.** This
organization holds almost no data — everything it does hold is public, and
the models its adopters build never reach it. And it operates no
infrastructure — every node belongs to a platform or to the adopter. Both
layers, filled independently, identify the same threshold: the portal
(`COA2`) is where archreator would stop being a method and become a service,
with data about people and something to keep running.

## How this tree relates to the others

Four trees in this repository, and it is worth knowing which you are in:

| Tree | Subject | Depth |
| ---- | ------- | ----- |
| `docs/` | **your** project — the blank scaffold a cloner inherits | declared at bootstrap |
| [`product-archreator/`](../../product-archreator/README.md) | how the **method** gets built, and its own development record | 1 |
| [`site/`](../../product-archreator/site/README.md) | the published guidance site | 1 |
| **this tree** | the **organization** that produces all of the above | 2 |

## Notation conventions

This project follows the template's conventions rather than restating them —
stereotypes, the layer palette, relationship labels, the human/AI/hybrid
actor notation, and element IDs all live in
[the template's EA README](../../.claude/skills/project-bootstrap/templates/architecture/README.md#notation-conventions)
and the `architecture-doc-style` skill.

The grounding rule reads differently here than in a software project: an
organization's capabilities are realized by **people, teams, and written
procedures**, not source files. Each element names the one that realizes it,
or is marked **"Pending — future initiative"**.
