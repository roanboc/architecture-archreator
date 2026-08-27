# Project Scope — Cross the boundary

_[← Scope index](./README.md) · [Model home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** the `claude/graph-navigator-architecture-m2fr9j` branch in
[`archreator`](https://github.com/roanboc/archreator), and the model changes
this document holds the gates for.
**Closes:** `GAP9` — reaching `PLAT4` on the
[roadmap](../roadmap/1_target-state.md).

[Initiative 8](./8_federate-the-graph.md) put three models in front of one
reader and joined none of them. An identifier is scoped to its model, so a
reference to a foreign element fails the reference check — which is correct,
and is why the fact simply goes unwritten. This organization's `ACMP1` is the
skill corpus; one tree over, the same corpus is decomposed into fifteen
components. Nothing in either model says so.

[Decision 1](../decisions/1_the-process-model-stays-with-the-skills.md) recorded
this as the accepted price of a split it made deliberately: "**no validator
crosses the repository boundary.** The mismatch would be caught by review or not
at all." This initiative stops that being true.

## The design

### 1. A foreign identifier says which model it is from

`product-archreator::ACMP1`. Two colons, because the dot already carries two
meanings — the domain path before the prefix, the catalogue's levels after it —
and a third would make the grammar ambiguous where it is currently only dense.

The name before `::` is the model's name **as the federation index gives it**.
That ties the grammar to `BOBJ8` on purpose: a model you may reference is a
model you have declared you federate with. There is no way to reach into
something you have not said you depend on.

### 2. Resolution, and the two cases that are genuinely different

| The foreign model is | How it resolves | Cost |
| -------------------- | --------------- | ---- |
| **In this repository** | Against that model's own definitions, which the parse already has. Exact, immediate, no network | None |
| **In another repository** | Against `architecture/imports.md` — an authored row naming the element, what it is called, and the revision it was read at | A row somebody wrote |

**The second case is not resolved over the network, and that is deliberate.** A
validator that fetched a sibling repository on every pull request would be slow,
would fail when someone else's site was down, and would let another repository's
push break this one's build. What it checks instead is that the reference was
**declared** — and, because the import row restates the foreign element's name,
that the restatement still matches what the row says. Whether the row still
matches the upstream is a different question, asked by a command somebody runs,
never by CI.

That is the same shape `model-domains` already gives a domain contract: what
you consume is written down, and changing it is a conversation rather than a
surprise.

### 3. The graph joins

The projection gains a `dst_project` on every edge — the model the far end
belongs to, which is the edge's own model for all but the new kind. Traversal
moves onto a qualified identifier, so `neighbourhood.sql` walks across a
boundary without knowing it crossed one, and the navigator draws a federated
graph as one graph because that is now what it is.

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 0_business-design | **Not used** — Depth 1 |
| 1_strategy | **No change.** No stakeholder, driver, goal or principle moves. `G3` — the model still describing today after the merge — is what this serves, and it already exists; `CAP4` gains reach, not a new purpose |
| 2_business | **`BOBJ9` added** — the import, in [4_business-objects.md](../2_business/4_business-objects.md): one foreign element this model consumes, and the revision it was read at. **`BSVC3` restated** — validation now covers a reference that leaves the model |
| 3_information | **`DOBJ4` restated** — every edge carries the model its far end belongs to, and the projection's schema version goes to 2 |
| 4_application | **`ACMP6`, `ACMP7`, `ACMP8`, `ACMP14`, `ACMP16` restated** — the grammar, the resolution, the column, and two readers that stop stopping at the boundary |
| 5_technology | **No change** |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — the subject is one application |
| Gate 1 — Strategy | — | — | **N/A for this initiative** — the direction was approved on the [roadmap](../roadmap/README.md) at Gate 1, 2026-08-27 |
| Gate 2 — Business | Delegated ([decision 2](../decisions/2_the-requester-delegates-the-remaining-gates.md)) | 2026-08-27 | `BOBJ9` and the restated `BSVC3` and `DOBJ4`. **Look first at:** the import row restating a foreign name, because it is a second copy of somebody else's fact and copies are what `P1` is about |
| Gate 3 — Solution design | Delegated ([decision 2](../decisions/2_the-requester-delegates-the-remaining-gates.md)) | 2026-08-27 | § The design. **Look first at:** the decision not to resolve over the network in CI. Everything else here follows from it |

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | A reference that names a foreign element fails. The relationship goes unwritten, and `trace` stops at the model boundary without saying that it did |
| **Target** (delivered) | `PLAT4`. A foreign reference has a grammar, resolves against the model that owns it or against a declared import, and joins the graph. Decision 1's consequence is closed for models in one repository and made explicit — a written, checked declaration — for models in another |

## Work packages and deliverables

### WP1 — The grammar and the resolution

- **Deliverables:** `ACMP7` parses `model::ID` and resolves it against the
  named model in this repository, or against `architecture/imports.md`;
  `ACMP6` fails a reference that is neither.
- **Outcome:** a foreign reference is a thing you can write and a thing that
  can be wrong.

### WP2 — The import declaration

- **Deliverables:** `architecture/imports.md` in the scaffold and filled in
  where this repository needs it; the restated name checked exactly as a
  relationship table's is.
- **Outcome:** what a model consumes from outside is written down, and stale
  is a build failure rather than a discovery.

### WP3 — The graph crosses

- **Deliverables:** `dst_project` on every edge, schema 2;
  `neighbourhood.sql` walking a qualified identifier; `ACMP14` and `ACMP16`
  showing a foreign neighbour as what it is.
- **Outcome:** "what would this change touch" stops quietly excluding
  everything in another model.

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| A foreign reference, resolved and checked | **Resolving it over the network in CI.** A check that fetches somebody else's repository is slow, flaky, and lets their push break your build |
| Drift between an import and its upstream, reported on request | **Failing a build on drift.** The upstream may be mid-change; that is a conversation, and the method already has one — a contract has two sides |
| Models in one repository, resolved exactly | **Automatic import discovery.** What a model depends on is a decision somebody makes and writes down |

## Gap notes

- **An import row is a copy of somebody else's fact**, and the check holds it
  against the declaration rather than against the truth. It can be internally
  consistent and out of date, which is the honest limit of not making network
  calls. The refresh command is what closes it, and running it is somebody's
  discipline — the failure mode `TSVC2` exists to complain about, accepted here
  because the alternative is worse.
- **Two colons is a third meaning for punctuation in an identifier.** The
  grammar was already dense. It is now `model::DOMAIN.PREFIX1.2`, which is
  legible only because each separator appears at most once and in a fixed
  order.
