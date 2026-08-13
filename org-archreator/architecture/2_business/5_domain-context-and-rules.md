# Domain Context and Rules — the organization behind archreator

_[← Business layer](./README.md) · [EA home](../README.md)_

**ArchiMate elements:** Business Rule, and the glossary that fixes what the
other documents' words mean.

Two sections, and one of them is deliberately empty.

## The glossary

Terms this organization uses in a fixed sense. A word not listed here means
what it ordinarily means; a word listed here means **only** this, in every
document in this tree.

| Term | Means, here | Does not mean |
| ---- | ----------- | ------------- |
| **Requester** | The human who grants gates for a given project — `ACT1` in this organization's own work, `ROLE3` on a client engagement. Always a person, never a committee and never an agent | A customer, a sponsor, or whoever paid |
| **Adopter** | Someone using the method on their own project, without engaging this organization. Reaches it through `BIF1`–`BIF3` and is never seen again — the source of `DOBJ5`'s absence | A client, a user account, anyone this organization can count |
| **Engagement** | A client relationship where `ROLE2` performs the work personally, delivering `BOBJ6`. Bounded, paid, and the only place client-confidential material exists | An installation of the method, or a support arrangement |
| **Initiative** | One change to one model, from framing through delivery, recorded in exactly one scope document with its own Approvals table — `BOBJ2` | A project, a release, or a body of work spanning several models |
| **Gate** | A named point where a Requester accepts named documents on a date, recorded whether granted, declined or `N/A`. An approval that is not recorded did not happen | A review, a checkpoint, or a stage a process passes through |
| **Tier** | How much design detail a model carries and which model it defers to — enterprise, product, or implementation. Held by the method, not by this organization | Modeling depth, which says how much of the six layers gets filled in |
| **Model** | A subject described through the numbered layers — `BOBJ1`. One per project, with its own identifier space | The repository holding it, or any one document within it |
| **The method** | `PROD1`: the skills, the conventions, the gates and the scaffold. Distinct from **this organization**, which publishes it, and from **archreator** unqualified, which is ambiguous between the two | The documentation, the site, or this model |

**"archreator" names three things** and the glossary cannot fix that: the
organization, `PROD1`, and the repository. Every document in this tree should
qualify it — *the method*, *this organization* — and where it appears bare, a
reader should assume the product. The collision is
[decision 7](../../../product-archreator/architecture/decisions/7_one-tree-per-federated-project.md)'s
subject, and the directory prefixes are what resolve it on disk.

## Business rules

**None at this tier — and that is a verdict, not an omission.**

Every rule that governs how this organization works is a rule of **the
method**, held one tier down in `product-archreator`'s business layer, where
twelve of them live. This organization does not add rules of its own: it
follows the method it publishes, which is the strongest available claim that
the method is usable, and the claim would be worth nothing if the organization
kept a private set.

The tier rule — a tier refines what the tier above exposed and never restates
it, in `architecture-doc-style` § What belongs at which tier — is what makes
this the correct answer rather than a gap. Copying the twelve rules up here to
make the file look complete is precisely what it forbids. (Naming that rule by
its identifier is not possible from this tree: identifiers are scoped per
project and the method owns it. That limitation is the method's open question
11, and this is its third occurrence.)

The one thing that would change this: a rule binding **the organization** and
not anyone using the method — how an engagement is priced, what may be said
about a client, when `ROLE2` declines work. `BOBJ5`'s confidentiality boundary
is the likeliest first candidate, and it is currently carried by the
`engagement-retrospective` skill rather than by a rule here.

## Retired

None. This document is new as of
[initiative 4](../scope/4_completing-the-business-layer.md).
