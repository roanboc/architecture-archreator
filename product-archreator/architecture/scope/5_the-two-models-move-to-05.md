# Project Scope — The two models move to 0.5

_[← Scope index](./README.md) · [Model home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** branch `claude/determined-lovelace-5ekizh`, in the pull
request that also carries [scope 4](./4_relationships-in-one-catalogue-and-plain-language.md).

Scope 4 took the method to 0.5 and named its own two models as the gap left
open: they still carried a relationship table beside every diagram, a legend
at the top of every element document, bare identifier lists in the tables a
person reads, layer READMEs that narrated which gate covered them, and
validators one version behind. This initiative moves both trees onto 0.5.
Every relationship is declared once per tree in `architecture/relationships.md`;
no element document carries a legend or a relationship table; a reference
names the type, the identifier and the name; the nine layer READMEs take the
one shape, with a metamodel inherited from the retired legends and a layer
view; the scripts are copied again from the scaffold, the third validator
included, with a word list tuned to models whose subject is the method itself;
and every page is written plainly. **One element is added**, the prose
validator, which scope 4 already counted as an impact on the application
layer. Nothing else is added, renamed or retired.

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 0_business-design | No change of content in the organization's canvases. The canvas-to-ArchiMate mapping leaves the business model canvas for the method's canvases reference, and the fit check becomes a table of checks and results with one row open |
| 1_strategy | No change of content in either tree. Columns that duplicated a diagram are gone; the `Source` column keeps provenance in the reference shape |
| 2_business | No change of content. The organization's process map keeps its two processes and the table of why depth stops at level 2 |
| 3_information | No change of content |
| 4_application | The component [`ACMP13`] The prose validator is added, realizing [`ASVC3`] Self-checking and aggregated by [`ACMP8`] The scaffold; the scaffold's file count reads thirteen wherever a row read eleven |
| 5_technology | No change of content; the note on what CI runs says three validators |

## What the evidence said

Measured on both trees, before and after:

| Measure | Before | After |
| ------- | ------ | ----- |
| Elements, organization and product | 143 and 76 | 143 and 77 |
| Rows in the relationship catalogues, organization and product | none | 188 and 115, every pair the tables, the columns and the diagrams held |
| Element documents opening with a legend | 12 | 0 |
| Relationship tables inside element documents | 6 | 0 |
| Sentences the prose validator flagged, with the list tuned to these models | 38 | 0 |
| Words of prose and tables, both trees, without diagrams and the catalogues | 13 893 | 12 713 |

## Work packages and deliverables

### WP1 — The scripts and the guides

- **Deliverables:** `scripts/model_graph.py` and `scripts/check_model.py`
  copied from the scaffold; `scripts/check_prose.py`, made to find every
  `architecture/` folder of a repository, and `scripts/prose-denylist.json`
  tuned to the subject: the method's own words stay off the list, and what
  is caught is narration about a page's approval, its construction or its
  layout; the third step in `.github/workflows/docs-check.yml`; `README.md`,
  `CLAUDE.md`, `CONTRIBUTING.md`, `scripts/README.md` and both `AGENTS.md`
  naming three validators, the catalogue, the reference shape, the subject
  test and the layer README shape.
- **Outcome:** the repository checks itself on 0.5 and says what its
  conventions are.

### WP2 — One catalogue per tree

- **Deliverables:** `org-archreator/architecture/relationships.md` and
  `product-archreator/architecture/relationships.md`, built by reading the
  relationship tables, the identifier columns and the content diagrams once:
  one row per pair, the direction and the label as the diagram drew them,
  the table's label where a table and a diagram differed, no decomposition
  and no self-loop, a cross-model target written as `ORG.<ID>`, and the notes
  the technology table carried moved to the Notes column.
- **Outcome:** an agent reads every relationship of a tree in one file, and
  the parser reads the same pairs it read before.

### WP3 — The twelve element documents

- **Deliverables:** the six documents of the organization and the six of the
  product with no legend and no relationship table; every column that
  duplicated the section's diagram removed, and every identifier cell that
  stays written as a readable reference; every sentence about the gate that
  covers a document reduced to its status line; asides between em dashes,
  sentences in bold and paragraphs about the document itself rewritten.
- **Outcome:** a person reads a page about the organization or the product
  and meets no bare identifier list and no sentence about how the page is
  approved.

### WP4 — The layer READMEs and the front doors

- **Deliverables:** nine layer READMEs in the one shape, title, one sentence,
  the viewpoint line, `## Documents`, `## Metamodel`, `## Layer view`, the
  metamodel inherited from the legends the documents retired; the two front
  doors without the narration of pending gates, each linking the tree's
  catalogue.
- **Outcome:** how to read every document of a layer is written in one
  place, and a front door says what is modeled and how far it is validated
  and nothing more.

### WP5 — This document

- **Deliverables:** this scope document and its row in the index; the gap
  note in scope 4 pointing here.
- **Outcome:** the method's own models are the worked reference an adopter
  reads, on the version the method ships.

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| Both trees on 0.5 | A check that a drawn edge is declared in the catalogue; the catalogues were built by reading the diagrams once |
| One added element, counted by scope 4 | Approving anything: Direction and Understanding stay pending for both trees |
| The word list tuned to a subject that is the method | The fit check's open row, which names no capability for a pain reliever or a gain creator |

## Gap notes

- **A four-column table whose first two cells are identifiers reads as a
  compact relationship row.** The old fit-check table declared
  `PAIN1 → PREL1` with the label `GAIN1`; the new one leads every row with
  prose. A project that writes a cross-reference table needs the same care.
- **Two names for one relationship, resolved by a rule.** Where a column and
  a diagram named the same pair differently, the diagram's label was kept
  (`serves` over `for`, `measures` over `for`); where a relationship table
  and a diagram differed, the table's (`influences` over `shapes`, `imports`
  over `imports the project's`). No relationship changed direction, and no
  pair was lost.
- **Six names shortened to the noun the diagrams already used.** `CH1`,
  `CH2`, `CH3` and `CR2` in the organization and `ASM4` and `ASM5` in the
  product had no bold name, so the parser read the whole cell as the name,
  aside included; the bold now marks the noun and the rest of the cell
  describes it. No diagram label changed.
- **The word list is the subject's.** On these two models the method's words
  are the business: skill, validator, gate, Requester, scaffold. The list
  keeps only the narration a page makes about itself, and a project whose
  subject is anything else keeps the scaffold's list.

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| | | | |

<!--
  Nothing here has been granted. The initiative changes one claim of the
  product model, the added component, which meets Understanding; the row is
  written when it is granted, and not before. Both trees stay `◐`.
-->
