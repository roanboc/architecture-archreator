# AGENTS.md

The architecture model of **the organization that publishes archreator** —
the company, not the method. What it builds is modeled in its own tree,
[`product-archreator/`](../product-archreator/architecture/README.md); this
model names *that* the product exists and never reaches into its elements.

## How a change happens here

The owner says what they want. The agent works out which layers the change
touches, edits them, writes a short note in
[`product-archreator/architecture/scope/`](../product-archreator/architecture/scope/README.md),
and opens a pull request. **The owner's merge is the approval.** The agent
stops to ask only when the change contradicts a principle or a written
decision, or when two readings of the request would build different things.
Pure corrections are just fixed.

## Who decides

The owner. The agent drafts and implements; the owner reviews and merges.

## Modeling depth

**Declared depth: 2 — Organization.** One capability base, one portfolio,
one person who says yes: `0_business-design/` holds the canvases,
`1_strategy/` is derived from them, and domains stay unused until something
the organization builds acquires customers, economics and an approver of its
own.

## Structure and commands

Everything architectural is under [`architecture/`](./architecture/README.md)
— the front door's status table says what is modeled and what deliberately is
not. Changes touching this tree are noted in
[`product-archreator/architecture/scope/`](../product-archreator/architecture/scope/README.md),
one change spanning both trees carrying one note.

The validators are shared at the repository root and run before every push:

```bash
python3 ../scripts/check_links.py
python3 ../scripts/check_model.py
```

**Documentation language: English.**
