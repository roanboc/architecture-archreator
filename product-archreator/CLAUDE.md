# CLAUDE.md

This tree models **archreator itself** — `PROD1`, the open method: the
skills, the conventions, the gates, and the scaffold they emit. It is
archreator applied to archreator, which is what makes the method's own
claims checkable. The organization that publishes it is modeled in
[`../org-archreator/`](../org-archreator/README.md); the guidance site that
explains it is nested here as [`site/`](./site/README.md), because it
realizes `BSVC2` for this product rather than standing on its own. See
[`../CLAUDE.md`](../CLAUDE.md) for the repository-wide rule.

## The rule that governs everything else

**Strategy and business architecture are validated before any other layer,
and the Requester approves at explicit gates before development.** A change
in requirements is never coded directly: align it through the numbered EA
layers (`architecture/1_strategy` → … → `5_technology`), stop at the gates
for the Requester's approval, record it in a scope document (`architecture/scope/`), then
implement. Use `architecture-first-change` for the process, `architecture-doc-style` when
touching anything under `architecture/`, `scope-doc` for the scope document,
`decision-record` for a call smaller than an initiative, and
`restate-current-state` when the model reads as a history rather than a
description of today.

## Modeling depth

**Declared depth: 1 — Application.** The subject is one thing that gets
built: a method that ships as instructions. `architecture/0_business-design/`
and `architecture/domains/` are not used — the canvases belong to the
organization, one tree up — and layer 3 is absent because the method holds
no data objects of its own.

## Where the method actually lives

The model here **describes** the method; it is not the method. The shipped
artifacts are:

- `../.claude/skills/` — the skill bodies, which are the method's
  instructions
- `../.claude/skills/project-bootstrap/templates/` — the scaffold a new
  project is generated from
- `../.claude/.claude-plugin/plugin.json` and `../.claude-plugin/marketplace.json`
  — the packaging

What may and may not be provider-specific among those is fixed by
[decision 6](./architecture/decisions/6_the-portability-boundary.md): method content and
skill frontmatter are portable, packaging is not.

## Layout

- `architecture/` — the current-state model, numbered ArchiMate layers
  (1, 2, 4, 5)
- `architecture/scope/` — one document per initiative, each carrying its Approvals table
- `architecture/decisions/` — consequential calls smaller than an initiative
- `architecture/reviews/` — point-in-time assessments of the method against itself
- `architecture/scope/open-questions.md` — the consolidated index of adopted
  interpretations still awaiting confirmation, read as step 0 of
  `architecture-first-change`
- `site/` — the guidance site, its own Depth 1 project

## Conventions

- Documentation language: English.
- Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`, …).
- Element IDs are assigned once and never reused;
  `.claude/skills/project-bootstrap/templates/scripts/check_model.py` enforces it.
- A merged scope document is a historical record. Its link targets may be
  repaired when files move; its words may not change (`RULE6`).
