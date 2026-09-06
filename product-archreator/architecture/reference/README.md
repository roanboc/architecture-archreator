# Reference documents

_[← Front door](../README.md) · [Scope documents](../scope/README.md)_

The material this model was built from, kept exactly as it was provided.

**This is not the model.** Nothing here defines an element or carries an
identifier, and the validators do not read it — a message in which somebody
names an element is a person talking, not a definition. Neither is it
published: the portal and a brief hand a reader the model, and what somebody
said in a working session carries everything else that was in the room.

Agent guidance: the `architecture-document-style` skill § Reference documents.

## What it is for

One question, asked late and hard to answer without it: **where did this come
from?** An element identified in a draft catalogue names its source here,
which is what lets the gate that validates it be a review rather than an act
of faith.

## Naming

`YYYY-MM-DD-<short-description>.<ext>`, plain ASCII with hyphens. The date is
when the meeting happened, else when the document was shared, else when it
was added here — the first that can be established, and the index says which.

## Index

Every file gets a row, including one nothing has been derived from yet — this
is a record of what was received, not only of what was used.

| Date | Fixed by | File | Original name | Provided by | Derived into |
| ---- | -------- | ---- | ------------- | ----------- | ------------ |
| 2026-09-06 | shared | [`2026-09-06-poc-features-request.md`](./2026-09-06-poc-features-request.md) | — a message in the working session, not a file | The Requester | [The roadmap](../6_transition/README.md), every plateau and gap in it; [scope document 2](../scope/2_say-where-the-product-is-going.md) |

- **Fixed by** — which rule gave the date: *meeting*, *shared* or *added*.
- **Derived into** — the documents or elements that came out of it, or
  *nothing yet*.

## What does not belong here

| Not this | Where it goes |
| -------- | ------------- |
| A reading of what a document means | The layer document it informs, cited back here |
| A decision taken in the conversation | `architecture/decisions/`, or a scope document |
| Anything with an element identifier | The model. If it has identifiers, it is not a reference document |
| Credentials, personal data, or anything shared in confidence that the model does not need | Nowhere in the repository |
