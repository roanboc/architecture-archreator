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
| `CS2` | **Customer Segment 2 — Established business owners.** A running company with operational knowledge and existing documentation, but no structure or shared language a builder can act on | ✅ Consulting hours today | ❌ Today — ✅ in the target state | ✅ |
| `CS3` | **Customer Segment 3 — Founders at the idea stage.** Pre-operational: a business model in formation, nothing running yet, wanting to refine the idea and prototype at the same time | Rarely — price sensitivity is highest here | ❌ Today — ✅ in the target state | ✅ |

`CS1` is the segment the project is **built around**, and the one that would
notice first if it stopped — a designer part-way through modeling something.
`CS2` and `CS3` are where the target-state service is aimed, and where the
Requester says the greatest value lies: owners who want to build a solution
**by themselves**, with small businesses and startups named as the key
target.

### Why `CS2` and `CS3` are two segments and not one

Both are "business owners", and separating them is a judgement worth
justifying. They differ on every axis the profile records:

| | `CS2` established owner | `CS3` pre-operational founder |
| --- | --- | --- |
| Core job | Confirm and correct what they believe they already know | Form a model that does not exist yet, and re-form it after each pivot |
| Dominant pain | Blind spots; knowledge trapped in the owner's head | Churn — re-explaining to each new builder, pivots discarding earlier work |
| Dominant gain | An organizational brain others can read without the owner mediating | Pivot without losing the design, and show value early |
| First contact with the product | **Ingest** — existing documentation feeds a draft architecture | **Elicit** — nothing to feed, so it has to be drawn out through questions |

The last row is decisive: the first run is a materially different product
experience. A single merged profile would average two real segments into one
true of neither.

**Split by business stage, not by how they buy.** An owner who commissions
a designer today and self-serves tomorrow is the same person at two moments,
not two segments — that distinction is a **customer relationship and channel**
difference and belongs in the business model canvas, not here.

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

## Customer profile — `CS2` (Customer Segment 2: established business owners)

### Jobs to be done

| ID | Job | Kind |
| --- | --- | --- |
| `JOB6` | **Build a solution themselves**, without a designer standing between the intention and the thing built | Functional |
| `JOB7` | **Give their own knowledge a structure and a language a builder can act on** — where the builder is increasingly an AI system | Functional |
| `JOB8` | **Actually understand their own business.** Nobody knows their business fully until they have considered all the architectural elements; owners routinely frame it wrongly — identifying the wrong customer segments, for instance. Designing *is* the understanding | Functional |
| `JOB9` | **Be understood by others without personally doing the alignment every time** — internal teams, stakeholders, and any builder who joins | Social |

`JOB8` is the counter-intuitive one and the Requester was emphatic about it:
the architecture is not a record of a strategy already known, it is how the
strategy gets confirmed or corrected. An owner arrives believing they know;
the process is what tests that.

### Pains

| ID | Pain | Severity |
| --- | --- | --- |
| `PAIN7` | **Enterprise architects are expensive**, so this segment does not hire them at all | Unacceptable — it is why the segment is unserved |
| `PAIN8` | **Knowledge is lost between builders.** The owner directs a builder over many calls; the knowledge is never properly designed, so when the next builder arrives the owner explains it all again | **Unacceptable** — the churn compounds |
| `PAIN9` | **Documentation that does not drive a solution is useless to them.** A deliverable they cannot build from is a cost, not an asset | **Unacceptable** — stated plainly |
| `PAIN10` | **Blind spots about their own business**, because nothing forces a complete frame | Serious, and invisible until something fails |

### Gains

| ID | Gain | Kind |
| --- | --- | --- |
| `GAIN6` | **Understanding their business at wider and deeper scope**, with strategic and business gaps surfacing *during* the process rather than after | Required — the Requester ranked this first |
| `GAIN7` | **A shared vision they can hand to designers and builders** to accelerate delivery, and that keeps working as the shared language that holds delivery outcomes together | Expected — ranked second |
| `GAIN8` | **Building specific solutions themselves from the design**, with no designer or builder in between | Delight — ranked third and explicitly optional, depending on appetite |

`GAIN8` is optional by design. It is what a small initiative or a more
technical founder will reach for; assuming every owner wants it would
overstate the proposition.

## Customer profile — `CS3` (Customer Segment 3: founders at the idea stage)

### Jobs to be done

| ID | Job | Kind |
| --- | --- | --- |
| `JOB10` | **Refine the idea and build prototypes at the same time**, rather than finishing the thinking before starting the making | Functional |
| `JOB11` | **Pivot without throwing away what has been designed** — keeping the business design on top, shaping the model as it changes | Functional |
| `JOB12` | **Show value early**, to themselves and to whoever they need to convince | Social |

### Pains

| ID | Pain | Severity |
| --- | --- | --- |
| `PAIN11` | **They know how to start and not how to continue.** Founders work with a business model canvas and value propositions, and then have no path from there to implementation | **Unacceptable** — it is the specific gap this segment falls into |
| `PAIN12` | Same knowledge loss as `PAIN8`, and worse here: with nothing operational to anchor it, everything lives in the founder's head and each pivot invalidates whatever a builder had absorbed | **Unacceptable** |
| `PAIN13` | Enterprise architecture help is out of reach on price, as in `PAIN7`, and more so pre-revenue | Unacceptable |

### Gains

| ID | Gain | Kind |
| --- | --- | --- |
| `GAIN9` | **A path that continues past the canvas** — from business model to something built, without changing tools or losing the thread | Required |
| `GAIN10` | **Pivots that cost less**, because the design survives the change instead of being redone | Expected |
| `GAIN11` | **Horizontal and vertical coverage at once** — the business design staying on top while a prototype gets built underneath it | Delight |

### The language correction

The value here is **better** language, not *simpler* language. Better means
less confusing: standardised concepts with defined relationships. The
distinction matters because it decides the product.

"Simpler" would mean hiding the model from the owner. "Better" means the
standardisation **is** the value — an owner gains a comprehensive view of
their own business precisely *because* the method forced a frame, not
despite it. That is what makes `JOB8` and `GAIN6` possible at all, and it is
why this is not a matter of dumbing anything down.

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
