# Project Scope — Referencing across models

_[← Scope index](./README.md) · [EA home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Status: proposed, not approved.** Gate 2 was declined on 2026-08-12 —
twelve business rules already exist and a thirteenth was judged not to earn
its place yet. [Open question 11](./open-questions.md) stays open, and this
document is the analysis behind it rather than an initiative that ran. Nothing
here has been implemented.

archreator tells every adopter to federate: model the organization once, and
give each application its own project consuming that model. It provides no way
for one of those models to **reference an element in another**. Identifiers are
scoped per project, so a document in `org-archreator/` writing `` `RULE11` ``
— an element `product-archreator/` owns — is not a citation but a dangling
reference, and `check_model` correctly rejects it.

That was discovered the hard way in
[initiative 10](./10_what-belongs-at-which-tier.md), which wrote a rule about
tiers deferring to one another and then could not make one tier cite the
other's rule. The workaround shipped there — naming the owning skill and
section in prose — is what this initiative replaces.

## Why now, and why it is testable now

The method already solves this **one level down**.
`architecture-doc-style` § Namespacing across domains qualifies an identifier
by its owning domain (`SALES.BSVC3`), keeps numbering per prefix per domain,
and states the reason: *"forcing globally unique numbers would make every new
domain a merge conflict against every other."* That argument applies unchanged
one level out. This initiative extends the existing rule rather than inventing
a second scheme.

**No second repository is needed to test it.** `org-archreator/`,
`product-archreator/` and `product-archreator/site/` are already three
separate identifier namespaces — that is why the failure happened at all. The
notation and its validation can be exercised against them today. Only
*physical availability* — whether a parent model is on disk when a child is
checked — depends on a second repository, and that case is handled by
degrading rather than failing.

## What this deliberately does not build

The Requester's constraint was to avoid over-engineering, and two tempting
mechanisms are refused:

**No allocated prefixes.** A scheme numbering repositories (`E`, `P1`, `I1`, …)
needs someone to allocate the numbers and keep a register — and that register
*is* a central catalogue. The repository name is already globally unique,
allocated by the host at creation time, and free.

**No identifier encoding its position.** Linking a number to the product or
initiative it belongs to breaks `RULE5`: an identifier is assigned once and
never reused, and one that encodes where a thing sits has to change when the
thing moves. Every tree in this repository moved twice in two days.

**No central catalogue.** For *identity* it is unnecessary — the qualifier
carries the ownership. For *discovery* — "what already exists that I could
reuse?" — it is the model database, which
[decision 4](../decisions/4_defer-the-model-database.md) already deferred with
four recorded triggers. Cross-model reuse becoming real would be a fifth
trigger to add there, not a new mechanism here.

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 1_strategy | **No change.** `P3` — each fact in exactly one document — is what a qualified reference serves: it lets a model point at a fact instead of copying it |
| 2_business | **`RULE13` added.** `RULE5` gains a clarifying sentence — qualification is addressing, not a change to how identifiers are assigned |
| 3_information | **No change** |
| 4_application | **`ACMP6` and `ACMP15` change** — the notation authority gains the cross-model form, and the validator learns to resolve it and to report an unresolvable-but-declared reference as its own class rather than an error |
| 5_technology | **No change.** How a parent model becomes physically available to a child repository is left open — see the gap notes |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — the subject is the method at Depth 1 |
| Gate 1 — Strategy | — | — | **N/A** — no Stakeholder, Driver, Goal or Principle added or modified |
| Gate 2 — Business | Requester | 2026-08-12 | **Not granted.** `RULE13` judged not to earn its place against `P5` — consolidate before enumerating. The problem stays recorded as open question 11 |
| Gate 3 — Solution design | — | — | **N/A** — Gate 2 not granted |

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | Three models, three identifier namespaces, and no way for one to cite another. The method recommends federation to every adopter and leaves the first cross-model citation to be invented under pressure |
| **Target** (delivered) | A qualified form that reuses the domain rule one level out, validated where the owning model is present and reported rather than failed where it is not |

## The notation, as proposed

| Where the reference is written | How it is written | Example |
| ------------------------------ | ----------------- | ------- |
| Inside the model that owns the element | bare | `RULE11` |
| From another **domain** of the same model | `<DOMAIN>.` prefix | `SALES.BSVC3` |
| From another **model** | `<model>:` prefix | `product-archreator:RULE11` |

**Two separators, two axes.** A dot crosses a domain boundary inside one
model; a colon crosses a model boundary. A reader can tell which without
knowing the repository, and a domain and a model may share a name without
ambiguity.

The qualifier is the owning model's directory or repository name, lower case,
exactly as it appears — no upper-casing, because unlike a domain folder it is
a proper name that may be typed into a URL.

**References are one-directional.** A model cites the tier above it. The tier
above never cites down: an enterprise names *that* an application exists and
links to its model, not to its elements (`RULE11`). This is what removes the
coordination problem — a new child needs to know its parent, and the parent
needs to know nothing about the child, so no model needs the context of models
that do not exist yet.

**Only what the tier above exposes may be cited**, extending the constraint
domain charters already carry. Reaching past a parent's exposed surface into
its internals is the same modeling error one level down.

## Work packages and deliverables

### WP1 — The notation

- **Deliverables:** `architecture-doc-style` § Namespacing across domains
  becomes § Namespacing, covering both axes, with the table above, the
  one-directional rule and the exposure constraint.
- **Outcome:** the first adopter to federate has a correct way to write a
  cross-model citation instead of inventing one.

### WP2 — `RULE13`

- **Deliverables:** `RULE13` — a reference to an element another model owns is
  qualified by that model's name and points only at what that model exposes —
  in [`2_business-services.md`](../2_business/2_business-services.md), plus a
  clarifying sentence on `RULE5`.
- **Outcome:** the rule is a model element, traceable like the others.

### WP3 — Teach the validator

- **Deliverables:** `check_model` parses `<model>:ID`; resolves it against
  that model when it is discoverable in the repository; **reports it as
  declared-but-unresolvable when the model is absent**, counted in the summary
  rather than failed; and errors when the model *is* present and the element
  is not defined there.
- **Outcome:** a child repository checked on its own does not fail for
  citing a parent it cannot see, and does fail for citing something that
  does not exist.

### WP4 — Exercise it, and close open question 11

- **Deliverables:** the prose workaround in
  [`org-archreator/architecture/4_application/2_application-components.md`](../../../org-archreator/architecture/4_application/2_application-components.md)
  becomes a real citation of `product-archreator:RULE11`, validated by WP3.
  Open question 11 moves to Resolved.
- **Outcome:** the notation is demonstrated on the case that motivated it,
  not asserted. This is the test the Requester asked to be ready for.

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| The notation, the rule, and validation across models in one repository | **How a parent model becomes physically available to a child repository** — submodule, published artifact, or vendored copy. No second repository exists yet, and the answer will be clearer when one does |
| Resolving and reporting cross-model references | A catalogue of what exists to be reused — that is the deferred model database |
| One-directional citation | Any mechanism for a parent to discover its children |
| Replacing the workaround initiative 10 shipped | Migrating the site's model, still deferred |

## Gap notes

- **Physical availability is unanswered on purpose.** A submodule pins the
  parent at a commit, which makes the coupling explicit and means a parent
  cannot shift under a child without a deliberate bump; it costs a credential
  when the parent is private. A published artifact gives versioned semantics
  and more machinery. Both work; neither is worth choosing before a second
  repository exists, and WP3's degrade-rather-fail behavior is what makes
  postponing safe.
- **The one-directional rule is carried by review.** Nothing detects a parent
  citing a child's element — it would simply be an unresolvable reference in a
  model with no parent, which WP3 reports rather than fails. Making it an
  error would require knowing which model is above which, and nothing records
  that today except prose.
- **The qualifier is a name, so renaming a model breaks every citation of
  it.** That is the same exposure the directory names already carry, and the
  same mitigation applies — it is a rename plus a repair, mechanical and
  greppable. Worth stating because a scheme of allocated numbers would not
  have this property, and it is the one real thing given up by refusing them.

## Open questions

- **Should a cross-model citation record the version it was written against?**
  Adopted interpretation: **no, not yet.** A bare `product-archreator:RULE11`
  says nothing about which commit of that model was true when it was written,
  so a parent can silently change under a child. A submodule pin would answer
  it structurally, which is a reason to prefer one when the question becomes
  real. Recorded rather than solved. Mirrored to
  [open questions](./open-questions.md).
