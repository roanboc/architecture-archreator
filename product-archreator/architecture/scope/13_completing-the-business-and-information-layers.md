# Project Scope — Completing the business and information layers

_[← Scope index](./README.md) · [EA home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** branch `claude/product-1-roadmap-74giay`.

Both models stop short of a complete business layer, and the method's own
vocabulary — the forty-one element types `ACMP15` enforces — is defined
nowhere except a Python list. This completes what the tier rule says each
model should hold, and grounds the vocabulary in the model that owns it.

Gate 2 on [initiative 12](./12_the-site-becomes-an-implementation-tier.md)
waits on this: migrating the site to an implementation tier means citing
parents in the tiers above, and two of those tiers are unfinished.

## What is missing, and what only looks missing

| Tree | Tier | State |
| ---- | ---- | ----- |
| `org-archreator` | Enterprise | Strategy complete. Business has actors and services; **processes, objects and domain context are absent** |
| `product-archreator` | Product | Business has actors and services; the twelve rules sit **in the wrong file**. **Layer 3 does not exist at all** |
| `product-archreator/site` | Implementation | Owns a `3_value-stream.md` that **restates the enterprise's** |

Two apparent gaps are the tier rule working and are deliberately left alone.
`product-archreator` has no capabilities document and no value stream because
[decision 5](../decisions/5_no-per-product-strategy-folders.md) fixed that the
strategy layer stays enterprise-wide — a per-product copy is precisely what it
forbids, and `RULE11` says the same from the other direction. The site's
value stream is the inverse case: an implementation tier restating what the
enterprise owns, which is a defect rather than a gap, and it joins initiative
12's retirement list.

## The vocabulary has no home

`check_model.py` carries forty-one element-type prefixes — `STK`, `CAP`,
`BPROC`, `GCRE`, `COST` and the rest — and decides from that list what counts
as an element reference. **Nothing in any model defines them.**
`architecture-doc-style` describes how identifiers are *formed* and where the
glyph and shape come from, but carries no table of the types themselves.

So the validator enforces a vocabulary that `RULE2` cannot reach: the code
exists, and the thing it implements is undocumented. Every per-document legend
in the repository is a local restatement of a global fact that is written down
in one place, and that place is a source file.

The Requester's direction settles where it belongs: the information layer
holds **document objects and data entities**, and the entities include the
ArchiMate types the method adopts — referenced, not restated — together with
the concepts archreator has added of its own.

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 1_strategy | **No change** in any tree |
| 2_business | **`org-archreator` gains business processes and business objects**, and a domain-context document carrying its glossary. **`product-archreator`'s twelve rules move** from `2_business-services.md` to `5_domain-context-and-rules.md`, unchanged in content |
| 3_information | **`product-archreator` gains layer 3**, which its `CLAUDE.md` currently says it does not need. That statement was true when the method was thought to hold no data of its own; its vocabulary is data of its own |
| 4_application | **No element change.** `ACMP15` gains a grounding reference to the entity catalogue its prefix list implements |
| 5_technology | **No change** |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — the canvases are unaffected; nothing about products, segments or economics changes |
| Gate 1 — Strategy | — | — | **N/A** — no Stakeholder, Driver, Goal or Principle added or modified. The value stream is the *source* for the processes, not changed by them |
| Gate 2 — Business | _awaiting_ | — | This document, the process spine, the object scope, and the entity catalogue |
| Gate 3 — Solution design | _to be asked at Gate 2_ | — | No code changes are proposed; likely `N/A` |

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | Two models with half a business layer, a product model with no information layer, and a vocabulary of forty-one types that lives only in a validator |
| **Target** (delivered) | Each tier holds what `RULE11` says it should. The vocabulary is a catalogue in the model, and the validator implements it rather than defining it |

## Work packages and deliverables

### WP1 — The organization's business processes

- **Deliverables:**
  `org-archreator/architecture/2_business/3_business-processes.md`, one
  high-level process per stage of `VS1` — **Reach, Frame, Approve, Model,
  Build, Feed back** — each naming the services it realizes and the actors it
  is assigned to.
- **Outcome:** the value stream stops being the only place the organization's
  work is described, and the services gain the processes that deliver them.

### WP2 — The organization's business objects

- **Deliverables:**
  `org-archreator/architecture/2_business/4_business-objects.md`, covering
  **both** the client-facing objects — an engagement, a delivered architecture,
  an approval given by a client's Requester — and the internal ones: a model,
  an initiative, a scope document, an engagement note.
- **Outcome:** the things the business handles are named, which is what the
  processes in WP1 act on and what layer 3's documents represent.

### WP3 — Domain context and rules, in their proper file

- **Deliverables:**
  `org-archreator/architecture/2_business/5_domain-context-and-rules.md` — the
  organization's glossary and any rules it owns.
  `product-archreator/architecture/2_business/5_domain-context-and-rules.md` —
  the twelve existing rules **moved unchanged** out of `2_business-services.md`,
  where they have been living since before the file existed.
- **Outcome:** a reader looking for the rules finds them where the method's own
  template says they are.

### WP4 — The entity catalogue

- **Deliverables:** `product-archreator/architecture/3_information/1_data-entities.md`,
  in two parts:
  - **ArchiMate-aligned entities** — the types the method adopts, *referenced
    rather than restated*, linked to the
    [ArchiMate 101 reference](https://archimate-community.pages.opengroup.org/workgroups/archimate-101/).
    The method does not redefine what a «Business Service» is; it records that
    it uses one, with which prefix and glyph.
  - **archreator's own entities** — the concepts that have no ArchiMate
    equivalent: **tier** (enterprise, product, implementation), **modeling
    depth**, **gate**, **initiative**, **element identifier**, and the
    human/AI/hybrid **actor kind** with its autonomy level.
- **Outcome:** the vocabulary `ACMP15` enforces is documented in the model, and
  `ACMP15`'s prefix list becomes an implementation of it rather than its only
  definition.

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| The enterprise's processes, objects and domain context | Business processes at the product tier — the method's gated walk is already the enterprise's `Frame`/`Approve`/`Model` stages, and a copy is what `RULE11` forbids |
| Relocating the twelve rules, content unchanged | Any change to what the rules say. This is a move |
| The entity catalogue, ArchiMate types referenced not restated | Redefining ArchiMate. The catalogue records adoption, not semantics |
| `ACMP15` naming the catalogue it implements | Making `check_model` *read* the catalogue at runtime — see the gap notes |
| Adding the site's value stream to initiative 12's retirement list | Retiring it here; it belongs with the rest of that migration |

## Gap notes

- **The catalogue and the validator will be two copies of one list.** The
  model defines the vocabulary; the Python list implements it; nothing keeps
  them in step, so a prefix added to one and not the other is a silent
  divergence. Having `check_model` parse the catalogue would close it, and is
  deliberately not proposed here: it would make the validator depend on a
  document's formatting, which is a worse coupling than the one it fixes. The
  honest position is that this is `RULE2` grounding — the code is named as the
  realization of the model element — and grounding has always been carried by
  review.
- **Business objects at the enterprise tier will overlap the layer-3
  documents.** A "scope document" is a business object and its file is a data
  object, and the boundary between them is a judgement the method states but
  does not test. Expect the first reader to ask which one a thing is.
- **The six processes come from a value stream with one stream in it.** `VS1`
  is the only value stream the organization has, so the process spine inherits
  whatever is wrong with it. If a second stream appears — the portal under
  `COA2` would likely bring one — the processes will need revisiting rather
  than extending.
