# Decision 1 — Take `COA1` before `COA2`, in four stages

_[← Decisions index](./README.md)_

**Status:** Accepted
**Date:** 2026-08-09
**Touches:** [`COA1`, `COA2`, `CAP2.3` in the strategy layer](../1_strategy/2_capabilities-and-resources.md#courses-of-action)

## Context

Two courses of action have sat Pending since Gate 0, and the strategy layer
records that they **pull opposite ways on `RES1`** — the Requester's time.
`COA1`, AI agents acting as consultants, would relieve it; `COA2`, building
the portal, would spend a great deal of it first. Which came first was left
open deliberately, as a strategy decision rather than a sequencing detail.

The Requester has chosen `COA1`.

## What `COA1` actually is

The model already contains the contradiction that defines it.

Consulting is delivered by a business service whose realizing artifact is a
role, in person, and the application layer states the consequence plainly:
**there is no software to scale.** Meanwhile `CAP3.2` claims *method-carried
competence* — the expertise sits in the method, so the price of an
architecture drops to the price of an agent.

**Both cannot be fully true.** If the method already carried the competence,
hiring the Requester would add nothing. It does add something, and nobody has
ever written down what.

That gap is `COA1`. The course of action is not "build an AI consultant
product". It is:

> **Find what the consultant does that the method does not tell anyone to do,
> and move it into the method.**

Which makes `COA1` the completion of `CAP3.2` rather than a new direction.

## Options considered

| Option | Consequence |
| ------ | ----------- |
| **`COA2` first — build the portal** | Ships a delivery channel for `CAP3.2` before anyone has verified `CAP3.2` holds. Needs an application and technology layer this organization does not have, and spends `RES1` heavily before returning anything |
| **`COA1` first — capture, then encode** | Needs nothing new. Improves `PROD1` as a side effect, because everything encoded ships in the open method. Measurable, which almost nothing else here is |
| **Neither — accept the ceiling** | Legitimate: the Requester has no interest in scaling large. But it leaves `CAP3.2` overstated in a model published as evidence, which `P4` rules out |

## Decision

**Take `COA1` first, in four stages, with client-facing as the declared
destination and stage 1 running behind the Requester.**

| Stage | What changes | What it needs |
| ----- | ------------ | ------------- |
| **1 — Capture** | Every completed engagement **or initiative** produces a pattern note: what the method did not tell you to do, and what you did instead | Nothing new. Delivered by `CAP2.3` |
| **2 — Encode** | Patterns that recur move into skills. Success is the Requester's hours per engagement falling | Stage 1 evidence, across more than one engagement |
| **3 — Delegate, behind the Requester** | The agent's autonomy raised inside its role for defined parts — running discovery rounds, drafting the model — with the Requester still in the room | Its own decision record |
| **4 — Client-facing** | An agent runs discovery with a client directly, the Requester reviewing at gates | Holding client data — an information-layer change this organization has never made — plus an autonomy decision, plus stage 2 evidence |

**Stage 4 is the declared destination, not a schedule.** Naming it matters: it
tells stage 3 what to build toward, and it makes the information-layer
obligation visible now rather than as a surprise later.

## Why stage 1 runs on any initiative, not only paid engagements

The obvious reading of `COA1` is "learn from clients". That would make the
mechanism wait for consulting work, which is intermittent.

The same capture applies to any completed initiative — and the evidence is
this repository. The notation standard, the consolidate-before-enumerating
principle, and the rule that gate presentations carry full branch links all
came from exactly this kind of noticing, done ad hoc during the work and never
captured as a mechanism. Widening stage 1 costs nothing and makes it useful
immediately.

## `P1` survives this, and it is worth saying why

`P1` holds that humans hold strategy and business judgement while AI assists
and executes. An AI acting as consultant looks like a violation.

It is not. **The consultant never held the client's judgement either.** The
client holds it, at their own gates. What an agent takes over is *running the
method* — the Agent role's work — not the client's authority over their own
business. What *would* violate `P1` is an agent deciding what a client's
business is, and no stage above proposes that.

## Consequences

- **`CAP2.3` exists because of this decision.** Engagement-to-method learning
  is the only capability with no canvas source; it was added to give stage 1 a
  mechanism rather than a good intention.
- **`COA2` is now explicitly second**, and the model says so rather than
  leaving two Pending courses of action in an unstated order.
- **Stage 4 commits the organization to an information layer it does not
  have.** Holding client data is a category of obligation — retention,
  classification, jurisdiction — that this model has never had to describe.
  Naming it here means stage 3 cannot arrive at it by surprise.
- **Each later stage needs its own decision record.** Stage 3 changes an
  actor's autonomy, which is precisely the recurring case decision records
  exist for.

## What would reopen this

Evidence that `CAP3.2` already holds — an adopter with no seniority producing
an architecture that survives contact with delivery, without the Requester in
the room. That would mean the gap `COA1` targets is smaller than assumed, and
the case for spending `RES1` on `COA2` instead becomes the stronger one.
