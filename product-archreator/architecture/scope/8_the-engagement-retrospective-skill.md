# Project Scope — The engagement-retrospective skill

_[← Scope index](./README.md) · [EA home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** `.claude/skills/engagement-retrospective/SKILL.md`, on
branch `claude/repo-value-ux-review-3ur5y4`.

The organization behind archreator took `COA1` and needs a mechanism for its
first stage — capturing what the method did not tell someone to do. That
mechanism is a skill, so it is a change to **the method**, and it is recorded
here rather than in the organization's own scope document.

Twelve skills becomes thirteen. It earns the place because it is the
mechanism of `RS1`, the organization's primary non-monetary return, which
until now has been claimed with nothing behind it. No existing skill fits:
`restate-current-state` compacts a model, `decision-record` captures one
call, and the discovery skills run before the work rather than after it.

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 1_strategy | **No change.** `G4` — the method improves without breaking its users — is served, not altered |
| 2_business | **No change to elements.** `BSVC6` ("staying true") gains a second realizing skill; no new service, because this is the same service reached from the other end — one keeps a model current, the other keeps the method current |
| 3_information | **No change** |
| 4_application | **`ACMP16` added** — the skill, naming its file |
| 5_technology | **No change.** `NODE1` loads it like every other skill |
| domains | **No change** |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — Depth 1 |
| Gate 1 — Strategy | — | — | **N/A** — no strategy change |
| Gate 2 — Business | _awaiting_ | — | The skill, its six questions, its three rules, and `ACMP16` |
| Gate 3 — Solution design | — | — | **N/A** — not requested |

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | Twelve skills. Every method improvement so far came from somebody noticing mid-work; nothing turned that noticing into a step |
| **Target** (delivered) | Thirteen. The noticing has a procedure, an output shape, and a rule about what may not be written down |

## Work packages and deliverables

### WP1 — The skill

- **Deliverables:** `.claude/skills/engagement-retrospective/SKILL.md` — six
  questions, three rules, a note template, and the confidentiality boundary
- **Outcome:** an agent finishing an initiative knows to ask what the method
  failed to cover, and knows what it may not write down

### WP2 — Register it

- **Deliverables:** `ACMP16` in
  [`4_application/1_application-components.md`](../4_application/1_application-components.md);
  the skill tables in [`CLAUDE.md`](../../../CLAUDE.md),
  [`README.md`](../../../README.md) and
  [`.claude/skills/README.md`](../../../.claude/skills/README.md)
- **Outcome:** thirteen skills everywhere the count appears, and the
  grounding rule holds for the new row

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| The skill and its registration | Running it — the first note belongs to the organization, not the method |
| The confidentiality rule | Enforcing it. Nothing checks a note for client facts, and nothing could |
| One skill | Any change to the discovery skills, which stay as they are until a note proposes otherwise |

## Gap notes

- **The confidentiality rule is carried entirely by whoever writes the
  note.** No tool can tell a generalized pattern from a thin disguise. This
  is the same shape as `RULE2` — a rule the method states and review carries
  — but the consequence of failure is worse, because it is somebody else's
  confidence rather than an inaccurate document.
- **A skill nobody invokes is dead code**, and this one has the narrowest
  trigger yet: the end of an initiative, which is exactly when everyone wants
  to stop. `ACMP10` was effectively dead for ten pull requests for the same
  reason — a good description that nothing pointed at. Worth watching whether
  this one gets invoked without being asked for.
- **It proposes and never edits, by design**, which means it can generate a
  backlog nobody works. Two notes containing the same pattern is the trigger
  the skill names; nothing enforces that either.
