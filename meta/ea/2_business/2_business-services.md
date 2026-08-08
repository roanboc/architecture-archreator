# Business Services and Rules — archreator

_[← Business layer](./README.md) · [EA home](../README.md)_

**ArchiMate elements:** Business Service, Business Process, Business Rule.

## Business services

What archreator offers whoever adopts it. Each names the document or skill
that realizes it, per `P1`.

| ID | Service | Serves | Realized by |
| -- | ------- | ------ | ----------- |
| `BSVC1` | **Aligned change** — a requirement becomes a change that is consistent with everything already decided | `STK1`, `STK2` | [`ea-first-change`](../../../.claude/skills/ea-first-change/SKILL.md) |
| `BSVC2` | **Discovery** — an unstated strategy or business model becomes a documented one, by asking rather than assuming | `STK1`, `STK2` | [`operating-model-discovery`](../../../.claude/skills/operating-model-discovery/SKILL.md), [`strategy-discovery`](../../../.claude/skills/strategy-discovery/SKILL.md) |
| `BSVC3` | **Right-sizing** — the method costs what the subject is worth, and says which weight it picked | `STK1`, `STK2` | The depth ladder in [`docs/ea/README.md`](../../../docs/ea/README.md#modeling-depth); [`project-bootstrap`](../../../.claude/skills/project-bootstrap/SKILL.md) |
| `BSVC4` | **Approval that counts** — a business judgment is exercised by whoever holds it and survives in the record | `STK3` | `ea-first-change` § The gates and § Where a gate happens; the Approvals table in [`scope-doc`](../../../.claude/skills/scope-doc/SKILL.md) |
| `BSVC5` | **Federated scale** — a business line is modeled on its own terms without being flattened into the enterprise | `STK1` | [`domain-modeling`](../../../.claude/skills/domain-modeling/SKILL.md); [`docs/ea/domains/`](../../../docs/ea/domains/README.md) |
| `BSVC6` | **Staying true** — the model keeps describing today rather than accumulating into an archive | `STK1`, `STK2` | [`restate-current-state`](../../../.claude/skills/restate-current-state/SKILL.md) |
| `BSVC7` | **Method upgrade** — an improvement to the method reaches an existing project without a migration | `STK5` | The plugin manifest at `.claude/.claude-plugin/plugin.json`; **partially Pending** — the mechanism exists, no second version has shipped through it yet |

## Business rules

The rules that constrain how the services are delivered. Each traces to the
principle it enforces.

| ID | Rule | Enforces | Where it bites |
| -- | ---- | -------- | -------------- |
| `RULE1` | No code is written before the Requester grants Gate 2 | `P2` | `ea-first-change` Step 4 |
| `RULE2` | Every EA element names its realizing artifact, or is explicitly "Pending — future initiative" | `P1` | `ea-doc-style` § Grounding rule; `ea-first-change` Step 7 |
| `RULE3` | Every layer gets an explicit verdict in a scope document, including "no change" | `P2` | `scope-doc` § Rules |
| `RULE4` | An approval that isn't recorded didn't happen; a gate that didn't apply is written `N/A — <why>` rather than deleted | `P2` | The Approvals table |
| `RULE5` | An element ID is assigned once and never reused, even after the element is retired | `P5` | `ea-doc-style` § Element IDs; `restate-current-state` |
| `RULE6` | A merged scope document is never rewritten — follow-up work gets a new numbered document | `P5` | `scope-doc`; `restate-current-state` § The one rule |
| `RULE7` | A change that contradicts an existing Principle stops and goes back to the Requester | `P2` | `ea-first-change` Step 1c, Conflict verdict |
| `RULE8` | Changing a domain's exposed service requires the consuming domains' Requesters at Gate 2 | `P2` | `domain-modeling` § Cross-domain changes |
| `RULE9` | A skill links only within `.claude/skills/`; it names a project's documents in code spans | `P3` | `ea-doc-style` § Links. Added when packaging as a plugin made outbound links resolve to nothing |

## The process, in one view

```mermaid
flowchart LR
  req(["Requirement<br>or problem"]):::business
  depth["«Business Process»<br>Confirm depth,<br>locate domain"]:::business
  align["«Business Process»<br>Align layers 1–3"]:::business
  gate{"RULE1<br>Gate 2 granted?"}:::business
  build["«Business Process»<br>Align 4–5,<br>implement"]:::business
  verify["«Business Process»<br>Verify RULE2,<br>open PR"]:::business
  merged(["Merged"]):::business

  req --> depth --> align --> gate
  gate -- no --> align
  gate -- yes --> build --> verify --> merged

  classDef business fill:#fffbb5,stroke:#b8a200,color:#333
```

The full version, including the discovery branches and all four gates, is
the process flow in [CONTRIBUTING.md](../../../CONTRIBUTING.md) — not
restated here, per `P3`.
