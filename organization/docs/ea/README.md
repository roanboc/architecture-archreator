# Enterprise Architecture — the organization behind archreator

_[← Project README](../../README.md) · [Scope documents](../scope/README.md)_

**Modeling depth: 2 — Organization.** The subject is the organization that
produces archreator, not the method itself. The method is one of the things
this organization makes, and appears in layer 4 as a product rather than as
the subject.

**Status: discovery in progress.** Only layer 0 exists, and only partly.
Everything below it is derived after **Gate 0**, and nothing has been
approved yet.

## Layers, in assessment order

| # | Layer | ArchiMate viewpoint | State |
| - | ----- | ------------------- | ----- |
| 0 | [0_business-design/](./0_business-design/README.md) | _none — business design input_ | **In progress** — segments identified; profiles, value map, and business model canvases pending |
| 1 | `1_strategy/` | Motivation + Strategy | **Not started** — derived from layer 0 after Gate 0 |
| 2 | `2_business/` | Business layer | **Not started** — derived from layer 0 after Gate 0 |
| 3 | `3_information/` | Passive structure (data) | **Not started** |
| 4 | `4_application/` | Application layer | **Not started** — this is where the method, the site, and any future platform land |
| 5 | `5_technology/` | Technology layer | **Not started** |
| — | `domains/` | _the same layers, nested_ | **Not used** — Depth 2. Revisit only if the organization grows business lines that pass the split test |

Layers 1–5 are named without links because they do not exist yet. That is
the expected shape mid-discovery: the canvases come first, are approved, and
only then is anything derived from them.

## How this tree relates to the others

Four trees in this repository, and it is worth knowing which you are in:

| Tree | Subject | Depth |
| ---- | ------- | ----- |
| `docs/` | **your** project — the blank scaffold a cloner inherits | declared at bootstrap |
| [`meta/`](../../../meta/README.md) | how the **method** gets built, and its own development record | 1 |
| [`site/`](../../../site/README.md) | the published guidance site | 1 |
| **this tree** | the **organization** that produces all of the above | 2 |

## Notation conventions

This project follows the template's conventions rather than restating them —
stereotypes, the layer palette, relationship labels, the human/AI/hybrid
actor notation, and element IDs all live in
[the template's EA README](../../../docs/ea/README.md#notation-conventions)
and the `ea-doc-style` skill.

The grounding rule reads differently here than in a software project: an
organization's capabilities are realized by **people, teams, and written
procedures**, not source files. Each element names the one that realizes it,
or is marked **"Pending — future initiative"**.
