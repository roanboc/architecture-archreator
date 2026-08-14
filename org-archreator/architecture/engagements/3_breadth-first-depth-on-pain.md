# 3 — Modeling an organization that already knew its own processes

**Date:** 2026-08-14
**Kind:** client engagement
**Delivered:** not public

## What the method did not cover

**How far down to decompose.** The method says to model business processes and
capabilities. It does not say at what level, how many levels there are, or when
to stop — so the only defensible reading is "model them", and the only
defensible depth is "all of them, equally". On an organization of any size that
produces more model in a week than the people who commissioned it will read in
a month.

**What an organization's process model looks like before we arrive.** The
organization already had macro processes identified, in the classification its
own quality management uses — strategic, operational, support, evaluation. The
method has no concept of a macro process, no concept of a level, and no place
to put a classification the client already thinks in. It would have started
from the value stream and produced a decomposition the client did not
recognize as theirs.

**Where the detail was worth having.** The pain was concentrated in one
operational macro process. Every other branch was working well enough that
nobody had a question about it. The method offered no way to say "this branch
is detailed because of this pain, and that one is deliberately not" — so an
undetailed branch reads as an unfinished one.

**What a capability map starts from.** "What must this organization be able to
do?" is a question the method asks directly, and businesses answer it badly —
they describe their org chart, or their current projects. Nothing in the method
suggests bringing a starting point to the question.

**Diagram labels.** With enough elements on one row, the stereotype word is the
widest thing on every node and the least informative, because the legend
directly above already said what the shape means.

## What was done instead, and why

**Levels were invented on the spot**, borrowed from ordinary business analysis
practice: macro process, process, sub-process, task. Then levels 1 and 2 were
completed across the whole organization and level 3 was written for the painful
branch only. The reasoning was that horizontal completeness is what makes a
model trustworthy — a reader can see nothing is missing — while vertical
completeness is what makes it unreadable, and only the second one is optional.

**The client's own classification was adopted rather than replaced.** Arriving
with a different decomposition of work the client had already decomposed spends
the engagement's credibility on nothing. The four quality-management categories
are standard practice, the client already used them, and they answer a question
the method had no way to ask: which whole category of work is undocumented?

**The capability map was drafted from what businesses in that industry
generally must be able to do, and then taken back as a proposal.** Not as an
answer — every item was confirmed, renamed or rejected out loud. This inverts
the question from recall to recognition, which is the difference between an
hour of vague answers and twenty minutes of sharp ones.

**Stereotypes were dropped from labels** on the diagrams that ran widest, and
nobody asked what a shape meant.

## Does it generalize?

| Moment | Verdict |
| ------ | ------- |
| Levels for processes and capabilities | **Yes.** Every organization has them whether or not the model names them |
| The four macro categories | **Yes, for organizations.** They are quality-management standard practice, not this client's invention. Not for a single application, which has no strategic or support processes of its own |
| Detail follows pain | **Yes, and it is the important one.** It is the standing "well-done less is more" principle applied to depth rather than to element count |
| Seeding a capability map from an industry reference | **Yes, with a safeguard.** The same move that makes a good question makes an excellent way to put words in a client's mouth. It has to propose and never fill |
| Dropping the stereotype | **Yes.** The type is already carried by glyph, shape, colour and a mandatory legend |

## What surprised us

**The client had already done level 1 and did not consider it architecture.**
It sat in the quality management system, not in anything anyone called an
architecture, and it was better than what a discovery conversation would have
produced from scratch. The method assumes an organization arrives with
canvases to fill and nothing else; this one arrived with the top of its process
model already correct.

**Naming the branches that would *not* be detailed was received better than
the detail itself.** The expectation was that scoping down would read as
scoping out. It read as judgement — as the difference between a consultant and
a transcript.

## Deliberately not recorded

The client, the industry, the process names, the pain, and the reference model
matched to that industry — all of which would identify the organization to
anyone in its market. What is above is the shape of the engagement with those
removed; nothing in it depends on which business it was.

## Proposed

| # | Skill or document | The sentence it would add | Raised as |
| - | ----------------- | ------------------------- | --------- |
| 1 | new skill | An organization's processes and capabilities are modeled in levels; levels 1 and 2 are complete and level 3 exists only where a named pain justifies it | [product initiative 14](../../../product-archreator/architecture/scope/14_a-model-a-human-can-read.md) |
| 2 | new skill | Level 1 of a process model is the macro process map, classified into strategic, operational, support and evaluation | product initiative 14 |
| 3 | new skill | Propose a capability map from a named industry reference model, and have the Requester confirm every item — a reference proposes and never fills | product initiative 14 |
| 4 | `architecture-doc-style` | `«Stereotype»` appears only in a diagram whose subject is the notation itself | product initiative 14 |
| 5 | `operating-model-discovery` | Ask what the organization has already modeled before modeling it — a quality management system often holds a correct level 1 | **not yet** — one case |

**Proposals 1–4 were acted on immediately, against this skill's own advice to
wait for a second note.** The rule exists to stop an agent generalizing from a
single case; here the Requester who ran the engagement asked for the change
directly. Recorded so the exception is visible. Proposal 5 waits, because it is
the one nobody has asked for.
