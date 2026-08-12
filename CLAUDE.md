# CLAUDE.md

This repository is **archreator** — an enterprise architecture method that
lives in git as markdown, and the organization that publishes it. It holds
four things, each named for what it is:

| Directory | What it holds | Depth |
| --------- | ------------- | ----- |
| [`.claude/skills/`](./.claude/skills/README.md) | **The method itself** — the skill bodies, and the scaffold `project-bootstrap` emits from `project-bootstrap/templates/` | — |
| [`org-archreator/`](./org-archreator/CLAUDE.md) | The organization behind archreator: segments, products, capabilities, economics | 2 — Organization |
| [`product-archreator/`](./product-archreator/CLAUDE.md) | archreator modeled with archreator — the method's own architecture | 1 — Application |
| [`product-archreator/site/`](./product-archreator/site/CLAUDE.md) | The guidance site, deployed to GitHub Pages | 1 — Application |

The model **describes** the method; `.claude/skills/` **is** the method.
Each tree declares its own modeling depth in its own `CLAUDE.md` — read the
one for the tree you are working in.

## The rule that governs everything else

**Strategy and business architecture are validated before any other layer,
and the Requester approves at explicit gates before development.** A change
in requirements is never coded directly: align it through the numbered EA
layers (`architecture/1_strategy` → … → `5_technology`), stop at the gates
for the Requester's approval, record it in a scope document (`architecture/scope/`), then
implement. Pure bug fixes that change no documented behavior skip the
alignment and the gates, but still keep the docs true.

A change to **the method** is recorded in
[`product-archreator/architecture/scope/`](./product-archreator/architecture/scope/README.md); a change
to **the organization** in
[`org-archreator/architecture/scope/`](./org-archreator/architecture/scope/README.md) — even when the
organization is what motivated the method change.

## Portability

archreator ships as a Claude Code plugin today, and is not tied to it.
[Decision 6](./product-archreator/architecture/decisions/6_the-portability-boundary.md)
fixes the boundary: **method content and skill frontmatter are portable;
packaging is provider-specific and disposable.** The test for any file is
_would this need editing if Claude Code vanished tomorrow, or just moving?_
Anything in a skill body that would need editing violates `P6`. Further
platforms are additive — each adds a manifest, none forks the method.

## The skills

Claude Code surfaces these from their `description:` frontmatter; you don't
invoke them by name in normal use.

| Skill | Reach for it when |
| ----- | ----------------- |
| `project-bootstrap` | A project from the template hasn't been set up yet — start here |
| `architecture-first-change` | Any requirement change. **The spine**: it defines the gates and the order |
| `architecture-doc-style` | Editing anything under `architecture/` — numbering, element IDs, ArchiMate-on-Mermaid, the grounding rule |
| `scope-doc` | Writing the initiative's scope document; its Approvals table is the durable record of the gates |
| `pr-description` | Opening or updating a PR — the body covers the whole branch, not the latest commit |
| `operating-model-discovery` | The subject is an organization: canvases first (Gate 0), strategy derived from them |
| `strategy-discovery` | The strategy is unfilled or the change shifts it (Gate 1) |
| `domain-modeling` | The organization is large enough to split into business lines, or a change crosses a domain boundary |
| `restate-current-state` | The model has accumulated history — shipped "Pending"s, superseded elements, resolved questions — and no longer reads as a description of today |
| `decision-record` | One consequential call smaller than an initiative — most often an AI actor's autonomy level |
| `story-sharding` | A work package is too large to finish in one sitting |
| `stack-selection` | No technology stack chosen yet on a small application |
| `engagement-retrospective` | An initiative or engagement just finished — capture what the method didn't cover before it evaporates |

## Commands

```bash
python3 .claude/skills/project-bootstrap/templates/scripts/check_links.py    # relative links and HTML anchors resolve
python3 .claude/skills/project-bootstrap/templates/scripts/check_model.py    # element-ID references resolve, per project
```

Both must be green before pushing; CI runs the same.

## Conventions

- Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`, …).
- Documentation language: **English**.
- Element IDs are assigned once and never reused, and are scoped per
  project — two trees may each own a `G1`.
- **A merged scope document is a historical record.** When a file moves, its
  link *targets* are repaired so they still resolve; its words — including
  link text — are never changed (`RULE6`).
