# Federation

_[← EA home](./README.md)_

**Status:** ● Validated at **Gate 2**, 2026-08-27 with
[initiative 8](../../product-archreator/architecture/scope/8_federate-the-graph.md).

This organization builds one product, and that product has a site nested under
it. Three models, maintained apart, belonging together — which is what a
federation is, at the smallest size one can be.

The index lives here rather than in either product model because "which models
exist and where they are" is an enterprise-layer fact. It is the machine-readable
form of something this tree already carried in prose: the **Modeled in** column
of [the component catalogue](./4_application/2_application-components.md), which
names the tree holding each component's detail.

## Nobody owns the union

There is no central model here and there is not meant to be one. A model that
held every other model's elements would restate what those models own, which
the tier rule in `architecture-document-style` forbids, and its owner would
need approval rights over elements they did not write.

What is centralized is **this list**. The graph is a view, assembled when
somebody opens it, owned by no one.

## The index

| Model | Subject | Projection |
| ----- | ------- | ---------- |
| org-archreator | The organization that publishes archreator | ../../org-archreator/navigator/ |
| product-archreator | archreator the method, as a product | ../../product-archreator/navigator/ |
| product-archreator/site | The published guidance site | ../../product-archreator/site/navigator/ |

Cell 1 is the model's name, cell 2 what it models, cell 3 where its projection
is published — read by position, like the rest of the notation. Cell 3 names
the directory: a projection is two files, `model.json` for a consumer that
parses and `model.db` for one that queries.

**These are relative paths because all three are published from one
repository.** A model in another repository is named by its full HTTPS URL
instead; the navigator resolves either.

**They point at a portal this repository does not yet publish.** Every tree
here builds one — `scripts/build_docs.py` produces it — and no workflow puts it
anywhere. The index is correct about where a projection goes and premature
about whether it is there yet, which is the honest state and exactly what the
navigator reports when it cannot fetch one.

## What this cannot do

**Nothing checks that a location still answers**, and nothing should: the
alternative is a validator making network calls on every pull request, which is
a slow, flaky check on a fact that changes rarely. The navigator names what it
could not reach, and a person decides whether that is news.

**A relationship still does not cross a model.** These three graphs are shown
together and are not joined. This tree's `ACMP1` — the skill corpus — is
described in far more detail one tree over, and there is no way to write that
relationship down: an identifier is scoped to its model, and naming a foreign
one fails the reference check.

Writing this document proved it. A first draft cited the roadmap gap that
tracks the problem, which lives in `product-archreator`, and
`scripts/check_model.py` rejected it — correctly, and for exactly the reason
the gap exists. Until the next initiative gives a foreign identifier a grammar,
a cross-model reference is a sentence and a link, as here.
