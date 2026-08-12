# 8 — Where an implementation's model lives is the Requester's call

_[← Decisions](./README.md)_

**Status:** Accepted
**Date:** 2026-08-12
**Touches:** [decision 7](./7_one-tree-per-federated-project.md), `RULE11`,
[scope document 10](../scope/10_what-belongs-at-which-tier.md)

## Context

[Decision 7](./7_one-tree-per-federated-project.md) established one tree per
federated project and gave a test: *a tree with its own application components
and its own technology is a project, not a folder.* Read literally, that makes
a separate tree the only correct answer for anything with real design of its
own — and it was written before there was any rule about **what** each tier's
model should contain.

Scope document 10 supplies that rule (`RULE11`), and it makes the location
question independent. Once the tier rule says what an implementation's model
holds, where the directory sits stops being an architectural claim and becomes
a working preference.

The two implementations this organization has or plans differ sharply. The
guidance site is a handful of static pages; the portal (`PROD3`, Pending under
`COA2`) would be a running service with inference costs, hosting, and a
security surface. Forcing both to the same answer serves neither.

## Options considered

| Option | Consequence |
| ------ | ----------- |
| **Always a child tree** | Decision 7 read literally. Consistent, and heavy: a small implementation carries a full second model, its own scope index and its own identifier space for very little design |
| **Always local to the product's tree** | One model per product, simplest to read. Breaks down when an implementation genuinely needs a lot of design — the product's layers 4 and 5 fill with detail that belongs one tier down, which is `RULE11` violated from the other direction |
| **The Requester chooses, per implementation** | Matches the actual variance. Costs a decision each time, and an inconsistent-looking repository until someone reads why |

## Decision

**Both are legitimate, and the choice belongs to the Requester, made per
implementation.** Keep an implementation's model local to the product's tree
when it needs little design of its own; give it a child tree when it needs a
lot — enough that its detail would otherwise crowd the product's layers.

`RULE11` is unaffected either way. It governs what the model *contains*, not
which directory holds it.

## Why

**The tier rule made location a non-question.** Decision 7's test was doing
two jobs: deciding whether something was a project, and deciding where it
lived. Once `RULE11` says what each tier owns, only the second job is left,
and it has no architectural content — the same elements, in the same
relationships, in a different folder.

**The variance is real and large.** A static site and a hosted service with
inference costs are not the same kind of thing, and a method that pretends
otherwise will be ignored on one of them.

**This repository demonstrates both, which is worth more than consistency.**
`product-archreator` holds its own implementation detail directly — the
skills are described in its layers 4 and 5 with no child tree — while the
guidance site has one. An adopter reading the repository sees the choice
exercised in both directions rather than described in the abstract.

**A gate is the right instrument for a preference.** archreator's whole
posture is that judgement calls belong to a human at a named moment rather
than to a default nobody chose. This is one of those calls.

## Consequences

- **Decision 7 is narrowed, not reversed.** One tree per federated *project*
  still holds. What no longer holds is the implication that every
  implementation with design of its own must become one.
- **`product-archreator` is now the demonstration of the local case**, and
  its layers 4 and 5 legitimately carry implementation detail for the skills
  while staying high-level about the site. That asymmetry inside one model is
  expected, not a defect.
- **The choice is recorded where it is made** — in the initiative's scope
  document, at Gate 2, alongside the depth declaration.
- **A local implementation that outgrows its home can be split later**, and
  the split is a normal initiative. The reverse — folding a child tree back
  in — is harder, because identifiers were assigned in a separate space and
  the method has no rule for merging two models. That asymmetry is a reason
  to start local when the answer is unclear.

## What would reopen this

A project where the choice turned out not to be free — where keeping an
implementation local, or splitting it out, changed what the model could
express rather than only where it sat. That would mean `RULE11` is
underspecified and the tier rule needs the work, not this decision.
