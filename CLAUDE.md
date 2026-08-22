# CLAUDE.md

This repository holds **the worked models** — archreator applied to real
subjects, so that a prospective adopter can read a filled-in model rather than
an empty scaffold. The method itself is the sibling repository
[`archreator`](https://github.com/roanboc/archreator): skills, scaffold and
docs there, models here.

## The rule that governs everything else

**Strategy and business architecture are validated before any other layer,
and the Requester approves at explicit gates before development.** A
requirement is never coded directly: it is aligned through the numbered
layers, stopped at the gates, recorded in a scope document under the tree's
`architecture/scope/`, and only then implemented. Pure bug fixes that change
no documented behavior skip the gates but still update whatever the fix
falsifies.

The Requester for every tree here is the repository owner.

## Layout

**One tree per federated project.** Each thing the organization builds keeps a
model of its own rather than becoming a folder inside the organization's, and
the prefix says which kind of thing it is. `org-` is the organization;
`product-` is something it builds and delivers.

| Tree | Subject | Depth |
| ---- | ------- | ----- |
| [`org-archreator/`](./org-archreator/architecture/README.md) | The organization that publishes archreator — its stakeholders, capabilities and courses of action | 2 — Organization |
| [`product-archreator/`](./product-archreator/architecture/README.md) | archreator the method, as a product: its skills, validators and scaffold | 1 — Application |
| [`product-archreator/site/`](./product-archreator/site/architecture/README.md) | The published guidance site, nested because it realizes a service of the product rather than standing alone | 1 — Application |
| [`scripts/`](./scripts/README.md) | The two validators and the projection, one copy for the whole repository |

A tree earns its place by having **application components and technology of
its own**. A directory that only restates elements belonging somewhere else is
a folder pretending to be a project, and its contents belong in the model
above it.

## What is modeled where

The method's **motivation** — why archreator exists, who it serves, what it
must be true of — is modeled here, in `product-archreator/1_strategy/`.

The method's **process model** is not. `BPROC1`–`BPROC4` and their level-2
children live in `docs/process/` of the `archreator` repository, beside the
skills that realize them, because that adjacency is what lets CI prove that
every process has a skill and every skill a process. Splitting the two would
leave the binding the process model exists for unenforced. See
[decision 1](./product-archreator/architecture/decisions/1_the-process-model-stays-with-the-skills.md).

## Commands

```bash
python3 scripts/check_links.py    # relative links and HTML anchors resolve
python3 scripts/check_model.py    # element-ID references resolve, per tree
```

Both must be green before pushing; CI runs the same two.
`python3 scripts/build_model.py` projects every tree into `.model/` for a
rendered view — a tool, not a gate.

## Conventions

- Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`, …).
- **Documentation language: English.**
- Element IDs are scoped per tree, so each tree may own its own `G1`. An ID is
  assigned once and never reused after the gate that approves its element.
- The skills come from the [archreator](https://github.com/roanboc/archreator)
  plugin, enabled in [`.claude/settings.json`](./.claude/settings.json). They
  are never vendored into this repository: a copy is a thing that drifts from
  the method it is supposed to be.
