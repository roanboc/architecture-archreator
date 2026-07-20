# Business Actors and Roles

_[← Business layer](./README.md) · [EA home](../README.md)_

**ArchiMate elements:** Business Actor, Business Role.

Notation: `ea-doc-style`'s human/AI/hybrid actor convention — every actor
states its kind, and AI/hybrid actors carry autonomy level, decision
rights, and escalation path.

## Actors

| Actor | Kind | Role | Autonomy level | Decision rights | Escalation path |
| ----- | ---- | ---- | --------------- | ---------------- | ----------------- |
| Maintainer | Human | Guidance author (reviewer) | — (human) | Approves/merges any change to `site/`, `docs/`, or repo settings; sole authority over GitHub Pages configuration | — |
| Docs Agent | AI | Guidance author (drafter) | **Co-pilot** — drafts complete changes; nothing it writes reaches the published site without a human merging it | May edit `site/*.html`, `docs/ea/**`, `docs/scope/**` within this `example/` folder and open a PR. May **not** merge PRs, change GitHub Pages/repo settings, or edit content outside `example/` | Opens a PR to **Maintainer**; if a proposed change would contradict a Principle in [`1_strategy/1_motivation.md`](../1_strategy/1_motivation.md), stops and surfaces the conflict to **Maintainer** instead of proceeding (mirrors `ea-first-change` step 1) |
| Template adopter | Human, external | Consumer of the guidance service | — (human) | None — read-only visitor to the published site | — |

See [`../../decisions/1_docs-agent-autonomy.md`](../../decisions/1_docs-agent-autonomy.md)
for why Docs Agent's autonomy is set at co-pilot rather than fully
autonomous or advisory-only.

## Role

**Guidance author** — drafts, reviews, and publishes updates to the
guidance site. Both Maintainer and Docs Agent are assigned to it; the
autonomy/decision-rights columns above are what actually distinguishes
their authority within the same role, not a separate role each.
