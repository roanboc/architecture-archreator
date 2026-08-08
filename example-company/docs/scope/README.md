# Project Scope Documents — Solvara AI

_[← Project README](../../README.md) · [Enterprise architecture](../ea/README.md)_

One document per initiative, numbered chronologically. The
[EA docs](../ea/README.md) describe the **current** state of the operating
model; each document here describes one **change** to it.

**ArchiMate viewpoint:** Implementation & Migration (Work Package,
Deliverable, Plateau, Gap).

This project runs the template's EA-first process on the **company track**:
because the subject is an organization rather than an application, the walk
starts at [0_business-design](../ea/0_business-design/README.md) and passes
**Gate 0 — Business model** before anything is derived. See
[the template's process write-up](../../../docs/scope/README.md) and the
`operating-model-discovery` skill.

## Initiatives

| #   | Scope document | Delivered as | Summary |
| --- | --------------- | ------------ | ------- |
| 1   | [1_model-the-operating-model.md](./1_model-the-operating-model.md) | `example-company/` on `claude/archreator-operative-model-scaling-0aw3cs` | Documented the business model as two value proposition canvases and two business model canvases, then derived the strategy and key business layers from them — including two AI actors at different autonomy levels. No software delivered |
| 2   | [2_split-into-domains.md](./2_split-into-domains.md) | `example-company/docs/ea/domains/` on `claude/repo-value-ux-review-3ur5y4` | Split the model into Advisory and Product domains with charters, and turned the pending resource `RES6` into an owned cross-domain service, `ADVISORY.BSVC9`. No software delivered |
