# Project Scope — Adopt Approval Gates in the Guidance

_[← Scope index](./README.md) · [EA home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** `example/` on branch `claude/agent-strategy-gates-vfny5p`
([PR #8](https://github.com/roanboc/archreator/pull/8)).

The archreator method gained explicit Requester approval gates and a
strategy-discovery path (defined canonically in
[`.claude/skills/ea-first-change`](../../../../.claude/skills/architecture-first-change/SKILL.md)
and
[`.claude/skills/strategy-discovery`](../../../../.claude/skills/strategy-discovery/SKILL.md)).
This site's pages are a **derived** representation of those canonical
skills, so they were describing a method that no longer existed. This
initiative brings the example back in step: the guidance pages (both
language editions) now teach the gated process, this project's own scope
documents carry the Approvals table the method now requires — recorded
retroactively for initiatives 1–6 from the commit history, since their
approvals were granted by the Pilot's merges before gates existed — and
`CLAUDE.md` states the gated rule.

## EA alignment (assessed top-down before implementing)

| Layer         | Impact                                              |
| ------------- | ---------------------------------------------------- |
| 1_strategy    | **No change.** No new stakeholder, driver, goal, or principle — the change serves existing Goal G1 (legible guidance) by keeping the derived pages true to their canonical sources (Principle P1). Strategy discovery not triggered |
| 2_business    | **No change** to services, processes, actors, or rules. The content of the *EA-first method guidance* service now describes the gated method, which is content maintenance under the existing derived/canonical rule |
| 3_information | The **Scope document** record kept by this project gains an Approvals section (gate, approver, date, what was approved), as the `scope-doc` skill now prescribes. No new data object; the Guidance page object is unchanged in structure |
| 4_application | **No change** to components. The five page components (both editions) get updated content: gates in the guide's process description, a reordered walkthrough timeline with the Gate 2 stop and the optional Gate 3, and the ladder/loop copy on the home page |
| 5_technology  | **No change.** Same hosting, same deploy workflow, still no build step |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 2 — Business | Pilot | 2026-07-22 | The alignment above and this initiative's scope, requested and accepted in the Pilot's [PR #8 review comment](https://github.com/roanboc/archreator/pull/8#issuecomment-5051604321) ("Let's align the example to demonstrate those steps, approvals taken from file commits as decision made"), which also set the retroactive-approvals convention for initiatives 1–6. Gate 3 not requested |

## Plateaus

| Plateau                | State                     |
| ----------------------- | ------------------------- |
| **Baseline** (before)  | The guidance pages describe the pre-gate, three-step method (align → scope → implement); scope documents 1–6 carry no approval record beyond the merge history itself |
| **Target** (delivered) | Both editions of the guidance teach the gated method (strategy discovery + Gate 1, Gate 2 before code, optional Gate 3); every scope document, including this one, carries an Approvals table — 1–6 retroactively from commits, 7 onward as the gates are passed |

## Work packages and deliverables

### WP1 — Approvals record in scope documents

- **Deliverables:** an `## Approvals` section in
  [`1_publish-guidance-site.md`](./1_publish-guidance-site.md) through
  [`6_spanish-language-support.md`](./6_spanish-language-support.md)
  (retroactive: approver Pilot, date and commit taken from each
  initiative's merged PR), and in this document (a live Gate 2 row).
- **Outcome:** every initiative in this project shows who accepted what,
  when — the durable record the gated method requires.

### WP2 — Guidance pages teach the gated method

- **Deliverables:** updated `site/guide.html` (gates in the process
  section; `strategy-discovery` and the Approvals table in the skills
  overview), `site/walkthrough.html` (timeline reordered to draft the
  scope document after layer 3, a Gate 2 stop before any code, the
  optional Gate 3 on the solution design, and a strategy-discovery note
  at the start), `site/index.html` (ladder and loop copy mention the
  gates) — each with its `site/es/` twin updated in the same change.
- **Outcome:** a reader of either edition learns the method as it
  actually is (Principle P1: pages derive from canonical sources).

### WP3 — Project rule alignment

- **Deliverables:** [`CLAUDE.md`](../../CLAUDE.md) restates the governing
  rule in its gated form and points at `strategy-discovery`; the
  [scope index](./README.md) gains this initiative's row.
- **Outcome:** an agent working on this example follows the same gated
  process the pages describe.

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| Approvals tables in all seven scope documents (1–6 retroactive, 7 live) | Retro-fitting Gate 1/Gate 3 rows for initiatives 1–6 — no discovery or solution-design review happened, so there is nothing truthful to record |
| Gated-method content on guide, walkthrough, and home pages, both editions | A dedicated site page or diagram devoted to the gates alone — the existing pages carry the story |
| `CLAUDE.md` rule update for this project | Mechanical gate enforcement (branch protection, labels) — process-level by design, as in the root method |

## Gap notes

- **No standalone gates visual.** The walkthrough shows the gates in
  sequence and the guide describes them, but there is no single diagram of
  the three gates as a governance view. If readers ask for one, it is a
  small addition to `guide.html`/`architecture.html`.
- **Retroactive rows are approximations.** For initiatives 1–6 the
  approval date is the merge date and the approver the merging Pilot; the
  gates as formal stops did not exist then. The rows say "retroactive"
  precisely so the record doesn't overclaim.

## Open questions

- None. The Pilot's PR #8 comment defined both the requirement and the
  approval convention; this project keeps no `open-questions.md` log.
