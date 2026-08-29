# Project Scope — Recover pre-rebuild learning

_[← Scope index](./README.md) · [Model home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** the pull request for this initiative.

The clean-room rebuild correctly discarded an obsolete model and vendored
skill corpus, but it also made the evidence behind two lasting method rules
hard to discover. This initiative restores the reusable engagement evidence
and links the immutable approval history without presenting the old model as
current architecture.

## EA alignment

| Layer | Impact |
| ----- | ------ |
| 0_business-design | **No change.** The restored note contains no client business facts |
| 1_strategy | **`CAP2.3` evidence corrected.** Engagement-to-method learning has one recorded exercise rather than none |
| 2_business | **No service or rule change.** Existing method behavior gains its missing rationale and approval trail |
| 3_information | **No change.** The recovered note is an existing kind of record |
| 4_application | **No change.** No component or script changes |
| 5_technology | **No change.** No runtime or hosting impact |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — no canvas or business-model change |
| Gate 1 — Strategy | — | — | **N/A** — no stakeholder, driver, goal, outcome or principle changes |
| Gate 2 — Business | Requester | 2026-08-29 | Restore the anonymized engagement evidence, expose initiatives 14–15 as tagged prior art, and retain the roughly fifteen-element catalogue split as the accepted implementation |
| Gate 3 — Solution design | — | — | **N/A** — documentation recovery only |

## Recovered decision

The open question in prior initiative 14 is answered **yes**: below roughly
fifteen elements a leveled catalogue remains one document; above it, it becomes
a folder with one document per level. This keeps small catalogues together and
large catalogues navigable. The threshold remains guidance rather than a hard
validator limit, as current `process-and-capability-levels` specifies.

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** | Current method behavior survived, but its engagement evidence and Gate 2 rationale were reachable only by knowing the preservation tag |
| **Target** | Current readers can find the anonymized evidence, its effect on `CAP2.3`, the accepted threshold, and immutable links to both prior approvals |

## Work packages and deliverables

### WP1 — Restore evidence

- **Deliverables:** engagement note 3, its index row, and the corrected
  `CAP2.3` evidence statement.
- **Outcome:** the learning capability no longer claims it has never run.

### WP2 — Expose prior art without reviving the old model

- **Deliverables:** tagged links to prior initiatives 14 and 15 in the scope
  index, plus this initiative's answer to the threshold question.
- **Outcome:** the old approvals and rationale are discoverable while obsolete
  `.claude/skills/`, component IDs and model structure remain historical.

## In scope / out of scope

| In scope | Out of scope |
| -------- | ------------ |
| Anonymized evidence and immutable prior-art links | Restoring the pre-rebuild model, vendored skills or retired element IDs |
| Recording the threshold already used by the current method | Changing `archreator` behavior |

## Gap notes

- Other pre-rebuild records remain accessible through the preservation tag and
  are not promoted without a demonstrated current use.

## Open questions

None.
