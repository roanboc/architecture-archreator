# 3 — The Agent actor sits at co-pilot autonomy

_[← Decisions](./README.md)_

**Status:** Accepted
**Date:** 2026-08-08
**Touches:** [`ACT2` Agent](../2_business/1_business-actors-and-roles.md)

## Context

`ea-doc-style` requires every AI actor to carry an explicit autonomy level,
and says that setting or changing one is exactly what a decision record is
for. archreator models its own executing actor, `ACT2`, as an AI — so the
rule applies to it.

The four levels are advisory, co-pilot, autonomous-with-checkpoint, and
fully autonomous. `ACT2` drafts every document, writes the code, and opens
the PR; the question is what happens before and after.

## Options considered

| Option | Consequence |
| ------ | ----------- |
| **Advisory** — suggests, a human writes | Discards the whole point. The method is designed so an agent can execute it |
| **Co-pilot** — acts, a human approves before it takes effect | Two independent human checks: Gate 2 before code, merge after. Slower on trivial changes |
| **Autonomous with checkpoint** — acts, a human is notified and can intervene after | Faster. The "can intervene after" clause is doing a lot of work when the artifact is an architecture other work then builds on |
| **Fully autonomous** | Contradicts `P2` outright |

## Decision

**Co-pilot.** `ACT2` may draft anything, implement within an approved
design, and open a PR. It may not approve its own gate, merge, change a
Principle, or proceed past a Conflict verdict.

## Consequences

- **Trivial changes carry the same two checks as significant ones**, which
  is the real cost. The bug-fix path exists precisely to relieve it — a fix
  that changes no documented behavior passes no gates.
- **The reasoning follows the same test the examples use**: who bears the
  consequence, and who can undo it. A wrong architectural change is absorbed
  by whoever maintains the project later, and stops being reversible once
  other work depends on it. That is the same test that put
  `example-company`'s `ACT3` at co-pilot and `ACT4` at
  autonomous-with-checkpoint, applied here.
- **Raising it later is a decision record, not a preference.** If a project
  using archreator wants its agent at higher autonomy, that is legitimate
  and local — this record binds archreator's own development, not every
  downstream project's.
- **`restate-current-state` carves out an explicit exception**: `ACT2` may
  not retire an element during restatement without the Requester confirming,
  even though retirement is a documentation edit that co-pilot autonomy
  would otherwise cover. Deleting something real is harder to notice in
  review than adding something wrong.
