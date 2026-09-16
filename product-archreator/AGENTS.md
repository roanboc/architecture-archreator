# AGENTS.md

The architecture model of **archreator the method, as a product**: its
skills, validators, tools, scaffold and guidance site. The organization that
publishes it is modeled in
[`org-archreator/`](../org-archreator/architecture/README.md); this model
cites the organization's elements where it serves them, never the reverse.

Repository-wide rules, commands and conventions live in the root
[`AGENTS.md`](../AGENTS.md). This file carries only what is this tree's.

## Modeling depth

**Declared depth: 1 — Application.** The subject is one product: a light
strategy layer to judge changes against, and the layers that describe what
actually ships. The guidance site is part of this product, realizing one of
its services, not a project of its own.

## This tree

- **Federation ID:** `PRD_MTD`. This model cites the organization's elements
  as `ORG.<ID>`, mapped in [`architecture/federation.md`](./architecture/federation.md).
- The model is under [`architecture/`](./architecture/README.md). Its front
  door says what is modeled and what deliberately is not, and
  [`relationships.md`](./architecture/relationships.md) declares every
  relationship once.
- Initiatives, including those spanning both trees, live in
  [`architecture/scope/`](./architecture/scope/README.md), one document each.
  Retrospective notes, one per finished initiative or engagement, live in
  `architecture/engagements/`.
- The validators run from the repository root, before every push:
  `python3 scripts/check_links.py`, `python3 scripts/check_model.py` and
  `python3 scripts/check_prose.py`.
