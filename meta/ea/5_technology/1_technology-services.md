# Technology Services — archreator

_[← Technology layer](./README.md) · [EA home](../README.md)_

**ArchiMate elements:** Node, Technology Service, Artifact.

The stack is deliberately close to nothing. archreator has no runtime, no
database, no dependencies, and no build. Everything below either ships with
the developer's machine or is a GitHub feature.

## Nodes

| ID | Node | Runs | State |
| -- | ---- | ---- | ----- |
| `NODE1` | Claude Code | `ACMP1`–`ACMP12` — the skills are loaded and executed by it, from `.claude/skills/` or from the installed plugin | In use |
| `NODE2` | GitHub Actions | `ACMP13` on every PR and every push to `main` touching markdown or HTML | In use — [`.github/workflows/docs-check.yml`](../../../.github/workflows/docs-check.yml) |
| `NODE3` | GitHub Pages | The guidance site built by the `example/` project | In use — [`.github/workflows/deploy-example-site.yml`](../../../.github/workflows/deploy-example-site.yml) |
| `NODE4` | Python 3 standard library | `ACMP13`. No packages, no lockfile, no `setup-python` step — the runner's Python is enough | In use |
| `NODE5` | Git | The model's storage and its history. `RULE6`'s immutability is enforced by convention, not by git — nothing prevents editing a merged scope document except the rule | In use |

## Technology services

| ID | Service | Realizes | Realized by |
| -- | ------- | -------- | ----------- |
| `TSVC1` | Skill discovery — a component is selected by matching its description against the situation | `ACMP1`–`ACMP12`'s interface | `NODE1` |
| `TSVC2` | Link validation on every change | `RULE2`, partially | `NODE2` + `NODE4` |
| `TSVC3` | Plugin distribution and update | `BSVC7` | `NODE1`'s marketplace mechanism, over `NODE5` |
| `TSVC4` | Published read-only view of a model | `BSVC4`'s third gate surface | `NODE3` |

## Artifacts

| ID | Artifact | Deployed on |
| -- | -------- | ----------- |
| `ART1` | `SKILL.md` files under `.claude/skills/` | `NODE1` |
| `ART2` | [`plugin.json`](../../../.claude/.claude-plugin/plugin.json) and [`marketplace.json`](../../../.claude-plugin/marketplace.json) | `NODE1` via `TSVC3` |
| `ART3` | [`check_links.py`](../../../scripts/check_links.py) | `NODE2` |
| `ART4` | The `example/site/` static pages | `NODE3` |

## Why there is no more than this

`stack-selection`'s first principle is that a project's traffic and data
volume essentially never justify operating infrastructure. archreator has
neither, so it operates none. Two consequences worth stating rather than
discovering later:

- **CI enforces one rule out of nine.** `TSVC2` checks that links resolve.
  Nothing checks element references, ID reuse, or whether an element's
  named artifact exists. `ACMP15` would need `NODE4` and nothing else —
  `sqlite3` ships with Python — which is why it is the cheapest large
  improvement available.
- **`RULE6` has no technical enforcement.** Nothing stops someone editing a
  merged scope document; git records that they did, but only if someone
  looks. A pre-merge check comparing merged scope documents against their
  merge-commit versions would close it. Not built, and probably not worth it
  until a project has enough contributors for the convention to fail.
