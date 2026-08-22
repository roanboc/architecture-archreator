# CLAUDE.md

The architecture model of **the published guidance site** — the one-page
public front door at <https://roanboc.github.io/archreator/>, whose source is
`site/` in the [`archreator`](https://github.com/roanboc/archreator)
repository.

Repository-wide rules, the actors and the commands are in the
[root `CLAUDE.md`](../../CLAUDE.md). This file carries only what is specific
to this tree.

## Modeling depth

**Declared depth: 1 — Application.**

The subject is one deliverable. It has no customers, revenue or staff of its
own, so `0_business-design/` stays empty and `domains/` stays unused. **Gate 2
is the gate that applies.**

## Why this is a tree and not a folder

It nests inside [`product-archreator/`](../CLAUDE.md) because it realizes one
of that product's services rather than standing alone — but it keeps a model
of its own because it has **application components and technology that exist
nowhere else**. That is the test: a folder restates elements belonging
somewhere else; a project has elements of its own.

## What this tree models

The site is a **derived view** of the method: it explains, in public and in
plain English, what the documents in `archreator` say. This model refines what
the product exposes and never restates it — where the site and the method
would say the same thing, this tree points one level up.
