# AGENTS.md

The architecture model of **archreator the method, as a product** — its
skills, validators, tools, scaffold and guidance site. The organization that
publishes it is modeled in
[`org-archreator/`](../org-archreator/architecture/README.md); this model
cites the organization's elements where it serves them, never the reverse.

## How a change happens here

The owner says what they want. The agent works out which layers the change
touches, edits them, writes a short note in
[`architecture/scope/`](./architecture/scope/README.md), and opens a pull
request. **The owner's merge is the approval.** The agent stops to ask only
when the change contradicts a principle or a written decision, or when two
readings of the request would build different things. Pure corrections are
just fixed.

## Who decides

The owner. The agent drafts and implements; the owner reviews and merges.

## Modeling depth

**Declared depth: 1 — Application.** The subject is one product: a light
strategy layer to judge changes against, and the layers that describe what
actually ships. The guidance site is part of this product — it realizes one
of its services — not a project of its own.

## Structure and commands

Everything architectural is under [`architecture/`](./architecture/README.md);
the front door's status table is the map. Notes on changes live in
[`architecture/scope/`](./architecture/scope/README.md), one per change,
including changes that span this tree and the organization's. Where the
product is going is [`architecture/6_transition/`](./architecture/6_transition/README.md).
Retrospective notes — one per finished change or engagement, numbered
chronologically — live in `architecture/engagements/`.

The validators are shared at the repository root and run before every push:

```bash
python3 ../scripts/check_links.py
python3 ../scripts/check_model.py
```

**Documentation language: English.**
