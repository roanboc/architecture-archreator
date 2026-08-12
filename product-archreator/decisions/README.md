# Decisions — archreator

_[← meta index](../README.md) · [EA home](../architecture/README.md)_

Consequential calls about **the method itself** that are smaller than an
initiative but too significant to leave buried in a PR thread. Written with
the [`decision-record`](../../.claude/skills/decision-record/SKILL.md)
skill, numbered chronologically.

A decision record supplements a scope document, never replaces it: if the
call also changed EA elements, the scope document in
[`product-archreator/scope/`](../scope/README.md) is the primary record and the decision
explains *why* one row reads the way it does.

| # | Decision | Status | Touches |
| - | -------- | ------ | ------- |
| 1 | [1_plugin-root-inside-claude-dir.md](./1_plugin-root-inside-claude-dir.md) | Accepted | `ACMP14`, `RULE9` |
| 2 | [2_no-renumbering-on-domain-split.md](./2_no-renumbering-on-domain-split.md) | Accepted | `RULE5`, `P5` |
| 3 | [3_agent-autonomy-level.md](./3_agent-autonomy-level.md) | Accepted | `ACT2` |
| 4 | [4_defer-the-model-database.md](./4_defer-the-model-database.md) | Accepted | `ACMP15`, `RULE5` |
| 5 | [5_no-per-product-strategy-folders.md](./5_no-per-product-strategy-folders.md) | Accepted | `1_strategy/`, `domains/` |
| 6 | [6_the-portability-boundary.md](./6_the-portability-boundary.md) | Accepted | `P6`, `RULE9`, `CH3`, `ACMP4` |
| 7 | [7_one-tree-per-federated-project.md](./7_one-tree-per-federated-project.md) | Accepted | decision 5, `ACMP4`, `BSVC2` |
