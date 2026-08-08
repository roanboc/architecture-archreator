---
name: ea-first-change
description: Use when requirements change or a new feature/behavior change is requested in this repo. Assesses whether the change needs strategy discovery first, aligns the change through the enterprise architecture layers (strategy → business → information → application → technology) with explicit Requester approval gates before implementation, records it in a scope document, and only then implements. Not needed for pure bug fixes that change no documented behavior.
---

# EA-first change process

_New to this repository? `README.md` orients a person,
`CONTRIBUTING.md` draws this same process as a
flow, and the `project-bootstrap` skill handles a project that was created
from the template but never set up._

In this repository, **strategy and business architecture are validated
before any other layer is touched** — and "validated" means the Requester
explicitly approves at named gates before development proceeds, the way a
business reference group signs off before building starts. A requirement
change is never implemented directly: it is first aligned through the EA
documents (`docs/ea/`), approved at the gates below, captured in a scope
document (`docs/scope/`), and only then coded. The folder numbers give you
the assessment order.

## The gates

| Gate | When | The Requester approves |
| ---- | ---- | ----------------------- |
| **Gate 0 — Business model** | Only when step 1 finds the initiative is modeling an organization | The Value Proposition Canvas per customer segment and the Business Model Canvas per product, before anything is derived from them — see the `operating-model-discovery` skill |
| **Gate 1 — Strategy** | Only when step 1 triggers strategy discovery | The strategy layer itself (motivation, capabilities, value stream) and the key business elements discovered with it — see the `strategy-discovery` skill |
| **Gate 2 — Business** | Every initiative that changes documented behavior — which is every initiative that will produce code. A docs-only initiative passes Gate 0 and/or Gate 1 instead | The changes (or explicit "no change" verdicts) to `1_strategy`, `2_business`, and `3_information` |
| **Gate 3 — Solution design** | Only if the Requester opts in when asked at Gate 2 | The solution architecture and logical application components, with the good practices and design patterns applied called out |

**This table is the single source for which gate applies when.**
`CONTRIBUTING.md`, `docs/scope/README.md`, and the `scope-doc` skill point
here rather than restating it.

Approval is granted by the **Requester** (see `CONTRIBUTING.md` § Actors)
and recorded in the scope document's **Approvals** table (see the
`scope-doc` skill) — which gate, who approved, when, and what was shown. A
gate that didn't apply gets an `N/A — <why>` row rather than being deleted,
so a reader can tell a skipped gate from a forgotten one. An approval that
isn't recorded didn't happen. Pure bug fixes that change no documented
behavior pass no gates — they follow the bug-fix path in `CONTRIBUTING.md`.

### Where a gate happens

The skill says to *present* to the Requester; this says **where**, because
for a Requester who doesn't work in a terminal that surface is the entire
experience. Pick the one that fits who is approving:

| Surface | Use it when | Why |
| ------- | ----------- | --- |
| **The conversation** (Claude Code in the terminal, desktop, or on the web) | The Requester is in the session with you | Fastest; the discovery back-and-forth already lives here. Web and desktop need no terminal, so a non-technical Requester can use them |
| **A pull-request comment** | The Requester is not in the session, or the approval should be durable and reviewable by others | Post the gate presentation as a PR comment and let the Requester reply. The reply *is* the record — it satisfies "an approval that isn't recorded didn't happen" without anyone editing a file, and reviewers can see it later |
| **A published view of the model** | Stakeholders need to read the model but will never open GitHub | Only worth it once the project publishes a site |

Whichever surface is used, the approval is still transcribed into the scope
document's Approvals table with its date and what was shown — the table is
the durable record, the surface is just where the conversation happened.

## Step 0 — Check the open-questions log (if the project keeps one)

If this project maintains `docs/scope/open-questions.md`, read it: does any
row bear on the requested change? If the user (or whoever owns the product)
answers one during this conversation, record the answer there and in the
originating scope document's "Resolved" section in the same change, before
continuing. Skip this step if the project has no such log yet — it is
optional (see the `scope-doc` skill).

## Step 1 — Locate the change, then assess strategy

### 1a — Confirm the modeling depth, and say it out loud

`CLAUDE.md` records this project's declared **modeling depth** (see
`docs/ea/README.md` § Modeling depth).
Read it, and check the request against it:

