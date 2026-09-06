# CLAUDE.md

This repository holds **the worked models** — archreator applied to real
subjects, so that a prospective adopter can read a filled-in model rather than
an empty scaffold. The method itself is the sibling repository
[`archreator`](https://github.com/roanboc/archreator): skills, scaffold and
docs there, models here. The models run on method **0.2**.

## How a change happens here

The owner says what they want, in plain words. The agent works out which
layers the change touches, edits them, writes a short note under
`product-archreator/architecture/scope/`, and opens a pull request. **The
owner's merge is the approval.** Nothing else records one, and the agent never
stops the conversation to ask for an approval.

The agent stops to ask only when the change contradicts a principle or a
decision already written down, or when two readings of the request would
build different things. It does not ask about the future, and it does not ask
the owner to decide what the model already settles.

A pure correction — a broken link, a stale path, a validator brought level
with the method — is just fixed, together with whatever it falsifies.

**Where a skill from the plugin says otherwise, this file wins.** The skills
describe the method's full process; this repository runs the light form above.

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
Where the product is going is `product-archreator/architecture/6_transition/`.

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
build_brief.py --project product-archreator --scope product-archreator --element BSVC1 --focus impact
```

`--project` picks the tree's parse and where output lands, not which model
answers: an element both trees own — `BSVC1` — also needs `--scope <tree>`.
The `Makefile` at the root wraps all of this: `make method` fetches the plugin
under gitignored `.archreator/method/`; `make trace E=ACMP1`, `make coverage`,
`make brief E=BSVC1 F=impact` and `make portal P=org-archreator` run one
tool each; and `make smoke` runs every tool over both trees and builds both
portals, before a push, beside the validators. Everything they generate
lands under gitignored `.archreator/`; nothing is cached, and every run parses
the Markdown fresh.

## Conventions

- Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`, …).
- **Documentation language: English**, in plain words. The name leads and the
  identifier rides along — `the skill corpus [ACMP1]` — except in a defining
  row and in a machine-read relationship column.
- Every document that defines elements carries one status mark in its
  preamble. `◐` means nobody has said it is right yet; `●` means the owner has
  read it and stands behind it. The owner flips a mark, or asks for it to be
  flipped, whenever they like. No ceremony is attached to it.
- Element IDs are scoped per tree, so each tree may own its own `G1`. An ID
  is never reused once the element has been merged.
- A cross-model reference leads with the target's **federation ID** —
  `ORG.G1`, `PRD_MTD.BSVC1` — declared on that model's front door
  (`ORG` for the organization, `PRD_MTD` for the method as a product) and
  mapped in the citing model's `architecture/federation.md`. A child model
  refines its parent's elements and never restates them, and a child cannot
  define a stakeholder the parent has never heard of.
- The skills come from the [archreator](https://github.com/roanboc/archreator)
  plugin, enabled in [`.claude/settings.json`](./.claude/settings.json). They
  are never vendored into this repository: a copy is a thing that drifts from
  the method it is supposed to be.
