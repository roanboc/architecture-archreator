# Project Scope — Completing the business layer

_[← Scope index](./README.md) · [EA home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** branch `claude/product-1-roadmap-74giay`.

This organization's business layer names its actors and its services and stops
there. It has never said **what work it does** or **what things that work
handles** — the two questions layers `2_business/3` and `2_business/4` exist to
answer. The value stream has described the work since Gate 1, one level up, but
nothing in the business layer derives from it.

This completes the layer, so that the tiers below have something to refine.
[Initiative 12](../../../product-archreator/architecture/scope/12_the-site-becomes-an-implementation-tier.md)
in the method's model waits on it: migrating the site to an implementation tier
means citing parents in the tier above, and half of what it would cite does not
exist yet.

## Why the scope splits in two

The work that motivated this touches both models. The rule in the repository's
`CLAUDE.md` is that a change to **the organization** is recorded here and a
change to **the method** in `product-archreator/architecture/scope/` — so it is
two initiatives, not one, and this is the organization's half.

The method's half —
[initiative 13](../../../product-archreator/architecture/scope/13_completing-the-business-and-information-layers.md) —
relocates its twelve business rules and grounds the element-type vocabulary
that `check_model` currently enforces from a Python list alone. Neither half
depends on the other; they were separated because the alternative was a
document in this tree citing an initiative in that one, which the method has no
notation for (open question 11 there).

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 0_business-design | **No change.** Nothing about products, segments or economics moves |
| 1_strategy | **No change.** `VS1` is the *source* for the processes, not altered by them. This is the derivation Gate 1 always implied and no initiative had performed |
| 2_business | **`BPROC1`–`BPROC6` added**, one per value-stream stage. **`BOBJ1`–`BOBJ7` added**, covering both the organization's own objects and the client's. A domain-context document carries the glossary |
| 3_information | **No change to elements.** `DOBJ1`–`DOBJ7` gain business-object counterparts, which makes explicit which of them represent something the business names |
| 4_application | **No change** |
| 5_technology | **No change** |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — the canvases are unaffected; this derives from them rather than revising them |
| Gate 1 — Strategy | — | — | **N/A** — no Stakeholder, Driver, Goal or Principle added or modified. `VS1` is read, not changed |
| Gate 2 — Business | _awaiting_ | — | [`3_business-processes.md`](../2_business/3_business-processes.md), [`4_business-objects.md`](../2_business/4_business-objects.md), the domain-context document, and this scope document |
| Gate 3 — Solution design | _to be asked at Gate 2_ | — | No application or technology change is proposed; likely `N/A` |

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | A business layer with actors and services and no processes or objects. The work is described only in the value stream, one layer up, in a document about strategy |
| **Target** (delivered) | Six processes, one per stream stage, each naming what it realizes and who performs it; seven objects, split by who owns them; a glossary |

## Work packages and deliverables

### WP1 — Business processes

- **Deliverables:** [`2_business/3_business-processes.md`](../2_business/3_business-processes.md) —
  `BPROC1` Reach, `BPROC2` Frame, `BPROC3` Approve, `BPROC4` Model,
  `BPROC5` Build, `BPROC6` Feed back. One per stage of `VS1`, each naming the
  services it realizes, the actors assigned, the capabilities it draws on and
  the artifact that realizes it.
- **Outcome:** the organization's work is described in the layer that exists
  for it, and the value stream stops being the only place to find it.

### WP2 — Business objects

- **Deliverables:** [`2_business/4_business-objects.md`](../2_business/4_business-objects.md) —
  `BOBJ1`–`BOBJ4` the organization's own (a model, an initiative, a gate
  approval, an engagement note) and `BOBJ5`–`BOBJ7` the client's (an
  engagement, a delivered architecture, a client's own approval), with the
  confidentiality boundary drawn as the single edge between the groups.
- **Outcome:** what the processes handle is named, and the distinction between
  what this organization owns and what merely passes through it is in the
  model rather than in someone's judgement.

### WP3 — Domain context and glossary

- **Deliverables:** `2_business/5_domain-context-and-rules.md` — the terms this
  organization uses in a fixed sense (Requester, adopter, engagement, gate,
  initiative, tier) and the note that its business rules are the method's, held
  one tier down rather than restated here.
- **Outcome:** the vocabulary a reader needs is in one place, and the absence
  of rules at this tier is a stated verdict rather than an empty file.

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| Six processes, derived from `VS1` | Any change to `VS1` itself — it is read, not revised |
| Objects on both sides of the client boundary | Modeling a client's internals. `BOBJ5`–`BOBJ7` are named because the processes touch them, not described |
| A glossary at this tier | Business rules at this tier — they belong to the method and are recorded there |
| `▧` added to the palette for «Business Object» | Resolving the `❒` collision — see the gap notes |

## Gap notes

- **`❒` is assigned to two elements.** The canonical glyph table gives it to
  «Contract»; `product-archreator` has used it for «Business Rule» across
  twelve rules and several merged documents. This initiative needed a glyph for
  «Business Object», found none, and assigned `▧` — but it deliberately did not
  touch `❒`, because reassigning a glyph in active use is a change to published
  notation and belongs in an initiative that says so. The collision is real and
  now recorded.
- **`BOBJ5`–`BOBJ7` are modeled and not held.** Naming a client's objects in a
  public repository is safe only while they stay abstractions. The moment one
  carries a client's name it stops being a business object and becomes the
  confidentiality breach `DOBJ4` exists to prevent.
- **Six processes from one value stream.** `VS1` is the only stream this
  organization has, so the decomposition inherits whatever is wrong with it. A
  second stream — the portal under `COA2` would likely bring one — means
  revisiting the six rather than adding to them.
