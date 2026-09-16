# AGENTS.md

The architecture model of **the organization that publishes archreator**: the
company, not the method. What it builds is modeled in its own tree,
[`product-archreator/`](../product-archreator/architecture/README.md); this
model names *that* the product exists and never reaches into its elements.

Repository-wide rules, commands and conventions live in the root
[`AGENTS.md`](../AGENTS.md). This file carries only what is this tree's.

## Modeling depth

**Declared depth: 2 — Organization.** One capability base, one portfolio,
one person who says yes: `0_business-design/` holds the canvases,
`1_strategy/` is derived from them, and domains stay unused until something
the organization builds acquires customers, economics and an approver of its
own.

## This tree

- **Federation ID:** `ORG`. The product cites this model's elements as
  `ORG.<ID>`; this model never cites the product's.
- The model is under [`architecture/`](./architecture/README.md). Its front
  door says what is modeled and what deliberately is not, and
  [`relationships.md`](./architecture/relationships.md) declares every
  relationship once.
- Initiatives touching this tree are recorded in
  [`product-archreator/architecture/scope/`](../product-archreator/architecture/scope/README.md);
  an initiative spanning both trees carries one document.
- The validators run from the repository root, before every push:
  `python3 scripts/check_links.py`, `python3 scripts/check_model.py` and
  `python3 scripts/check_prose.py`.
