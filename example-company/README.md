# Solvara AI — a company modeled with archreator

_[← Repository README](../README.md)_

**Solvara AI is fictional.** It is a small AI consultancy that also sells an
AI product subscription, invented to demonstrate what
[archreator](../README.md)'s **company track** produces: an operating model
documented end-to-end, where the architecture itself is the deliverable and
no application is built at all.

If [`example/`](../example/README.md) answers "what does a filled-in
`docs/ea/` look like for a small app", this answers "what does it look like
for a whole company".

## What's here

```
docs/ea/0_business-design/   two value proposition canvases,
                            two business model canvases
docs/ea/1_strategy/          derived from them — motivation,
                            capabilities and resources, value streams
docs/ea/2_business/          actors and roles, products, services, channels
docs/ea/domains/             the two business lines as domains, each with
                            a charter, and the one service between them
docs/scope/                  two initiatives, recording Gates 0, 1, and 2
```

No `site/`, no `src/`, no build. That is not an omission — it is what an
operating-model initiative delivers.

## Start here

Read in this order and each document answers a question the previous one
raised:

1. [The two value proposition canvases](./docs/ea/0_business-design/1_value-proposition-canvas.md)
   — two customer segments, what they're trying to do, what hurts, and what
   relieves it.
2. [The two business model canvases](./docs/ea/0_business-design/2_business-model-canvas.md)
   — how each product is delivered and paid for, and what the two share.
3. [The derived strategy](./docs/ea/1_strategy/1_motivation.md) — where
   every stakeholder, driver, assessment, goal, and outcome came from.
4. [The business layer](./docs/ea/2_business/1_business-actors-and-roles.md)
   — who does the work, including two AI actors.
5. [The two domains](./docs/ea/domains/README.md) — why the two business
   lines are modeled separately, what each exposes, and the single service
   that crosses between them.
6. [The scope documents](./docs/scope/README.md) — the record of what was
   approved, at which gate, and what was deliberately left out.

## The four things this example exists to show

**1. The architecture is derived, not invented.** Every element in layers 1
and 2 carries a `Source` column naming the canvas block it came from. The
only elements with no source are the three **Principles** — which the
method says are discovered directly with the Requester, because no canvas
block produces them.

**2. One business model canvas per product, not one per company.** `PROD1`
(advisory engagements) and `PROD2` (the subscription) share every key
partner and three of six capabilities, and agree on nothing else: opposite
channels, opposite customer relationships, and dominant costs that scale on
different axes. A single merged canvas would have averaged that into
something true of neither. The
[shared-versus-different table](./docs/ea/0_business-design/2_business-model-canvas.md#what-the-two-share)
is where the operating model actually lives.

**3. Two AI actors, two autonomy levels, for a stated reason.** The
**Delivery Copilot** (`ACT3`) drafts consulting work at **co-pilot**
autonomy — a human approves before anything reaches a customer system. The
**Product Agent** (`ACT4`) acts inside a subscriber's own project at
**autonomous with checkpoint** — no prior approval, the customer can revert.
The difference follows [who bears the consequence and who can undo
it](./docs/ea/2_business/1_business-actors-and-roles.md#internal-actors),
not how capable each one is. Both escalate to a **named role**, which
principle `P2` requires and the actor diagram makes checkable.

**4. A domain boundary turns a gap into a commitment.** The two lines are
modeled as [domains](./docs/ea/domains/README.md) because they meet four of
the five [split tests](../docs/ea/domains/README.md#when-to-split-a-domain-out)
— different customers, different economics, different decision rights,
different capabilities. The fifth, *a named interface*, was the one they
failed, and fixing it is what the split was worth. `COA1` — the strategic
bet behind `G3` — depended on `RES6`, an engagement archive listed as
pending in a resource table that no role owned. Asking "what exactly does
Advisory owe Product?" turned it into `ADVISORY.BSVC9`, an exposed service
with an owner, an escalation path, and a domain on the other side that
notices when it doesn't arrive.

## What it deliberately doesn't do

The model states its own gaps rather than hiding them — `ADVISORY.BSVC9` is
exposed but unbuilt, both domains carry charters with no layer folders yet,
both product lines share a single cloud host with no mitigation, and one
customer job is knowingly unserved. They are in the gap notes of
[initiative 1](./docs/scope/1_model-the-operating-model.md#gap-notes) and
[initiative 2](./docs/scope/2_split-into-domains.md#gap-notes). A model that
has no gaps is usually a model that hasn't been checked.
