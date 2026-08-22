# Decision 1 — The process model stays beside the skills

_[← Decisions index](./README.md)_

**Status:** Accepted
**Date:** 2026-08-22
**Touches:** [2_business/README.md § The process catalogue](../2_business/README.md)

## Context

archreator's own process model — `BPROC1`–`BPROC4`, levelled, with a SIPOC on
every level-2 process — lives in `docs/process/` of the `archreator`
repository. This tree is the model of the method, and a business layer without
its processes looks like a hole.

Two rules pull against each other. Elements belong under `architecture/` in
their numbered layer, which would put the processes here. But each fact has
exactly one home, which forbids keeping them in both places, and the method's
own CI depends on where they sit.

## Options considered

| Option | Why not (or why) |
| ------ | ---------------- |
| **Move the catalogue into `2_business/3_business-processes/`** | Puts the elements in the layer that owns their type, and `check_model.py` would validate them like everything else. But `check_skills.py` binds skills to processes bidirectionally — every process must name a skill that exists, every skill must name a process that exists — and it reads `docs/process/` in its own repository. Moving the catalogue means the method can no longer check itself without cloning this one |
| **Keep it in both places** | Ten processes with a full SIPOC, written twice. The copies drift silently, which is the failure the one-fact-one-place rule exists to prevent |
| **Leave it beside the skills, and say so here** | The catalogue stays where its binding is enforceable; this layer states where it lives instead of copying it |

## Decision

**The process catalogue stays in `docs/process/` of the `archreator`
repository.** `2_business/` models the method's services, actors, roles and
rules, and its process slot names the catalogue's home rather than restating
it.

## Consequences

- **The binding the catalogue exists for stays enforced.** Its stated purpose
  is that "a process no skill implements is a hole in the method, and CI can
  say so" — a check that only works where the processes and the skills sit
  together. Separating them would have kept the documents and lost the proof.
- **The method stays checkable on its own.** `archreator` validates itself
  without cloning this repository, which is what its portability rule asks of
  every piece of method content.
- **This tree's business layer is incomplete by design, and says so.** A
  reader looking for the processes is sent one repository over rather than
  finding an empty section and assuming nobody wrote it.
- **It commits this model to following a document it does not own.** If the
  catalogue is renumbered or restructured in `archreator`, nothing here fails
  — no validator crosses the repository boundary. The mismatch would be caught
  by review or not at all, which is the price of the split.
