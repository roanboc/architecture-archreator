# Project Scope — Make it readable

_[← Scope index](./README.md) · [Model home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** the `claude/graph-navigator-architecture-m2fr9j` branch in
[`archreator`](https://github.com/roanboc/archreator).
**Closes:** `GAP10`–`GAP13` — reaching `PLAT5` on the
[roadmap](../6_transition/1_target-state.md).

[Initiative 7](./7_walk-the-model.md) built a reader and proved the graph could
be drawn. It did not make the graph legible. A node is a six-pixel circle whose
identifier disappears once a hundred are on screen; the panel beside it shows a
catalogue row; there is no way to find anything without already knowing its
identifier; and every visit recomputes the same layout and forgets whatever the
reader did.

The Requester's direction is quoted in full on the
[target state](../6_transition/1_target-state.md); this delivers it.

## What a reader is actually doing

The gaps are one gap seen four times: **the page was built to display a model
and not to answer a question.** Someone opens it because they want to know what
something is, what it touches, or whether it exists at all — and every one of
those runs aground on a different missing thing.

| They want to | Today they | This delivers |
| ------------ | ---------- | ------------- |
| See what something is called | Read a six-pixel dot, or nothing at all past a hundred nodes | A box, sized to the name, carrying glyph, name and identifier |
| Understand what it means | Follow a link, leave the page, find the paragraph | The paragraph, in the panel, from the document that wrote it |
| Find it in the first place | Know the identifier already | Search that suggests what exists as they type |
| Show it to somebody | Rebuild the arrangement from memory each time | A saved view, and a link that reproduces it |

## The design

### 1. Boxes, and two ways to arrange them

An element becomes a rounded box sized to its name: layer colour as fill, the
type's glyph, the name, and the identifier beneath it. That is the notation
`architecture/README.md` already fixes for a diagram node, applied to a node
that is drawn rather than written.

**Two layouts, because two questions.** Force-directed answers "what clusters";
**layered** answers "what realizes what", which is the question an ArchiMate
model is organized around — one row per layer, motivation at the top,
technology at the bottom, edges crossing rows. A reader can drag any box
afterwards, and dragging is what makes a saved view worth saving.

### 2. A panel that carries the prose

`DOBJ4` gains **excerpts**: the paragraphs in the model that name an element,
with the document and heading they came from. A bolded lead-in definition —
which is how the method writes a goal or a principle — is exactly such a
paragraph, so the definition arrives with no special case.

The panel then shows what the element is, every catalogue column, what the
documents say, its relationships grouped by direction and clickable, and the
route back to each source document. **Nothing is summarized.** An excerpt is
the sentence the document contains, which is what makes it safe to read here
instead of there.

### 3. Search that says what exists

No language model runs in a static page, so "intelligent" has to mean
*structured and guiding* rather than clever:

- Free text matches identifier, name and type as you type.
- Facets narrow it: `type:`, `layer:`, `model:`, `status:`, `grounded:`.
- **The suggestions are the guidance.** Typing `type:` offers the element types
  this model actually has, with counts. A reader learns the vocabulary from the
  thing they are searching, which is the only vocabulary that will match.
- Results are a list; picking one focuses it and opens the panel.

### 4. Saved views, and the line they do not cross

A view is a name plus what the reader arranged: model, layer filters, focus and
depth, layout, hand-placed positions, camera. It is **a lens, never content**.

| Where a view lives | For | Written by |
| ------------------ | --- | ---------- |
| The browser's local storage | A reader's own working views | The page |
| An exported JSON file | Sending one to a colleague | The reader, deliberately |
| `architecture/views/*.json`, published with the portal | Views a team agrees on | A person, through a pull request |

**The page never writes to the model, and this is the boundary decision 3
reserved.** A curated view is a file somebody commits like any other change; the
navigator reads it and cannot create it. That is what keeps "it displays" true
when the next feature makes writing tempting.

### 5. The rest of what a reader needs

Deep links (`#e=<identifier>&depth=2`) so a view is shareable without saving
one. Back and forward through visited elements. A legend for colours and edge
styles. PNG export of what is on screen. Keyboard: `/` to search, `Escape` to
clear, arrows through results.

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 0_business-design | **Not used** — Depth 1 |
| 1_strategy | **No change.** No stakeholder, driver, goal or principle moves. `G5` — the model reaching people who never open the repository — is what this serves, and legibility is the difference between reaching them and being opened by them once |
| 2_business | **`BSVC8` restated** — interrogation gains finding, which is the question that precedes the other two. **`BOBJ10` added** — the saved view, a lens over the model that is never part of it |
| 3_information | **`DOBJ4` restated** — the projection carries the prose that defines an element, not only the row that lists it |
| 4_application | **`ACMP16` restated** — boxes, layouts, panel, search, views. **`ACMP7` and `ACMP8` restated** — the parse extracts prose blocks and the projection carries them |
| 5_technology | **No change.** Still one static page and files beside it |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — the subject is one application |
| Gate 1 — Strategy | Requester | 2026-08-27 | `PLAT5` and its gaps, in their own words, quoted on the [target state](../6_transition/1_target-state.md). See [decision 3](../decisions/3_the-navigator-earns-its-own-initiative.md) |
| Gate 2 — Business | Delegated ([decision 3](../decisions/3_the-navigator-earns-its-own-initiative.md)) | 2026-08-27 | `BOBJ10`, the restated `BSVC8` and `DOBJ4`. **Look first at:** `BOBJ10` being a business object at all. A saved view is the first thing the method has modeled that is deliberately *not* part of the model |
| Gate 3 — Solution design | Delegated ([decision 3](../decisions/3_the-navigator-earns-its-own-initiative.md)) | 2026-08-27 | § The design. **Look first at:** where a saved view is stored, because it is the only decision here that a reasonable person might make differently and the only one that is awkward to change later |

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | A drawable graph nobody can read: dots, a catalogue row, no search, no memory |
| **Target** (delivered) | `PLAT5`. Named boxes in two layouts, a panel carrying the documents' own prose and every relationship, guided search over everything the model contains, and views that survive the page being closed |

## Work packages and deliverables

### WP1 — The prose reaches the projection

- **Deliverables:** `ACMP7` extracts prose blocks naming an element, with
  document and heading; `ACMP8` writes an `excerpts` table; schema 3.
- **Outcome:** `GAP11`'s data exists.

### WP2 — Boxes, layouts, direct manipulation

- **Deliverables:** labelled boxes sized to content; force and layered
  layouts; drag; legend; PNG export.
- **Outcome:** `GAP10` closed.

### WP3 — The panel and the search

- **Deliverables:** the panel described above; the faceted omnibox with
  suggestions drawn from the model; history; deep links; keyboard.
- **Outcome:** `GAP11` and `GAP12` closed.

### WP4 — Saved views

- **Deliverables:** save, list, apply, rename, delete against local storage;
  export and import; published views read from `architecture/views/`.
- **Outcome:** `GAP13` closed.

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| Reading, arranging, finding and keeping a view | **Writing anything to the model.** Reserved by decision 3, and the boundary that makes the rest safe |
| Prose the documents already contain, shown verbatim | **Summarizing it.** A page that paraphrased a definition would be a second model with no way to tell it had drifted |
| Facets over what the projection carries | **Natural-language querying.** No language model runs in a static page, and pretending otherwise means a search that fails in ways a reader cannot predict |
| Views as files a person commits | **Views the page writes back to the repository.** Same boundary |

## Gap notes

- **A local-storage view is one browser's.** Clearing site data loses it, and
  another machine never had it. Export exists for exactly that, and the
  committed-view path is what a team should use for anything that matters — but
  a reader who saves a working view and loses it has been let down by a design
  decision, and it is recorded here rather than discovered.
- **Excerpts make the projection meaningfully larger.** Prose is bulkier than
  identifiers, and it is fetched by a browser. Capped per element and per
  excerpt, measured before shipping, and the first thing to trim if the file
  gets uncomfortable.
- **The layered layout assumes the layer a document sits in.** An element
  defined in a numbered folder lands in that row; one defined outside them —
  the roadmap's plateaus, the canvases — has no row and goes to a lane of its
  own rather than being forced into a layer it does not belong to.
