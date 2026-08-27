# Decision 3 — Initiative 10 is directed, and its gates are delegated

_[← Decisions index](./README.md)_

**Status:** Accepted
**Date:** 2026-08-27
**Touches:** [roadmap/](../roadmap/README.md), [scope/](../scope/README.md)

## Context

[Decision 2](./2_the-requester-delegates-the-remaining-gates.md) delegated the
gates on initiatives 7–9 and said so in terms that expire: "It covers
initiatives 7, 8 and 9 only… There is no mechanism here for extending it, and
adding one would be a second decision." It also reserved one thing absolutely:
"**A change to the roadmap** — a new plateau, a dropped one, a reordering.
Gate 1 approved a destination and an order, and altering either is the one
thing this delegation cannot cover."

Those three shipped. The Requester then asked for something that is not on the
sequence: a navigator a person can actually read and search, with element
names in boxes, a properties panel carrying what the documents say, guided
search, and saved views arranged by hand.

That is a new plateau, so decision 2 cannot cover it — and it does not need to,
because the request **is** the Requester setting direction. Gate 1 asks them to
approve a destination; they named one.

## Options considered

| Option | Why not (or why) |
| ------ | ---------------- |
| **Treat decision 2 as still running** | It says in as many words that it does not. Reading a spent delegation as a standing one is how a delegation becomes an absence of gates |
| **Stop and ask the Requester to approve a roadmap they just dictated** | Gate 1 exists so a direction is the Requester's. This one is, in their own words. Asking them to approve their own instruction is ceremony, and ceremony is what makes people stop reading gates |
| **Skip the roadmap and go straight to a scope document** | The roadmap is the only place the method permits a future to be described, and a plateau nobody wrote down is a plan nobody can read in one place |
| **Record the direction as theirs, and delegate the gates below it** | What actually happened, written down as what actually happened |

## Decision

**`PLAT5` and its gaps are added to the roadmap on the Requester's own
direction, quoted in the target state**, and **Gates 2 and 3 of initiative 10
are delegated on the same terms as decision 2** — each Approvals row citing
this record, and each naming what a reviewer should look at first.

The reservations from decision 2 carry over unchanged and are not restated
here: a further change to the roadmap returns to the Requester, and so does any
call that trades away what they said they wanted.

**One reservation is specific to this initiative.** The Requester asked for
saved views "as if I was creating visualisations in Archi, but nothing is
created from there". Anything that would let the navigator write to the model —
a view that adds an element, a layout that renames one, an export that
round-trips into `architecture/` — is outside what was directed, and would need
them.

## Consequences

- **The roadmap gains a plateau nobody has to guess the provenance of.** The
  sentence that set the direction is quoted where the plateau is defined.
- **The delegation stays finite.** This covers initiative 10. An eleventh
  returns to the Requester, exactly as the tenth did.
- **The navigator's boundary is written down before it is built.** "It displays
  and it never writes" is easy to hold now and easy to erode later, and the
  place to state it is here, once, rather than in each pull request that tests
  it.
