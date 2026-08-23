# Project Scope — Publish the model beyond the repository

_[← Scope index](./README.md) · [Model home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** [`archreator` PR #33](https://github.com/roanboc/archreator/pull/33), merged; and the model changes this document holds the gate for.

The method could describe an organization to an agent and to anyone who
browses a repository, and to nobody else. The people who must *agree* with an
architecture — the executive who will fund it, the auditor who will test it,
the stakeholder whose process it describes — do not clone anything. Scope
document 1 said this out loud and parked it: *"the projection was built
because a rendered view needs it; the rendered view is a later initiative."*
This is that initiative.

The method now renders any model as a searchable website and prints it as one
PDF, both from the Markdown and both disposable. **What changed is what the
method can do, not what these models say** — but a method that gained a
capability has falsified the model that describes it, and this document is the
repair.

## The gate is ahead of the work, and the work is ahead of the gate

The implementation merged in `archreator` before this record existed, at the
Requester's direction. That is the wrong order and the record says so rather
than being backdated.

What follows from it is that **the gates below are real, not retrospective**.
The model changes in the EA alignment table have *not* been applied: they are
what Gate 1 and Gate 2 approve, and the branch carrying them starts once they
are granted. A gate whose work is already done approves nothing; a gate whose
work is still in front of it is the method working as written.

Every identifier proposed below is draft under `RULE4` — renumbering to close
a gap is free until the gate passes, and forbidden afterwards.

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 0_business-design | **Not used** — Depth 1, unchanged. The canvases describe an organization's customers and economics; this subject has neither |
| 1_strategy | **Changed — Gate 1.** A stakeholder nobody modeled (`STK5`, the reader outside the repository), the goal that serves them (`G5`), and the capability that delivers it (`CAP7`). No new driver: `STK5`'s concern carries the change, and `P4` says an element earns its place or does not get one. **`G1`'s realization is corrected**: "no export, no tool, no database" now reads as "nothing has to be exported before the model can be used", which is what it always meant and is no longer what it literally says |
| 2_business | **Changed.** `BSVC7` — model publication, realizing `CAP7`; `BIF5` — the model, rendered, as the interface `STK5` meets it through; `RULE7` — a rendering is never the model, which is the constraint the whole feature stands on |
| 3_information | **No change.** The portal introduces no information. Its staged copy, its built site and the PDF are renderings of documents rather than structures anything parses, and they already follow `DOBJ4`'s discipline — regenerated, never hand-edited, never committed. A data object for each would model the same four documents a second time |
| 4_application | **Changed.** `ASVC9` — model publication, realizing `BSVC7`; `ACMP12` — the portal builder (`scaffold/scripts/build_docs.py`, with `scaffold/mkdocs.yml` and `scaffold/overrides/`); `ACMP13` — the document exporter (`scaffold/scripts/export_pdf.py`). `ACMP10`'s description gains the portal configuration it now ships. **`ASVC8`'s note is falsified and must be repaired**: it says the projection's intended consumer is a published view of the model that the organization has not built. The published view now exists and does not read the projection — it reads the Markdown. `ASVC8` stays dashed, for a better-evidenced reason |
| 5_technology | **Changed.** `TSVC5` — documentation rendering, provided by `NODE5`, the toolchain the portal needs: MkDocs with Material, and a Chromium-family browser for the PDF. `NODE3` — static hosting — is **explicitly unchanged**: nothing publishes these models, and the method deliberately ships no workflow that would |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — Depth 1; this tree holds no canvases |
| Gate 1 — Strategy | — | — | **Pending.** `STK5`, `G5`, `CAP7` and the correction to `G1`, as stated in the EA alignment table above. This document is the presentation |
| Gate 2 — Business | — | — | **Pending.** `BSVC7`, `BIF5` and `RULE7`, and with them the application and technology changes that follow. This document is the presentation |
| Gate 3 — Solution design | — | — | **N/A — not requested.** The design it would cover is merged in `archreator` and was reviewed there as PR #33. Available on request, against the same code |

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | A model whose readers are the three roles that open the repository. The projection exists for a consumer that does not, and the model says that consumer is a later initiative |
| **Target** (delivered) | The same model, plus the reader who never opens the repository, the capability that reaches them, the two components that do it, and the toolchain they need. The projection is still consumed by nothing, and now says so with evidence rather than expectation |

## Work packages and deliverables

### WP1 — The strategy layer gains the reader nobody modeled

- **Deliverables:** `STK5` and `G5` in
  [1_motivation.md](../1_strategy/1_motivation.md), with `G1`'s realization
  corrected in the same pass; `CAP7` in
  [2_capabilities-and-resources.md](../1_strategy/2_capabilities-and-resources.md),
  and its edge to `BSVC7`.
- **Outcome:** the model names the audience the method just learned to serve,
  instead of implying the only readers are the three roles inside the repository.

### WP2 — The business layer gains the service, the interface and the rule

- **Deliverables:** `BSVC7` and `BIF5` in
  [2_business-services.md](../2_business/2_business-services.md); `RULE7` in
  [5_domain-context-and-rules.md](../2_business/5_domain-context-and-rules.md),
  naming what enforces it — staging regenerated on every run, the whole tree
  gitignored, and every page carrying the path of the file that produced it.
- **Outcome:** publishing is a service with a stated constraint, rather than a
  script somebody found in `scripts/`.

### WP3 — The application layer gains two components, and `ASVC8` stops promising a consumer

- **Deliverables:** `ASVC9` in
  [1_application-services.md](../4_application/1_application-services.md) with
  its note on `ASVC8` rewritten; `ACMP12` and `ACMP13` in
  [2_application-components.md](../4_application/2_application-components.md),
  and `ACMP10`'s description extended to the portal configuration it ships.
- **Outcome:** every file the initiative added is named by the element that
  realizes it, per `P2`, and the model's one dashed edge is honest for a
  reason that has been tested rather than assumed.

### WP4 — The technology layer gains the toolchain

- **Deliverables:** `TSVC5` and `NODE5` in
  [1_technology-services.md](../5_technology/1_technology-services.md), with
  `NODE5`'s substitutability stated: the portal is MkDocs-shaped, the PDF is
  any Chromium-family browser, and the second is replaceable in a line while
  the first is not.
- **Outcome:** the dependency the method took on is visible, including the one
  it takes at *view* time — the diagram library the theme fetches from a CDN.

### WP5 — The index

- **Deliverables:** the row for this document in
  [README.md](./README.md).
- **Outcome:** the initiative is findable from the index rather than only from
  the filename.

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| The four layers repaired to describe a method that can publish a model | **Publishing *these* models.** Hosting `product-archreator` or `org-archreator` anywhere is a course of action the organization has not taken, and it belongs to [`org-archreator`](../../../org-archreator/architecture/README.md) rather than here |
| `ASVC8`'s note corrected to what the initiative proved | **Giving `ASVC8` a consumer.** Still nothing reads the projection, and the candidate that was expected to is now ruled out |
| `NODE5` recorded, including the CDN it reaches at view time | **Removing that CDN dependency.** The offline recipe is documented in the method; vendoring a 3.5 MB library into every generated project is not |
| `RULE7`, and what enforces it | **Comment threads on these models.** The method ships the wiring; switching it on is a decision about audience, not a modeling change |

## Gap notes

- **`ASVC8` has no consumer, and now has no candidate.** Scope document 1
  drew it dashed on the expectation that a published view would read it. The
  published view reads the Markdown directly, because a renderer that reads a
  projection would render a second-hand copy of the documents. Closing the gap
  needs a consumer that genuinely asks graph questions — a coverage dashboard,
  a blast-radius report — and none exists.
- **Nothing hosts the portal, deliberately.** Until an organization takes that
  course of action, the audience is whoever is handed the PDF. The method ships
  no workflow, because one that fails until somebody enables a hosting product
  is worse than none.
- **The diagrams need the network at view time.** The theme fetches Mermaid
  from a CDN, so a reader behind a strict proxy sees diagram source instead of
  diagrams. The exporter detects exactly this and refuses to stay quiet about
  it; the portal cannot, because nothing runs after it is published.
- **No check crosses the repository boundary in this direction either.** If
  `build_docs.py` is renamed in `archreator`, `ACMP12` points at nothing and
  nothing here fails — the same unenforced dependency decision 1 records, now
  with two more components riding on it.

## Open questions

- **Is correcting `G1`'s realization a Gate 1 matter or a pure correction?**
  Adopted interpretation: **Gate 1**. The words being repaired are the ones a
  reader uses to judge whether the method still holds its own line — "no
  export" is the sentence the method has been sold on — so the Requester sees
  the new wording rather than finding it in a diff. Applied in WP1.
