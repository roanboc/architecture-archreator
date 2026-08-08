# Open questions — archreator

_[← meta index](./README.md) · [Scope documents](./scope/README.md)_

Interpretations adopted while changing **the method itself** that still need
confirmation, plus the record of ones that have been settled. The
consolidated index across all of [`meta/scope/`](./scope/README.md), so a
question doesn't get lost inside an old scope document.

Rows move from Pending to Resolved by the
[`restate-current-state`](../.claude/skills/restate-current-state/SKILL.md)
skill, or by the initiative that answers them. A row only moves when the
answer already exists somewhere — closing a question because nobody
remembers it is how a model starts lying.

## Pending

| # | Question | Interpretation adopted | Raised in |
| - | -------- | ---------------------- | --------- |
| 1 | Should the template repository be **generated** from the plugin, or hand-maintained alongside it? | Hand-maintained for now — acceptable while twelve skills are reviewable by eye. The two can drift, and nothing detects it | [1_repo-value-and-fractal-domains.md](./scope/1_repo-value-and-fractal-domains.md) |
| 2 | Should the shared capability base in a Depth 3 model ever become a domain of its own? | No — a domain with no customers of its own and no distinct economics is a shared service, not an organization. Revisit if a real project hits three or more consuming lines | [`example-company` initiative 2](../example-company/docs/scope/2_split-into-domains.md) |
| 3 | Does `RULE6` (merged scope documents are never rewritten) need technical enforcement, or is the convention enough? | Convention is enough at current scale. A pre-merge check comparing merged scope documents against their merge-commit versions would close it, and is not worth building until a project has enough contributors for the convention to fail | [1_technology-services.md](./ea/5_technology/1_technology-services.md) |
| 4 | Is a three-level cap on domain nesting right, or should a fourth level be allowed for genuine conglomerates? | Three, with separate repositories federated by contract as the answer beyond it. Untested — no model has reached even three | [1_repo-value-and-fractal-domains.md](./scope/1_repo-value-and-fractal-domains.md) |

## Resolved

| # | Question | Answer | Resolved in |
| - | -------- | ------ | ----------- |
| 5 | Where should archreator record its own architecture, given that `docs/` must stay blank for cloners? | In `meta/` — a parallel tree holding archreator's own EA, scope documents, decisions, and this log. `docs/` is what a cloner gets; `meta/` is what archreator did to itself | [2_archreator-models-itself.md](./scope/2_archreator-models-itself.md) |
| 6 | Should skills keep relative links to project documents, now that they ship as a plugin? | No — a plugin is copied to a cache, so an outbound link resolves to nothing. Skills name paths in code spans instead. Became `RULE9` | [decision 1](./decisions/1_plugin-root-inside-claude-dir.md) |
| 7 | Should element IDs be renumbered per domain when a flat model is split? | No. Existing IDs keep their numbers; per-domain numbering applies to new elements only | [decision 2](./decisions/2_no-renumbering-on-domain-split.md) |
