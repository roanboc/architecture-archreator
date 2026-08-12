# Business design — the organization behind archreator

_[← EA home](../README.md)_

**Not an ArchiMate layer.** This folder holds the Strategyzer canvases that
layers 1 and 2 are *derived* from — the reason the numbering starts at 0.
It is filled in because the subject here is an **organization**, not an
application.

| # | Document | Covers | State |
| - | -------- | ------ | ----- |
| 1 | [1_value-proposition-canvas.md](./1_value-proposition-canvas.md) | Three customer segments — jobs, pains, gains, and the value map that addresses them | **Filled** |
| 2 | [2_business-model-canvas.md](./2_business-model-canvas.md) | One canvas per product — the nine blocks, plus monetary and non-monetary return | **Filled** — three products |

## The rule this folder exists to enforce

**Nothing below this folder is written until the canvases are approved at
Gate 0.** A company's strategy layer is a consequence of its business model,
not an independent statement — so deriving from an unapproved canvas means
redoing layers 1 and 2 when the canvas moves.

**Gate 0 was granted on 2026-08-08**, and
[layers 1](../1_strategy/README.md) and [2](../2_business/README.md) were
derived after it. The rule now cuts the other way: a change to either canvas
is a change to everything derived from it, so it re-enters `architecture-first-change`
rather than being edited in place.

The canvas-block-to-ArchiMate mapping lives in
[the template's business-design README](../../../.claude/skills/project-bootstrap/templates/architecture/0_business-design/README.md#from-canvas-to-archimate)
and is not restated here.
