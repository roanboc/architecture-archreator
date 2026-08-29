# Federation

_[← EA home](./README.md)_

**Status:** ● Validated at **Gate 2**, 2026-08-27 with
[initiative 9](../../product-archreator/architecture/scope/9_federate-the-graph.md).

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
| org-archreator | The organization that publishes archreator | ../../org-archreator/projection/ |
| product-archreator | archreator the method, as a product | ../../product-archreator/projection/ |
| product-archreator/site | The published guidance site | ../../product-archreator/site/projection/ |

Cell 1 is the model's name, cell 2 what it models, cell 3 the directory its
projection is published in — read by position, like the rest of the notation. A
projection is two files: `model.json` for a consumer that parses and `model.db`
for one that queries.

**These are relative paths because all three are published from one
repository.** A model in another repository is named by its full HTTPS URL
instead; a consumer resolves either.

**They point at a portal this repository does not yet publish.** Every tree
here builds one — `scripts/build_docs.py` produces it, projection included —
and no workflow puts it anywhere. The index is correct about where a projection
goes and premature about whether it is there yet, which is the honest state.

## What this cannot do

**Nothing checks that a location still answers**, and nothing should: the
alternative is a validator making network calls on every pull request, which is
a slow, flaky check on a fact that changes rarely. A reader who follows a dead
location learns it the ordinary way, and decides whether that is news.

**A relationship crosses a model now, and this table is what lets it.** When
this document was written it could not: a first draft cited a roadmap gap that
lives in `product-archreator`, and `scripts/check_model.py` rejected it —
correctly, and for exactly the reason the gap existed. The next initiative gave
a foreign identifier a grammar, and the model name it uses is the one **this
table** gives it. A model you may reference is a model you have declared you
federate with.

**The reference still runs one way.** A product's model cites the
organization's; this one never reaches into a product's elements. That is not
a limitation of the grammar — it is the rule this tree is built on, so that a
new product needs to know its parent and the parent needs to know nothing about
it.