- **The request fits the declared depth** — say which depth you're working
  at in one line, and continue.
- **The request outgrows it** — say so, and what it would cost to deepen.
  Moving from Depth 1 to Depth 2 means the organization becomes the subject
  and the canvases get filled; Depth 2 to Depth 3 means splitting the model
  into domains. A depth change is its own initiative, decided by the
  Requester, not something to absorb quietly mid-change.

If `CLAUDE.md` declares no depth, the project was never bootstrapped — run
the `project-bootstrap` skill first.

Never let the depth go unstated. A Requester who is told "I'm treating this
as Depth 1 — one application, light strategy layer; say the word if you want
the organization modeled properly" can correct you in one sentence. A
Requester who is told nothing finds out three initiatives later.

### 1b — Locate the domain (Depth 3 only)

At Depth 3 the model is split into domains
(`docs/ea/domains/README.md`). Before
assessing anything, name which domain owns this change, and check whether it
touches another domain's **exposed** services. If it does, this is a
cross-domain change: the consuming domains' Requesters approve at Gate 2 too,
and the `domain-modeling` skill governs how the contract changes. At Depth 1
and 2 skip this step.

### 1c — Assess strategy, and decide whether this is discovery

Read `docs/ea/1_strategy/` against the requested change and reach one of
four verdicts, explicitly:

- **Operating-model discovery needed.** Triggered when the subject being
  modeled is an **organization** rather than a single application — a
  company, a department, or a service line whose operating model is itself
  the deliverable — and `docs/ea/0_business-design/` is empty or no longer
  matches. Switch to the `operating-model-discovery` skill: the initiative
  becomes documenting the Value Proposition Canvas per segment and the
  Business Model Canvas per product, ending at **Gate 0**, and then handing
  off to `strategy-discovery` to derive layers 1–2 from the approved
  canvases. Tell the two apart by the subject, not the size of the request:
  "several products share one capability base and I need to model the
  business" is this verdict; "this app needs a new feature" is not.
  **Step 3 still applies** — see "Handing off is not an exit" below.
- **Strategy discovery needed.** Triggered when either (a)
  `docs/ea/1_strategy/` still contains template placeholders — this is the
  first real initiative of a project created from the template — or (b) the
  change adds or modifies a Stakeholder, Driver, Goal, or Principle, or
  reshapes the value stream. Stop treating this as an implementation
  initiative: switch to the `strategy-discovery` skill. The entire
  initiative becomes refining the strategy and discovering the key business
  elements by asking the Requester the important questions, delivered as a
  docs-only initiative that ends at **Gate 1**. Implementation follows as a
  separate initiative — which re-enters this step and now finds the
  strategy filled in and current. **Step 3 still applies** — see below.
- **Conflict.** The change contradicts an existing Principle in
  `1_motivation.md`: stop and surface the conflict to the Requester instead
  of proceeding. Resolving it may amount to changing the Principle — which
  is trigger (b) above.
- **Aligned.** The change serves an existing goal and value-stream stage.
  Record which ones, and continue.

### Handing off is not an exit

Both discovery verdicts switch skills, but they do **not** leave this
process. A discovery initiative is still an initiative: it gets the next
numbered scope document in `docs/scope/`, indexed in `docs/scope/README.md`,
exactly as Step 3 describes — created **before** its gate, so the Requester
approves against a concrete document and the approval has somewhere to be
recorded. Then it finishes at Step 7 (verify) and Step 8 (PR) like any other.

What a discovery initiative skips is Steps 2, 4, 5 and 6 — there is no
business/information alignment to do beyond what discovery itself produces,
no Gate 2, no application layer, and no code. Its Approvals table records
Gate 0 and/or Gate 1, with Gate 2 and Gate 3 marked `N/A`.

## Step 2 — Align business and information

For each layer, read the layer README and answer its question for the
requested change. Update the affected documents as you go (they are part of
the same change set, not an afterthought):

