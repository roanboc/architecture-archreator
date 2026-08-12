# Strategy & Motivation — the organization behind archreator

_[← EA home](../README.md)_

Who has a stake in this organization, what pressures them, what must become
true, what it must be able to do, and how value flows from a first contact to
a delivered outcome.

**Every element here is derived from [layer 0](../0_business-design/README.md),
which was approved at Gate 0 on 2026-08-08.** The `Source` column on each
document names the canvas block it came from; the block-by-block mapping
lives in
[the template's business-design README](../../../.claude/skills/project-bootstrap/templates/architecture/0_business-design/README.md#from-canvas-to-archimate)
and is not restated here. **Principles are the exception** — no canvas block
feeds them, so they were discovered directly with the Requester.

## Analysis order

| # | Document | Elements | Question it answers | Source |
| - | -------- | -------- | ------------------- | ------ |
| 1 | [1_motivation.md](./1_motivation.md) | Stakeholders, Drivers, Assessments, Goals, Outcomes, Principles | Who cares, what pressures them, what must be true? | Customer Segments, Jobs, Pains, Gains |
| 2 | [2_capabilities-and-resources.md](./2_capabilities-and-resources.md) | Capabilities, Resources, Courses of Action | What must this organization be able to do, and with what? | Pain Relievers, Gain Creators, Key Resources, Key Activities |
| 3 | [3_value-stream.md](./3_value-stream.md) | Value Stream and its stage mapping | How does value flow end to end? | Key Activities, Channels |

## What derivation did to the element count

Deriving is not translating, and the count shows it. Two things happened at
once:

- **Where layer 0 said the same thing twice, layer 1 says it once.** Eleven
  Pain Relievers and Gain Creators became **six Capabilities**, because most
  of them were one ability described from the customer's side and then from
  the method's side. Six customer Jobs became **five job-derived Goals**, for
  the same reason.
- **Where layer 0 said nothing, layer 1 has to.** Drivers, Principles,
  Values and Courses of Action have no canvas block behind them — a canvas
  records what a business offers, not what constrains it or what it has
  chosen not to do yet. Those elements were discovered, not derived.

So this layer is larger than the canvases despite the consolidation, and both
halves of that are deliberate. Where two canvas elements became one, the
`Source` column names both; where an element has no `Source`, it was
discovered directly with the Requester.

Nothing was dropped silently. An element with no derived counterpart would be
one the organization has no way to act on, and the only one is `PREL5` — the
whole thing operating together — which is modeled as the *aggregate* of the
six capabilities rather than as a seventh.
