# Project Scope — Spanish Language Support

_[← Scope index](./README.md) · [EA home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** `example/` on branch `claude/spanish-language-support-7k2sxw`.

The guidance site was English-only, which excluded a large group of
prospective adopters — Spanish-speaking builders who would rather learn a
process in their own language than parse dense method prose in English.
This initiative publishes a complete Spanish edition of the site: every
guidance page gets a one-to-one Spanish counterpart under `site/es/`, and
every page (in both languages) carries an EN ⇄ ES switcher in its header.
The site stays what it is — hand-written, dependency-free static HTML with
no build step — so the translation is a parallel set of pages, not a
translation framework.

## EA alignment (assessed top-down before implementing)

| Layer         | Impact                                              |
| ------------- | ---------------------------------------------------- |
| 1_strategy    | One new stakeholder row (**Spanish-speaking template adopters**) and one new goal **G4 — Guidance legible in Spanish** — see [1_strategy/1_motivation.md](../1_strategy/1_motivation.md). No Principle conflict: Spanish pages link the same canonical sources (P1) and ship through the same reviewed-PR path (P2). The value stream gains a note that its stages are language-independent — see [1_strategy/3_value-stream.md](../1_strategy/3_value-stream.md) |
| 2_business    | No new service, process, actor, or rule. The **EA-first method guidance** service description now states the service is offered in English and Spanish, and that updating a page means updating both editions in the same change — see [2_business/2_business-services.md](../2_business/2_business-services.md) |
| 3_information | No new data object. The **Guidance page** object gains a second representation: a Spanish edition per page, one derivation step further out. Chain of authority: skill/EA doc → English page → Spanish page; the English edition wins a disagreement between the two — see [3_information/1_data-objects.md](../3_information/1_data-objects.md) |
| 4_application | No new component. Each of the five components of **Guidance publishing** ships in two language editions (same filename under `site/es/`), linked by a header language switcher and `hreflang` alternate tags — see [4_application/2_application-components.md](../4_application/2_application-components.md) |
| 5_technology  | **No change.** The deploy workflow uploads `example/site` recursively, so `site/es/` publishes with the existing pipeline; still no build step, nothing fetched at request time — see [5_technology/2_deployment.md](../5_technology/2_deployment.md) |

## Approvals

_Recorded retroactively by [initiative 7](./7_adopt-approval-gates.md):
the approval gates postdate this initiative, so the decision on record is
the commit history — the Pilot's review and merge accepted the aligned
strategy, business, and information changes together with the
implementation._

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 2 — Business (retroactive) | Pilot | 2026-07-22 | EA alignment and scope as delivered by commit `fb86ffa`, accepted at the merge of [PR #7](https://github.com/roanboc/archreator/pull/7) |

## Plateaus

| Plateau                | State                     |
| ----------------------- | ------------------------- |
| **Baseline** (before)  | Five guidance pages, English only; a Spanish-speaking visitor had no way to read the method in their language |
| **Target** (delivered) | Ten pages: the five English pages unchanged in content, each now paired with a Spanish edition under `site/es/` sharing the same structure, ids, and styles; every header switches language for the page being read |

## Work packages and deliverables

### WP1 — Spanish editions of the five pages

- **Deliverables:** `example/site/es/index.html`, `es/start.html`,
  `es/guide.html`, `es/walkthrough.html`, `es/architecture.html` —
  full Spanish translations with `lang="es"`, the same element `id`s and
  page structure as their English counterparts, internal links pointing
  within `es/`, and source links pointing to the same canonical repo
  documents (which remain in English). Actor names (Pilot, Copilot) and
  the canonical role vocabulary are kept with the English term introduced
  once alongside the Spanish (e.g. "Solicitante (*Requester*)").
- **Outcome:** a Spanish-speaking adopter can move Discover → Understand →
  Adopt entirely in Spanish (Goal G4).

### WP2 — Language switcher and pairing metadata

- **Deliverables:** an `ES` / `EN` link in the header nav of all ten
  pages, each pointing at the same page in the other language; a
  `.lang-switch` style in `example/site/styles.css`;
  `<link rel="alternate" hreflang="…">` tags on all ten pages declaring
  each EN/ES pair.
- **Outcome:** the other language is one click away from any page, and
  search engines index the pair as one document in two languages.

### WP3 — EA and convention alignment

- **Deliverables:** the EA-doc edits listed in the alignment table above
  (`1_strategy`, `2_business`, `3_information`, `4_application`), plus
  `example/CLAUDE.md` layout/conventions updates recording the two-edition
  rule.
- **Outcome:** the EA set stays verifiable — every new file is named by a
  document, and the "both editions in the same change" rule is recorded
  where future changes will find it.

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| Full Spanish editions of all five site pages, hand-written like the rest of the site | Translating the repo documentation (`docs/ea/`, `docs/scope/`, skills, README) — documentation language stays English |
| A per-page EN ⇄ ES switcher and `hreflang` pairing | Automatic language negotiation or redirects (needs request-time logic GitHub Pages doesn't provide; the switcher covers it) |
| Spanish UI copy for nav, footers, and diagrams' text | Further languages — the `es/` directory pattern extends to `fr/`, `de/`, … but each is its own initiative |
| Keeping canonical source links pointing at the (English) repo docs | Translating linked third-party/vendor pages or the GitHub UI they land on — outside this repo's control |

## Gap notes

- **Translation drift.** The two editions are hand-maintained; nothing
  mechanical forces them to stay in sync. Mitigated by the recorded rule
  (business layer + `CLAUDE.md`) that a page change updates both editions
  in the same change, and by identical structure/`id`s making a
  side-by-side diff easy. A CI check that flags an English page changing
  without its Spanish twin would close this properly — cheap to add to the
  existing `docs-check` workflow if drift actually occurs.
- **Docs stay English.** A Spanish reader who clicks a "source" link lands
  on an English skill or EA document. That is a real seam, but translating
  canonical sources would create a second authority for every fact —
  exactly what Principle P1 exists to prevent — so the pages keep the
  derived/canonical split and only the derived layer is translated.
- **More languages.** The chosen layout (`site/<lang>/`, same filenames)
  and the authority chain recorded in `3_information` generalize as-is;
  adding a language is a repeat of WP1–WP2 per language.

## Open questions

- None. The initiative interprets "the webpage should also have Spanish"
  as a full per-page translation with a manual switcher (rather than
  machine translation, partial translation, or auto-detection); the Pilot
  confirms by reviewing and merging the branch. This project keeps no
  `open-questions.md` log.
