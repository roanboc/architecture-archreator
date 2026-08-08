# 1 — The plugin root is `.claude/`, not the repository root

_[← Decisions](./README.md)_

**Status:** Accepted
**Date:** 2026-08-08
**Touches:** [`ACMP14` Plugin package](../ea/4_application/1_application-components.md),
[`RULE9`](../ea/2_business/2_business-services.md)

## Context

archreator needed to ship as an installable Claude Code plugin so that
`/plugin update` could propagate method improvements — `G4`, previously
unrealized, with the README documenting hand-porting as the only option.

A plugin's components must sit at its root: `skills/`, `agents/`, `hooks/`.
The skills already lived at `.claude/skills/`, where Claude Code auto-loads
them for anyone using the template path. Those two facts conflict if the
plugin root is the repository root.

## Options considered

| Option | Consequence |
| ------ | ----------- |
| **Move skills to `/skills/` at the repository root** | The plugin works. The template path breaks — Claude Code auto-loads `.claude/skills/`, not `/skills/`, so a cloner gets nothing |
| **Duplicate: `/skills/` for the plugin, `.claude/skills/` for the template** | Both paths work and immediately diverge. Two copies of twelve skills is the drift `P3` exists to prevent |
| **A separate marketplace repository**, as ArcKit does | Cleanest separation, and what a mature project should do. Requires a second repository and a sync mechanism between them |
| **Make `.claude/` the plugin root** — manifest at `.claude/.claude-plugin/plugin.json`, marketplace at `.claude-plugin/marketplace.json` | Both paths serve the same files. No move, no duplication, no second repository |

## Decision

`.claude/` is the plugin root. The skills do not move.

`claude plugin validate` passes for both the plugin and the marketplace, and
plugin skills namespace as `archreator:<name>` so a project that both cloned
the template and installed the plugin gets two invocable copies rather than
a collision.

## Consequences

- **A skill may no longer link outside `.claude/skills/`.** Installing a
  plugin copies its directory to a cache, so `../../../docs/ea/README.md`
  resolves to nothing for a plugin user. All twenty-two outbound links were
  converted to code-span paths (`` `docs/ea/README.md` ``), which read
  correctly on both paths. This became `RULE9`.
- **`.claude/` now carries two responsibilities** — project configuration
  and plugin payload. Today it contains only `skills/`, so nothing leaks. If
  archreator ever adds a `settings.json` for its own development, that file
  would ship to every plugin installer, and this decision would need
  revisiting.
- **The separate-repository option stays open** and is probably right
  eventually. It was rejected on cost, not on merit; see the open question
  about generating the template from the plugin.
