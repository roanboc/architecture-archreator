# Federation

_[← Front door](./README.md)_

The models this one cites. A reference into another model is written
`model::ID` — `org-archreator::G1` — and resolves against that model's own
definitions, because both live in this repository.

| Model | Level | Owner | Where | Relationship |
| ----- | ----- | ----- | ----- | ------------ |
| `org-archreator` | Organization | The Requester | [`../../org-archreator/architecture/`](../../org-archreator/architecture/README.md) | The organization that publishes this product; the product's goals serve its goals |

References run one way: this model cites the organization's elements, never
the reverse — a new product needs to know its parent, and the parent needs
to know nothing about it.
