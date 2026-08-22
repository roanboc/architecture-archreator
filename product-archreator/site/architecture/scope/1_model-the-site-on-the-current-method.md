# Project Scope — Model the site on the current method

_[← Scope index](./README.md) · [Model home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** the `rebuild` branch and the pull request replacing `main`.

Part of the clean-room rebuild recorded in the method's own
[scope document 1](../../../architecture/scope/1_rebuild-the-models-on-the-current-method.md).
The previous model of this site described a multi-page structure — an index,
a how page, a start page and a Spanish translation — that no longer exists.
The site is now one 167-line file, and the model is rebuilt to describe that.

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 0_business-design | **Not used** — Depth 1. The site has no customers and no economics of its own |
| 1_strategy | **Rebuilt.** Two stakeholders, two drivers, two assessments, two goals, three principles; three capabilities and two resources. No value stream — one stage is not a flow |
| 2_business | **Rebuilt.** Three actors and two roles, four services, one interface. No product: the whole is the method, one tree up. No collaboration or contract — a reader owes nothing and is owed nothing |
| 3_information | **Not used.** The site holds no information at all, and the folder says so |
| 4_application | **Rebuilt.** One service and one component, with what is inlined inside it and why |
| 5_technology | **Rebuilt.** Two nodes, two services, one artifact, and a deployment with no build |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — Depth 1; this tree holds no canvases |
| Gate 1 — Strategy | Requester | 2026-08-22 | [1_motivation.md](../1_strategy/1_motivation.md) and [2_capabilities-and-resources.md](../1_strategy/2_capabilities-and-resources.md) — new in a clean room, so approved rather than assumed unchanged |
| Gate 2 — Business | Requester | 2026-08-22 | [1_business-actors-and-roles.md](../2_business/1_business-actors-and-roles.md) and [2_business-services.md](../2_business/2_business-services.md) |
| Gate 3 — Solution design | — | — | **N/A — declined at Gate 2.** The application and technology layers describe a page that already exists; there is no design being proposed |

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | A model of a multi-page site with its own diagram-rendering components, none of which the current page has |
| **Target** (delivered) | A model of one static file, its two weak points named, and both validators green |

## Work packages and deliverables

### WP1 — The strategy and business layers

- **Deliverables:** [1_motivation.md](../1_strategy/1_motivation.md),
  [2_capabilities-and-resources.md](../1_strategy/2_capabilities-and-resources.md),
  [1_business-actors-and-roles.md](../2_business/1_business-actors-and-roles.md),
  [2_business-services.md](../2_business/2_business-services.md).
- **Outcome:** the page's reason for existing is written down, including the
  principle that it may never be where a fact first appears.

### WP2 — The application and technology layers

- **Deliverables:**
  [1_application-services.md](../4_application/1_application-services.md),
  [2_application-components.md](../4_application/2_application-components.md),
  [1_technology-services.md](../5_technology/1_technology-services.md),
  [2_deployment.md](../5_technology/2_deployment.md).
- **Outcome:** one component, two nodes, and the property that makes the whole
  thing cheap — the reviewed bytes are the deployed bytes.

### WP3 — The unused layers state their state

- **Deliverables:** `0_business-design/`, `3_information/` and `domains/`
  READMEs each say they are unused and what would fill them.
- **Outcome:** an empty folder is a known gap rather than an unknown one.

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| Modeling the page as it is today | **Changing the page.** Nothing in `archreator/site/` is touched by this initiative |
| Naming the two weak points | **Closing them.** Both would need tooling that does not exist |
| Recording that the site shows no diagrams | **Making it show them.** That is the decision that would put pressure on `P2`, and it has not been taken |

## Gap notes

- **Nothing checks that the page is still true.** It reproduces a skill count,
  two install commands and a description of the scaffold, all owned by another
  repository. A link checker proves the links resolve, not that the sentence
  around them is still correct. Closing this would need a check that reads one
  repository and asserts against another — the same cross-repository problem
  decision 1 leaves open in the tree above.
- **The layer palette is duplicated.** The page's CSS custom properties are the
  method's notation colours, copied with nothing holding them in step. Small,
  real, and accepted because the alternative is a build step.
- **The site shows no diagrams**, so a visitor never sees what the notation
  actually looks like — arguably the most persuasive thing the method has.
  Fixing it means a renderer, a self-hosted bundle, or hand-written HTML, and
  each costs something `P2` currently buys for free.
