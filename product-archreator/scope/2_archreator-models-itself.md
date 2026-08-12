# Project Scope — archreator models itself, and learns to restate

_[← Scope index](./README.md) · [EA home](../architecture/README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** `meta/ea/`, `meta/decisions/`, `meta/open-questions.md`,
and `.claude/skills/restate-current-state/` on
`claude/repo-value-ux-review-3ur5y4`.

[Initiative 1](./1_repo-value-and-fractal-domains.md) created `meta/` to
hold archreator's own record and closed the tension that its `docs/` must
stay blank for cloners. It carried a review and a scope document and nothing
else — archreator still had no architecture of its own. This initiative
finishes that: **archreator is now modeled with archreator**, at Depth 1,
with the full set of components a downstream project gets.

It also adds the twelfth skill, `restate-current-state`, and states the
positioning that initiative 1's review identified but did not write down:
archreator models to *implement*, which is the reason for ArchiMate over
TOGAF and the reason the grounding rule exists.

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 0_business-design | **Not used** — Depth 1. archreator is one thing that gets built, not an organization |
| 1_strategy | **New.** [`meta/ea/1_strategy/1_motivation.md`](../architecture/1_strategy/1_motivation.md) — five stakeholders, five drivers, four goals, and five principles. `P5` (history is never rewritten) is new, written because `restate-current-state` made it necessary to say what compaction may not touch |
| 2_business | **New.** Three actors — one of them the AI executing the method, at co-pilot autonomy — seven business services, and nine business rules traced to the principles they enforce |
| 3_information | **Not started.** The model is markdown in git. `ACMP15` would create a data architecture; until then there is none to describe |
| 4_application | **New.** Twelve skills, the link checker, and the plugin as components, each naming its file. `ACMP15` (the model exporter) is Pending and carries two rules nothing else enforces |
| 5_technology | **New.** Five nodes, four technology services, four artifacts. Records that CI enforces one rule out of nine |
| domains | **Not used** — Depth 1 |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — Depth 1; no canvases |
| Gate 1 — Strategy | Requester | 2026-08-08 | archreator's own strategy layer, in particular the framing that it models to implement rather than to document — which is what `P1` enforces and what separates it from TOGAF and ArcKit |
| Gate 2 — Business | Requester | 2026-08-08 | The self-model, the full `meta/` component set, and `restate-current-state` including its rule that merged scope documents are never rewritten |
| Gate 3 — Solution design | — | — | **N/A** — not requested |

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | archreator asked every project to model itself and had no model. `meta/` held a review and one scope document. The ArchiMate-over-TOGAF choice was unexplained, and a reader could take it as notation preference |
| **Target** (delivered) | archreator is modeled at Depth 1 with strategy, business, application, and technology layers, three decision records, an open-questions log, and two scope documents. The positioning is stated. The model can be compacted as it ages |

## Work packages and deliverables

### WP1 — State the positioning against known frameworks

- **Deliverables:** [`README.md`](../../README.md) § Why this isn't TOGAF,
  with a four-way comparison against TOGAF, ArcKit, BMAD, and C4;
  the same framing added to
  [the review](../reviews/1_value-and-ux-review.md)
- **Outcome:** a reader learns why the method picks a modeling language over
  a process framework, and what test distinguishes the two

### WP2 — Model archreator with archreator

- **Deliverables:** [`meta/ea/`](../architecture/README.md) — four filled layers,
  eight documents; [`meta/decisions/`](../decisions/README.md) — three
  records; [`meta/open-questions.md`](../open-questions.md) — four pending,
  three resolved
- **Outcome:** the method survives being pointed at its own author, and the
  gaps it finds in itself are in tables rather than prose

### WP3 — Add `restate-current-state`

- **Deliverables:**
  [`.claude/skills/restate-current-state/SKILL.md`](../../.claude/skills/restate-current-state/SKILL.md);
  the Retired-section convention; wiring into `CLAUDE.md`, `README.md`, the
  skills index, and `docs/scope/README.md`
- **Outcome:** a model that has accumulated history can be compacted to
  describe today, without the compaction becoming a way to rewrite the past

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| archreator's strategy, business, application, and technology layers | An information layer — there is no data architecture until `ACMP15` exists |
| The framework positioning, in README and the review | Rewriting the guidance site to match; `example/` still carries the older framing |
| `restate-current-state` and the Retired convention | Running a restatement — nothing has aged enough to need one |
| Three decision records for calls already made | Backfilling decision records for the first ten pull requests |

## Gap notes

- **`ACMP15`, the model exporter, is Pending and carries two rules nothing
  else enforces.** `RULE2` (grounding) is checked only for links, and
  `RULE5` (IDs never reused) is checked by nothing at all. Modeling
  archreator made this concrete rather than theoretical: the application
  layer now has a row whose "Realized by" column reads Pending while two
  business rules point at it. It is the cheapest large improvement available
  — `sqlite3` ships with Python, and `check_links.py` is the precedent for a
  stdlib-only CI check.
- **`example/` still carries the pre-repositioning framing.** The guidance
  site was built when archreator described itself for vibe coders. It is not
  wrong, but it no longer leads with what the README leads with. Updating it
  is a separate initiative in that project's own `docs/scope/`.
- **`restate-current-state` has never been run.** It is designed against
  failure modes observed in this repository's own history — shipped Pendings,
  an orphaned skill, resolved questions nobody recorded — but a skill that
  has not been exercised is a hypothesis. The first real restatement will
  probably change it.

## Open questions

All four pending questions are consolidated in
[`meta/open-questions.md`](../open-questions.md) rather than restated here,
per `P3`. This initiative resolved three: where archreator records its own
architecture, whether skills may keep relative links, and whether IDs are
renumbered on a domain split.
