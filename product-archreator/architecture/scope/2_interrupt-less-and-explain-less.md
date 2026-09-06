# Project Scope — Interrupt less and explain less

_[← Scope index](./README.md) · [Model home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** branch `claude/archreator-validation-feedback-gt00b7` across
the three repositories on the method.

The Requester used the method on a fourth project and reported that it made
the *user* think about archreator instead of about their own product: it asked
questions it then answered itself, asked others about a future nobody had
scheduled, and put its own vocabulary in front of somebody who only wanted a
feature. This initiative takes the method to 0.3 by deleting what generated
that, and adds the principle that decides when to interrupt at all.

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 0_business-design | No change in this tree. In the organization's, `PREL5` drops the Design gate's output from what the method delivers |
| 1_strategy | The organization gains `ORG.P8`. Here, `G2` and `OUT2` are restated for two gates and for an Approvals table that records only what happened |
| 2_business | `BSVC1` still stops the change at the gates that apply, and there are two of them. In the organization's tree, `ORG.ACT2`'s decision rights and escalation now state the same rule |
| 3_information | No change — the record types are unchanged, and the retired open-questions log was never one of them |
| 4_application | `ASVC1` stops at Direction and Understanding. `ACMP1` is still eighteen skills |
| 5_technology | No change |

## What the evidence said

Read across the twenty-six scope documents in this repository and in
[`ea_bigview`](https://github.com/roanboc/ea_bigview), including the
[pre-0.2 corpus](https://github.com/roanboc/architecture-archreator/tree/pre-02-2026-08).

| Measure | Count |
| ------- | ----- |
| Approval rows written | 103 |
| Of those, a real grant with a named approver and a date | 32 |
| Written only to say a gate did not apply | 48 |
| Direction rows, and Direction rows ever granted | 27, and 1 |
| Understanding rows, and Understanding rows granted | 27, and 21 |
| Design rows, and Design rows marked not applicable | 26, and 16 |
| Open questions recorded | 41 |
| Answered by the Requester | 9 |
| Closed by the agent alone, having asked nobody | 22 of the 30 indexed |
| About a hypothetical future rather than anything blocking | 14 |

**The gate the complaint never mentions is the only one that reliably fired.**
Understanding was granted in 21 of its 27 rows. Direction fired once in
twenty-seven. What the Requester met was not a gate stopping the work — it was
the bookkeeping and the questions around it.

**The Requester had already said this once, in the method's own records.** On
2026-08-27, quoted in decision 2 of the pre-0.2 corpus: *"Move on with all the
gates. Ask me only real critical questions and decide all the rest."* The
method's answer at the time was to invent a record type for delegating gates,
and three more delegations followed. This initiative answers it by asking less.

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | Three gates, one of them an opt-in offered to the Requester as a method choice; a row for every gate that did not apply; an optional register of questions the agent would go on to answer itself; skills that argued for their own rules |
| **Target** (delivered) | Two gates, both blocking before code; a row only where something happened; a call the agent takes, applies and marks draft; skills that state the behaviour |

## Work packages and deliverables

### WP1 — The Design gate is deleted

- **Deliverables:** `align-change-through-layers/SKILL.md`,
  `discover-current-landscape/SKILL.md` (its two gate presentations merged into
  one at Understanding), `docs/method.md`, `docs/process/*`,
  `docs/standards-alignment.md`, the three manifests, `site/index.html`,
  `site/start.html`, the scaffold and eleven asset templates.
- **Outcome:** an ordinary change meets one gate and is never asked to choose
  a second.

### WP2 — An ungranted gate gets no row

- **Deliverables:** `write-scope-document/SKILL.md`, both pull-request
  templates, `assets/layers/scope/README.md`.
- **Outcome:** the Approvals table is a record rather than a census.

### WP3 — The open-questions log is retired

- **Deliverables:** `assets/layers/scope/open-questions.md` deleted; the
  optional-log section of `write-scope-document`, the template's Open questions
  block, and every cross-reference removed.
- **Outcome:** an interpretation the agent adopted is recorded where it
  applies, in that row's `Source` cell, in a document that stays `◐`.

### WP4 — The zen principle

- **Deliverables:** `ORG.P8` in the organization's motivation; one invariant,
  *Ask only what blocks the work now*, in `align-change-through-layers`.
- **Outcome:** the method has one written test for when to interrupt, and the
  question-cadence rules, announcement rules and focus menu are deleted rather
  than reworded.

### WP5 — Diagrams say less and sit where they belong

- **Deliverables:** `check_model.py` checks diagram placement per section
  rather than per document and fails a stereotype on a node outside a fence
  marked `%% legend`; the scaffold's `AGENTS.md` no longer says a *document*
  opens with its diagrams; the `3_information`, `4_application` and deployment
  templates no longer teach a node label with a stereotype, no glyph and no
  identifier.
- **Outcome:** the two rules that were already written are now enforced.

### WP6 — Skills state the behaviour

- **Deliverables:** every skill and reference swept; `docs/skill-format.md`
  gains the one line that says so.
- **Outcome:** the corpus falls from 5,660 lines to 5,088.

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| The method at 0.3, and both worked models corrected for it | Adding the diagram that thirty-three catalogue sections across the three models still lack |
| `ea_bigview` swept for the same change | Whether `1_strategy/README.md` or `1_motivation.md` is right about Direction having been granted |
| The `%% legend` migration across all three repositories | Re-presenting anything already approved |

## Gap notes

- **Thirty-three sections define elements and carry no diagram of their own** —
  eighteen in this repository, fifteen in `ea_bigview`. The rule *one diagram
  per section* has always asked for them; the new check enforces order, not
  presence, because a diagram that only restates the rows beneath it is one the
  same rulebook says to cut. Closing this is per-section modeling work and its
  own initiative.
- **This tree contradicts itself about Direction.**
  `1_strategy/README.md` says Direction covers the layer and was granted when
  the strategy was first discovered; `1_strategy/1_motivation.md` and the front
  door both say the gates are still pending. Correcting either way would invent
  or erase an approval, so both were left. It predates this change.
- **`ART` and `NODE` have prefixes; Application Interface and Representation do
  not.** Two asset templates drew them, could not give them identifiers, and
  lost those nodes in the rewrite. Giving them prefixes is a method change.

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| | | | |

<!--
  Nothing here has been granted. The initiative changes the method's own
  strategy layer through ORG.P8, so it reaches Direction; the row is written
  when it is granted, and not before.
-->
