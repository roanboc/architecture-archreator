# Project Scope — The gates are gone

_[← Scope index](./README.md) · [Model home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** branch `claude/beautiful-mendel-c193id` here, and a
companion branch in [`archreator`](https://github.com/roanboc/archreator)
taking the method itself to 0.6.

The Requester asked to reduce gate bureaucracy — approval required only when
a request contradicts the architecture or a decision already made, or reads
two ways — believing this was already how the method worked. It was not:
this tree's `CLAUDE.md`/`AGENTS.md` still ran the two-gate process scope 2
and scope 3 left in place, and the method itself still prescribed it. This
initiative retires Direction and Understanding as mandatory
pre-implementation gates, replaces them with three named stops —
Contradiction, Ambiguity, Authorization — and takes the method to 0.6 to
match, so the worked models here keep running on the version the method
ships.

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 0_business-design | No change to this tree, which does not use the layer. In the organization's, `PREL1` renamed **The layered walk** (from "The gated layer walk") and restated; `PREL5` and `KR2` drop "gates" from what they name |
| 1_strategy | `G2`, `OUT1` and `OUT2` restated for the pull request's merge as the only approval. In the organization's, `OUT1` and `OUT2` restated the same way; `P1` restated for "the merge requirement" in place of "the gates"; `CAP1.1` and `RES2` drop "gates" from what they encode and hold |
| 2_business | `BSVC1` renamed **Change alignment** (from "Gated change alignment") and restated; `BSVC4` restated. In the organization's, `ACT2`'s decision rights and escalation restated; `BPROC1.1` and `BPROC1.2` restated; the value stream's `VS1.3` renamed **Check** (from "Approve") and restated; `VS1.4` and `VS1.5` restated, `VS1.5` now naming the merge as the approval; `CAP3.2` drops "approved" |
| 3_information | No change of content; the status line on the one document here reads `not yet validated` instead of naming a gate |
| 4_application | `ASVC1` restated for the same reason |
| 5_technology | `NODE1`'s note restated |

No element is added, renamed away, or retired. `BSVC1`, `PREL1` and `VS1.3`
keep their identifiers and are corrected in place — the rule that a change
reaches a model only if it makes a row false, applied to rows that had
become false.

## What the evidence said

Measured on both trees, before and after:

| Measure | Before | After |
| ------- | ------ | ----- |
| Elements, organization and product | 143 and 77 | 143 and 77 |
| Live (non-frozen) mentions of "gate" as the approval mechanism, both trees | 34 | 0 (one idiomatic use of "gate" meaning bottleneck, in `GCRE5`, left as ordinary English) |
| `check_links.py`, `check_model.py`, `check_prose.py` | green | green |
| Files touched in the sibling `archreator` repository | — | the core skill and its retired reference, six more procedure skills, the four-diagram process model, the scaffold, both pull-request templates, the plugin and marketplace manifests, `model.py`'s `health` command and its test, and the public README's two pitch diagrams |
| `archreator`'s own test suite (`pytest`) and `check_skills.py` | — | 44 passed; 18 skills, zero errors |

## Work packages and deliverables

### WP1 — The rule, here

- **Deliverables:** `AGENTS.md` ("How a change happens here" replaces "The
  rule that governs everything else"); `CONTRIBUTING.md` (the Actors table,
  the "What kind of change is this?" table, and the rules that catch people
  out); `product-archreator/architecture/scope/README.md`'s intro line, no
  longer pointing at an Approvals table.
- **Outcome:** the repository's own governance describes what it now does,
  and this document is itself the first scope document with no Approvals
  section.

### WP2 — The model, restated

- **Deliverables:** in `product-archreator`, `1_strategy/1_motivation.md`
  (`G2`, `OUT1`, `OUT2`), `2_business/1_business-services.md` (`BSVC1`
  renamed, `BSVC4`), `2_business/README.md`, `4_application/1_application-services.md`
  (`ASVC1`), `5_technology/1_technology-and-deployment.md` (`NODE1`), and
  `architecture/README.md`'s status legend. In `org-archreator`,
  `0_business-design/1_value-proposition-canvas.md` (`PREL1` renamed,
  `PREL5`), `0_business-design/2_business-model-canvas.md` (`KR2`),
  `1_strategy/1_motivation.md` (`OUT1`, `OUT2`, `P1`),
  `1_strategy/2_capabilities-and-value-stream.md` (`CAP1.1`, `RES2`, `VS1.3`
  renamed, `VS1.4`, `VS1.5`, `CAP3.2`), `2_business/1_business-architecture.md`
  (`ACT2`, `BPROC1.1`, `BPROC1.2`), and the status lines and legends on
  `3_information/1_information-domains-and-objects.md` and both trees'
  `architecture/README.md`.
- **Outcome:** nothing in either model still claims a two-gate process.

### WP3 — The method itself, to 0.6

- **Deliverables:** `align-change-through-layers` rewritten (§ "Where this
  stops" replaces § "The gates"; the eight steps keep their numbers, Step 4
  becomes "Check for a stop"); `references/presenting-a-gate.md` retired,
  folded into the same section; `write-scope-document` (no Approvals-table
  template); the scaffold's `assets/layers/scope/README.md`; the six other
  procedure skills that owned Direction or Understanding
  (`discover-business-model`, `discover-strategy`, `plan-the-transition`,
  `discover-current-landscape`, `model-domains`, `restate-current-state`)
  rewritten the same way; `establish-project`, `write-pr-description`,
  `document-style`, `architecture-document-style` (the status-glyph trigger
  is now the merge, not a gate) and the remaining skills with scattered
  mentions, corrected; the process model in `docs/process/` (gate nodes
  removed from all four macro-process diagrams and the level-3 diagram,
  SIPOC outputs and the notation legend restated); `docs/method.md`,
  `docs/adopting.md`, `docs/migrating.md` (new § "The gates are gone
  (0.6)"), `docs/standards-alignment.md`; both pull-request templates; root
  `AGENTS.md`, `CONTRIBUTING.md`, `README.md` (including its two pitch
  diagrams); the scaffold's own `AGENTS.md`, `README.md`,
  `architecture/README.md`, `CONTRIBUTING.md`; `docs/skill-format.md` (the
  `gates` frontmatter field retired, `gated-procedure` renamed `procedure`,
  purely an internal kind value); `check_skills.py` (the gate-glyph
  cross-check removed); `model.py`'s `health` command (the Approvals-table
  parse retired, replaced with a plain status count) and its test;
  `prose-denylist.json` (the two retired gate-name patterns replaced with
  patterns for the new self-referential vocabulary); the plugin and
  marketplace manifests, version bumped to 0.6.0.
- **Outcome:** the method's own prescribed process matches what this tree
  claims it does, and its own checks (`check_skills.py`, the pytest suite)
  are green.

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| Retiring Direction and Understanding as mandatory pre-implementation gates, in this tree's model and in the method's own skills, process model and docs | Reordering the organization's value-stream stage IDs so "approve" visibly follows "build" — `VS1.3` was corrected in place instead, since resequencing a merged element's position is a restructuring, not a content fix |
| The three named stops (Contradiction, Ambiguity, Authorization) replacing the two gates and the two unscheduled stops that preceded them | The roadmap and local bench tooling raised while assessing the now-superseded PR #21 on this repository — still undecided, not part of this initiative |
| The method's own version, bumped to 0.6.0, and its manifests | Any change to what the method's skills actually do beyond the approval mechanism — `discover-business-model`'s discovery questions, for instance, are untouched |

## Gap notes

- **The organization's value stream still lists `Check` (`VS1.3`) between
  Frame and Model, though the real approval now follows Build.** Renumbering
  `VS1.1`–`VS1.6` to reflect the new order would be a value-stream
  restructuring, and the convention holds an identifier once assigned and
  never reused after merge. `VS1.3` is renamed and redefined as the point
  where a contradiction or ambiguity is caught, and `VS1.5` **Build** now
  names the merge as the approval — both true, in their existing positions.
  A later initiative may resequence the stream properly if drawing the
  two-step shape (check early, approve at merge) as its own stage order
  turns out to matter.
- **PR #21's roadmap (`6_transition/`) and local bench (`Makefile`) are
  still an open question for the Requester**, separate from this initiative.
  They were surfaced while assessing why PR #21 conflicted; nothing here
  decides whether to bring them back.

## Approvals

Nothing here. Per WP1, the pull request whose merge approves this document
is the only record that it happened.
