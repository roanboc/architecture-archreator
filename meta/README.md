# meta — archreator, modeled with archreator

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
filling them in with archreator's own architecture would hand every new
project someone else's stakeholders on day one, and the template would stop
being a template.

For its first ten pull requests that left the method's own development
unrecorded — the process was followed in the PR bodies and nowhere else.
This folder closes that gap without polluting the scaffold, and it holds the
**full component set** a downstream project gets, so the method is exercised
rather than merely described:

| Folder | What it holds |
| ------ | ------------- |
| [`ea/`](./ea/README.md) | archreator's own enterprise architecture, at **Depth 1** — strategy, business, application, technology. Layers 0, 3, and `domains/` are not used, and say so |
| [`scope/`](./scope/README.md) | One document per initiative that changes the method, with its Approvals table |
| [`decisions/`](./decisions/README.md) | Single consequential calls smaller than an initiative — why the plugin root is `.claude/`, why IDs aren't renumbered on a split, why the Agent sits at co-pilot autonomy |
| [`open-questions.md`](./open-questions.md) | The consolidated index of adopted interpretations still awaiting confirmation |
| [`reviews/`](./reviews/1_value-and-ux-review.md) | Assessments of the template itself — its value against comparable tools, and whether the workflows land for a new user |

The distinction that keeps this honest: **`docs/` is what a cloner gets;
`meta/` is what archreator did to itself.** A change to the method — a new
skill, a new layer, a changed gate — gets a scope document in `meta/scope/`.
A change to a project *built from* archreator gets one in that project's own
`docs/scope/`.

## What modeling itself actually surfaced

Dogfooding is only worth the effort if it finds something. Three things this
model makes visible that prose had not:

- **`ACMP15` is Pending and two business rules point at it.** The model
  exporter doesn't exist, so `RULE2` (every element names what realizes it)
  is enforced only for links, and `RULE5` (IDs are never reused) is enforced
  by nothing. In the [application layer](./ea/4_application/1_application-components.md)
  that is a row with an empty realization and two inbound dependencies —
  much harder to leave alone than a backlog paragraph.
- **CI enforces one rule out of nine.** Stated plainly in the
  [technology layer](./ea/5_technology/1_technology-services.md), which is
  where you would look for it and where it had never been written down.
- **A skill's `description:` is its contract.** Modeling the skills as
  components with one interface made it obvious why `story-sharding` was
  dead for ten pull requests: the description was accurate, and nothing
  pointed at it.

## Index

| # | Document | What it is |
| - | -------- | ---------- |
| — | [ea/README.md](./ea/README.md) | The current-state model of the method |
| 1 | [reviews/1_value-and-ux-review.md](./reviews/1_value-and-ux-review.md) | Value against BMAD and ArcKit, ten verified new-user defects, and the improvement backlog |
| 1 | [scope/1_repo-value-and-fractal-domains.md](./scope/1_repo-value-and-fractal-domains.md) | Enterprise-first positioning, modeling depth, fractal domains, plugin packaging |
| 2 | [scope/2_archreator-models-itself.md](./scope/2_archreator-models-itself.md) | The framework positioning, this self-model, and `restate-current-state` |
