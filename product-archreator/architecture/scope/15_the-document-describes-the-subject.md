# Project Scope — The document describes the subject

_[← Scope index](./README.md) · [EA home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** the branch and pull request opened for this initiative.

An architecture document produced by this method currently narrates its own
construction. It says what the source material contained, how many elements
were consolidated into how many, why identifiers were renumbered before a
gate, and which initiative the document is new as of. None of that is about
the subject being modeled, and a reader who came to learn how a business works
has to read past it to get there.

This is the sibling of [initiative 14](./14_a-model-a-human-can-read.md) and
comes from the same place: correct and unreadable is not delivered. Fourteen
made the diagrams quieter; this makes the prose around them describe one thing
rather than two.

## The line, and where it falls

**A sentence in an architecture document is either about the subject or about
the act of modeling it.** The first stays. The second goes to the scope
document, which is where a modeling decision was already supposed to be
recorded and presented at a gate.

| Stays — it is about the subject | Goes — it is about making the document |
| ------------------------------- | -------------------------------------- |
| "This diagram is the risk, drawn" | "The source material lists seven industries and eight customer types" |
| "`BPROC1` uses no capability — Reach is the only stage the organization does not do anything skilful in" | "Writing them as separate elements would have produced an unreadable catalogue" |
| "`VAL1` is the only value every stakeholder receives" | "Twelve pains were consolidated into five" |
| "The areas have no realizing artifact, and that is correct rather than a gap" | "Capability identifiers were renumbered once, here, before Gate 1" |

The right-hand column is not deleted from the world — **it is exactly what a
gate presentation is made of**, and `operating-model-discovery` already
requires naming the consolidation when asking for Gate 0. It belongs in the
initiative's record, where a Requester decides on it once, and not in the
document a reader opens two years later to find out what the business does.

Consolidation counts written into the layer document are also `P3` broken: the
scope document states them, so the layer document restating them is a second
copy that will drift.

### Two carve-outs, both deliberate

**Anything awaiting validation stays inline.** A "Pending — future initiative"
marker, an adopted interpretation, a figure nobody has confirmed — these sit in
the body where the reviewer who can correct them will actually see them. Moving
them to the end is how they stop being corrected.

**Provenance attaches to elements; history attaches to documents.** A table
cell naming the initiative that delivered an element is a trace worth keeping.
A sentence saying the *document* is new as of that initiative is the document
talking about itself. The first is a reference, the second is a narrative.

## Notes that survive go to the end

A note genuinely worth keeping — one that is about the subject but does not
belong to any one section — goes in a final **Additional notes** section,
after the last element group. Not woven between a diagram and the table it
explains, where it displaces the thing the reader came for.

## No version commentary at all

No "as of initiative N", no note about what an unapproved proposal would
change, no record of a draft's revisions. The document states what is true
now; git holds how it got there and the scope documents hold why. A model that
carries its own changelog gives a reader two accounts to reconcile and no way
to tell which one is current.

## Identifiers are continuous until they are approved

`RULE5` says an identifier is assigned once and never reused. That has been
applied from the moment an element is first written down, which produces gaps
in a sequence that was never approved by anyone — a reader wondering what
happened to `CS2` when `CS2` existed for an afternoon during drafting.

**The never-reuse rule starts at approval.** Before the gate that approves an
element, identifiers are draft: remove an element and renumber so the sequence
stays continuous, with no Retired row and no note explaining the gap. After
approval the identifier is permanent, and retiring it is recorded.

This is not new practice — it is practice that was already being taken as an
exception and explained in prose each time. Two documents in this repository
renumbered before their gate and wrote a paragraph justifying it. Making it a
rule removes both the doubt and the paragraph.

**The consequence for the Retired table:** it holds only elements that passed a
gate. An element that never did leaves nothing behind, and a document that has
retired nothing has no Retired section at all — not one saying "None".

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 0_business-design | **Not used** — Depth 1 |
| 1_strategy | **No change.** No Stakeholder, Driver, Goal or Principle added or modified |
| 2_business | **`RULE5` is amended** — never-reuse begins at approval rather than at first writing — and **`RULE13` is added**: an architecture document describes its subject, not its own construction. Both are the rules table in `2_business-services.md` |
| 3_information | **Not started** in this tree |
| 4_application | **No new component.** `ACMP6` (notation authority) and `ACMP8` (restatement) change behavior |
| 5_technology | **No change.** `ACMP15` reads a `## Retired` heading only when one is present, so documents that stop writing an empty one still pass |

**`RULE13` is proposed knowing that a thirteenth rule was declined once.**
[Initiative 11](./11_referencing-across-models.md) proposed an addressing
convention as a rule and Gate 2 judged it had not earned the row. This one is
a different kind of thing: a constraint on what a delivered document may
contain, traceable to `P3` — the consolidation record lives in the scope
document, and a layer document repeating it is the duplication `P3` forbids.
It is the same shape as `RULE10`, which also constrains document content. If
the judgement is that it still does not earn the row, the guidance works as
skill text and the rest of this initiative is unaffected.

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — Depth 1; no canvases in this tree |
| Gate 1 — Strategy | — | — | **N/A** — no Stakeholder, Driver, Goal or Principle added or modified |
| Gate 2 — Business | Requester | 2026-08-15 | This document, presented with a branch link, including `RULE13` flagged as a judgement call after a thirteenth rule was declined once before |
| Gate 3 — Solution design | — | — | **N/A** — not requested; no component is added and no code is written |

## Plateaus

| Plateau | State |
| ------- | ------ |
| **Baseline** (before) | Architecture documents narrate their own drafting; identifiers gap for elements nobody ever approved; a document that retired nothing still carries a Retired section saying so |
| **Target** (delivered) | The body describes the subject, notes that survive sit at the end, nothing awaiting validation is hidden, and an identifier becomes permanent at the gate that approves it |

## Work packages and deliverables

### WP1 — What an architecture document contains

- **Deliverables:** a new section in
  `.claude/skills/architecture-doc-style/SKILL.md` carrying the subject/act-of-
  modeling test, the table of examples, the two carve-outs, the Additional
  notes placement and the no-version-commentary rule; and § Document skeleton
  updated so Additional notes has a stated position.
- **Outcome:** an agent writing a layer document has a test it can apply per
  sentence, rather than a preference it has to infer.

### WP2 — Identifiers become permanent at the gate

- **Deliverables:** `architecture-doc-style` § Element IDs — the never-reuse
  rule gains its starting point, and pre-approval renumbering becomes stated
  practice rather than a per-document exception;
  `restate-current-state` § The one rule that governs this skill and § The
  Retired section — the table holds gate-approved elements only, and the empty
  form is not written.
- **Outcome:** a gap in an identifier sequence means something, because the
  only way to make one is to retire something that was approved.

### WP3 — The rules, and the skills that carry them

- **Deliverables:** `RULE5` amended and `RULE13` added in
  `product-archreator/architecture/2_business/2_business-services.md`;
  `restate-current-state` Step 1 gains modeling commentary as a thing to find;
  `scope-doc` § Rules states that consolidation counts and their rationale
  live in the scope document; `operating-model-discovery` § Gate 0 says the
  consolidation is named in the presentation and the scope document rather
  than written into the canvas.
- **Outcome:** the material this removes from one place has a stated home in
  another, instead of being deleted from the method.

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| The rules, in the skills | **Cleaning this repository's own four trees** — the Requester chose method only, no sweep, when these notes were handed over |
| `RULE5` amended, `RULE13` added | Any tooling that checks either. Both are carried by review, like `RULE10`–`RULE12` |
| Modeling commentary added to what `restate-current-state` looks for | Running a restatement here. That is its own initiative with its own Gate 2 |
| The Retired table narrowed to approved elements | Removing the Retired mechanism. It is what keeps a dangling reference explicable |

## Gap notes

- **This repository will publish a second rule it does not yet follow.** The
  three "Retired — None. This document is new as of initiative 4" sections, the
  renumbering paragraph in the organization's capability map, and the
  consolidation note in its value proposition canvas are all examples of what
  `RULE13` forbids. That was the Requester's call at this gate — the method
  changes so new work is right, and the existing models are left until there is
  a reason to open them. Combined with initiative 14's diagram sweep, the
  backlog for a future cleanup pass is now two rules deep and written down.
- **The subject/act-of-modeling test is a judgement, not a check.** "This
  diagram is the risk, drawn" is about the subject; "writing them separately
  would have been unreadable" is about the writing. Most sentences are that
  clear and some will not be, and nothing can tell them apart mechanically —
  which is why the rule ships with a table of worked examples rather than a
  definition.
- **Pre-approval renumbering is safe with the validators and not with a
  reader.** `ACMP15` only checks that references resolve, so renumbering a
  draft passes as long as every reference moves with it. A Requester who
  reviewed a draft between gates will see identifiers shift under them. The
  rule is right anyway — the alternative is permanent gaps from elements nobody
  ever agreed to — but a gate presentation on a renumbered draft should say so
  in one line.
