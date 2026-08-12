# 4 — Validate the model in memory; defer the database

_[← Decisions](./README.md)_

**Status:** Accepted
**Date:** 2026-08-08
**Touches:** [`ACMP15` Element-ID validator](../4_application/1_application-components.md),
[`RULE5`](../2_business/2_business-services.md)

## Context

`stack-selection` § The model as data had specified a `nodes`/`edges` SQLite
projection since before archreator modeled itself, and the
[review](../reviews/1_value-and-ux-review.md) put it first in the backlog as
"load-bearing, not nice-to-have". Modeling archreator made the gap concrete:
`RULE5` (an ID is assigned once and never reused) was enforced by nothing at
all, and `RULE2` only for links.

The Requester challenged whether the database earned its place, on the
grounds that the graph is already implicit in the documentation. That
challenge was correct, and it exposed that two separable things had been
bundled into one backlog item.

## Options considered

| Option | Consequence |
| ------ | ----------- |
| **Build the projection as specified** | A second representation of the model that can fall behind the first. `grep` already traverses the graph; an agent already reads Markdown natively. Infrastructure ahead of any question that needs it — which `stack-selection`'s own principles warn against |
| **Build nothing** | The graph stays implicit and readable, which is true and sufficient for *reading*. But nothing catches a reference to a deleted element, which is the failure that actually hurts |
| **Validate in memory, persist nothing** | Closes `RULE5` without creating a derived artifact. The parse that a projection would need is written either way |

## Decision

**`scripts/check_model.py` builds the graph in memory, checks it, and
exits.** No database, no export, no generated file.

The reasoning that settles it: catching a dangling reference requires a
*parse*, not a *store*. Everything the projection was for — traversal,
lookup, "what references this" — `grep` already does against the source of
truth, and does it without any risk of being out of date.

## Consequences

- **The failure that motivated all of this is now caught.** An agent reading
  `relieves GAIN2` cannot cheaply tell that `GAIN2` was deleted three
  initiatives ago, and will reason confidently from the stale reference —
  `ASM2`'s confident inconsistency, in its most literal form. `grep` tells
  you what *references* `GAIN2`; only a validator tells you `GAIN2` is gone.
- **Nothing can go stale**, because nothing persists. A projection would have
  needed a regeneration discipline that `P3` exists to avoid needing.
- **The projection is ~20 lines away if it is ever justified.** The validator
  already extracts nodes and references; writing them to SQLite instead of
  discarding them is the whole remaining job. Deferring costs nothing.
- **`stack-selection` § The model as data was rewritten**, because its old
  framing presented the export as the default and made the database sound
  inevitable. That framing is what over-scoped this in the first place, and
  leaving it would have re-created the same mistake for the next reader.
- **`RULE2` stays only partly enforced.** The validator checks that element
  *references* resolve, not that a "Realized by" cell points at a file that
  exists. That check was considered and deliberately left out: distinguishing
  a repository path from a team name is fuzzy, and a wrong failure in CI
  teaches people to ignore CI.

### What would change the answer

Any one of these, recorded as its own decision record at the time:

- The model stops fitting in one context read, so an agent must query rather
  than read.
- Domains move into separate repositories, so federation needs an
  interchange format an agent cannot `grep`.
- A genuinely **transitive** question recurs — "blast radius of retiring
  `CAP3`" is a traversal, not a lookup. A one-off is a script, not
  infrastructure.
- A non-agent consumer appears: a dashboard, a report, or a rendered model
  for stakeholders who will not read Markdown tables.

None were true when this was decided. All are plausible at Depth 3 with real
domains, which is exactly when to revisit.
