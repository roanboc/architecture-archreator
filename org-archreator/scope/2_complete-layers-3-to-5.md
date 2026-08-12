# Project Scope — Complete layers 3 to 5

_[← Scope index](./README.md) · [EA home](../architecture/README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** `organization/docs/ea/3_information/`, `4_application/`
and `5_technology/` on branch `claude/repo-value-ux-review-3ur5y4`.

[The first initiative](./1_model-the-operating-model.md) stopped at layer 2
and said layers 3–5 would be filled "by the initiatives that touch them" —
correct as a rule against inventing intentions, but it left a claim untested:
that the bottom three layers describe **what already exists**, not what is
planned. This organization has a repository, a published site, two
validators, a plugin and a set of clients. All of that is real today and
none of it was modeled.

So this initiative fills layers 3–5 with **current state only**. Everything
that does not exist stays marked Pending, and the portal (`COA2`) is Pending
in every one of them.

This is a **docs-only initiative**. No code is delivered.

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 0_business-design | **No change.** Neither canvas moves |
| 1_strategy | **No change.** No new goal, capability or principle. Two existing elements are explained rather than altered: `OUT7`'s missing measure and `COA2`'s real cost |
| 2_business | **No change.** Actors, products and services are referenced, not revised |
| 3_information | **Filled.** 6 data objects with classification; documents 2 and 3 explicitly not started, with the reason |
| 4_application | **Filled.** 4 application services, 5 components; documents 3–5 explicitly not started, with the reason |
| 5_technology | **Filled.** 5 technology services, 4 nodes, 3 artifacts, and the absence of a build |
| domains | **No change** — still Depth 2 |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — no business model change; the canvases are unchanged |
| Gate 1 — Strategy | — | — | **N/A** — no strategy change; layer 1 is referenced, not revised |
| Gate 2 — Business | Requester | 2026-08-09 | The information, application and technology layers, and the explicit "no change" verdicts for layers 0–2. Presented in the session with branch links to all five documents, alongside the two findings the layers agree on and the `DOBJ4` confidentiality gap. Gate 3 declined — nothing here is designed |
| Gate 3 — Solution design | — | — | **N/A** — no solution is designed; the components documented already exist |

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | Layers 0–2 modeled and approved. The repository, the site, the validators and the plugin existed and appeared nowhere in the model |
| **Target** (delivered) | All six layers modeled. What the organization holds, what software it owns, and what it runs are all stated — including three places where the honest answer is "nothing" |

## Work packages and deliverables

### WP1 — The information layer

- **Deliverables:** [`3_information/README.md`](../architecture/3_information/README.md),
  [`1_data-objects.md`](../architecture/3_information/1_data-objects.md) — `DOBJ1`–`DOBJ6`
  with classification, and explicit not-started verdicts for data flows and
  data architecture
- **Outcome:** the reason `OUT7` cannot be measured is written down where it
  belongs — this organization holds no data about its adopters

### WP2 — The application layer

- **Deliverables:** [`4_application/README.md`](../architecture/4_application/README.md),
  [`1_application-services.md`](../architecture/4_application/1_application-services.md),
  [`2_application-components.md`](../architecture/4_application/2_application-components.md)
  — `ASVC1`–`ASVC4`, `ACMP1`–`ACMP5`, each component naming its files and the
  Depth 1 model that details it
- **Outcome:** the relationship between this tree, `meta/` and `site/` is
  defined rather than assumed

### WP3 — The technology layer

- **Deliverables:** [`5_technology/README.md`](../architecture/5_technology/README.md),
  [`1_technology-services.md`](../architecture/5_technology/1_technology-services.md),
  [`2_deployment.md`](../architecture/5_technology/2_deployment.md) — `TSVC1`–`TSVC5`,
  `NODE1`–`NODE4`, `ART1`–`ART3`
- **Outcome:** the organization's dependence on one platform and on the
  adopter's own machine is explicit, and so is the absence of a build

### WP4 — Extend the notation source

- **Deliverables:** [`docs/ea/README.md`](../../.claude/skills/project-bootstrap/templates/architecture/README.md)
  § Notation conventions — glyphs, shapes and tone ramps for the
  information, application and technology layers
- **Outcome:** the standard covers all six layers rather than the three that
  had been drawn when it was written

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| Layers 3–5 as they are today | Anything the portal would introduce — it stays Pending in all three |
| The `meta/` and `site/` relationship, defined in layer 4 | Changing either of those trees |
| Data classification, as three lines in one table | A data architecture — there is no storage to describe |
| The absence of a build, stated | Introducing versioning or releases |

## Gap notes

- **`DOBJ4` is the only confidential data and it has no system.** One person
  holds every client's business information outside anything modeled here.
  Defensible at one consultant; indefensible the moment `ROLE2` is filled by
  anyone else. There is no access control to document because there is
  nothing to control it with.
- **`COA3` is a data decision, not a reporting task.** Instrumenting the
  adoption measure means beginning to hold information about adopters, which
  this organization has never done — even self-reporting crosses that line.
  Whoever opens that initiative is changing layer 3.
- **`NODE1` provides four of five technology services.** One platform, like
  one person. It is substitutable in a weekend where `RES1` is not, which is
  why only one of the two carries a course of action — but a single-platform
  dependency that also carries `BIF1`–`BIF3` is worth naming.
- **Layer 4 documents 3–5 and layer 3 documents 2–3 are empty**, and the
  reason matters: the components do not call each other and the organization
  stores nothing. An empty data architecture usually means the analysis
  stopped; here it means there is nothing there. If `COA2` ever runs, all
  five documents become necessary at once.
- **There is no version boundary.** `ART1` and `ART3` are source read where
  it lies, so an adopter who pulls gets whatever the default branch says
  today. Nobody has needed more, and `2_deployment.md` is where it would be
  recorded when someone does.

## Open questions

| # | Question | State |
| - | -------- | ----- |
| 1 | How do this tree and `meta/` relate once layer 4 exists? | **Resolved by this initiative.** Layer 4 names *that* an application exists and what it offers; the Depth 1 model says *how* it is built. Neither restates the other, and the `Modeled in full by` column is the link. Raised as question 5 of [initiative 1](./1_model-the-operating-model.md), which is merged and therefore not edited — the answer is recorded here instead |
| 2 | Should the confidentiality of `DOBJ4` be addressed before `ROLE2` is ever shared? | Open. Named in the gap notes; no initiative proposed |
