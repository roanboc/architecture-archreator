# Project Scope — Rebuild the site around why the project exists

_[← Scope index](./README.md) · [EA home](../ea/README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** `site/public/` rebuilt, on branch
`claude/repo-value-ux-review-3ur5y4`.

The site explained the mechanism to people who had not been given a reason
to care. Five pages of reference material — the process, a walkthrough, this
project's own architecture — all of it accurate, none of it answering the
first question a stranger has: **why does this exist, and what would it do
for me?**

The parent organization's model also moved on. archreator is now positioned
as one thing: a **free, open-source method**. Consulting and the future
portal are real parts of that organization and have no business on this site,
which exists to serve the open project.

So the pages were rebuilt from scratch, marketing-first: the problem, the
belief behind the project, what a reader gets, the proof, and the way in.
Three pages instead of five, in both languages.

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 1_strategy | **`DRV3` and `G5` added.** A reader could not tell why the project exists or whether it was for them; the site's first job is now that it lands before anything is explained. `STK2` re-scoped from "template adopters" to prospective adopters who have never heard of it |
| 2_business | **`BSVC1` re-scoped**, not replaced: from browsable reference material to the case for the method plus the way in. Same service, different purpose |
| 3_information | **`DOBJ1` unchanged in kind**, changed in extent: three pages per language instead of five |
| 4_application | **`ACMP3`, `ACMP4`, `ACMP5` retired; `ACMP7` added.** `ACMP1`, `ACMP2` and `ACMP6` rewritten, keeping their identifiers because they are the same components with new content |
| 5_technology | **No change.** Still static files on Pages, still no build |
| domains | **No change** — Depth 1 |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — Depth 1; no business model |
| Gate 1 — Strategy | Requester | 2026-08-09 | The shift in what the site is for: the open-source project only, the why before the how, marketing rather than reference. Stated as the requirement itself |
| Gate 2 — Business | Requester | 2026-08-09 | The rebuild, with the explicit instruction that the content would change substantially and that starting from scratch was acceptable |
| Gate 3 — Solution design | — | — | **N/A** — not requested |

**Recorded honestly:** both gates were granted on the **requirement**, in one
instruction, rather than against a presented design. That is a deviation from
the usual order — normally Gate 2 comes after a design is shown — and it is
written down rather than smoothed over. The design itself is offered for
review on the pull request.

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | Five pages per language explaining the method as reference; a reader had to already care |
| **Target** (delivered) | Three pages per language that argue for the project first, explain second, and hand over to GitHub third — on a rebuilt design system |

## Work packages and deliverables

### WP1 — The design system

- **Deliverables:** [`public/styles.css`](../../public/styles.css) — rewritten
  from scratch: design tokens, a light and dark palette built on the ArchiMate
  layer colours as the brand, layout primitives, and the components the pages
  use
- **Outcome:** a visual identity that belongs to this project rather than a
  generic document theme, still with **no external requests** — no web fonts,
  no scripts, no CDN

### WP2 — The three pages, in English

- **Deliverables:** [`public/index.html`](../../public/index.html) — the whole
  argument; [`public/how.html`](../../public/how.html) — the mechanism;
  [`public/start.html`](../../public/start.html) — the way in
- **Outcome:** a stranger can decide in one page whether this is for them
  (`G5`), and the two supporting pages exist for the reader who says yes

### WP3 — The Spanish edition

- **Deliverables:** [`public/es/`](../../public/es/index.html) — all three
  pages, translated rather than transliterated
- **Outcome:** `G4` holds through the rebuild instead of being quietly
  dropped, which a rebuild is the easiest moment to do

### WP4 — Realign the model

- **Deliverables:** the motivation, value stream, business service,
  information and application documents in [`docs/ea/`](../ea/README.md), plus
  [`site/CLAUDE.md`](../../CLAUDE.md)
- **Outcome:** the model describes the site that now exists, including three
  retired components that will never have their identifiers reused

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| The open-source project's story | Consulting and the portal — real parts of the organization, not this site's job |
| Three pages, two languages | A blog, changelog, or docs section |
| A rebuilt design system | Any build step, framework, or dependency |

## Gap notes

- **The architecture page is gone, and with it a real thing.** `ACMP5`
  rendered this project's own EA layers in hand-written CSS, and it was the
  most direct evidence the method produces something. It was also a second
  copy of the model that went stale every time the model moved — the drift
  recorded in [initiative 9](./9_element-ids-and-the-notation.md). The
  landing page now *links* to the real models on GitHub instead, which is
  more honest and less immediate. If the proof section underperforms, this is
  the first thing to reconsider.
- **Links in merged scope documents were pinned to a commit, not repaired.**
  Documents 2, 3, 5 and 8 link to pages this initiative deleted. Under the
  rule that a merged record's *words* are immutable but its *link targets*
  may be repaired, they now point at the pages as they existed at
  `baafc8d` — the commit before removal. **This is a new precedent:** the
  earlier carve-out covered files that moved, and nothing had yet been
  deleted outright. Whether pinning is the right general answer is worth
  settling before the next deletion.
- **The rebuild is unmeasured, like everything else here.** There is no
  analytics and there will not be — the parent organization holds no data
  about anyone. Whether the new framing works better than the old one cannot
  be observed, only argued.
- **`G1` and `G2` now sit slightly awkwardly.** Legible guidance and living
  proof were written when the site was reference material. Both still hold,
  but `G1` is now carried by one page rather than three, and `G2` by links
  rather than by a rendered page. Neither was rewritten here — a strategy
  layer should not be reshaped to flatter the delivery that follows it.
