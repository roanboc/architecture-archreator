# meta — archreator, modeled with archreator

_[← Repository README](../README.md) · [The method](../CONTRIBUTING.md)_

**Delete this folder when you create a project from archreator.** Like
[`site/`](./site/README.md), it is here to read, not to inherit — it
documents how *this template* is built, not how your project should be.

## Why this folder exists

archreator asks every project to align changes through `architecture/` and record
them in `architecture/scope/`. archreator cannot do that to itself: its own
`architecture/` and `architecture/scope/` are the **blank scaffold a cloner receives**, so
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
| [`ea/`](./architecture/README.md) | archreator's own enterprise architecture, at **Depth 1** — strategy, business, application, technology. Layers 0, 3, and `domains/` are not used, and say so |
| [`architecture/scope/`](./architecture/scope/README.md) | One document per initiative that changes the method, with its Approvals table |
| [`architecture/decisions/`](./architecture/decisions/README.md) | Single consequential calls smaller than an initiative — why the plugin root is `.claude/`, why IDs aren't renumbered on a split, why the Agent sits at co-pilot autonomy |
| [`open-questions.md`](./architecture/scope/open-questions.md) | The consolidated index of adopted interpretations still awaiting confirmation |
| [`architecture/reviews/`](./architecture/reviews/1_value-and-ux-review.md) | Assessments of the template itself — its value against comparable tools, and whether the workflows land for a new user |

The distinction that keeps this honest: **`docs/` is what a cloner gets;
`product-archreator/` is what archreator did to itself.** A change to the method — a new
skill, a new layer, a changed gate — gets a scope document in `product-archreator/scope/`.
A change to a project *built from* archreator gets one in that project's own
`architecture/scope/`.

## What modeling itself actually surfaced

Dogfooding is only worth the effort if it finds something. Three things this
model makes visible that prose had not:

- **A Pending row with two rules pointing at it got built.** `ACMP15` was
  the model exporter, and modeling archreator turned "we should validate the
  IDs someday" into a row with an empty realization and two inbound
  dependencies — much harder to leave alone than a backlog paragraph. It now
  exists, scoped down to what the rules actually needed
  ([decision 4](./architecture/decisions/4_defer-the-model-database.md) explains why the
  database was dropped from it).
- **CI enforces two rules out of nine**, and the
  [technology layer](./architecture/5_technology/1_technology-services.md) says which —
  including that the grounding rule is still carried by review rather than
  tooling. That is where you would look for it, and it had never been
  written down before the model existed.
- **A skill's `description:` is its contract.** Modeling the skills as
  components with one interface made it obvious why `story-sharding` was
  dead for ten pull requests: the description was accurate, and nothing
  pointed at it.

## Index

| # | Document | What it is |
| - | -------- | ---------- |
| — | [ea/README.md](./architecture/README.md) | The current-state model of the method |
| 1 | [architecture/reviews/1_value-and-ux-review.md](./architecture/reviews/1_value-and-ux-review.md) | Value against BMAD and ArcKit, ten verified new-user defects, and the improvement backlog |
| 2 | [architecture/reviews/2_diagram-notation-icons.md](./architecture/reviews/2_diagram-notation-icons.md) | Whether ArchiMate element icons can be drawn in Mermaid — five options, rendered side by side, pending a decision |
| 1 | [architecture/scope/1_repo-value-and-fractal-domains.md](./architecture/scope/1_repo-value-and-fractal-domains.md) | Enterprise-first positioning, modeling depth, fractal domains, plugin packaging |
| 2 | [architecture/scope/2_archreator-models-itself.md](./architecture/scope/2_archreator-models-itself.md) | The framework positioning, this self-model, and `restate-current-state` |
