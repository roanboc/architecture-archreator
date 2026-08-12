# 1 — Take `COA1` before `COA2`, in four stages

_[← Decisions](./README.md)_

**Status:** Accepted
**Date:** 2026-08-09
**Touches:** [`COA1`, `COA2`, `CAP10`](../1_strategy/2_capabilities-and-resources.md),
[`DOBJ7`](../3_information/1_data-objects.md)

## Context

Two courses of action have sat Pending since Gate 0, and
[the strategy layer](../1_strategy/2_capabilities-and-resources.md#courses-of-action)
records that they **pull opposite ways on `RES1`** — the Requester's time.
`COA1` (AI agents acting as consultants) would relieve it; `COA2` (build the
portal) would spend a great deal of it first. Which came first was left
open, deliberately, as a strategy decision rather than a sequencing detail.

The Requester has now chosen `COA1`.

## What `COA1` actually is

The model already contains the contradiction that defines it.

`PROD2` is delivered by `BSVC3`, whose realizing artifact is "`ROLE2`, in
person", and [layer 4](../4_application/1_application-services.md#what-the-business-does-not-get-from-software)
states the consequence plainly: **there is no software to scale.** Meanwhile
`CAP9` claims *method-carried competence* — the expertise sits in the method,
so the price of an architecture drops to the price of an agent.

**Both cannot be fully true.** If the method already carried the competence,
hiring the Requester would add nothing. It does add something, and nobody has
ever written down what.

That gap is `COA1`. So the course of action is not "build an AI consultant
product". It is:

> **Find what the consultant does that the method does not tell anyone to
> do, and move it into the method.**

Which makes `COA1` the completion of `CAP9` rather than a new direction.

## Options considered

| Option | Consequence |
| ------ | ----------- |
| **`COA2` first — build the portal** | Ships a delivery channel for `CAP9` before anyone has verified `CAP9` holds. Needs `NODE4`, `DOBJ6` and `PROD3`, all Pending, and spends `RES1` heavily before returning anything |
| **`COA1` first — capture, then encode** | Needs nothing new. Improves `PROD1` as a side effect, because everything encoded ships in the open method. Measurable, which almost nothing else here is |
| **Neither — accept the ceiling** | Legitimate: the Requester has no interest in scaling large. But it leaves `CAP9` overstated in a model that is published as evidence, which `P4` rules out |

## Decision

**Take `COA1` first, in four stages, with client-facing as the declared
destination and stage 1 running behind the Requester.**

| Stage | What changes | What it needs |
| ----- | ------------ | ------------- |
| **1 — Capture** | Every completed engagement **or initiative** produces a pattern note: what the method did not tell you to do, and what you did instead | Nothing new. Delivered by [scope document 3](../scope/3_take-coa1-stage-one.md) |
| **2 — Encode** | Patterns that recur move into skills. Success is the Requester's hours per engagement falling | Stage 1 evidence, across more than one engagement |
| **3 — Delegate, behind the Requester** | `ACT2`'s autonomy raised inside `ROLE2` for defined parts — running discovery rounds, drafting the model — with the Requester still in the room | Its own decision record |
| **4 — Client-facing** | An agent runs discovery with a client directly, the Requester reviewing at gates | Holding client data — a layer 3 change this organization has never made — plus an autonomy decision, plus stage 2 evidence |

**Stage 4 is the declared destination, not a schedule.** Naming it matters:
it tells stage 3 what to build toward, and it makes the layer 3 obligation
visible now rather than as a surprise later.

## Why stage 1 runs on any initiative, not only paid engagements

The obvious reading of `COA1` is "learn from clients". That would make the
mechanism wait for `PROD2` work, which is intermittent.

But the same capture applies to any completed initiative — and the evidence
is this repository. The notation standard, the consolidate-before-you-
enumerate principle, and the rule that gate presentations carry full branch
links all came from **exactly this kind of noticing**, done ad hoc during the
work and never captured as a mechanism. Widening stage 1 costs nothing and
makes it useful immediately.

## `P1` survives this, and it is worth saying why

`P1` holds that humans hold strategy and business judgment; AI assists and
executes. An AI acting as consultant looks like a violation.

It is not. **The consultant never held the client's judgment either.** The
client holds it, at their own gates. What an agent takes over is *running the
method* — `ROLE2`'s work — not the client's authority over their own
business. What *would* violate `P1` is an agent deciding what a client's
business is, and the gates exist precisely to prevent that.

Stage 4 will need this argument to survive contact with a real client. It is
recorded now so that it is argued rather than assumed.

## Consequences

- **`CAP10` is added** — engagement-to-method learning — under `CAP2`. It is
  the first capability this organization has for improving `RES2` on purpose
  rather than by noticing.
- **`RS1` gets its first mechanism.** The primary non-monetary return has
  been claimed since Gate 0 with nothing behind it. `CAP10` is that
  something. `RS1` itself is a layer 0 element and is not edited.
- **`DOBJ7` is added**, and it is the first thing in this model that crosses
  from confidential to public — patterns extracted from `DOBJ4` with client
  facts removed. The rule governing that crossing is part of stage 1's
  deliverable, not a later refinement.
- **`COA2` is not abandoned**, only ordered. It stays Pending, and stage 2's
  evidence is what would justify it: a portal is worth building when the
  method can carry consultant-grade competence, and not before.
- **A measurement exists.** Hours per engagement is observable because
  clients are known — unlike adopters (`DOBJ5`), whom this organization
  cannot see. It is the only place in this model where an outcome can be
  measured without holding data on anyone.

## What would reopen this

**Stage 1 producing nothing generalizable across several engagements.** That
would not mean the plan failed — it would mean `CAP9` is overstated, and the
thing to fix is the strategy layer rather than the sequencing. The honest
consequence would be to narrow `CAP9` and reconsider whether `PROD3` should
exist at all.
