# Project Scope — Walk the model

_[← Scope index](./README.md) · [Model home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** the `claude/graph-navigator-architecture-m2fr9j` branch in
[`archreator`](https://github.com/roanboc/archreator), and the model changes
this document holds the gates for.
**Closes:** `GAP5`, `GAP6` — reaching `PLAT2` on the
[roadmap](../roadmap/1_target-state.md).

[Initiative 6](./6_declare-the-relationships-and-let-the-graph-be-walked.md)
made the graph real: 619 stated relationships across three trees, where 306
were mostly a byproduct of who felt like drawing a diagram. Nothing renders it.
`ACMP14` prints text to a terminal, and the reader `G5` was written for — the
one who will never open a repository — has the portal, which renders documents
and draws no graph.

This initiative gives the graph a reader. One static page, no server, no
deployed database.

## The two gaps

**`GAP5` — nothing renders the graph.** The obvious half.

**`GAP6` — traversal would be written twice.** The half that decides the
design. `ACMP14` walks `model.json` in Python; a web reader would walk the
same graph in JavaScript. Two implementations of one traversal is the drift
`ACMP7` exists to prevent, one level up — and the second one would be the one
nobody tests, because it runs in a browser.

So the page does not reimplement the walk. **It runs the same SQL.**
`stack-selection` settled this before there was anything to settle it for: the
projection "writes SQLite, as a `nodes`/`edges` pair traversed with recursive
CTEs. At the scale a model reaches, SQLite *is* the graph database." `ACMP14`
moves onto that statement, and the page executes the identical query text
against the identical file.

## What the page does

| Capability | How |
| ---------- | --- |
| **Show the graph** | Every element as a node, coloured by its layer using the palette `architecture/README.md` already fixes, shaped by its group |
| **Filter by layer** | Motivation, Strategy, Business, Information, Application, Technology, Implementation & Migration, and the two canvases — the groups `element-prefixes.json` already defines, so the filter is generated rather than written |
| **Bring everything related to a node** | Select an element, walk outward N hops, and show only what was reached. This is `trace` with a viewport, and it is the same recursive CTE |
| **Tell a stated relationship from an inferred one** | `origin` is on every edge: a catalogue column, a relationship table, or the decomposition an identifier carries. Structure renders differently from assertion |
| **Tell a live relationship from a planned one** | `pending` is on every edge, dashed where true — the one place a dashed line is still the right answer, because here it is a rendering |
| **Route back to the source** | Every node names the document that defines it and links to it, the same rule that puts a source path on every portal page. **A rendering nobody can trace back to its source is how a published copy quietly becomes a second model** |

## Three decisions worth stating

**The page reads `model.db`, not `model.json`.** The Requester asked for it and
the reason holds up: SQL is what makes the traversal shared rather than
duplicated. JSON would have meant a JavaScript walk beside the Python one,
which is `GAP6` closed on paper and open in fact.

**sql.js is fetched at build time, never committed.** Reading SQLite in a
browser needs a WASM build — 709 KB of it. Three ways to get it there, and
only one is honest:

| Option | Why not (or why) |
| ------ | ---------------- |
| **Vendor it into the scaffold** | Every project the method emits would carry a 660 KB binary in git, in a repository that is otherwise Markdown and standard-library Python. A binary nobody can review is a strange thing for a method about reviewable models to ship |
| **Fetch it from a CDN at page load** | The published page acquires a runtime dependency on a third party. It breaks when they break, and it is a supply-chain surface on a page whose whole appeal is that it has no infrastructure |
| **Fetch it at build time, pinned** | `build_docs.py` already needs the network — it fetches MkDocs through `uv`. One more pinned fetch, verified against a recorded SHA-256, into the gitignored site. The published output is self-contained; the repository stays text |

The build **degrades rather than fails** when the fetch cannot happen: the
portal still builds, and the navigator page says what is missing and how to
get it. A model that will not publish because a graph viewer could not
download a library is a bad trade.

**The projection is copied into the published site.** The page has to read it
from somewhere, and it is the same `model.db` `build_model.py` already writes.
This puts a project's projection at a stable path under its portal, which is
most of what `GAP7` asks for — [initiative 8](../roadmap/2_sequence.md) is what
turns that path into a contract other projects may depend on, with an index
and a documented shape. Here it is an implementation detail of the page.

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 0_business-design | **Not used** — Depth 1, one application |
| 1_strategy | **No change.** No stakeholder, driver, goal or principle is added or modified. It serves `G5` — the model reaching people who never open the repository — which the portal and the PDF already realize and this extends to the graph. `CAP4` already covers proving the model consistent; a visual reader is a new surface on an existing capability, not a new one |
| 2_business | **`BSVC8` restated** in [2_business-services.md](../2_business/2_business-services.md): interrogation stops requiring a terminal. The two questions are unchanged; who can ask them is not |
| 3_information | **`DOBJ4` restated** in [1_data-objects.md](../3_information/1_data-objects.md): the projection gains a second reader that is a browser, and `model.db` becomes the read format rather than a second output nothing opened |
| 4_application | **`ACMP16` added** — the graph navigator. **`ASVC10` and `ACMP14` restated** — the query tool reads `model.db` and shares its traversal with the page. See § Solution design |
| 5_technology | **`TSVC5` restated** — the documentation toolchain gains one pinned build-time asset. No new node, no new host, nothing to operate |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — the subject is one application |
| Gate 1 — Strategy | — | — | **N/A for this initiative** — no strategy element moves. The direction was approved on the [roadmap](../roadmap/README.md) at Gate 1, 2026-08-27 |
| Gate 2 — Business | Delegated ([decision 2](../decisions/2_the-requester-delegates-the-remaining-gates.md)) | 2026-08-27 | The restated `BSVC8` and `DOBJ4`. **Look first at:** whether "interrogation without a terminal" is a promise the method wants to make, because it is the one thing here that widens what `BSVC8` owes |
| Gate 3 — Solution design | Delegated ([decision 2](../decisions/2_the-requester-delegates-the-remaining-gates.md)) | 2026-08-27 | `ACMP16`, the restated `ACMP14`, and § Solution design. **Look first at:** the build-time fetch of sql.js — it is the only new dependency, and the only decision here that a reasonable person might make differently |

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | 619 stated relationships and nothing that draws them. `ACMP14` answers two questions as text, to whoever has a terminal and knows the element identifier they want |
| **Target** (delivered) | `PLAT2`. One static page, filters by layer and element type, expansion outward from any node, every node routed back to its defining document. The traversal is one recursive CTE that the page and `ACMP14` both run |

## Work packages and deliverables

### WP1 — The traversal becomes one query

- **Deliverables:** `ACMP14` reads `.model/model.db`; the neighbourhood walk
  becomes a recursive CTE held in one place and executed by both readers.
- **Outcome:** `GAP6` closed before the second reader exists, rather than
  after it has already drifted.

### WP2 — The navigator

- **Deliverables:** `scaffold/navigator/` — one HTML page, its stylesheet and
  its script, reading `model.db` through sql.js. Layer and type filters
  generated from `element-prefixes.json`; neighbourhood expansion from any
  node; `origin` and `pending` rendered distinctly; every node linking to the
  document that defines it.
- **Outcome:** `GAP5` closed.

### WP3 — It reaches the reader

- **Deliverables:** `build_docs.py` builds the projection, copies it and the
  navigator into `.docs/site/`, and fetches sql.js against a pinned SHA-256 —
  reporting and continuing when it cannot.
- **Outcome:** the page is part of what a project publishes, not a file
  somebody has to open locally.

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| One project's graph, drawn, filtered and walked | **More than one project at a time.** `GAP7`, `GAP8`, initiative 8. The page reads one database; the switcher and the union come with the index |
| The traversal shared between the page and `ACMP14` | **Cross-project traversal.** `GAP9`, initiative 9. A walk still stops at the tree boundary, and says so |
| `origin` and `pending` rendered | **Editing anything.** The page is a reader. The Markdown is the source of truth and a graph that could write to it would be a second one |
| Layer and element-type filters | **Search by name, saved views, export.** Worth having, none of them load-bearing, and each is cheaper to add once somebody has used the page and said which they missed |

## Gap notes

- **The page draws a whole tree, and a whole tree is a lot.** 184 elements and
  326 edges is legible when filtered and a hairball when not. The filters are
  therefore not a convenience: the default view is a single layer, and the
  reader opens outward from there. If a model arrives that is illegible even
  filtered, the answer is a better default rather than a bigger canvas.
- **`build_docs.py` gains a network fetch it can fail.** It already needs the
  network for MkDocs, so this is not a new class of dependency — but it is a
  new way for a build to be partially successful, and the page has to say so
  itself rather than rendering blank.
