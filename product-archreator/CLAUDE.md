# CLAUDE.md

The architecture model of **archreator the method**, treated as the product it
is. The method's own source — skills, scaffold, validators, docs — lives in
the [`archreator`](https://github.com/roanboc/archreator) repository; this
tree is the model *of* it.

Repository-wide rules, the actors and the commands are in the
[root `CLAUDE.md`](../CLAUDE.md). This file carries only what is specific to
this tree.

## Modeling depth

**Declared depth: 1 — Application.**

The subject is one deliverable with one aim, not an organization. It has no
customers of its own, no revenue and no staff — those belong to
[`org-archreator/`](../org-archreator/architecture/README.md) one tree up, and
this model consumes that one rather than restating it. So
`0_business-design/` stays empty and says so, `domains/` stays unused, and
**Gate 2 is the gate that applies** to a change here. Gates 0 and 1 belong to
the organization's tree.

## What this tree does not model

**The process model.** `BPROC1`–`BPROC4` and their level-2 children live in
`docs/process/` of the `archreator` repository, beside the skills that realize
them. The reason is in
[decision 1](./architecture/decisions/1_the-process-model-stays-with-the-skills.md):
the catalogue exists so that CI can prove every process has a skill and every
skill a process, and that proof only works where both sit together.

`2_business/` therefore models the services, actors, roles and rules of the
method, and states where the process catalogue lives rather than copying it.

## Structure

- `architecture/` — the six numbered layers describing the method as it is
  today, plus `scope/` (one document per initiative) and `decisions/`.
- `site/` — a tree of its own, for the published guidance site. It nests here
  because it realizes one of this product's services rather than standing
  alone.

## Conventions

Beyond the repository-wide ones:

- **This model describes the method, not the repository that holds it.** A
  statement about how many files something takes belongs nowhere; a statement
  about what the method can do belongs in a layer.
- **An element names what realizes it** — a skill file, a script, a manifest —
  or is marked `Pending — future initiative`. An element grounded in nothing
  is a claim, not an architecture.
