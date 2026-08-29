# Decision 2 — The Requester delegates the gates on initiatives 9–11

_[← Decisions index](./README.md)_

**Status:** Accepted
**Date:** 2026-08-27
**Touches:** [scope/](../scope/README.md) — the Approvals table of every
initiative on the [roadmap](../6_transition/2_sequence.md) sequence

## Context

The Requester approved Gate 1 on the roadmap, and Gate 2 and Gate 3 on
initiative 8, in the ordinary way: presented, questioned, changed once, then
granted. With the direction settled and one initiative delivered against it,
they delegated the remaining three:

> Move on with all the gates. Ask me only real critical questions and decide
> all the rest, you already know what I want and the motivation behind it, so
> I trust you to execute the entire plan until I get all the functionality
> initially scoped.

That sentence is an approval of something, and the method has no row for it.
`P3` says an approval that is not recorded did not happen, and the Approvals
table records *a gate*, not *a standing permission*. Left unrecorded, three
initiatives would carry Approvals tables that either lie about who granted
them or sit empty against merged work.

## Options considered

| Option | Why not (or why) |
| ------ | ---------------- |
| **Write "Requester" in each Approvals row** | It is what the table asks for and it is not what happened. A reader two years on would conclude the Requester was shown each gate and answered, which is exactly the confident-wrong-answer the method spends its validators preventing |
| **Leave the rows empty and merge anyway** | Removes every gate on the sequence. `P3` exists to stop precisely this, and Gate 1's own text says a roadmap read as pre-approval has quietly removed every gate the method has |
| **Stop and re-ask at each gate** | Contradicts an explicit instruction from the person the gates protect. The Requester is entitled to delegate their own review; what they are not entitled to do is make it invisible |
| **Record the delegation once, and cite it** | The delegation is a decision — consequential, smaller than an initiative, and it explains a *why* that no layer document carries. Each Approvals row then names what actually granted it |

## Decision

**The delegation is recorded here, and every gate it covers cites this record
by name in its Approvals table**, in the form:

> `Delegated (decision 2)` | 2026-08-27 | what was decided, and what a
> reviewer should look at first

It covers **initiatives 9, 10 and 11 only** — the three already named on the
approved sequence. It is not a standing grant: an initiative that is not on
that sequence, or a change to the sequence itself, returns to the Requester.

**Two things stay with the Requester regardless**, because delegation of
review is not delegation of direction:

- **A change to the roadmap** — a new plateau, a dropped one, a reordering.
  Gate 1 approved a destination and an order, and altering either is the one
  thing this delegation cannot cover.
- **A decision that forecloses something the Requester said they wanted.**
  Their stated motivation is a graph they can navigate with no infrastructure
  beyond a webpage, federated across public projects. A call that trades any
  of that away is a critical question, not a judgement call.

## Consequences

- **The Approvals tables stay honest.** A reader can tell a gate the Requester
  answered from a gate delivered under delegation, which is the distinction
  that would otherwise be lost.
- **The gates still happen.** Each initiative still walks the layers, still
  writes a scope document before implementation, and still records what was
  decided at each gate. What is delegated is who says yes, not whether
  anything is presented.
- **It expires on its own.** Three initiatives, named in advance. There is no
  mechanism here for extending it, and adding one would be a second decision.
- **A wrong call is visible rather than deniable.** Every delegated gate names
  what a reviewer should look at first, so the Requester can audit the three
  initiatives in the time it takes to read three rows.
