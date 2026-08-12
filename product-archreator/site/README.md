# archreator-guide — the published guidance site

_[← Repository README](../../README.md)_

This is archreator's **own public documentation**: the guidance site live at
**https://roanboc.github.io/archreator/**, written for people deciding
whether and how to use the method. The pages are in
[`public/`](./public/index.html); this folder's `docs/` is the project's own
architecture.

It is also a real project built by following the exact process it describes
— EA layers walked top-down, a scope document written before implementation,
gate approvals recorded — at **Depth 1**, because the subject is one thing
that gets built. That makes it the answer to "what does a filled-in
`architecture/` look like for an application", and specifically to "what does an
AI actor look like in the business layer": one of its own business actors —
"Copilot" — is an AI, modeled with an explicit autonomy level, decision
rights, and escalation path
([`architecture/2_business/1_business-actors-and-roles.md`](./architecture/2_business/1_business-actors-and-roles.md)),
alongside the human Pilot who reviews its work.

It used to be called `example/`, back when a fictional company sat beside it
as the second worked example. That company was
[removed](../scope/4_remove-the-fractal-example.md) — real projects are
better evidence than a maintained fiction — and this folder was renamed for
what it actually is.

## Why this lives in its own subfolder

The root of this repository is the template — intentionally blank, so
that clicking "Use this template" hands a new project a clean scaffold,
not someone else's filled-in architecture. This folder is kept separate
from that scaffold on purpose: read it as a reference, don't inherit it.
If you bootstrapped your own project from archreator, your `architecture/` and
`scope/` live at your project's root, structured exactly like this
folder's — just about your project instead.

## Reading it

- [`architecture/`](./architecture/README.md) — this project's current-state
  architecture, including the actor-notation example.
- [`scope/`](./scope/README.md) — the one initiative that built
  this project, `1_publish-guidance-site.md`.
- [`decisions/`](./decisions/README.md) — the smaller rationale
  calls behind this project: why the Copilot's autonomy level was set the
  way it was, and why the site renders its diagrams in CSS rather than with a
  library.
- [`site/`](./public/index.html) — the static pages themselves, deployed by
  [`.github/workflows/deploy-site.yml`](../../.github/workflows/deploy-site.yml)
  to GitHub Pages on every push to `main`. This is the only application
  code this project has — see
  [`architecture/4_application/2_application-components.md`](./architecture/4_application/2_application-components.md).
