# Project Scope — Say what a document is worth, and keep what it came from

_[← Scope index](./README.md) · [Model home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** the `claude/archreator-next-functionality-ta1tyx` branch in [`archreator`](https://github.com/roanboc/archreator), and the model changes this document holds the gate for.

Scope document 3 gave the method a way to sweep an estate into the four layers
below the strategy. It also gave it a way to fill those layers fast, from
material of wildly varying reliability, and left no way to tell the results
apart afterwards. A capability read off a licence file, a process someone
described once in a workshop, and a service the Requester approved at a gate
all arrive as the same table, with the same identifiers, in the same document.

Two things follow from that, and both are in this initiative.

**A document now says how far it has been validated.** One glyph in the
preamble — `○` not started, `◐` a draft catalogue, `●` validated — with the
gate and the date beside it. `check_model.py` fails a document that defines an
element and declares nothing.

**And the material a model was built from is kept.** `architecture/reference/`
holds transcripts, decks and documents exactly as they were provided, under a
dated name, indexed. It is not the model, the validators do not read it, and
the portal does not publish it.

## Why a draft catalogue is not an architecture draft

The distinction is the whole initiative, and it is a naming problem before it
is a tooling one.

An **architecture draft** is a proposal about how something should be
structured. A reader of one knows to argue with the structure. A **draft
catalogue** is a list of things somebody said exist, written down so that they
can be checked — the structure is not the claim, the existence of the items is,
and nobody has verified it.

Calling the second one a draft architecture invites exactly the wrong reading.
The Requester critiques the shape of something whose contents were never
confirmed; the agent, finding no warning on the page, builds on a system that
was mentioned once. Naming it a catalogue, and marking it, makes the honest
question — *is this list right?* — the first one anybody asks.

## The gates were granted on the request, not on this document

As with scope document 3, the Requester stated the requirement and directed
implementation in the same message. This document was written during the work,
and says so rather than being backdated.

## EA alignment (assessed top-down before implementing)

| Layer         | Impact                                              |
| ------------- | ---------------------------------------------------- |
| 0_business-design | Not used — the subject is a product, at Depth 1 |
| 1_strategy    | `ASM7` and `ASM8` added — an unapproved element looks like an approved one, and a claim outlives the conversation it came from. `G7` added, measured by the new `OUT4`. `CAP1` and `CAP4` widened |
| 2_business    | `BSVC3` covers the status check; `BSVC2` covers filing what a discovery was given |
| 3_information | `DOBJ5` added for provided source documents; `DOBJ4` now carries each element's declared status |
| 4_application | `ASVC4` requires a declared status; `ASVC9` publishes no source document |
| 5_technology  | No change. A glyph in a preamble runs on the node the validators already run on |

Every element-defining document in all three trees also gained the status line
the change requires. That is not a modeling change and has no row above: it is
this repository complying with a rule it now publishes, and a method that ships
a rule its own models do not follow is asking on credit.

## Approvals

| Gate                     | Approved by | Date         | What was approved                          |
| ------------------------ | ----------- | ------------ | ------------------------------------------- |
| Gate 0 — Business model  | — | — | N/A — the subject is a product, not an organization |
| Gate 1 — Strategy        | Requester | 2026-08-24 | The requirement as stated: a reference folder for provided documents, with a dating rule, and a guarantee that anything placed in the other layers is identifiable as a draft catalogue of elements with notes rather than as architecture |
| Gate 2 — Business        | Requester | 2026-08-24 | The same message, which directed the implementation of both halves |
| Gate 3 — Solution design | — | 2026-08-24 | N/A — not requested. The Requester described the outcome and left the mechanism open |

## Plateaus

| Plateau                | State                     |
| ----------------------- | ------------------------- |
| **Baseline** (before)  | A catalogue swept from a licence file and a layer approved at a gate were indistinguishable on the page. Source material was read and discarded, so a claim's provenance survived only as long as the conversation |
| **Target** (delivered) | Every element-defining document declares its standing, and CI fails one that does not. Provided material is kept, dated and indexed beside the model, unread by the validators and unpublished by the portal |

## Work packages and deliverables

### WP1 — The status convention

- **Deliverables:** `architecture-document-style` § Document status; the status check in `scaffold/scripts/check_model.py`, with `STATUS_GLYPHS`, `preamble()` and `status_of()` in `model_graph.py`; the status carried through `build_model.py` onto every node and reported by `query_model.py coverage`; § Document status in `scaffold/architecture/README.md`; the gate-promotion rules in `align-change-through-layers`, `write-scope-document`, `discover-business-model`, `discover-strategy`, `discover-current-landscape`, `plan-the-transition` and `restate-current-state`
- **Outcome:** a reader, and an agent, can tell in one glyph whether anybody has confirmed what they are about to rely on

### WP2 — The reference folder

- **Deliverables:** `scaffold/architecture/reference/README.md`; `architecture-document-style` § Reference documents; `reference` added to `NARRATIVE` in `model_graph.py` and to `NOT_PUBLISHED` in `build_docs.py`; `unpublished_links()` in `build_docs.py`, which reports staged links pointing at files the portal drops; the filing step in `discover-current-landscape`
- **Outcome:** a claim in the model can be taken back to the document it came from, and the document is still there

### WP3 — Comply with both, everywhere

- **Deliverables:** a status line on all 32 element-defining documents across `org-archreator`, `product-archreator` and `product-archreator/site`; the model repair named in the alignment table; this scope document
- **Outcome:** the method's own models pass the check the method now ships

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| The status convention, its check, and its use across three trees | Checking that a status line is *true* — that a gate named actually granted it |
| The reference folder, its naming, its index | A reference folder in this repository, which has been given no source documents |
| Excluding source material from the portal, and reporting the links that costs | Any handling of confidential material beyond a warning in the folder's README |
| `Source` and `Notes` columns on draft catalogues | A check that a draft catalogue actually carries them |

## Gap notes

- **The check asks whether a declaration was made, never whether it is true.**
  A document can say `● Validated at Gate 2, 2026-08-24` with no such gate in
  any Approvals table, and nothing will object. Closing that means parsing
  scope documents, which are narrative and immutable and deliberately unread
  by the validators — so it is not a small change, and it may not be a wanted
  one. What makes the weak check worth having is that the failure it prevents
  is silence, not lying.
- **Nothing checks that a `◐` document carries `Source` and `Notes`.** Those
  columns are named in prose, in a language the projection does not read. The
  same reasoning that keeps the grounding rule out of CI applies.
- **`Notes` emptying at the gate is a discipline, not a mechanism.** A note
  that survives its gate should have become a fact, a logged question or
  nothing; whether it did is a review step.
- **The three trees here were marked from their own Approvals tables, and one
  case did not fit.** Layers 3 to 5 in all three were never taken to a gate —
  Gate 3 was declined at Gate 2 and they were routed to pull-request review.
  Marking them `◐` would have been wrong, since they are grounded descriptions
  of code that exists; marking them `●` without saying why would have implied
  a gate that never happened. The rule was widened during the work so that a
  `●` earned outside a gate must name the recorded decision that routed it —
  a narrow escape, and one that needs a real record to point at.
- **`ea_bigview` is again untouched**, for the reasons in scope document 3.
  Adopting the status convention there means marking every document in a live
  Spanish-language model against gates that are still Pending, which is that
  project's initiative and a useful first test of the convention: it is the one
  model whose gates have not been granted, so almost everything in it is `◐`.

## Open questions

- None. The Requester stated the requirement and directed the implementation,
  and the one interpretation adopted mid-work — widening `●` to cover a layer
  routed away from its gate by a recorded decision — is written into the rule
  and named in the gap notes above rather than left as an assumption.
