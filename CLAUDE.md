# CLAUDE.md

This repository holds **the worked models** — archreator applied to real
subjects, so that a prospective adopter can read a filled-in model rather than
an empty scaffold. The method itself is the sibling repository
[`archreator`](https://github.com/roanboc/archreator): skills, scaffold and
docs there, models here. The models run on method **0.2**.

## The rule that governs everything else

**Strategy and business architecture are validated before any other layer,
and the Requester approves at explicit gates before development.** A
requirement is never coded directly: it is aligned through the numbered
layers, stopped at the gates — Direction, Understanding, Design — recorded in
a scope document, and only then implemented. Pure bug fixes that change no
documented behavior skip the gates but still update whatever the fix
falsifies.

The Requester for every tree here is the repository owner.

## Layout

**One tree per federated project.** Each thing the organization builds keeps
a model of its own rather than becoming a folder inside the organization's,
and the prefix says which kind of thing it is.

| Tree | Subject | Depth |
| ---- | ------- | ----- |
| [`org-archreator/`](./org-archreator/architecture/README.md) | The organization that publishes archreator — its customers, capabilities and value stream | 2 — Organization |
| [`product-archreator/`](./product-archreator/architecture/README.md) | archreator the method, as a product: its skills, validators, tools, scaffold and guidance site | 1 — Application |
| [`scripts/`](./scripts/README.md) | The two validators and the parse they share — one copy for the whole repository, serving both trees |

**A tree is a subject — an organization or a product — never a component.**
One product commonly spans several repositories: the method's repository and
the guidance site it carries are components of the same product, and a
component gets no tree here. Its architecture lives at the product level;
a component's own repository may carry whatever design detail it likes,
unprescribed, as long as it aligns with the product's model.

## What is modeled where

The method's **motivation** — why archreator exists, who it serves, what it
must be true of — is modeled here, in `product-archreator/1_strategy/`.

The method's **process model** is not. It lives in `docs/process/` of the
`archreator` repository, beside the skills that realize it, because that
adjacency is what lets CI prove that every process has a skill and every
skill a process.

## Commands

```bash
python3 scripts/check_links.py    # relative links and HTML anchors resolve
python3 scripts/check_model.py    # element-ID references resolve, per tree
```

Both must be green before pushing; CI runs the same two. The reading tools
live in the plugin, not here, and take `--project <tree>`:

```bash
model.py --project product-archreator trace ACMP1
model.py --project product-archreator coverage
model.py --project org-archreator portal
build_brief.py --project product-archreator --element BSVC1 --focus impact
```

Everything they generate lands under gitignored `.archreator/`; nothing is
cached, and every run parses the Markdown fresh.

## Conventions

- Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`, …).
- **Documentation language: English.**
- Element IDs are scoped per tree, so each tree may own its own `G1`. An ID
  is assigned once and never reused after the gate that approves its element.
- A cross-model reference leads with the target's **federation ID** —
  `ORG.G1`, `PRD_MTD.BSVC1` — declared on that model's front door
  (`ORG` for the organization, `PRD_MTD` for the method as a product) and
  mapped in the citing model's `architecture/federation.md`. A child model
  refines its parent's elements and never restates them, and a child cannot
  define a stakeholder the parent has never heard of.
- References lead with the name and the identifier rides along —
  `the skill corpus [ACMP1]` — except in a defining row and in a
  machine-read relationship column.
- The skills come from the [archreator](https://github.com/roanboc/archreator)
  plugin, enabled in [`.claude/settings.json`](./.claude/settings.json). They
  are never vendored into this repository: a copy is a thing that drifts from
  the method it is supposed to be.
