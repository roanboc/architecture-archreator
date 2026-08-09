# 1 — Modeling this organization, and standardising the notation

**Date:** 2026-08-09
**Kind:** initiative — six of them, run back to back
**Delivered:** [scope documents 1–3](../scope/README.md) here, and
[5–7](../../../meta/scope/README.md) in `meta/`

The first note, written against the work that produced the mechanism. Not
ideal — the retrospective is meant to run on work done *before* it existed,
and this is recollection from the same sitting. Recorded anyway, because a
mechanism nobody has ever run is a claim.

## What the method did not cover

**Presenting a gate to someone who cannot check out a branch.** The method
said to present with links to the documents. It did not say what kind of
link. A Requester reading a summary in a chat window has no working copy, so
relative paths and file names resolve to nothing for them.

**A merged scope document whose link target was deleted.** `RULE6` makes a
merged record's words immutable, and a carve-out already allowed repairing
*where* its links point when files move. Nothing covered a file that stopped
existing anywhere.

**Renumbering element identifiers before a gate.** The value proposition
canvas carried a note allowing one renumbering before Gate 0. When the
capability hierarchy gained a level, the same question arose at Gate 1, and
the rule said nothing about it.

**An element with no canvas source.** `strategy-discovery` says derive, don't
re-ask, which implies every strategy element traces back to a canvas block.
`CAP10` does not — it came from noticing a claim with no mechanism behind it,
long after Gate 0.

**A gate granted on a requirement rather than on a presented design.** The
method assumes design, then present, then approve. The site rebuild was
approved as an instruction — "rebuild it, I'm okay with that" — before any
design existed.

## What was done instead, and why

Full branch URLs, one per document, in every gate presentation. The reasoning
was that an approval given against a summary the Requester cannot verify is
an approval of the summary, not the model.

Links in the four affected merged documents were pinned to the commit before
deletion. The carve-out protects *words*; a permalink preserves what the
document said while pointing at something that exists.

The renumbering was done and explicitly declared spent — "the second and last
time this carve-out can be used on this model" — on the reasoning that the
carve-out belongs to the gate that approves the layer, not to Gate 0
specifically.

`CAP10` was added with an explicit "no canvas source" in its `Source` column
and a pointer to the decision that introduced it, rather than inventing a
canvas ancestor for tidiness.

The out-of-order gate was recorded as a deviation in the Approvals table,
naming what was approved and what was not, rather than presenting it as
normal.

## Does it generalize?

| Moment | Verdict |
| ------ | ------- |
| Gate links must be full URLs | **Yes — already encoded** in `ea-first-change` § Show the Requester what they are approving |
| Pinning a deleted link target | **Not yet known.** One case. Pinning is defensible and there may be a better answer |
| Renumbering before *the* gate | **Yes, and it has now happened twice** — Gate 0 and Gate 1. Two occurrences is the threshold this mechanism names |
| An element with no canvas source | **Probably.** Any long-lived model will discover elements after its canvases were approved; the method currently reads as though it will not |
| Gate granted on a requirement | **Specific to this**, most likely. It happens when the Requester is also the person doing the work, which is not the general case |

## What surprised us

**The bottom layers explained the top one.** Layer 3 said this organization
holds no data about adopters, and that turned out to be the reason four of
its seven outcomes cannot be measured — a fact the strategy layer had stated
as a gap without knowing its cause. Nobody expected layer 3 of a
documentation project to be load-bearing.

**Two layers agreed independently.** Information and technology were filled
separately and both identified the portal as the moment this stops being a
method and becomes a service. Neither was written with the other open.

**Applying a rule narrowed it.** `RULE10` was written as "every EA document
opens with its notation legend" and survived about an hour of use before it
became clear that an index page has no elements to legend.

## Deliberately not recorded

Nothing. This was internal work on a public repository — there was no
confidential material to exclude, so the boundary this mechanism exists to
police was never tested. **That is worth stating rather than leaving as
silence**: the confidentiality rule remains completely unexercised.

## Proposed

| # | Skill or document | The sentence it would add | Raised as |
| - | ----------------- | ------------------------- | --------- |
| 1 | `ea-doc-style` § Element IDs | Identifiers in a layer may be renumbered once, before the gate that approves **that layer** — not only before Gate 0 — and the carve-out is spent per layer | **Ready.** Seen twice; meets the threshold |
| 2 | `strategy-discovery` § Derive, don't re-ask | An element discovered after the canvases were approved is legitimate; record it with an explicit "no canvas source" and a pointer to what introduced it, rather than inventing an ancestor | Not yet — one case |
| 3 | `scope-doc` § Rules | When a link in a merged document points at something deleted, pin it to the last commit where it existed | Not yet — one case, and the general answer is unsettled |
