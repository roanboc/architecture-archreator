# Project Scope — Federate the graph

_[← Scope index](./README.md) · [Model home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** the `claude/graph-navigator-architecture-m2fr9j` branch in
[`archreator`](https://github.com/roanboc/archreator), and the model changes
this document holds the gates for.
**Closes:** `GAP7`, `GAP8` — reaching `PLAT3` on the
[roadmap](../6_transition/1_target-state.md).

[Initiative 7](./7_walk-the-model.md) gave one model a reader. An organization
does not have one model: `model-domains` caps a domain tree at three levels and
says that past it you want "separate repositories federated by contract", and
this repository already holds three trees for one small organization. A reader
that can only ever see one of them at a time answers "what would this change
touch" with half an answer and no warning that it is half.

**Nobody owns the union.** A tree that held every other tree's elements would
restate what those trees own, which the tier rule in
`architecture-document-style` forbids in as many words, and would need approval
rights over elements it did not own. What is centralized is **a list of URLs**.
The graph is a view, computed when somebody opens it.

## The two gaps

**`GAP7` — the projection is never published.** `DOBJ4` is gitignored and
local. `stack-selection` § A persisted projection needs one of four triggers
names this case exactly: "Domains live in separate repositories — federation
needs an interchange format; an agent cannot `grep` a repository it has not
cloned." Initiative 7 already writes `model.db` into the built site because the
navigator needs it. That made a file appear at a path; it did not make it a
promise.

**`GAP8` — no index names the projects in a federation.** The fact exists in
prose today: `org-archreator`'s component catalogue carries a **Modeled in**
column pointing at the tree that holds each component's detail. Nothing
machine-readable carries it, so nothing can follow it.

## The design

### 1. The projection becomes a contract

Two files at a documented path under a project's published portal:

| Path | What it is |
| ---- | ---------- |
| `navigator/model.json` | The projection, and the interchange format. Carries a `schema` version and the commit it was built from |
| `navigator/model.db` | The same thing as SQLite, for a reader that wants to query rather than parse |

The **`schema` field is the whole point of calling it a contract.** A consumer
fetching another project's projection is reading a file it does not control,
built by a version of the method it may not have. A number it can compare beats
a shape it has to guess at, and a consumer that finds a schema it does not know
says so instead of misreading the file.

### 2. The index is authored, and it is Markdown

**The index is not derived, so it is not JSON.** Every other machine-readable
file in this method is regenerated from the Markdown and gitignored, because a
derived store that falls behind its source is the drift `P1` exists to prevent.
A federation index is the opposite kind of thing: somebody decides which
projects are in the federation and writes it down. That makes it model content
— reviewed, gated, and validated like everything else.

So it is a table in `architecture/federation.md` of the **topmost tree**: the
organization, or the parent business function where no organization is modeled.
`build_docs.py` derives `navigator/federation.json` from it, regenerated on
every build and never committed, exactly like the projection it points at.

**Who owns it follows from what it is.** "Which projects exist and where their
models live" is an enterprise-layer fact. `org-archreator` already carries it
in prose; this gives it a machine-readable home in the same tree, and no tree
below it gains a fact about its siblings.

### 3. The navigator reads the index

Where a `federation.json` sits beside the navigator, the page fetches every
projection it names and loads them into one database in the browser. Where
there is none, it reads its own `model.db` and behaves exactly as it does
today. A project that is not in a federation should not have to know what one
is.

**A federated walk still stops at the project boundary, and the page says so.**
Elements are scoped per project, and no relationship crosses a project until
[initiative 9](../6_transition/2_sequence.md) gives one a way to be written. Showing
several graphs at once is worth having on its own — it is how a reader sees
that `product-archreator` and `product-archreator/site` are different sizes of
thing — but it is not yet one graph, and a page that implied otherwise would be
lying about the most important thing on it.

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 0_business-design | **Not used** — Depth 1 |
| 1_strategy | **No change.** No stakeholder, driver, goal or principle moves. `G5` already commits the method to reaching readers outside the repository; this widens what those readers can reach, not why |
| 2_business | **`BOBJ8` added** — the federation index, in [4_business-objects.md](../2_business/4_business-objects.md). It is a document somebody authors and a gate approves, which is what makes it a business object rather than a configuration file |
| 3_information | **`DOBJ4` restated** — the projection gains a published form with a schema version, which is what a second project reads. **`DOBJ6` added** — the derived federation manifest |
| 4_application | **`ASVC9` and `ACMP12` restated** — publication now includes the projection and the derived manifest. **`ACMP16` restated** — the navigator reads an index when there is one |
| 5_technology | **No change.** Static files on the hosting `TSVC3` already provides. Federation across repositories is one public URL fetching another |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — the subject is one application |
| Gate 1 — Strategy | — | — | **N/A for this initiative** — the direction was approved on the [roadmap](../6_transition/README.md) at Gate 1, 2026-08-27 |
| Gate 2 — Business | Delegated ([decision 2](../decisions/2_the-requester-delegates-the-remaining-gates.md)) | 2026-08-27 | `BOBJ8`, the restated `DOBJ4`, and `DOBJ6`. **Look first at:** the index being authored Markdown rather than generated. It is the call the rest of the design rests on, and the one a reasonable person might make differently |
| Gate 3 — Solution design | Delegated ([decision 2](../decisions/2_the-requester-delegates-the-remaining-gates.md)) | 2026-08-27 | § The design and the work packages below. **Look first at:** what happens when a federated projection cannot be fetched, because that is the failure a reader will actually meet |

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | Each project's projection is a local file the navigator happens to read. Which projects exist is prose in one tree's component catalogue |
| **Target** (delivered) | `PLAT3`. Every published project offers its projection at a documented path with a schema version. The topmost tree names the federation in a document a gate approves. The navigator reads that index and shows what it names, saying plainly what it could not reach |

## Work packages and deliverables

### WP1 — The projection says what it is

- **Deliverables:** `model.json` carries `schema` and the commit it was built
  from; both formats are published under `navigator/`; the path and the shape
  are documented where an adopter will find them.
- **Outcome:** `GAP7` closed. A second project has something it can depend on
  rather than something it can only hope stays put.

### WP2 — The index

- **Deliverables:** `architecture/federation.md` in the topmost tree, filled in
  for this repository; `build_docs.py` derives `navigator/federation.json` from
  it; `establish-project` and the scaffold carry an empty one with the rule.
- **Outcome:** `GAP8` closed.

### WP3 — The navigator federates

- **Deliverables:** the page loads every projection the index names into one
  in-browser database, facets by project, and reports each one it could not
  fetch by name and reason. No index, no change in behavior.
- **Outcome:** one reader for a federation, and an honest one.

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| Public projects, fetched over HTTPS | **Private repositories.** A page cannot authenticate to a private Pages site, and building a credential store into a static page would trade away the one property that makes it worth having |
| Several projects visible at once, faceted | **One graph across projects.** `GAP9`, initiative 9. Nothing yet lets a relationship cross a boundary, and the page says so rather than implying otherwise |
| A schema version on the interchange format | **Migrating an old schema.** A consumer that meets a version it does not know reports it. Translating between versions is work for the first time it actually happens |
| An index in the topmost tree | **Discovering projects automatically.** Somebody decides what is in a federation. A crawler would make that decision silently and get it wrong at the worst moment |

## Gap notes

- **Cross-origin fetching is the assumption this rests on.** GitHub Pages
  serves assets with a permissive CORS header today, which is what lets one
  published portal read another's projection. A host that does not is a host
  where federation degrades to one project — handled, reported, and not
  designed around, because designing around it means a build step that vendors
  other people's models into yours, which is a copy that goes stale.
- **The index will drift from reality, and only a person can notice.** A URL in
  it can 404 because a project moved, was renamed, or stopped publishing. The
  page reports what it could not reach; nothing fails a build over it, because
  the alternative is a validator that makes network calls on every pull
  request.
