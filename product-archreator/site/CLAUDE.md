# CLAUDE.md

archreator-guide is a small static site whose job is to make a stranger
care about the archreator method — why it exists, what it solves, and how to
start — and only then explain how it works. It is itself built by following that same
process — see [`../../CLAUDE.md`](../../CLAUDE.md) for the rule, and
[`scope/1_publish-guidance-site.md`](./scope/1_publish-guidance-site.md)
for how it was applied here.

## The rule that governs everything else

**Strategy and business architecture are validated before any other
layer, and the requester approves at explicit gates before development.**
A change in requirements is never coded directly: align it through the
numbered EA layers (`architecture/1_strategy` → … → `5_technology`), stop at
the gates for the Requester's approval, record it all in a scope document
(`scope/`), then implement. Use the `ea-first-change` skill for the
process (it defines the gates), `strategy-discovery` if a change shifts
the strategy itself, `scope-doc` for the scope document (its Approvals
table is the durable record of the gates), `ea-doc-style` when touching
anything under `architecture/`, `restate-current-state` when the model has drifted
into a history rather than a description of today, and `pr-description`
when opening or updating a PR. If a change touches the Copilot's autonomy
level or decision rights,
also see
[`decisions/1_docs-agent-autonomy.md`](./decisions/1_docs-agent-autonomy.md)
and the `decision-record` skill.

## Modeling depth

**Declared depth: 1 — Application.** The subject is one thing that gets
built: a static site. `architecture/0_business-design/` and `architecture/domains/`
are not used, and the strategy layer stays light — goals and principles,
enough to judge a change against.

## Layout

- `architecture/` — this project's current-state architecture (numbered
  ArchiMate layers); `scope/` — one document per initiative;
  `decisions/` — smaller rationale calls, notably the Copilot's
  autonomy.
- `public/` — the static pages, deployed as-is (no build step) by GitHub
  Actions to GitHub Pages. `index.html` (the whole argument), `how.html`
  (the mechanism), `start.html` (the way in), `styles.css`; `public/es/`
  mirrors the three pages in Spanish.

## Commands

No build step. `public/` is hand-written, dependency-free HTML/CSS —
open any page directly in a browser to preview it. Deployment runs
automatically via
[`../.github/workflows/deploy-site.yml`](../../.github/workflows/deploy-site.yml)
on push to `main`.

## Conventions

- Documentation language: English. Site pages are published in English
  (`public/*.html`, canonical between the two editions) and Spanish
  (`public/es/*.html`); a change to a page updates both editions in the
  same change (see
  [`architecture/3_information/1_data-objects.md`](./architecture/3_information/1_data-objects.md)).
- Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`, …).
- Site content is a **derived** representation of this project's own
  `architecture/` and of the canonical skill files under `../.claude/skills/` —
  it summarizes them for a public reader, it is not a second canonical
  source. If a page and its source EA doc disagree, the EA doc is right
  and the page is stale (see
  [`architecture/3_information/1_data-objects.md`](./architecture/3_information/1_data-objects.md)).
