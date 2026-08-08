# CLAUDE.md

Solvara AI (fictional) is a small AI consultancy that also sells an AI
product subscription. This folder holds its **operating model** — the
business model canvases and the enterprise architecture derived from them.
There is no application code here and there is not meant to be: the
architecture is the product. See [`../CLAUDE.md`](../CLAUDE.md) for the rule
that governs the method, and
[`docs/scope/1_model-the-operating-model.md`](./docs/scope/1_model-the-operating-model.md)
for how it was applied here.

## The rule that governs everything else

**Strategy and business architecture are validated before any other layer,
and the requester approves at explicit gates before development.** Because
the subject here is an organization rather than an application, the walk
starts one layer earlier than usual: the value proposition and business
model canvases in `docs/ea/0_business-design/` come first, are approved at
**Gate 0 — Business model**, and everything in `1_strategy` and `2_business`
is *derived* from them rather than written alongside them.

Use the `operating-model-discovery` skill for the canvases and Gate 0,
`strategy-discovery` for the derivation and Gate 1, `ea-first-change` for
the process as a whole, `scope-doc` for the scope document (its Approvals
table is the durable record of the gates), and `ea-doc-style` when touching
anything under `docs/`. If a change touches an AI actor's autonomy level or
decision rights — `ACT3` or `ACT4` — it needs a `decision-record` alongside
the scope document.

## Modeling depth

**Declared depth: 3 — Enterprise.** Two business lines — Advisory and
Product — are modeled as [domains](./docs/ea/domains/README.md), each with a
charter naming what it exposes. The enterprise layers hold what is true
across both; the domains hold what isn't.

Use the `domain-modeling` skill for anything touching a domain boundary.
Changing `ADVISORY.BSVC9` — the one service that crosses between them —
needs the Product domain's Requester at Gate 2 as well as Advisory's.

## Layout

- `docs/ea/0_business-design/` — the canvases everything else derives from;
  `docs/ea/1_strategy/`, `docs/ea/2_business/` — the derived architecture,
  at the enterprise level; `docs/ea/domains/` — one charter per business
  line; `docs/scope/` — one document per initiative.
- Layers 3–5 do not exist. Nothing has been built, so there is no data,
  application, or technology architecture to describe.
- The domains carry charters and no layer folders yet — the charter comes
  first by design, and each domain layer is created by the initiative that
  first touches it.

## Commands

None. This project has no code, no build, and no tests. Verification is
`python3 ../scripts/check_links.py` from the repository root, plus the
alignment checklist in `ea-first-change` step 7.

## Conventions

- Documentation language: English. Folder and file names stay plain ASCII.
- Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`, …).
- **Element IDs** (`ea-doc-style` § Element IDs) are how documents refer to
  each other's elements — write `relieves PAIN2`, not a repeated
  description. An ID is assigned once and never reused.
- **The grounding rule applies to people, not files.** An organization's
  capabilities are realized by teams, roles, and written procedures; name
  the one that realizes each element, or mark it
  **"Pending — future initiative"**.
- **Canvases are the source; layers 1–2 are derived.** If a derived element
  and its canvas block disagree, the canvas is right and the derivation is
  stale — and correcting the canvas means re-passing Gate 0.
