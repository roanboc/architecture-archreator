# Project Scope Documents

_[← Repository README](../README.md) · [Enterprise architecture](../architecture/README.md)_

One document per delivered (or in-flight) initiative, numbered
chronologically. The [EA docs](../architecture/README.md) describe the **current**
state; each scope document describes one **change**.

**ArchiMate viewpoint:** Implementation & Migration (Work Package,
Deliverable, Plateau, Gap).

## Initiatives

| #   | Scope document | Delivered as | Summary |
| --- | --------------- | ------------ | ------- |
| 1   | [1_publish-guidance-site.md](./1_publish-guidance-site.md) | `site/` on `claude/enterprise-architecture-template-review-8addo4` | Built and published this guidance site, demonstrating the EA-first process and the human/AI actor notation on a real, small project |
| 2   | [2_redesign-guidance-site.md](./2_redesign-guidance-site.md) | `site/` on `claude/repo-ux-example-app-dhy09b` | Gave the site a design system built on the ArchiMate layer palette, made the Requester → Agent → Reviewer loop its centrepiece, and replaced the Mermaid CDN with self-contained CSS diagrams |
| 3   | [3_deepen-guidance-coverage.md](./3_deepen-guidance-coverage.md) | `site/` on `claude/repo-ux-example-app-dhy09b` | Added a start-to-finish walkthrough page (a requirement climbing the five layers, Requester vs. Agent at each step) and dedicated coverage of the `stack-selection` and `story-sharding` skills |
| 4   | [4_standardize-structure-and-vocabulary.md](./4_standardize-structure-and-vocabulary.md) | `site/` on `claude/repo-ux-example-app-dhy09b` | Standardised the change loop on the canonical Requester/Agent/Reviewer vocabulary, mapped Pilot/Copilot to those roles, and fixed the application layer-view drift |
| 5   | [5_beginner-setup-guide.md](./5_beginner-setup-guide.md) | `site/` on `claude/beginner-setup-guide-dnef32` | Added a `Start here` page taking a total newcomer from no GitHub account to their first reviewed change — free-first, no editor install required |
| 6   | [6_spanish-language-support.md](./6_spanish-language-support.md) | `site/` on `claude/spanish-language-support-7k2sxw` | Published a Spanish edition of the site: every page mirrored under `public/es/`, an EN ⇄ ES switcher in every header, `hreflang` pairing — English edition stays canonical between the two |
| 7   | [7_adopt-approval-gates.md](./7_adopt-approval-gates.md) | `site/` on `claude/agent-strategy-gates-vfny5p` | Aligned the guidance with the gated method: pages (both editions) teach strategy discovery + Gates 1–3, and every scope document carries an Approvals table — retroactive for 1–6 from the commit history, live from this one on |
| 8   | [8_align-with-the-current-method.md](./8_align-with-the-current-method.md) | `site/` on `claude/repo-value-ux-review-3ur5y4` | Renamed `example/` to `site/` (pages under `public/`) now that this is the project's own documentation rather than one of two examples, and brought both editions up to the current method: layer 0, the modeling-depth ladder, domains, Gate 0, the plugin path, the gate surfaces, and why ArchiMate rather than TOGAF |
| 9   | [9_element-ids-and-the-notation.md](./9_element-ids-and-the-notation.md) | `site/` on `claude/repo-value-ux-review-3ur5y4` | Element identifiers assigned across the model (6 → 31, all validated in CI), and every document redrawn to the parent template's notation standard — 9 diagrams became 20, one per section |
| 10  | [10_rebuild-around-the-why.md](./10_rebuild-around-the-why.md) | `site/` on `claude/repo-value-ux-review-3ur5y4` | Rebuilt the site around why the project exists, for the open-source project only: three pages per language instead of five, a new design system, `G5` added and three components retired |
