# AGENTS.md

The architecture model of **the organization that publishes archreator** —
the company, not the method. What it builds is modeled in its own tree,
[`product-archreator/`](../product-archreator/architecture/README.md); this
model names *that* the product exists and never reaches into its elements.

## The rule that governs everything else

**Strategy and business architecture are validated before any other layer,
and the Requester approves at explicit gates before development.** A change
is aligned through the numbered layers, stopped at the gates — Direction,
Understanding, Design — recorded in a scope document, and only then acted
on. Pure bug fixes that change no documented behavior skip the gates but
still update whatever the fix falsifies.

## Who decides

| Role | Held by |
| ---- | ------- |
| **Requester** | The repository owner — the only person who grants a gate |
| **Agent** | Whatever AI agent is working the change, at co-pilot autonomy |
| **Reviewer** | The Requester, on the pull request |

## Modeling depth

**Declared depth: 2 — Organization.** One capability base, one portfolio,
one person who says yes: `0_business-design/` holds the canvases,
`1_strategy/` is derived from them, and domains stay unused until something
the organization builds acquires customers, economics and an approver of its
own.

## Structure and commands

Everything architectural is under [`architecture/`](./architecture/README.md)
— the front door's status table says what is modeled and what deliberately is
not. Initiatives touching this tree are recorded in
[`product-archreator/architecture/scope/`](../product-archreator/architecture/scope/README.md),
one initiative spanning both trees carrying one document.

The validators are shared at the repository root and run before every push:

```bash
python3 ../scripts/check_links.py
python3 ../scripts/check_model.py
```

**Documentation language: English.**
