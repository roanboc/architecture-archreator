# Project Scope — Answer one question

_[← Scope index](./README.md) · [Model home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** the `claude/graph-navigator-architecture-m2fr9j` branch in
[`archreator`](https://github.com/roanboc/archreator).
**Closes:** `GAP14`–`GAP16` — reaching `PLAT6` on the
[roadmap](../6_transition/1_target-state.md).
**Retires:** `PLAT2` and `PLAT5`, and deletes the graph navigator — see
[decision 4](../decisions/4_the-graph-portal-is-retired.md).

A reader with a question about one domain, one function or one use case has two
options today: open all 33 documents and hold the relevant rows in their head,
or open a graph and reconstruct the question by clicking. The Requester named
the third:

> the best thing I could get is a temporary document created in-time with the
> architectural elements relevant to me, no need to navigate graphs and explore
> blindly.

## The design

### 1. A scope is named, not browsed

    python3 scripts/build_brief.py --element BSVC1 --depth 2
    python3 scripts/build_brief.py --domain SALES
    python3 scripts/build_brief.py --type "Application Component" --layer Business

A brief is generated for a **scope**: anchors, how far to walk from them, and
optional filters. The selector vocabulary is the one
[initiative 12](./12_make-it-readable.md) built for search — `type`, `layer`,
`domain`, `model`, `status` — kept because it was already the right way to say
which part of a model you mean.

**The walk is `neighbourhood.sql`**, unchanged. It answered "what would a
change to this touch" for the terminal and for the page; it answers "what is
relevant to this" for a brief. One traversal, three readers, and only one of
those readers is left.

### 2. The multi-layer view leads, and the others follow it

The Requester was specific about which diagram matters:

> especially the multi layer dependencies per domain/function/scope as this
> where we need more understanding (business and info to application and tech
> layers)

So the brief opens with a **layered dependency view**: one subgraph per
ArchiMate layer in assessment order, only the elements in scope, and every
relationship that crosses a layer drawn between them. It is the chain a reader
came for — a business service, the information it uses, the component that
realizes it, the node it runs on — and it exists in no document today because
each document diagrams its own layer.

Three views, in this order, each omitted when the scope has nothing for it:

| View | Answers | Shape |
| ---- | ------- | ----- |
| **Layered dependencies** | How does this reach from business down to technology? | Subgraph per layer, cross-layer edges emphasised, within-layer edges thin |
| **Motivation** | Why does this exist? | The drivers, goals and capabilities the scope serves |
| **Neighbourhood** | What sits immediately around each anchor? | One per anchor, when there is more than one |

**Generating a diagram is correct now, and was not before.** Until
[initiative 8](./8_declare-the-relationships-and-let-the-graph-be-walked.md) a
generated diagram would have competed with an authored one for the same fact.
Relationships are declared and diagrams are renderings, so generating one is
the operation the notation already describes rather than a second source.

**A generated view never replaces an authored one.** The layer documents keep
their own diagrams: those are curated selections, and the notation is explicit
that "a selection that looks complete is worse than several honest parts". A
brief adds a view nobody drew; it does not overwrite the ones somebody did.

### 3. The brief carries what the documents say

Elements arrive with their catalogue row and with the paragraphs the model
already writes about them — the excerpts initiative 12 added, **verbatim**.
Nothing is summarized: a paraphrase in a generated document is a claim nobody
approved, and there would be no way to tell it had drifted.

It also says **what it left out**: how many elements the scope excluded, and
which neighbouring ones were one hop beyond the edge. A brief that looks
complete is the failure mode; one that names its own boundary is a tool.

### 4. Every derived document says it is disposable

`.docs/` holds the staged Markdown, the portal, the PDF and now the briefs.
None of it is committed and all of it is regenerated. Only the brief and the
PDF are handed to people, and neither says what it is.

Both gain a header: what generated it, from which revision, on which date, and
one sentence — **this is a disposable snapshot, the repository is the model.**
A generated document that does not announce itself gets committed, emailed and
quoted eight months later, which is the second source of truth this method
exists to prevent.

### 5. A transcript is summarized into facts

`architecture/reference/` holds what a model was built from, and a meeting
transcript is the most common thing in it. The rule it has says how to name and
index one; it says nothing about what may be written down from one.

**A summary of a transcript records facts, never judgements.** Decisions taken,
constraints stated, numbers quoted, systems named, dates and owners. Not who
seemed frustrated, not who is difficult to work with, not what somebody's tone
implied. Those are readings of people, they are usually wrong, and a repository
keeps them for as long as it exists — long after everyone has forgotten the
meeting and the reason the reading seemed fair.

The raw transcript, where one is kept at all, stays unpublished as it already
does. What changes is that the method now says what a summary of one may
contain.

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 0_business-design | **Not used** — Depth 1 |
| 1_strategy | **No change.** No stakeholder, driver, goal or principle moves. `G1` — an agent reads the business context natively — is what a brief serves and what the navigator could not; the goal already exists |
| 2_business | **`BSVC7` restated** — publication gains a third rendering, the brief. **`BOBJ10` restated** — the saved view becomes the generated brief: still a lens, still never model content, now Markdown instead of a canvas. **`RULE` on reference material** recorded in [5_domain-context-and-rules.md](../2_business/5_domain-context-and-rules.md): a transcript summary carries facts, not judgements |
| 3_information | **`DOBJ4` unchanged** — the projection already carries everything a brief needs. That is the whole reason this initiative is small |
| 4_application | **`ACMP16` retired and deleted** — the navigator. **`ACMP17` added** — the brief generator. **`ACMP13` restated** — the PDF says it is disposable |
| 5_technology | **`TSVC5` restated** — the toolchain loses sql.js. Nothing is added |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — the subject is one application |
| Gate 1 — Strategy | Requester | 2026-08-27 | `PLAT6`, and the abandonment of `PLAT2` and `PLAT5`, in their own words on the [target state](../6_transition/1_target-state.md). See [decision 4](../decisions/4_the-graph-portal-is-retired.md) |
| Gate 2 — Business | Delegated ([decision 4](../decisions/4_the-graph-portal-is-retired.md)) | 2026-08-27 | The restated `BSVC7` and `BOBJ10`, and the transcript rule. **Look first at:** the transcript rule, because it is the only change here that constrains what a person may write rather than what a script may do |
| Gate 3 — Solution design | Delegated ([decision 4](../decisions/4_the-graph-portal-is-retired.md)) | 2026-08-27 | § The design. **Look first at:** the layered view's selection rule — which cross-layer edges it draws and which it drops — because that is what decides whether the headline diagram is legible or is the hairball this initiative exists to escape |

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | 33 documents, 368 elements, and two ways to understand one topic: read all of it, or click through a graph. A graph navigator that works and answers the wrong question |
| **Target** (delivered) | `PLAT6`. One command names a scope and produces a Markdown brief: a multi-layer dependency view, the elements that matter with what the documents say about them, what was left out, and a header saying it is disposable. The navigator is gone |

## Work packages and deliverables

### WP1 — Retire the graph portal

- **Deliverables:** `scaffold/navigator/` deleted; `stage_navigator`, the
  pinned sql.js fetch and its link-check exemption removed from the build;
  `architecture/views/` removed from the scaffold; `ACMP16` retired in the
  model with the decision that retired it.
- **Outcome:** one reader, not two. About 1,470 lines and a 709 KB dependency
  leave; the parse, the projection and the traversal stay.

### WP2 — The brief

- **Deliverables:** `scripts/build_brief.py` — scope selection, the three
  views, element sections carrying catalogue rows and excerpts, the boundary
  report, and the disposable header. Output to `.docs/briefs/`.
- **Outcome:** `GAP14` and `GAP15` closed.

### WP3 — Derived documents say so

- **Deliverables:** the disposable header on the brief and on the PDF;
  `.gitignore` and the scripts README stating it once.
- **Outcome:** `GAP16` closed.

### WP4 — What a transcript summary may contain

- **Deliverables:** the rule in `architecture-document-style` § Reference
  documents, and in the discovery skills that gather transcripts; the
  corresponding rule element in this model's business layer.
- **Outcome:** the method says what may be written down about a meeting, and
  what may not.

### WP5 — Folders that are not the architecture

- **Deliverables:** `roadmap/` becomes `6_transition/`, numbered because it
  holds Implementation & Migration elements and is parsed like any other layer;
  [decision 5](../decisions/5_folders-that-are-not-the-architecture.md) records
  that a merged document's *claims* are immutable while its *links* may be
  repaired when a file moves, which is what made the rename possible at all;
  `GAP17` carries the larger move.
- **Outcome:** 22 plateau and gap elements stop being unnumbered. The
  narrative folders are named as the problem they are, and moving them is a
  separate initiative rather than a rename smuggled into this one.

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| A brief for a scope in one model | **A brief spanning federated models.** The index and the cross-model grammar exist; fetching another repository's projection from a command-line tool is a network dependency worth adding when somebody actually wants it |
| Three generated views | **Replacing authored diagrams.** A curated selection is an editorial act; generating over it deletes the author's judgement |
| The selector on a command line | **Committed topic files.** A saved scope that regenerates a brief is the useful half of what saved views were. It is one file format away and it is not needed to prove the idea |
| `roadmap/` numbered as the sixth layer | **Moving `scope/`, `decisions/` and `reference/` out of `architecture/`.** `GAP17`. It touches five folders in every tree, every skill that writes into one, and the parse constant that names them |
| Facts-not-judgements as a written rule | **Enforcing it.** No validator can tell a fact from a judgement. This is a rule a person follows and a reviewer checks |

## Gap notes

- **The layered view is the whole risk.** Every other part of a brief is
  assembling data that already exists. That diagram has to choose which
  cross-layer edges to draw, and a scope of forty elements with a hundred
  relationships between them is the hairball this initiative was created to
  escape. If it cannot be made legible, the honest answer is a narrower default
  scope rather than a bigger diagram.
- **A brief is only as good as the prose.** 183 of 368 elements carry an
  excerpt today; the other half arrive as a catalogue row and nothing more. The
  brief will make that visible in a way no other reader has, which is useful
  and will look like a defect in the tool.
- **Nothing stops somebody committing a brief.** `.gitignore` covers `.docs/`,
  and a person who copies one out of it can put it anywhere. The header is the
  only real defence, which is why it is a work package rather than a footnote.
