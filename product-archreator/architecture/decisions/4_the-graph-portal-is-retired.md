# Decision 4 — The graph portal is retired, and initiative 13 is delegated

_[← Decisions index](./README.md)_

**Status:** Accepted
**Date:** 2026-08-27
**Touches:** [6_transition/](../6_transition/README.md), [scope/](../scope/README.md)

## Context

[Initiative 9](../scope/9_walk-the-model.md) built a graph navigator and
[initiative 12](../scope/12_make-it-readable.md) made it legible: boxes,
layered layouts, a properties panel carrying the documents' own prose, faceted
search, saved views. It works, and it was shipped four days after the
relationships it draws became declarable.

The Requester then looked at it and said what it is for:

> I'm really considering the idea of having a graph portal, I think it might
> not be relevant as people might want to understand a specific topic and in
> that case we can just build a md file with the relevant context and relevant
> diagrams for reference instead. […] I see myself wanting to explore the
> architecture for specific use cases or domains, and the best thing I could
> get is a temporary document created in-time with the architectural elements
> relevant to me, no need to navigate graphs and explore blindly.

They are right, and the strongest argument is one the navigator itself made.
It opens on a single layer because the whole model at once is illegible —
recorded in initiative 9's own gap notes and treated there as a layout
problem. It is not. **A reader does not arrive at a graph; they arrive at a
question**, and a graph makes them reconstruct the question by clicking.

The second argument is `G1`: *an agent reads the business context natively*.
The navigator is the only thing this method ships that an agent cannot read.
The portal renders Markdown, the PDF prints Markdown, the projection feeds
scripts — and then one page requires a human with a mouse.

## Options considered

| Option | Why not (or why) |
| ------ | ---------------- |
| **Keep both** | Two readers answering the same question, one of them unused. "Simple and valuable" is the Requester's stated test and carrying two fails it |
| **Keep the navigator, stop investing** | The worst outcome: a page nobody maintains, with links that already 404, shipped into every project the method emits |
| **Retire the navigator, build the brief** | The reader arrives with a question and leaves with a document. Everything the navigator sat on — the parse, the projection, the excerpts, the traversal — is what a brief is generated from |

## Decision

**The graph navigator is deleted**, not left retired in place. Its plateaus
`PLAT2` and `PLAT5` are marked **Abandoned** on the roadmap with their reasons,
and the rows stay: *"an abandoned plateau that is removed invites somebody to
propose it again in two years."*

**`PLAT6` — the scoped brief — replaces them**, on the Requester's own
direction, and **Gates 2 and 3 of initiative 13 are delegated** on the terms
[decision 2](./2_the-requester-delegates-the-remaining-gates.md) set and
[decision 3](./3_the-navigator-earns-its-own-initiative.md) last renewed. It
covers initiative 13 and expires with it.

**What is kept is what was underneath.** Roughly 1,470 lines of page go;
roughly 1,870 lines of parse, projection, traversal and query stay, along with
376 elements, 615 declared relationships and 308 prose excerpts. Initiative 8
is untouched and is the foundation of both.

## Consequences

- **Two initiatives are written off, and the record says so.** Initiatives 9
  and 12 are merged history and are not rewritten; this record is where a
  reader learns that what they built no longer exists.
- **Generating a diagram is now correct.** Before initiative 8 a generated
  diagram would have competed with an authored one for the same fact. Since
  relationships are declared and diagrams are renderings, generating one from
  the declarations is the same operation the notation already describes.
- **The published portal stays.** It renders the documents; the brief answers a
  question. `ASVC9` gains a third rendering rather than losing its first two.
- **A brief is derived, and derived documents drift.** Every one carries the
  revision it came from and says on its face that it is disposable, and none
  of them is ever committed. That is the constraint that keeps a brief from
  becoming the second model this method exists to prevent.
