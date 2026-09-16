# Project Scope — Relationships in one catalogue, and documents written plainly

_[← Scope index](./README.md) · [Model home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** branch `claude/determined-lovelace-5ekizh` in the method
repository, and the same branch in BigView, the largest model on the method,
where the change was proved first (pull requests 18 and 19 of
`roanboc/ea_bigview`).

Every element document on the method carried a section written for agents: a
`## Relationships` table beside each diagram, in whichever of four shapes its
author chose, under a legend the parser never read. In BigView, ten level-2
pages and the level-1 map declared zero relationships while drawing 121, the
legends drifted from the diagrams under them, and the prose repeated what the
tables said. The Requester asked for one place agents read, human pages free of
anything a machine reads, and every page written so a newcomer understands it
on the first pass. This initiative takes the method to **0.5** by doing that,
and by simplifying how a process model is filed.

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 0_business-design | No change |
| 1_strategy | No change. `G1` and `G4` hold as written; writing plainly serves the organization's principles [`ORG.P3`] Better language, never simpler language and [`ORG.P5`] Well-done less is more |
| 2_business | No change. `BSVC1` and `BSVC3` do the same work on a document of a different shape |
| 3_information | The data object [`DOBJ1.1`] The skill corpus gains the rules; [`DOBJ2.1`] Layer documents lose their relationship table and their legend, every project model gains one relationships catalogue, and a layer README takes one shape; [`DOBJ1.3`] The scaffold and assets gain the catalogue template, a metamodel per layer, a third validator with its word list, and seven layer templates in that shape |
| 4_application | The component [`ACMP4`] The model parser reads a compact relationship row by shape and keeps catalogue cells out of mentions; [`ACMP3`] The element-ID validator stops asking for a legend and for a view before the first table; [`ACMP9`] The asset library gains one template, six metamodels and seven templates cut to the layer README shape; [`ACMP1`] The skill corpus changes five skills and seven references; [`ACMP8`] The scaffold follows and gains `check_prose.py`, the third validator, with `prose-denylist.json` and a CI step |
| 5_technology | No change |

## What the evidence said

Measured on BigView, before and after the two pull requests:

| Measure | Before | After |
| ------- | ------ | ----- |
| Relationships the parser read / drawn only in Mermaid | 385 / 121 | 561 / 0 |
| Documents carrying a section addressed to agents | 22, in four shapes | 0 |
| Legend sections | 20, one per document | 0; the notation is written once per layer, in three metamodels |
| Documents for the process catalogue | 1 level-1 map, 10 level-2 pages, 2 level-3 pages in a three-level folder | 1 process document and 2 activity documents in a flat folder |
| Words in the eleven pilot pages | about 31 000 | about 26 000 |
| Sentences over 30 words in the eleven pilot pages | 58 | 17, all of them lists of named references |
| Sentences about governance, the method or the page itself, in model pages | 73 on the validator's first pass | 0, and CI fails on the next one |
| Sections of a layer README beyond title, sentence, viewpoint, documents, metamodel and layer view | 7, across three layers | 0 |

A relationship that lives only in a picture is a fact no tool can hold, and a
legend drawn once per document is a second picture to keep in step with the
first. Both were removed rather than repaired.

## Work packages and deliverables

### WP1 — The parser reads a relationship row by its shape

- **Deliverables:** `model_graph.py` recognises a compact row by a bare
  identifier in its second cell, takes the label from the cell after the
  identifiers and the pending marker from the notes that follow it, and keeps
  catalogue cells out of an element's mentions so `trace` never lists the
  catalogue as a document naming it; a test that a four-column catalogue
  relates what no column relates. The BigView copy carries the same patch.
- **Outcome:** a table of four columns no longer fails the parse, and the
  word "pending" inside a relationship label no longer marks the row.

### WP2 — Relationships live in one catalogue

- **Deliverables:** `architecture-document-style` § Relationships are
  declared, never only drawn: one `architecture/relationships.md` per model,
  rows of `From | To | Relationship | Notes` grouped by the document that
  defines the source element, no decomposition and no self-loop, the pending
  marker opening the notes cell; a catalogue column still declares; a human
  document carries no `## Relationships` section and nothing addressed to
  agents. `references/archimate-relationships.md` § The relationship table
  rewritten around the two row forms; `assets/layers/relationships.md`
  emitted by `align-change-through-layers`; the scaffold's `AGENTS.md`.
- **Outcome:** an agent reads every relationship of a model in one file, and a
  person never meets a bare identifier in a table they read.

### WP3 — A reference names the type, the identifier and the name

- **Deliverables:** `document-style` § A reference names the type, the
  identifier and the name replaces § The name leads, and the identifier rides
  along: inside the defining document the bare identifier, anywhere else the
  type word, the identifier in backticks inside brackets, and the name, linked
  on first mention; a definition keeps the identifier first and a diagram node
  keeps `<glyph> <name> [ID]`. `document-style` § Write it plainly: eight
  rules for the documents a reader of the model opens, skills exempt.
- **Outcome:** a reference is validated by `check_model.py` and read aloud as
  a sentence, and the plainness rules have one home.

### WP4 — No legend; the notation is written once per layer

- **Deliverables:** `references/archimate-on-mermaid.md` § A diagram explains
  itself replaces § Every element document opens with "How to read this
  document": no element document opens with a legend, one sentence under a
  diagram says what a colour or a dashed border means, the `%% legend` marker
  stays for a notation diagram, and the layer README opens its diagrams with
  `## Metamodel` — the layer's element types with glyph, shape, colour,
  stereotype and prefix, connected as the layer's diagrams connect them —
  followed by `## Layer view`. The six layer templates ship their metamodel.
- **Outcome:** how to read every document of a layer is written in one place,
  and a legend cannot drift from the diagrams it explained.

### WP5 — Processes in one document, activities in a folder

- **Deliverables:** `process-and-capability-levels` references: levels 1 and 2
  stay in one document whatever their size, with a table of processes under
  each process group; level 3 is the activities of one process, one file per
  detailed process in a flat `activities/` folder named by identifier and
  name, opening with an inputs-and-outputs diagram before its flow; the level
  names follow APQC's five — category, process group, process, activity, task
  — with the category carrying no identifier; an agent covers tasks, never a
  whole activity, and a flow never colours an activity as the agent's.
- **Outcome:** a document per macro process, which restated the map and the
  table, is no longer written.

### WP6 — The validator asks for what the rules still say

- **Deliverables:** `check_model.py` no longer asks for a legend, nor for a
  view before a document's first table — that rule placed the legend first;
  it still asks a defining document for a diagram per section, before that
  section's tables, and for some view. The probe test staples the picture
  inside a section, which is what the remaining rule catches.
- **Outcome:** a document whose first section is a summary table passes
  without a picture it has nothing to draw.

### WP7 — Migration guide and version

- **Deliverables:** `docs/migrating.md` § Relationships live in one catalogue
  (0.5), naming what an existing project moves; `docs/method.md` § Where the
  model lives; `plugin.json`, the plugin manifest and the marketplace at
  0.5.0.
- **Outcome:** a project on 0.4 knows the six things it moves.

### WP8 — A page speaks about its subject

- **Deliverables:** `document-style` § Write it plainly, rule 7 sharpened —
  a page speaks about its subject, never about its own writing, its
  governance or the method — and § What the document contains naming
  governance and method as the same failure in another voice;
  `architecture-document-style` § The layer README, the one shape of a
  layer's front page: title, one sentence, the viewpoint line,
  `## Documents`, `## Metamodel`, `## Layer view`; the canvases reference
  gains § From canvas to ArchiMate and § Fit is a rule, moved out of the
  layer template, and `discover-business-model` § 3 gains the traceability
  check; the seven templates under `assets/layers/` cut to the shape, their
  author guidance kept as HTML comments the reader never sees; the scaffold
  gains `scripts/check_prose.py` and `scripts/prose-denylist.json`, the
  third validator and its word list, with a step in `checks.yml`, a row in
  the scripts README, the commands and conventions of `AGENTS.md` and the
  contributing template, three tests, and the language row of
  `establish-project` saying the list is translated with the documentation
  language.
- **Outcome:** the Requester of BigView stopped asking for the same cut at
  every review. The rule is written once, the validator names the sentence
  and the line, and a new project's layer READMEs start in the shape rather
  than being trimmed to it.

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| The method at 0.5, and BigView as the model that proved every rule first | Migrating the two models of the method itself, done as [scope 5](./5_the-two-models-move-to-05.md) |
| The catalogue template and the six metamodels in the layer templates | A check that a Mermaid edge is declared in the catalogue |
| The parser and validator patches, identical in the scaffold and in BigView | A check that names a malformed relationship row instead of dropping the table into "defined twice" |
| The plain-writing rules, written once in `document-style`, and the one of them a validator holds | Merging `document-style` into `architecture-document-style` |
| The layer README shape and the templates that ship it | A validator for the shape itself; `check_prose.py` catches the prose the retired sections carried, not a heading |

## Gap notes

- **The method's own two models moved in [scope 5](./5_the-two-models-move-to-05.md).**
  Until then their element documents kept `## Relationships` tables and
  legends, and nothing broke: the parser reads both the table beside a
  diagram and the catalogue.
- **Nothing checks that a drawn edge is declared.** BigView's catalogue was
  built by reading its Mermaid once, and 121 edges surfaced that no table
  held. Drift can return the same way until a check reads the diagrams.
- **A heading with an em dash gets two anchors.** GitHub keeps the double
  hyphen and the portal collapses it, so a link into a heading such as
  `**BPROC4 — Fabricar…**` resolves in one renderer and not the other. BigView
  links to the document instead of the heading; the definition-in-heading
  form the method fixes carries the issue.
- **A word list names vocabulary, not intent.** `check_prose.py` passes a
  sentence about governance written in the subject's own words and fails a
  subject whose own words are on the list, as BigView's "se consolidan" was
  in a measurement tool. The list is tuned per project and per language;
  the page is never exempted.
- **Two orders for one identifier, by design.** A diagram node keeps
  `<glyph> <name> [ID]`, a definition keeps the identifier first, and a
  reference in prose keeps the type word first. A reader meets three shapes
  and each says where it sits.

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| | | | |

<!--
  Nothing here has been granted. At Depth 1 the change meets Understanding;
  the row is written when it is granted, and not before. The Requester of
  BigView merged the two pull requests that proved the rules on that model;
  that approval belongs to BigView's scope document 10, not to this one.
-->
