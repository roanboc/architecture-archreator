# CLAUDE.md

This tree models **the organization behind archreator** — who it serves,
what it offers, how it makes and spends, and which capabilities carry that.
It is the enterprise model the other trees federate from: the method
([`../product-archreator/`](../product-archreator/README.md)) and the
guidance site are things this organization builds, each with its own project
model. See [`../CLAUDE.md`](../CLAUDE.md) for the repository-wide rule.

## The rule that governs everything else

**Strategy and business architecture are validated before any other layer,
and the Requester approves at explicit gates before development.** A change
in requirements is never coded directly: align it through the numbered EA
layers (`architecture/0_business-design` → … → `5_technology`), stop at the
gates for the Requester's approval, record it in a scope document
(`architecture/scope/`), then implement. The `ea-first-change` skill runs the process and
defines which gate applies.

## Modeling depth

**Declared depth: 2 — Organization.** The subject is one organization with
three products sharing one capability base, so
`architecture/0_business-design/` **is** used — a Value Proposition Canvas
per customer segment and a Business Model Canvas per product, approved at
Gate 0 before anything was derived from them.

`architecture/domains/` is **not** used. The split test asks whether a part
of the business has its own goals, its own people and its own economics;
nothing here does yet. See
[`../product-archreator/architecture/decisions/5_no-per-product-strategy-folders.md`](../product-archreator/architecture/decisions/5_no-per-product-strategy-folders.md)
for why products do not get folders inside the strategy layer, and
[`decision 7`](../product-archreator/architecture/decisions/7_one-tree-per-federated-project.md)
for why they do get trees of their own.

## Layout

- `architecture/` — the current-state model, numbered ArchiMate layers
  0–5, with the canvases at layer 0
- `architecture/scope/` — one document per initiative, each carrying its Approvals table
- `architecture/decisions/` — consequential calls smaller than an initiative
- `architecture/engagements/` — retrospective notes capturing what the method did not
  cover, the mechanism behind `COA1` stage 1

## Conventions

- Documentation language: English.
- Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`, …).
- Element IDs are assigned once and never reused
  (`ea-doc-style` § Element IDs); `.claude/skills/project-bootstrap/templates/scripts/check_model.py`
  enforces it.
- A merged scope document is a historical record. Its link targets may be
  repaired when files move; its words may not change (`RULE6`).
