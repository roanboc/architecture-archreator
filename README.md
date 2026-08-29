# architecture-archreator

**The worked models.** archreator is a method for modeling how an organization
works so that AI agents can help run it; this repository is that method
applied to real subjects, so a prospective adopter can read a filled-in model
instead of an empty scaffold.

The method itself — seventeen skills, the scaffold, the validators — lives in
[`archreator`](https://github.com/roanboc/archreator).

## What is modeled here

| Tree | Subject |
| ---- | ------- |
| [`org-archreator/`](./org-archreator/architecture/README.md) | The organization that publishes archreator: who it serves, what it must be able to do, and which courses of action it has taken |
| [`product-archreator/`](./product-archreator/architecture/README.md) | archreator the method, modeled as the product it is |
| [`product-archreator/site/`](./product-archreator/site/architecture/README.md) | The published guidance site |

Each tree is a complete model in its own right — six numbered layers, a scope
document per initiative, and a decision log. Identifiers are scoped per tree,
so each may own its own `G1` without collision.

## Reading a tree

Start at its `architecture/README.md`, which carries the notation: what each
glyph means, which shape each element takes, and the colour of each layer.
Then read the layers in their numbered order — the numbering *is* the
assessment order, and reading layer 4 before layer 1 is exactly the mistake
the method exists to prevent.

## Why the models are public

A method that asks organizations to model themselves and shows nothing of
itself is asking on credit. These trees are the evidence: the same skills,
the same gates, the same document conventions, applied to a real organization
and to the method's own development.
