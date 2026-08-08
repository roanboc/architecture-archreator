# Project Scope — Enterprise-first positioning, modeling depth, and fractal domains

_[← meta index](../README.md) · [EA home](../../docs/ea/README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** branch `claude/repo-value-ux-review-3ur5y4`.

This initiative acts on
[reviews/1_value-and-ux-review.md](../reviews/1_value-and-ux-review.md). The
review found the method sound and the documentation unusually consistent, but
the *positioning* aimed at single-application builders while the intent is
companies modeling an enterprise landscape; the *journey* had ten defects
that bite a new user before they reach any of the value; and the *packaging*
made method improvements impossible to propagate. It repositions archreator
enterprise-first with an explicit modeling-depth ladder so a simple
application stays cheap, adds fractal domain modeling so a business line can
own its own model, fixes the ten defects, and repackages the method as an
installable Claude Code plugin.

This is a change to **the method itself**, so it is recorded here rather than
in `docs/scope/` — see [meta/README.md](../README.md) for why that
distinction exists (it is defect D10's resolution).

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 0_business-design | **No change.** archreator's own canvases are not modeled; the template's `0_business-design/` must stay blank for cloners |
| 1_strategy | **Changed — the reason this needed a gate.** The primary subject moves from "an application built by a vibe coder" to "an organization modeling its enterprise landscape", with the application case retained as Depth 1. Adds the modeling-depth ladder as a governing concept |
| 2_business | **Changed.** Adds the *domain* as a modeled subject that serves other domains, with a charter, exposed services, and a federation rule; adds the Requester gate surface, which was previously unstated |
| 3_information | **No change to the template's information layer.** Element-ID namespacing (`SALES.BSVC3`) is a notation change in `ea-doc-style`, deliberately shaped to map one-for-one onto the future `nodes`/`edges` schema |
| 4_application | **Changed.** The method is repackaged as a Claude Code plugin (`.claude-plugin/`), and `project-bootstrap` becomes the component that writes a project's scaffold |
| 5_technology | **Changed.** Distribution moves from GitHub template-only to plugin marketplace plus template; `check_links.py` verified against nested domain paths |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — archreator's own business model is not modeled |
| Gate 1 — Strategy | Requester | 2026-08-08 | Enterprise-first positioning, with agent-declared right-sizing so a simple application remains cheap to model and the user can deepen or descope later |
| Gate 2 — Business | Requester | 2026-08-08 | The work packages below: fractal domains as the single structural bet, the ten defect fixes, plugin-plus-template distribution, and all six layer folders at every depth with unfilled ones marked "not started" |
| Gate 3 — Solution design | — | — | **N/A** — not requested |

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | A GitHub template for application projects, with a company track as a subsection. Flat single-organization `docs/ea/`. Method improvements propagated only by hand-porting. Bootstrap and the gate surface were prose, not process |
| **Target** (delivered) | An installable, versioned plugin whose primary subject is an organization. A declared modeling depth right-sizes every initiative. Business lines are modeled as fractal domains with charters and service contracts. The ten journey defects are closed |

## Work packages and deliverables

### WP0 — Distribution and the Requester gate surface

- **Deliverables:** `.claude-plugin/plugin.json`,
  `.claude-plugin/marketplace.json`; gate-surface guidance in
  [`ea-first-change`](../../.claude/skills/ea-first-change/SKILL.md);
  plugin-first install path in [`README.md`](../../README.md)
- **Outcome:** `/plugin update` propagates method improvements, and a
  non-technical Requester has a named place to grant approvals

### WP1 — Review and self-documentation

- **Deliverables:** [`meta/README.md`](../README.md),
  [`meta/reviews/1_value-and-ux-review.md`](../reviews/1_value-and-ux-review.md),
  this document
- **Outcome:** archreator records its own method changes without polluting
  the scaffold a cloner receives (D10)

### WP2 — Enterprise-first positioning and modeling depth

- **Deliverables:** [`README.md`](../../README.md),
  [`CLAUDE.md`](../../CLAUDE.md), [`CONTRIBUTING.md`](../../CONTRIBUTING.md),
  [`docs/ea/README.md`](../../docs/ea/README.md),
  [`.claude/skills/project-bootstrap/SKILL.md`](../../.claude/skills/project-bootstrap/SKILL.md)
- **Outcome:** the organization is the primary subject; the agent declares a
  modeling depth out loud and the Requester can change it later (D5, D6, D9)

### WP3 — Journey defect fixes

- **Deliverables:** edits to `ea-first-change`, `strategy-discovery`,
  `operating-model-discovery`, `scope-doc`, `ea-doc-style`, `story-sharding`
- **Outcome:** D1, D2, D3, D4, D7, D8 closed — the discovery tracks reach a
  scope document, sharding is reachable, and the ID scheme covers every
  element type the process makes mandatory

### WP4 — Fractal domain structure

- **Deliverables:** [`docs/ea/domains/README.md`](../../docs/ea/domains/README.md),
  [`.claude/skills/domain-modeling/SKILL.md`](../../.claude/skills/domain-modeling/SKILL.md),
  namespacing rules in `ea-doc-style`, domain routing in `ea-first-change`
- **Outcome:** a business line is modeled as an organization serving other
  domains, with a charter as its contract and a federation rule governing
  cross-domain change

### WP5 — Worked example

- **Deliverables:** `example-company/` split into `advisory/` and `product/`
  domains
- **Outcome:** the fractal design is proven against a real model rather than
  asserted, matching this repository's rule that every concept has a worked
  example

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| Enterprise-first positioning and the modeling-depth ladder | The SQLite graph exporter and the dangling-ID validator |
| Fractal domains: charter, split test, depth cap, namespaced IDs, federation rule | Multi-agent orchestration across layers or domains |
| Plugin packaging alongside the template | Executable process contracts, and any execution runtime |
| The ten reviewed journey defects | A Requester-facing surface outside GitHub |
| One worked domain split in `example-company/` | Splitting `example/` — it is a single application, correctly Depth 1 |

## Gap notes

- **The graph exporter is the next initiative, and it is load-bearing.**
  Element IDs are mandated but nothing verifies them: a deleted element
  leaves dangling references that no check catches. Namespaced domain IDs
  make this worse before better, because a cross-domain reference is exactly
  the kind that rots silently. Closing it is small — the schema is already
  specified in `stack-selection`, `sqlite3` ships with Python, and
  `check_links.py` is the precedent for a stdlib-only CI check.
- **Multi-agent orchestration is blocked on the graph, not on the domains.**
  The federation rule gives agents ownership boundaries, but without a
  queryable shared state two agents working adjacent domains cannot see each
  other's uncommitted changes. Sequencing it after the exporter is
  deliberate.
- **Depth 3 is capped at enterprise → domain → subdomain.** A genuine
  conglomerate with deeper structure would need either a fourth level or
  separate repositories federated by contract. The second is likely the
  right answer, and nothing here forecloses it.

## Open questions

- **Whether the template repository stays hand-maintained or is generated
  from the plugin.** This initiative keeps both paths working and treats the
  template as the demoted secondary path, but does not automate the
  generation — so the two can drift until that is closed. Interpretation
  adopted: acceptable while the skill set is small enough to review by eye.
