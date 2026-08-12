# 7 — One tree per federated project, named for what it is

_[← Decisions](./README.md)_

**Status:** Accepted
**Date:** 2026-08-12
**Touches:** [decision 5](./5_no-per-product-strategy-folders.md), `ACMP2`,
`BSVC2`, the repository layout

## Context

This repository holds four things — the organization that publishes
archreator, the method itself, the guidance site, and the scaffold a cloner
inherits — under directory names (`org-archreator/`, `product-archreator/`, `site/`, `docs/`)
that identify almost none of them. [Scope document 9](../scope/9_the-repository-says-what-it-is.md)
renames them `org-archreator/` and `product-archreator/`, with the site nested
inside the latter.

That raises a direct question against an accepted decision.
[Decision 5](./5_no-per-product-strategy-folders.md) rules that the strategy
layer stays enterprise-wide, that **products structure layers 0 and 2 only**,
and that when a product stops sharing the organization's strategy the answer
is _"a **domain**, not a folder inside layer 1"_. A top-level tree called
`product-archreator/` containing its own `1_strategy/` looks, at a glance,
exactly like the thing decision 5 forbids.

## Options considered

| Option | Consequence |
| ------ | ----------- |
| **One model for everything; products appear only as `PROD` elements in layers 0 and 2** | Decision 5 applied literally to the repository. But the method and the site each have their own application components, their own technology, and their own scope history — none of which has anywhere to live in the organization's model |
| **One tree per federated project, prefixed by what it is** | Each deliverable keeps a full model of its own, federated from the organization's. The prefix carries the distinction the bare name cannot. Costs a naming convention that must be explained, or it will be misread as the per-product split |
| **Split into domains at Depth 3** | The documented answer when a product diverges. But the split test asks whether something is a **business line** with its own goals, people and economics — the method and the site are not business lines, they are things the organization builds |

## Decision

**One tree per federated project.** The organization gets `org-archreator/`;
each thing the organization builds gets its own tree, prefixed `product-` when
it delivers a product. `product-archreator/site/` nests because the site
realizes `BSVC2` for `PROD1` rather than standing on its own.

**This is federation across projects, not decomposition within a model** —
a different axis from the one decision 5 governs, and decision 5 is unchanged.

## Why

**Decision 5 governs the inside of one model; this governs how many models
there are.** Its reasoning is about a capability being filed under a product,
so that no document shows three products sharing one capability base. Nothing
in that reasoning touches whether a separately-built application keeps its own
model — and the organization's own
[`2_application-components.md`](../../org-archreator/architecture/4_application/2_application-components.md)
already recommends the federated shape to adopters: model the organization
once, and give each application it builds its own project consuming that
model. This decision applies that recommendation to archreator itself.

**A tree with its own applications and its own technology is a project, not a
folder.** `product-archreator/` and `site/` both carry layers 4 and 5 with real components
in them. That is the test: a folder restates elements that belong somewhere
else, a project has elements of its own that exist nowhere else.

**Depth 3 would be the wrong instrument.** The split test asks whether
something has its own goals, its own people and its own economics — the
question that separates a business line from a product. The method and the
site fail that test cleanly. They are not domains; they are deliverables.

**The prefix is doing the disambiguation.** archreator names the
organization *and* `PROD1` — the same collision Facebook carried until the
portfolio outgrew it. `org-` and `product-` are what let the two sit as
siblings without a reader having to open them. Without the prefixes the
choice would be `org-archreator/` beside `archreator/`, which is worse.

## Consequences

- **`product-archreator/` has its own `1_strategy/`, and that does not reopen
  decision 5.** Its strategy layer is the method's own, not a per-product
  shard of the organization's — the organization's `1_strategy/` continues to
  hold one capability base serving all three products.
- **Adopters may copy the layout without reading this record** and conclude
  that products get folders — the precise misreading decision 5 exists to
  prevent. The line lives in a document rather than in the structure, which is
  a real weakness of this decision.
- **`PROD2` will never have a tree.** Consulting's realizing artifact is
  recorded as "`ROLE2`, in person" — it has no repository artifact. The prefix
  does not promise one directory per product.
- **`PROD3` has somewhere to go.** The portal, when `COA2` is taken, becomes
  `product-portal/` — the one product that does not share the organization's
  name, which is the case that tests the convention.
- **Renaming the organization would cost a directory move plus roughly 180
  link repairs.** Mitigated by having `project-bootstrap` generate the folder
  from a prompted organization name rather than hardcoding it, so an adopter
  never inherits archreator's name.

## What would reopen this

A tree that turns out to have **no application components and no technology of
its own** — that would be a folder pretending to be a project, and its
contents belong in the organization's model under decision 5.
