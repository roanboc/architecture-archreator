# Project Scope — Intention first, realization handed over

_[← Scope index](./README.md) · [Model home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** branch `ccr-a18fcfba-bdmhgn` here and in
[`archreator`](https://github.com/roanboc/archreator), taking the method to
0.7 together with [scope 7](./7_previews-in-the-conversation.md).

The Requester asked to keep the method on strategy, business and information,
leave technical specification to other frameworks, and focus on the human
loop. This initiative turns layers 4 and 5 into a register — which software
realizes each business service, where it is specified, which code realizes it
— hands design, stack, interfaces, deployment and work breakdown to the
delivery framework a project names, and carries the principles into that
framework's standing file.

## EA alignment (assessed top-down before implementing)

| Layer | Impact | Confirmed |
| ----- | ------ | --------- |
| 0_business-design | In the organization's, `GCRE3` restated: the skills turn a confirmed design into work a delivery framework builds, its principles carried with it | The shape — a thin register for layers 4 and 5, `stack-selection` and `shard-stories` retired — by the owner, in conversation, 2026-09-29. The rest not yet |
| 1_strategy | In the organization's, `G2` restated: the design flows into delivery with its meaning carried rather than retold, where it had read *without a handover*. The method now hands over on purpose, and the principles travel with it. `OUT3` reworded | Not yet |
| 2_business | `BSVC1` names the handover of the realization | Not yet |
| 3_information | `DOBJ1.1` counts seventeen skills | Not yet |
| 4_application | `ACMP1` counts seventeen skills, fourteen invoked by name. This tree's own layers 4 and 5 stay as written while they are true; a later restatement collapses them into the register | Not yet |
| 5_technology | No change | — |

## What the evidence said

| Source | What it said |
| ------ | ------------ |
| The research behind this initiative | Spec-driven tools — GitHub Spec Kit, Kiro, OpenSpec, BMAD — now own specification, design and task breakdown, one repository at a time. None of them traces a principle or a goal above the product |
| [`ea_bigview`](https://github.com/roanboc/ea_bigview) | The company's own delivery team already works spec-first, with its own tooling; the model's value to it is the intent, not a second design |
| The method's own corpus | `stack-selection` and `shard-stories` were the two skills whose subject was the software rather than the business; both duplicated what a delivery framework does |

**The gap nobody fills is the link, not the design.** The model's distinct
value is the intention and the operation, and the principles reaching the
delivery framework intact. Designing the software a second time in the model
added a copy to keep true and no understanding.

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (0.6) | Layers 4 and 5 carry application services, components, collaborations, solution design, interface contracts, technology services and deployment; two skills choose a stack and slice stories |
| **Target** (0.7) | Layers 4 and 5 are a register linked to the delivery framework's specification; `AGENTS.md` § Delivery names the framework and its standing file; the principles a change touches are carried into that file |

## Work packages and deliverables

### WP1 — The register

- **Deliverables:** `assets/layers/4_application/` (a README and
  `1_realization-register.md`), `assets/layers/5_technology/` (a README and
  `1_platforms.md`, replacing `2_deployment.md`);
  `architecture-document-style` (§ Grounding rule, and the tier table in
  `references/model-structure.md`); `discover-current-landscape` (Step 4 now
  "Register what realizes it").
- **Outcome:** a model says *that* software realizes the business and *where*
  it is specified, never how it is built.

### WP2 — The handover

- **Deliverables:** `align-change-through-layers` Step 5, "Hand the
  realization over"; the scaffold's `AGENTS.md` § Delivery;
  `establish-project`; `docs/adopting.md` § Pairing it with a delivery
  framework; `docs/method.md`; the process model's `BPROC2.1.5` and
  `BPROC2.2`; `stack-selection` and `shard-stories` retired, their rows gone
  from the catalogue, the process model and `docs/standards-alignment.md`.
- **Outcome:** a project names its delivery framework once, and every change
  carries the principles it touches into it.

### WP3 — These trees

- **Deliverables:** the elements named in the alignment table.
- **Outcome:** both models count the corpus as it ships.

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| The register, the handover, and retiring the two skills | A generator for a named framework's standing file — Spec Kit's constitution, Kiro's steering files — from the model's principles |
| Restating the organization's `G2`, which the handover would otherwise contradict | Collapsing this tree's own layers 4 and 5 into the register |
| Keeping every prefix, so no existing project's identifiers move | ArchiMate 4, whose smaller element set touches the notation; one migration, planned with the 1.0 freeze |

## Gap notes

- **The standing file is written by hand.** The rule says what it carries;
  nothing generates it. A generator per framework is the natural next
  initiative, and the first concrete handover between this method and a
  spec-driven tool.
- **This tree still designs its own software in layers 4 and 5.** The rule
  allows it while the documents are true; `restate-current-state` collapses
  them when they next drift.
