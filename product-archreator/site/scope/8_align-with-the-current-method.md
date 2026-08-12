# Project Scope — Rename to `site/`, and align the pages with the current method

_[← Scope index](./README.md) · [EA home](../architecture/README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** `site/` on `claude/repo-value-ux-review-3ur5y4`.

Two things this project had drifted on.

**It was named for what it used to be.** This folder was `example/` — one of
two worked examples, alongside a fictional company. That company has been
[removed](../../scope/4_remove-the-fractal-example.md), and with it
the reason to call this an example. It is not one: it is archreator's own
published documentation, built with the method and deployed to GitHub Pages
from this repository. It is now `site/`, with the pages under `public/`.

**Its content described a method that has since changed.** The pages still
said five layers, nine skills, and "a GitHub template" — written before
layer 0, the modeling-depth ladder, domains, the plugin, and the framework
positioning existed. A guidance site that misdescribes the thing it
documents is worse than no site.

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 0_business-design | **Not used** — Depth 1. This project builds a site; it does not model an organization |
| 1_strategy | **No change to goals or principles.** `G1` (legible guidance) is exactly what a stale page fails at, so this initiative serves it rather than shifting it. The value stream's stage-to-page mapping is unchanged |
| 2_business | **No change.** Same actors, same roles, same autonomy. `Pilot` still merges; `Copilot` still drafts at co-pilot autonomy |
| 3_information | **Changed.** Page locations move from `site/*.html` to `public/*.html`; the EN-canonical / ES-mirror rule and the derived-not-canonical rule are unchanged |
| 4_application | **Changed.** All five components (and their Spanish editions) keep their identity and change location; the walkthrough component's description no longer claims five layers |
| 5_technology | **Changed.** The Pages workflow is renamed `deploy-site.yml` and publishes `site/public` instead of `example/site` |
| domains | **Not used** — Depth 1 |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — Depth 1; no canvases |
| Gate 1 — Strategy | — | — | **N/A** — no goal, principle, or stakeholder changes |
| Gate 2 — Business | Requester | 2026-08-08 | Renaming `example/` to `site/` and updating both language editions to the current method |
| Gate 3 — Solution design | — | — | **N/A** — not requested; the change is content and paths, not architecture |

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | `example/`, with pages in `example/site/`, describing a five-layer, nine-skill, template-only method aimed at vibe coders |
| **Target** (delivered) | `site/`, with pages in `site/public/`, describing six layers, the depth ladder, domains, twelve skills, the plugin path, the gate surfaces, and why the method uses ArchiMate rather than TOGAF |

## Work packages and deliverables

### WP1 — Rename

- **Deliverables:** `example/` → `site/`; `example/site/` → `site/public/`;
  [`deploy-site.yml`](../../../.github/workflows/deploy-site.yml) publishing
  `site/public`; every inbound path repaired across the repository
- **Outcome:** the folder is named for what it is, and `site/site/` — the
  obvious but ugly alternative — is avoided

### WP2 — Align the English pages

- **Deliverables:** [`public/index.html`](../public/index.html) (hero,
  layer 0 rung, the depth ladder, the TOGAF section, the two-ways-in
  quickstart), [`public/guide.html`](https://github.com/roanboc/archreator/blob/baafc8d7d991e67d2a0d62326c142b93eac982e0/site/public/guide.html) (layer 0 row,
  Gate 0, `N/A` gate rows, the gate-surface callout, a depth section, six
  new skills), [`public/start.html`](../public/start.html) (the plugin
  path), [`public/architecture.html`](https://github.com/roanboc/archreator/blob/baafc8d7d991e67d2a0d62326c142b93eac982e0/site/public/architecture.html) and
  [`public/walkthrough.html`](https://github.com/roanboc/archreator/blob/baafc8d7d991e67d2a0d62326c142b93eac982e0/site/public/walkthrough.html) (paths and
  layer-count claims), plus a dashed `data-layer="design"` rung and a
  compact list style in [`public/styles.css`](../public/styles.css)
- **Outcome:** the site describes the method that exists

### WP3 — Mirror into Spanish

- **Deliverables:** the same five pages under
  [`public/es/`](../public/es/index.html)
- **Outcome:** the editions stay one-to-one, which
  [3_information/1_data-objects.md](../architecture/3_information/1_data-objects.md)
  requires — a change to a page updates both in the same change

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| The rename and every path that pointed at it | Element IDs for this project's own EA documents |
| Both language editions, kept in step | A page on the enterprise/Depth 3 track beyond the guide's summary |
| The EA documents describing the new locations | Re-rendering the diagrams; they were already accurate |

## Gap notes

- **This project's EA still has no element IDs.** It predates the
  convention, so `check_model.py` reports its tables as unvalidated coverage
  rather than checking them — the rest of the repository is validated and
  this project is not. Retrofitting is mechanical but touches every document
  here, and it was kept out of an initiative that is already a rename plus a
  bilingual content pass. Until then, a stale element reference in these
  documents is caught by review or not at all.
- **The Depth 3 material on the site is a summary, not a demonstration.**
  The guide explains domains, charters, and the federation rule in a
  paragraph and a callout. With the fictional company gone there is nothing
  to link to that shows one, so a reader who wants to see a real charter has
  only the skill file. That closes when a real project reaches that size.
- **The pages remain a derived representation.** They summarize the skill
  files and this project's EA for a public reader; nothing checks that they
  agree. This initiative is itself the evidence that drift happens — the
  pages went stale across several method changes before anyone noticed. A
  check comparing claims to sources is not obviously buildable, so the
  mitigation stays "update the site in the same initiative that changes the
  method".

## Open questions

- **Whether the site should track the method automatically.** It went stale
  because updating it is a separate, easily-deferred step. Interpretation
  adopted: keep it manual and treat a stale page as a defect, because the
  pages are prose written for humans and generating them from skill files
  would produce something nobody wants to read. Revisit if it drifts again.
