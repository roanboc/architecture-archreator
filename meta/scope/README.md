# Scope documents — archreator

_[← meta index](../README.md) · [EA home](../ea/README.md)_

One document per initiative that changes **the method itself**, numbered
chronologically. While [`meta/ea/`](../ea/README.md) describes archreator's
current state, each of these describes one **change** to it: what it started
from, what it delivered, and what it deliberately left out.

**ArchiMate viewpoint:** Implementation & Migration (Work Package,
Deliverable, Plateau, Gap).

The process is the one in [CONTRIBUTING.md](../../CONTRIBUTING.md) — the
same one a downstream project follows, applied here. A change to a project
*built from* archreator belongs in that project's own `docs/scope/`, not
here.

Related: [decisions](../decisions/README.md) for single calls smaller than
an initiative, and [open questions](../open-questions.md) for the
consolidated index of adopted interpretations awaiting confirmation.

## Initiatives

| # | Scope document | Delivered as | Summary |
| - | -------------- | ------------ | ------- |
| 1 | [1_repo-value-and-fractal-domains.md](./1_repo-value-and-fractal-domains.md) | `claude/repo-value-ux-review-3ur5y4` | Enterprise-first positioning and the modeling-depth ladder; fractal domains with charters and a federation rule; plugin packaging; ten journey defects closed; `example-company` split into two domains |
| 2 | [2_archreator-models-itself.md](./2_archreator-models-itself.md) | `claude/repo-value-ux-review-3ur5y4` | The positioning against TOGAF, ArcKit, BMAD and C4; archreator modeled with archreator at Depth 1, with decisions and an open-questions log; the `restate-current-state` skill |
| 3 | [3_element-id-validator.md](./3_element-id-validator.md) | `claude/repo-value-ux-review-3ur5y4` | `scripts/check_model.py` enforcing `RULE5` in CI; the database dropped from `ACMP15` and deferred with recorded triggers |
| 4 | [4_remove-the-fractal-example.md](./4_remove-the-fractal-example.md) | `claude/repo-value-ux-review-3ur5y4` | Removed the fictional worked example — real projects are the test. Depth 3 is now documented and undemonstrated |
