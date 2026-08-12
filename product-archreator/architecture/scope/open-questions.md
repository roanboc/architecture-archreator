# Open questions — archreator

_[← meta index](../../README.md) · [Scope documents](./README.md)_

Interpretations adopted while changing **the method itself** that still need
confirmation, plus the record of ones that have been settled. The
consolidated index across all of [`product-archreator/scope/`](./README.md), so a
question doesn't get lost inside an old scope document.

Rows move from Pending to Resolved by the
[`restate-current-state`](../../../.claude/skills/restate-current-state/SKILL.md)
skill, or by the initiative that answers them. A row only moves when the
answer already exists somewhere — closing a question because nobody
remembers it is how a model starts lying.

## Pending

| # | Question | Interpretation adopted | Raised in |
| - | -------- | ---------------------- | --------- |
| 3 | Does `RULE6` (merged scope documents are never rewritten) need technical enforcement, or is the convention enough? | Convention is enough at current scale. A pre-merge check comparing merged scope documents against their merge-commit versions would close it, and is not worth building until a project has enough contributors for the convention to fail | [1_technology-services.md](../5_technology/1_technology-services.md) |
| 4 | Is a three-level cap on domain nesting right, or should a fourth level be allowed for genuine conglomerates? | Three, with separate repositories federated by contract as the answer beyond it. Untested — no model has reached even three | [1_repo-value-and-fractal-domains.md](./1_repo-value-and-fractal-domains.md) |
| 10 | Does an implementation tier ever own a «Driver» of its own? | **Yes, when the driver is about delivery rather than about the product.** The site's `DRV2` — English-only guidance excludes readers — is its own; `DRV1` — nothing shows the method applied — is the method's. The boundary is judgement and the tier rule does not sharpen it | [10_what-belongs-at-which-tier.md](./10_what-belongs-at-which-tier.md) |
| 11 | How does a document in one project reference an element owned by another? | **No notation exists, and `check_model` correctly rejects the attempt** — IDs are scoped per project, so a backticked `RULE11` in the organization's tree is an unresolvable reference, not a citation. The workaround adopted here is to name the owning skill and section in prose instead of the identifier. `domain-modeling` has qualified IDs (`SALES.BSVC3`) for domains *within* a project; nothing covers across projects, which is the federation the method recommends to every adopter | [10_what-belongs-at-which-tier.md](./10_what-belongs-at-which-tier.md) |
| 12 | Should a cross-model citation record the version of the model it was written against? | **Not yet.** A bare `product-archreator:RULE11` says nothing about which commit was true when it was written, so a parent can change silently under a child. A submodule pin would answer it structurally, which is a reason to prefer one when a second repository exists | [11_referencing-across-models.md](./11_referencing-across-models.md) |

## Resolved

| # | Question | Answer | Resolved in |
| - | -------- | ------ | ----------- |
| 9 | Should the guidance site keep its own model once nested inside the method's tree, or fold into it? | **Keep its own, and now with a rule behind it.** `RULE11` says what an implementation tier's model contains — it refines what the product exposed and never restates it — so "keep its own" is a definition rather than an adopted interpretation. [Decision 8](../decisions/8_where-an-implementations-model-lives.md) separately makes the *location* the Requester's call | [10_what-belongs-at-which-tier.md](./10_what-belongs-at-which-tier.md) |
| 1 | Should the template repository be **generated** from the plugin, or hand-maintained alongside it? | **Generated.** The scaffold moved inside `project-bootstrap`, at `templates/`, and the skill copies it into the project. The two can no longer drift because there is only one of them | [9_the-repository-says-what-it-is.md](./9_the-repository-says-what-it-is.md) |
| 5 | Where should archreator record its own architecture, given that `docs/` must stay blank for cloners? | **Superseded, and the premise with it.** The answer was `meta/`, because a blank `docs/` had to sit at the root for cloners. Once the scaffold shipped inside the skill that emits it (question 1), nothing had to stay blank, and the tree was renamed `product-archreator/` for what it holds | [9_the-repository-says-what-it-is.md](./9_the-repository-says-what-it-is.md) |
| 6 | Should skills keep relative links to project documents, now that they ship as a plugin? | No — a plugin is copied to a cache, so an outbound link resolves to nothing. Skills name paths in code spans instead. Became `RULE9` | [decision 1](../decisions/1_plugin-root-inside-claude-dir.md) |
| 7 | Should element IDs be renumbered per domain when a flat model is split? | No. Existing IDs keep their numbers; per-domain numbering applies to new elements only | [decision 2](../decisions/2_no-renumbering-on-domain-split.md) |
| 2 | Should the shared capability base in a Depth 3 model ever become a domain of its own? | **Withdrawn, not answered.** The question came from a fictional model that has since been removed, so nothing in this repository turns on it. A real project with three or more consuming lines should ask it again from its own evidence — the previous answer ("a domain with no customers of its own is a shared service, not an organization") was reasoning about an invented case | [4_remove-the-fractal-example.md](./4_remove-the-fractal-example.md) |
| 8 | Is the SQLite projection worth building? | Not yet. Validation needs a parse, not a store; the graph is implicit and `grep` traverses it. Four trigger conditions would change the answer | [decision 4](../decisions/4_defer-the-model-database.md) |
