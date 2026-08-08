# Value Proposition Canvas

_[← Business design](./README.md) · [EA home](../README.md)_

**Strategyzer artifact, not ArchiMate.** One canvas per customer segment.
Layers 1 and 2 are *derived* from this after **Gate 0** — nothing below this
folder is written until the Requester approves what is here.

**Status: discovery in progress.** Segments identified; the profile for
Customer Segment 1 is written. Customer Segment 2's profile and the value
map are **Pending — this initiative**.

## Segments

| ID | Customer segment | Pays | Uses | Decides |
| --- | --- | --- | --- | --- |
| `CS1` | **Customer Segment 1 — Business and solution designers.** Enterprise architects at any level of experience, business analysts, and entrepreneurs acting as their own designer | Nothing today | ✅ Directly | On their own small projects |
| `CS2` | **Customer Segment 2 — Business owners commissioning the outcome.** A company that wants the deliverable and has no designer of its own | ✅ Consulting hours | ❌ Today, no — ✅ in the target state | ✅ Commissions and accepts the work |

`CS1` is the segment the project is **built around**, and the one that would
notice first if it stopped — a designer part-way through modeling something.
`CS2` is where money changes hands today, and it reaches archreator only
through a designer: the Requester, or another designer using it to deliver.

**One merged role, not two.** "Business and solution designers" names a
single role, not two roles grouped into a segment. Today the two ends are
split — designers do not generally deliver solutions, and solution builders
do not generally understand the business as a whole — and the whole point is
to **blur that boundary and let either end reach the other**. The segment is
named for the role the method creates, not the roles the market currently
has.

The Requester's framing, kept verbatim because it is the sharpest statement
of what the project is for:

> Merge business design and solution design **vertically**, with actual
> deliverables and outcomes — not only design (which doesn't deliver
> anything), and not only solutions (which are made inconsistently and are
> harder to maintain).

**Where the target state points.** The greatest value of the planned
enterprise-architecture-as-a-service offering is for `CS2`, not `CS1`: a
business owner with no designer available needs something lightweight that
speaks a simpler language. That makes `CS2` a *user* in the target state,
not only a payer — and it needs its own profile, which is the next
discovery round.

---

## Customer profile — `CS1` (Customer Segment 1: business and solution designers)

### Jobs to be done

| ID | Job | Kind |
| --- | --- | --- |
| `JOB1` | **Understand the problem before framing a solution.** Most solutions do not fail because they were technically hard — they fail because the problem was not properly understood. A good answer to the wrong question | Functional |
| `JOB2` | **Make the business's intention explicit and confirmable**, so everyone can agree on the problem before anyone frames an answer to it | Functional |
| `JOB3` | **Produce a design that guides implementation**, not one that stops at description. Design that cannot be built from is not finished work | Functional |
| `JOB4` | **Consolidate what is scattered** — insights from many documents and conversations, across business and technology, mapped onto architectural elements, new or existing | Functional |
| `JOB5` | **Do credible architectural work without decades of accumulated context.** Take the enterprise landscape in pieces rather than waiting for years of experience to settle it in your head | Social / emotional |

`JOB5` is the one a senior architect will not say out loud and a
non-senior one feels constantly. It is stated here because the Requester
named non-senior architects and analysts as the people who gain most.

### Pains

| ID | Pain | Severity |
| --- | --- | --- |
| `PAIN1` | The problem is misunderstood, and the work is a good answer to the wrong question | Unacceptable — it is the primary cause of failure |
| `PAIN2` | **Time to market.** The path from a business need to something delivered is too long | **Unacceptable** — stated as such |
| `PAIN3` | **The design-to-solution gap.** Designers do not deliver solutions; solution builders do not understand the business as a whole. The roles are split, so there are too many gates where information mutates and misaligns, and constant friction between what the business expected and what it got | **Unacceptable** — stated as such |
| `PAIN4` | Consolidating scattered information is one of the key burdens of architectural work: many documents, many meetings, and — where a landscape already exists — Visio files, Archi diagrams, wikis, enterprise-architecture repositories and portals, Word and Excel documents | Annoying, constant, absorbed |
| `PAIN5` | Judging what in an existing landscape is still current and what needs updating, before anything can be trusted | Annoying, constant, absorbed |
| `PAIN6` | **AI is already used for most of these activities, but in isolation — there is no framework behind it.** The designer *is* the framework, holding everything together by hand | Annoying today; the reason the others persist |

`PAIN6` is the load-bearing one. The others are long-standing;
what is new is that the tooling to relieve them now exists and has nothing
holding it together.

### Gains

| ID | Gain | Kind |
| --- | --- | --- |
| `GAIN1` | **Speed with structure** — moving fast without the output becoming inconsistent | Required |
| `GAIN2` | **Documentation ready to put in front of the business for validation**, without a rewrite. Human-legible by construction, which is why diagrams are preferred over walls of prose | Expected |
| `GAIN3` | **The ability to implement.** Let AI do the technical work and deliver from the design — the design is the input to building, not a document handed to someone else | **Delight** — this is the differentiator |
| `GAIN4` | **A methodology usable at any level of experience**, so competence comes from the method rather than only from seniority | Expected |
| `GAIN5` | **Designers lead the implementation** rather than handing it off — reaching an end of the process usually delegated to other roles | Delight |

## Customer profile — `CS2` (Customer Segment 2: business owners)

**Pending — this initiative.** The next discovery round. It matters more
than it first appeared: `CS2` is the segment the target-state service is
aimed at, and it needs a *simpler language* than `CS1` does.

## Value map

**Pending — this initiative (themes 5–6).** Products, pain relievers, and
gain creators, plus the fit check that every pain has a reliever and every
gain has a creator.

One anchor is already fixed. **Structured natural language over modeled
enterprise entities is a pain reliever, not the product.** The product is
that interface *plus running it to deliver outcomes* — business design and
solutions both. The distinction decides where it lands on the canvas, and it
is the same distinction that separates this from a notation.

## Resolved during discovery

| # | Question | Answer |
| - | -------- | ------ |
| 1 | Does the target-state service serve `CS1` paying for the first time, or `CS2` directly? | **`CS2` directly.** That is where the greatest value is: a business owner with no designer available, needing something lightweight in simpler language. `CS2` becomes a user, not only a payer |
| 2 | Is "non-profit" a decided posture or a current description? | **A posture, and a durable one.** Even if the initiative scales, the intent is not to charge much beyond operational cost. It constrains the revenue block and will shape the Goals at Gate 1 |
