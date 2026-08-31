# Architecture — archreator, the product

_The front door of this model. Repository-wide rules: [`AGENTS.md`](../AGENTS.md)._

**This folder is what the product knows about itself** — who it is for, which
services it offers, and which piece of the [archreator
repository](https://github.com/roanboc/archreator) realizes each part. Plain
Markdown, one source, no copies.

## What is modeled, and what is not

| # | Layer | The question it answers | Status |
| - | ----- | ----------------------- | ------ |
| 0 | Business design | Who are the customers, and how does each offering pay? | `Out of scope` — the subject is an application; the canvases belong to [the organization](../../org-archreator/architecture/README.md) |
| 1 | [Strategy](./1_strategy/README.md) | Why does this exist, and what must it be able to do? | `Local` — motivation: light, and enough to judge a change against |
| 2 | [Business](./2_business/README.md) | Who does what, and which services are offered? | `Local` — the services, one document |
| 3 | [Information](./3_information/README.md) | What information exists, and where does it live? | `Local` — the data domains and what each owns, one document |
| 4 | [Application](./4_application/README.md) | Which software realizes each service? | `Local` — services and components |
| 5 | [Technology](./5_technology/README.md) | What runs it all? | `Local` — hosts, runtimes and the deployment |
| — | Transition | Where is this going, and in what order? | `Gap` — this model describes the current state only; a roadmap is a later initiative through Direction |

Domains stay unused at Depth 1.

**What is modeled where.** The method's motivation is here, in
[`1_strategy/`](./1_strategy/README.md). Its **process model** is not: it
lives in `docs/process/` of the archreator repository, beside the skills
that realize it, because that adjacency is what lets CI prove every process
has a skill and every skill a process.

## How far each document has been validated

Every document that defines elements opens with `○` not started, `◐` draft
catalogue, or `●` validated at a named gate. **Everything in this model is
`◐` today** — it was rebuilt on method 0.2 from the previous corpus,
preserved at
[`pre-02-2026-08`](https://github.com/roanboc/architecture-archreator/tree/pre-02-2026-08),
and a rebuild is a new draft until the gates are granted again. The
initiative is [scope document 1](./scope/1_rebuild-the-models-on-method-02.md).

## Federation

This model cites the organization's — the contract is
[`federation.md`](./federation.md).
