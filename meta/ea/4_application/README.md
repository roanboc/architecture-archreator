# Application layer — archreator

_[← EA home](../README.md)_

**ArchiMate viewpoint:** Application layer.

archreator's "application" is unusual: most of it is markdown that a
language model reads and acts on. That doesn't exempt it from the layer —
a skill is a component with a responsibility, a dependency set, and a
contract with its callers, and modeling it as one is what makes the
grounding rule checkable here.

## Analysis order

| # | Document | Covers | Answers |
| - | -------- | ------ | ------- |
| 1 | [1_application-components.md](./1_application-components.md) | Application Component, Application Service | What realizes each business service, and where the file is |

`2_solution-design.md` and `3_interface-contracts.md` are **not started** —
there is one interface (a `SKILL.md` frontmatter description that Claude Code
matches against) and it is described inline.
