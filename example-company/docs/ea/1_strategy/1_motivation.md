# Motivation

_[← Strategy layer](./README.md) · [EA home](../README.md)_

**ArchiMate elements:** Stakeholder, Driver, Assessment, Goal, Outcome,
Principle.

Everything here except the Principles is **derived** from
[0_business-design/](../0_business-design/README.md) and approved at Gate 0
before it was written. The `Source` column names the canvas block each
element came from; an element with no source was discovered directly with
the Requester.

## Stakeholders and drivers

| ID | Stakeholder | Concern | Driver | Source |
| --- | --- | --- | --- | --- |
| `STK1` | Mid-market operations lead (external, pays and uses) | Getting a repeatable process into production without an ML team, and defending it afterwards | `DRV1` | `CS1` |
| `STK2` | Solo builder / small team lead (external, pays and uses) | Shipping and maintaining an AI-assisted workflow alone | `DRV2` | `CS2` |
| `STK3` | Founders (internal, owners) | A business whose revenue does not scale one-for-one with consultant hours | `DRV3` | — |
| `STK4` | Consultants (internal, staff) | Doing work that compounds instead of rebuilding the same thing per client | `DRV3` | — |
| `STK5` | Customers' auditors and compliance owners (external, can veto) | Being able to review and defend automated decisions | `DRV4` | `JOB3` |

| ID | Driver | What pressures it |
| --- | --- | --- |
| `DRV1` | **Capability scarcity** — mid-market companies cannot hire or retain ML talent at their size |
| `DRV2` | **Trust deficit** — AI claims cannot be verified before money is committed |
| `DRV3` | **Revenue concentration in consultant time** — the advisory model's cost and revenue rise together |
| `DRV4` | **Audit and regulatory pressure** — automated decisions must be explainable after the fact |

## Assessments

The current-state analysis, derived one-for-one from the canvas pains.

| ID | Assessment | Assesses | Source |
| --- | --- | --- | --- |
| `ASM1` | Customers cannot supply the capability themselves, and the hiring market will not fix it at their scale | `DRV1` | `PAIN1` |
| `ASM2` | Buyers cannot distinguish a credible AI vendor from a confident one before committing budget | `DRV2` | `PAIN2` |
| `ASM3` | Most AI pilots die between demo and production — the gap is operational, not technical | `DRV1` | `PAIN3` |
| `ASM4` | Systems that cannot explain a decision fail audit regardless of accuracy | `DRV4` | `PAIN4` |
| `ASM5` | The smallest and most numerous builders cannot buy consulting at all, and lose structure as they grow | `DRV3` | `PAIN5`, `PAIN6`, `PAIN7` |

## Goals

- **G1 — Customers reach production, not pilots.** Every engagement ends
  with a system running on real work, not a demo. Derived from `ASM3`,
  `GAIN1`.
- **G2 — Every decision we ship is reviewable.** Any automated decision in
  a delivered system can be explained, traced, and defended months later.
  Derived from `ASM4`, `GAIN2`.
- **G3 — Revenue that does not scale with consultant hours.** A growing
  share of revenue comes from `PROD2` rather than `PROD1`. Derived from
  `DRV3`, `ASM5`.
- **G4 — Customers can run it without us.** Handover is a deliverable, not
  a courtesy; the product line is the same promise at a smaller scale.
  Derived from `GAIN3`, `GAIN5`.

## Outcomes

| ID | Outcome | Realizes | Source | Measured by |
| --- | --- | --- | --- | --- |
| `OUT1` | A working process live in weeks | `G1` | `GAIN1` | Elapsed time from engagement start to first production run |
| `OUT2` | A decision trail an auditor accepts | `G2` | `GAIN2` | Audit findings raised against delivered systems |
| `OUT3` | Customer staff operate the system unaided | `G4` | `GAIN3` | Support requests after handover, trending to zero |
| `OUT4` | Guardrails available from day one | `G4` | `GAIN4` | Share of new `PROD2` projects starting from a guardrail template |
| `OUT5` | The product runs without a consultant | `G3`, `G4` | `GAIN5` | `PROD2` revenue as a share of total |

## Principles

**No canvas block feeds these** — they were discovered directly with the
Requester, and they are what every future change gets checked against.

- **P1 — Nothing ships without an evaluation baseline.** A delivered system
  (either product line) carries a documented evaluation of its outputs
  against stated intent before it reaches production. Without a baseline
  there is no way to detect drift later, so "we'll add evaluation after
  launch" is a rejected plan, not a deferred task.
- **P2 — Every AI actor has a named human escalation path.** No AI actor in
  our delivery or in our products escalates to "a human" — it escalates to a
  named Business Role with the authority to act. See
  [1_business-actors-and-roles.md](../2_business/1_business-actors-and-roles.md).
- **P3 — No customer deliverable is locked to one model provider.** Designs
  keep the provider substitutable, and `RES4` is negotiated on that basis.
  This constrains what we can promise on price and on provider-specific
  features, deliberately.

A proposed change that ships without an evaluation baseline, leaves an AI
actor escalating to nobody in particular, or hard-wires a single model
provider into a deliverable violates a Principle here — surface it instead
of proceeding (`ea-first-change`, step 1).