1. **`docs/ea/2_business/`** — Which business services/processes/objects
   are added or changed? New business rules get a row in the rules table of
   `5_domain-context-and-rules.md` (with the _why_) before they get code.
   New terms go into the glossary; reuse existing glossary terms in code.
   If the change adds an actor, or changes an existing AI actor's autonomy
   level or decision rights (`ea-doc-style`'s actor notation), consider a
   `decision-record` alongside the scope document explaining why.
2. **`docs/ea/3_information/`** — New or changed data objects, flows,
   representations, storage, classification, retention?

Layers with no impact still get a "no change" verdict — say so explicitly
in the scope document rather than skipping them.

## Step 3 — Draft the scope document

Create the next-numbered file in `docs/scope/` using the `scope-doc` skill.
Do this **before Gate 2**, so the Requester approves against a concrete
document; refine it as implementation proceeds.

## Step 4 — Gate 2: Requester approval before any code

Present to the Requester, in one message: the changed (or added) strategy,
business, and information documents — or their explicit "no change"
verdicts — and the draft scope document. Then ask two explicit questions:

1. **Do you approve these strategy, business, and information changes**,
   so implementation can start?
2. **Do you also want to review the solution design before it is coded**
   (Gate 3 — the application architecture: logical application components,
   good practices, design patterns)? This is a per-initiative choice aimed
   at technically inclined Requesters; declining it means layers 4–5 are
   covered by ordinary PR review instead.

Do not write application/technology docs or code until question 1 is
answered with an approval. Record the approval in the scope document's
Approvals table; if changes are requested, rework steps 1–3 and present
again.

## Step 5 — Align application and technology (Gate 3 if requested)

1. **`docs/ea/4_application/`** — Which application services/components
   change? New ports/interfaces follow `5_interface-contracts.md`; new
   platforms/adapters follow `4_solution-design.md`.
2. **`docs/ea/5_technology/`** — Any impact on runtimes, build, CI, or
   hosting? If no stack has been chosen yet, use the `stack-selection`
   skill instead of re-deriving one from scratch.

If the Requester opted into **Gate 3** at Gate 2: present the updated
solution design — the affected application services and logical application
components, their ports/interfaces — and name the good practices and design
patterns applied (and, where a pattern is load-bearing, why it is needed).
Wait for approval and record it in the Approvals table before implementing;
rework this step if changes are requested.

## Step 6 — Implement

**First, size the work.** If any work package is too large or long-running
to finish in one sitting — more than a handful of files, or spanning a
break, a session boundary, or a handoff to someone else — shard it with the
`story-sharding` skill before writing code. Each story is then actionable
from its own text and links alone, so whoever picks it up next doesn't
re-derive the plan from the whole EA tree. A small work package needs no
stories; an inline task list in the scope document is the default.

Only now write code. Keep the EA documents and the scope document true to
what is actually delivered — if implementation diverges from the plan,
update them in the same commit series; if the divergence touches what a
gate approved (strategy, business, or information — or the solution design
under an approved Gate 3), take the delta back to the Requester instead of
silently absorbing it. Follow `CONTRIBUTING.md` for the development
workflow (lint, typecheck, tests, build — whatever this project's stack
defines).

## Step 7 — Verify alignment before finishing

- Every new/changed code artifact is named by some EA document.
- Every EA element you added names the code artifact that realizes it, or
  is marked "Pending — future initiative" with a link to the initiative
  that will deliver it — the EA set stays verifiable against the code.
- The scope document's "in scope / out of scope" table matches the diff.
- The scope document's Approvals table has a row for **every** gate, each
  either approved or marked `N/A — <why>` (§ The gates is the single source
  for which applies).
- At Depth 3: every cross-domain ID reference points at a service the owning
  domain's charter actually exposes.
- Cross-links between docs resolve (paths and anchors both — check anchors
  carefully if the doc language uses accented headings).
- If the scope document gained or resolved an "Open question", the
  project's open-questions log (if it keeps one) reflects the same.

**If this was a discovery initiative, say what comes next.** Discovery ends
at Gate 0 or Gate 1 having delivered documents and no code — which is
correct, but a Requester who asked for a feature and received a merged
docs-only PR will reasonably think the process failed to build anything.
Close the loop explicitly: name the request that triggered discovery and
offer to open it as the next initiative. The process only continues if
someone restarts it, so don't leave that to chance.

## Step 8 — PR description

When opening (or updating) the pull request, use the `pr-description`
skill: it picks the right template (default, or
`.github/PULL_REQUEST_TEMPLATE/bugfix.md` for a pure bug fix) and covers
the whole branch (`main...HEAD`), not just the latest commit.
