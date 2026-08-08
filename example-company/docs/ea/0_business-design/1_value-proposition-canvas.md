# Value Proposition Canvas

_[← Business design layer](./README.md) · [EA home](../README.md)_

**Artifact:** Strategyzer Value Proposition Canvas — one canvas per customer
segment. Not ArchiMate; see [the layer README](../../../../docs/ea/0_business-design/README.md#from-canvas-to-archimate)
for how each block is derived into the strategy and business layers.

Solvara AI (fictional) serves two segments that want the same outcome —
an AI-assisted process that actually reaches production — but can afford
wildly different things to get there. That difference is why there are two
canvases here and two business models in
[2_business-model-canvas.md](./2_business-model-canvas.md).

## Segments

| ID | Customer segment | Buys | Derived into |
| --- | --- | --- | --- |
| `CS1` | Mid-market operations lead | `PROD1` advisory engagements | `STK1`, `ACT6` |
| `CS2` | Solo builder or small team lead | `PROD2` AI product subscription | `STK2`, `ACT7` |

## CS1 — Mid-market operations lead

A 50–500 person company. The operations or COO function owns a repeatable,
high-volume process and has been told to "do something with AI". No ML team,
a real budget, and a board asking for evidence.

### Customer profile

| ID | Job to be done | Kind |
| --- | --- | --- |
| `JOB1` | Automate a repeatable operational process without hiring an ML team | Functional |
| `JOB2` | Show the board that the investment produced something | Social |
| `JOB3` | Keep compliance and audit intact while doing it | Functional |

| ID | Pain | Severity |
| --- | --- | --- |
| `PAIN1` | No in-house ML capability, and the talent market for it is out of reach at this size | Extreme |
| `PAIN2` | Vendor claims can't be verified before committing budget | Extreme |
| `PAIN3` | Pilots look good in a demo and then stall before production | Extreme |
| `PAIN4` | AI decisions nobody can review, explain, or defend to an auditor | Moderate |

| ID | Gain | Kind |
| --- | --- | --- |
| `GAIN1` | A working process live in weeks, not quarters | Expected |
| `GAIN2` | A decision trail an auditor accepts without argument | Required |
| `GAIN3` | Staff who can run and change it after the consultants leave | Delight |

### Value map — [`PROD1`](./2_business-model-canvas.md#prod1--advisory-engagements) advisory engagements

| ID | Pain reliever | Addresses | Realized by |
| --- | --- | --- | --- |
| `PREL1` | Fixed-scope readiness assessment producing a costed plan **before** the build is committed to | `PAIN2` | Assessment procedure, Engagement Lead (`ACT1`) |
| `PREL2` | An embedded delivery team supplying the capability the customer can't hire | `PAIN1` | Consultant bench (`RES1`) |
| `PREL3` | A production-readiness gate in every engagement — no phase closes on a demo | `PAIN3` | Engagement procedure, `CAP4` |
| `PREL4` | Decision records and an evaluation trail produced as deliverables, not afterthoughts | `PAIN4` | `CAP3`, evaluation method (`RES2`) |

| ID | Gain creator | Produces | Realized by |
| --- | --- | --- | --- |
| `GCRE1` | Time-boxed phases with a demonstrable increment at the end of each | `GAIN1` | Engagement procedure, `CAP4` |
| `GCRE2` | An audit-ready documentation set handed over with the system | `GAIN2` | `CAP3` |
| `GCRE3` | Handover by paired operation — customer staff run it with us before they run it alone | `GAIN3` | `CAP2`, `CAP4` |

## CS2 — Solo builder or small team lead

One to five people shipping something real. Technically capable, no budget
for consulting, and no one to tell them their architecture is drifting.

### Customer profile

| ID | Job to be done | Kind |
| --- | --- | --- |
| `JOB4` | Ship an AI-assisted workflow themselves, without help | Functional |
| `JOB5` | Keep it from decaying as it grows past what fits in their head | Functional |

| ID | Pain | Severity |
| --- | --- | --- |
| `PAIN5` | Cannot fund a consulting engagement at any price we would charge | Extreme |
| `PAIN6` | No architecture discipline — structure decays as the project grows | Moderate |
| `PAIN7` | AI output drifts from the original intent over weeks, unnoticed | Extreme |

| ID | Gain | Kind |
| --- | --- | --- |
| `GAIN4` | Guardrails available from day one, without having to invent them | Expected |
| `GAIN5` | Something that runs without a consultant on retainer | Required |

### Value map — [`PROD2`](./2_business-model-canvas.md#prod2--ai-product-subscription) AI product subscription

| ID | Pain reliever | Addresses | Realized by |
| --- | --- | --- | --- |
| `PREL5` | Subscription pricing with no engagement minimum | `PAIN5` | Subscription terms (`CTR4`) |
| `PREL6` | An opinionated project structure the product enforces rather than suggests | `PAIN6` | `CAP5`, platform (`RES5`) |
| `PREL7` | Continuous evaluation of output against the stated intent, flagging drift | `PAIN7` | `CAP3`, `CAP5` |

| ID | Gain creator | Produces | Realized by |
| --- | --- | --- | --- |
| `GCRE4` | Guardrail templates shipped as the default, not an advanced feature | `GAIN4` | `CAP1`, `CAP5` |
| `GCRE5` | Self-serve documentation and an in-product assistant (`ACT4`) | `GAIN5` | `CAP6` |

## Fit check

Required by [the layer README](../../../../docs/ea/0_business-design/README.md#fit-is-a-rule-not-a-comment) and
re-run whenever either canvas changes.

| Check | Result |
| --- | --- |
| Every pain has a pain reliever | ✅ `PAIN1`→`PREL2`, `PAIN2`→`PREL1`, `PAIN3`→`PREL3`, `PAIN4`→`PREL4`, `PAIN5`→`PREL5`, `PAIN6`→`PREL6`, `PAIN7`→`PREL7` |
| Every gain has a gain creator | ✅ `GAIN1`→`GCRE1`, `GAIN2`→`GCRE2`, `GAIN3`→`GCRE3`, `GAIN4`→`GCRE4`, `GAIN5`→`GCRE5` |
| Every reliever/creator traces to a capability | ✅ see [2_capabilities-and-resources.md](../1_strategy/2_capabilities-and-resources.md) |
| Every product has a business model canvas | ✅ `PROD1` and `PROD2` in [2_business-model-canvas.md](./2_business-model-canvas.md) |

**`JOB2` is deliberately unserved.** "Show the board something happened" is
a real job for `CS1`, and nothing in either value map addresses it directly —
we produce evidence a board *can* use (`GCRE2`) but we do not do the
convincing. That is a decision, not an oversight: packaging board-facing
narrative would pull the engagement toward presentation work and away from
production systems. Recorded so a future initiative can revisit it rather
than rediscover it.

## Derivation

Per the [mapping](../../../../docs/ea/0_business-design/README.md#from-canvas-to-archimate), this canvas is the
source for:

| This canvas | Derived into |
| --- | --- |
| `CS1`, `CS2` | `STK1`, `STK2` in [1_motivation.md](../1_strategy/1_motivation.md); `ACT6`, `ACT7` in [1_business-actors-and-roles.md](../2_business/1_business-actors-and-roles.md) |
| `JOB1`–`JOB5` | Stakeholder goals in [1_motivation.md](../1_strategy/1_motivation.md) |
| `PAIN1`–`PAIN7` | `ASM1`–`ASM5` in [1_motivation.md](../1_strategy/1_motivation.md) |
| `GAIN1`–`GAIN5` | `OUT1`–`OUT5` in [1_motivation.md](../1_strategy/1_motivation.md) |
| `PREL*`, `GCRE*` | `CAP1`–`CAP6` in [2_capabilities-and-resources.md](../1_strategy/2_capabilities-and-resources.md) |
| `PROD1`, `PROD2` | [2_business-services.md](../2_business/2_business-services.md) |
