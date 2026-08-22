# CLAUDE.md

The architecture model of **the organization that publishes archreator** — the
company, not the method. What it builds is modeled in its own trees:
[`product-archreator/`](../product-archreator/architecture/README.md) for the
method, and the site nested inside it.

Repository-wide rules, the actors and the commands are in the
[root `CLAUDE.md`](../CLAUDE.md). This file carries only what is specific to
this tree.

## Modeling depth

**Declared depth: 2 — Organization.**

The subject is an organization sharing one strategy: one capability base, one
portfolio of things it builds, and one person who says yes. So
`0_business-design/` is filled with the value proposition and business model
canvases, `1_strategy/` is complete, and
[`architecture/domains/`](./architecture/domains/README.md) stays **unused**.
Gates 0 to 3 apply.

**When to move to Depth 3.** When something the organization builds acquires
customers, economics and an approver distinct from the rest of it. That day the
model splits into domains — an ordinary initiative, not a restart.

## What this tree owns, and what it does not

This model holds the organization's **motivation, capabilities, resources and
courses of action**. It names *that* a product exists and links to its tree; it
never reaches into that tree's elements. A product's own components, technology
and scope history belong to the product.

References run one way — a product's model cites the organization's, never the
reverse — so a new product needs to know its parent and the parent needs to
know nothing about it.

## Structure

- `architecture/` — six numbered layers, plus `scope/` (one document per
  initiative), `decisions/` and `engagements/`.
- `engagements/` — what applying the method to a real client taught, generalized
  past recognition of the client. Not architecture, and no elements are defined
  there.
