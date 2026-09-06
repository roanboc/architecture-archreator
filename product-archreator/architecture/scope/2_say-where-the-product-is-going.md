# Scope 2 — Say where the product is going, and put the tools on the bench

_[← Scope notes](./README.md) · [Front door](../README.md)_

**Delivered as:** the pull request for this change.
**Approval:** the owner's merge of that pull request. Nothing else records one.

## What and why

The owner asked for three things in one message, filed as
[the request](../reference/2026-09-06-poc-features-request.md): validate the
models as they stand, say what can change now so they keep being exercised
locally, and list the features the product's readers will need — keeping each
as simple as the one the owner values most, proposing a change to an
architecture with text and an agent instead of a modeling tool.

The models were mechanically sound and answered the other two asks not at
all. The product promised
[a model that says where the subject is going [G6]](../1_strategy/1_motivation.md#goals-and-outcomes)
and had no roadmap of its own; the reading tools were named in the repository
rules with no address; the validator here had fallen one check behind the
method's; and the only change on record was a rebuild.

## What changed

- **Where the product is going** — `architecture/6_transition/`: three
  features, nine missing pieces, and the order. Draft until the owner marks
  it reviewed.
- **The request, filed** — `architecture/reference/`, cited by every row
  above.
- **The bench** — a `Makefile` at the repository root: fetches the method
  under gitignored `.archreator/`, runs the validators, fails on drift from
  the method's scripts, wraps every reading tool and builds both portals. Run
  by hand before a push; CI keeps running the two validators only.
- **Corrections** — `scripts/check_model.py` level with the method, and the
  brief command in `CLAUDE.md` and `scripts/README.md` carrying the `--scope`
  it needs.
- **The rules of this repository** — `CLAUDE.md`, both `AGENTS.md` and
  `CONTRIBUTING.md` now say the light form: the agent walks the layers,
  writes the note and opens the pull request, and the owner's merge is the
  approval. No gates, no approvals table, no questions about the future.

## Layers touched

| Layer | Verdict |
| ----- | ------- |
| org, every layer | No change |
| product, 1 to 5 | No change — every feature serves a goal the strategy already holds, and every tool the bench wraps is catalogued already |
| product, transition | New |
| product, reference | New |

## Left out

- Closing any missing piece beyond the three this change closes. Each is its
  own change, in the order given.
- Any change to the method itself. The findings below belong in the
  archreator repository.
- Anything hosted on another platform. A separate solution, synced back when
  it exists.

## Findings for the method

1. `coverage` reports a row as not true yet when the marker appears
   mid-sentence, where the parse anchors it to the start of a cell; two rows
   in these trees are misreported.
2. `build_brief.py --project <tree>` still stops on an identifier both trees
   own until `--scope <tree>` is repeated.
3. The walk never asks `trace` or the impact brief what a change would touch
   before the pull request is opened.
4. No check opens the paths a `Lives at` cell names; with the method on the
   bench, it is one existence test per path.
5. A model declares the method version it was written against nowhere a
   tool can read.
6. `coverage` does not see `Lives at` as grounding, so the component
   catalogue counts as grounding nothing.
7. The full process — gates that stop the conversation, an approvals table,
   status marks promoted per gate, an authorization stop for publishing, an
   open-questions log — cost the owner a round of questions unrelated to the
   product. This repository now runs the light form above; the method could
   offer it as the default for a single owner who is also the reviewer.
