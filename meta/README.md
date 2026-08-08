# meta — archreator's own development record

_[← Repository README](../README.md) · [The method](../CONTRIBUTING.md)_

**Delete this folder when you create a project from archreator.** Like
[`example/`](../example/README.md) and
[`example-company/`](../example-company/README.md), it is here to read, not
to inherit — it documents how *this template* is built, not how your project
should be.

## Why this folder exists

archreator asks every project to align changes through `docs/ea/` and record
them in `docs/scope/`. archreator cannot do that to itself: its own
`docs/ea/` and `docs/scope/` are the **blank scaffold a cloner receives**, so
filling them in with archreator's own strategy would hand every new project
someone else's architecture on day one.

For its first ten pull requests that left the method's own development
unrecorded — the process was followed in the PR bodies and nowhere else.
This folder closes that gap without polluting the template:

| Folder | What it holds |
| ------ | ------------- |
| [`reviews/`](./reviews/1_value-and-ux-review.md) | Assessments of the template itself — its value against comparable tools, and whether the workflows land for a new user |
| [`scope/`](./scope/1_repo-value-and-fractal-domains.md) | Scope documents for initiatives that change **the method**, written with the same [`scope-doc`](../.claude/skills/scope-doc/SKILL.md) skill a downstream project uses |

The distinction that keeps this honest: **`docs/` is what a cloner gets;
`meta/` is what archreator did to itself.** A change to the method — a new
skill, a new layer, a changed gate — gets a scope document in `meta/scope/`.
A change to a *project built from* archreator gets one in that project's own
`docs/scope/`.

## Index

| # | Document | What it is |
| - | -------- | ---------- |
| 1 | [reviews/1_value-and-ux-review.md](./reviews/1_value-and-ux-review.md) | Value against BMAD and ArcKit, ten verified new-user defects, and the improvement backlog |
| 1 | [scope/1_repo-value-and-fractal-domains.md](./scope/1_repo-value-and-fractal-domains.md) | The initiative that acted on that review: enterprise-first positioning, modeling depth, fractal domains, plugin packaging |
