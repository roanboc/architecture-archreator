# AGENTS.md

The architecture model of **archreator the method, as a product** — its
skills, validators, tools, scaffold and guidance site. The organization that
publishes it is modeled in
[`org-archreator/`](../org-archreator/architecture/README.md); this model
cites the organization's elements where it serves them, never the reverse.

## The rule that governs everything else

**Strategy and business architecture are validated before any other layer,
and the Requester approves at explicit gates before development.** A change
is aligned through the numbered layers, stopped at the gates — Direction,
Understanding, Design — recorded in a scope document under
[`architecture/scope/`](./architecture/scope/README.md), and only then
implemented. Pure bug fixes that change no documented behavior skip the
gates but still update whatever the fix falsifies.

## Who decides

| Role | Held by |
| ---- | ------- |
| **Requester** | The repository owner — the only person who grants a gate |
| **Agent** | Whatever AI agent is working the change, at co-pilot autonomy |
| **Reviewer** | The Requester, on the pull request |

## Modeling depth

**Declared depth: 1 — Application.** The subject is one product: a light
strategy layer to judge changes against, and the layers that describe what
actually ships. The guidance site is part of this product — it realizes one
of its services — not a project of its own.

## Structure and commands

Everything architectural is under [`architecture/`](./architecture/README.md);
the front door's status table is the map. Initiatives live in
[`architecture/scope/`](./architecture/scope/README.md), one document each —
including initiatives that span this tree and the organization's.

The validators are shared at the repository root and run before every push:

```bash
python3 ../scripts/check_links.py
python3 ../scripts/check_model.py
```

**Documentation language: English.**
