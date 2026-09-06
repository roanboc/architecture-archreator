# Project Scope — Say where the product is going, and put the tools on the bench

_[← Scope index](./README.md) · [Front door](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** the pull request for this initiative, and everything it
contains.

## The problem

The Requester asked three things of the models in one message, filed as
[the request](../reference/2026-09-06-poc-features-request.md): validate the
solution as it stands; say what can change now so that it keeps being
exercised locally; and, wearing the product manager's hat, say which features
the different readers of the method will need — showing what is possible
before any of it moves to a hosted platform, and keeping each feature as
simple as the one the Requester already values most: proposing a change to an
architecture with text, documents and an agent, instead of a modeling tool.

The model answers the first question well and the other two not at all. Both
validators are green, the method's own tests pass, and every reading tool
reads both trees. But the front door said the transition layer was a gap, so
the product that promises
[a model that says where the subject is going [G6]](../1_strategy/1_motivation.md#goals-and-outcomes)
had never said where it was going itself; the reading tools are named in the
repository rules with no address, because they live in a plugin this
repository does not carry; the validators here had fallen one check behind the
scaffold's, and nothing would have said so; and the one initiative on record
is a rebuild, so nobody evaluating the method can read an ordinary change go
through it here.

## The design

- **The roadmap is the deliverable, and it is direction rather than
  permission.** Four plateaus, twelve gaps and a sequence in `6_transition/`,
  each plateau named for a state and each gap for the element it is measured
  from — approved at Direction, and approving it approves no work.
- **One plateau per reader.** The four states are, in the order the product's
  readers meet it: the change that arrives as text, for the Requester and the
  Reviewer of an adopting project; the bench that catches drift, for the agent
  and the maintainer; the federation as one site, for the reader outside the
  repository; and the walk itself brought to a Requester who is not in a
  terminal — on the hosted platform the Requester names, Databricks, where
  the same skills run against a working copy and every approval lands back in
  the repository.
- **The bench lands now, because everything else checks against it.** A
  `Makefile` at the repository root fetches the method under gitignored
  `.archreator/`, wraps every reading tool, fails when a validator here
  differs from the scaffold's, and runs all of it over both trees. It runs
  before a push, by hand: the Requester chose to keep the checks on every
  change to the two validators, so no layer document changes.
- **The request is filed where a source belongs.** `architecture/reference/`
  opens with the Requester's message as written, and every roadmap row cites
  it — the first time a source in this model can be followed back to what
  somebody said.
- **Corrections ride along, gate-free.** The validator is brought level with
  the scaffold, and a documented command that stopped on an identifier both
  trees own now carries `--scope`.
- **Not a graph to explore, and not a second model.** The Requester's
  direction on readers, given on the previous roadmap and preserved at
  [decision 4 of the pre-0.2 corpus](https://github.com/roanboc/architecture-archreator/blob/pre-02-2026-08/product-archreator/architecture/decisions/4_the-graph-portal-is-retired.md),
  holds: a reader arrives with a question and leaves with a document, and a
  Requester arrives with a sentence and leaves with a pull request. The host
  runs the walk over a working copy and never holds a model of its own.

## EA alignment (assessed top-down before recording)

| Tree | Layer | Impact |
| ---- | ----- | ------ |
| org | all | **No change** — the organization's roadmap stays a stated gap on its front door; where the organization is going is the Requester's business, never derived from the product's |
| product | 1_strategy | **No change** — every plateau serves a goal the layer already holds (`G2`, `G3`, `G4`, `G5`, `G7`), and the roadmap itself is what `G6` asks for; the local-first order is recorded in the sequence rather than as a course of action, because a Depth 1 strategy layer carries no catalogue for one |
| product | 2_business | **No change** — the walk the first plateau puts on record is the service [Gated change alignment [BSVC1]](../2_business/1_business-services.md) already describes |
| product | 3_information | **No change** — a reference document is a record the layer already names under [Records [DOBJ2.2]](../3_information/1_data-domains-and-objects.md); the folder now exists |
| product | 4_application | **No change** — the bench is this repository's, not a component of the product; every tool it wraps is catalogued already |
| product | 5_technology | **No change** — the checks on every change stay the two validators, as the deployment table says; the bench is run by hand |
| product | 6_transition | **New** — the roadmap: four plateaus, twelve gaps, the sequence |
| product | reference | **New** — the request, filed and indexed |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Direction, first sitting | The Requester | 2026-09-06 | [The target state](../6_transition/1_target-state.md) and [the sequence](../6_transition/2_sequence.md) as drafted, granted in the session. In the same sitting the Requester settled the two questions the draft had left open: the checks on every change stay the two validators, and the hosted platform runs the walk rather than reading only. Those answers redrew `PLAT2`, `GAP5`, `PLAT4`, `GAP11`, `GAP12` and initiative 7 |
| Direction, second sitting | — | — | **Pending** — the redrawn rows named above, and nothing else |
| Understanding | — | — | **N/A** — a docs-only initiative: no layer document changes, and the bench is this repository's tooling rather than the product's behaviour |
| Design | — | — | **N/A** — no solution design |

**Where these gates happen:** the session, or the pull request for this
initiative — a review reply naming what it covers is transcribed here.

## Plateaus

```mermaid
flowchart LR
  base[["≡ Baseline — two trees, every document ◐, the transition layer a stated gap"]]:::plateau

  wp1{{"⚙ WP1 — corrections"}}:::wp
  wp2{{"⚙ WP2 — the bench"}}:::wp
  wp3{{"⚙ WP3 — the roadmap, and the request it came from"}}:::wp

  target[["≡ Target — the same trees, a roadmap approved as direction, a bench that runs everything"]]:::plateau

  g1(("⊘ Direction — the second sitting")):::gap

  base --> wp1 --> target
  base --> wp2 --> target
  base --> wp3 --> target
  g1 -->|has to be granted before| target

  classDef plateau fill:#ffe8e8,stroke:#d99b9b,color:#333
  classDef wp fill:#fffbb5,stroke:#c8c04a,color:#333
  classDef gap fill:#ffd6d6,stroke:#c62828,color:#333
```

**The work is done and one sitting is not.** Three packages reach the
target; the circle is the Requester's, which is why the roadmap's documents
still open with `◐` and the sequence's first row says in flight rather than
reached.

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | Two trees on method 0.2, every document `◐`, the transition layer a stated gap; the reading tools reachable only through an installed plugin; the element-ID validator one check behind the scaffold's; one initiative on record, a rebuild |
| **Target** (this initiative) | The same two trees with a roadmap approved as direction, the request it came from filed as its source, the validator level with the scaffold, and a bench that runs every check and reading tool over both trees before a push |

## Work packages and deliverables

- **WP1 — Corrections**: `scripts/check_model.py` level with the scaffold, and
  the seventh check named in `scripts/README.md`; the brief command in
  `CLAUDE.md` and `scripts/README.md` carrying `--scope`.
- **WP2 — The bench**: `Makefile`; `README.md` § Working locally.
- **WP3 — The roadmap, and the request it came from**:
  `architecture/6_transition/README.md`, `1_target-state.md` and
  `2_sequence.md`; `architecture/reference/README.md` and the filed request;
  the front door's transition row, diagram and validation note; this document
  and its row in the index.

## In scope / out of scope

| In | Out |
| -- | --- |
| The roadmap, approved as direction | **Closing any gap beyond the three this initiative closes** — each is its own initiative through the spine, in the sequence's order |
| The bench, run by hand over both trees | **A check in CI beyond the two validators** — the Requester keeps the bench a command a contributor runs |
| The request filed as the roadmap's source | **Any change to the method** — five findings below belong in the archreator repository; they are gap notes here so the Requester can carry them across |
| The validator brought level with the scaffold | **Publishing anything, and holding a copy off the repository** — an authorization the Requester grants when the initiative that needs it reaches its gate |

## Gap notes

- **The three gaps this initiative closes** — `GAP2`, `GAP4` and `GAP5` — are
  marked in flight on the roadmap, and the merge that delivers this document
  is what turns them to reached, with the sequence's first row following.
- **Five findings belong to the method, not to these models.** Each is a gap
  on the roadmap and a change in the archreator repository whose scope
  document would land here:
  1. `coverage` reports a row as not true yet when the marker appears
     mid-sentence, where the parse anchors it to the start of a cell; two
     rows in these trees are misreported — `GAP7`.
  2. `build_brief.py --project <tree>` still stops on an identifier both trees
     own until `--scope <tree>` is repeated — `GAP7`.
  3. The alignment walk never asks `trace` or the impact brief what a change
     would touch before the gate — `GAP3`.
  4. No check opens the paths a `Lives at` cell names — `GAP8`; with the
     method on the bench, it is one existence test per path.
  5. A model declares the method version it was written against nowhere a
     tool can read — `GAP6`; a `Method` line on the front door compared with
     the plugin manifest would answer the standing request that an agent
     prompt before realigning a model to a newer plugin.
- **`coverage` cannot see `Lives at` as grounding.** The component catalogue
  grounds every row in a path under a header the reader's short list of
  realization headers does not carry, so the report counts the document
  among those that ground nothing. Harmless today, misleading the day a row
  goes blank; the fix is the method's, or a column rename here, and it is the
  Requester's call at the next Understanding.
- **The bench tracks the method's `main`.** `make method` fetches whatever the
  method's default branch holds; `METHOD_REF` pins a branch or a tag when a
  change upstream is understood and not yet answered here.

## Open questions

- **When a rendering or a copy may leave the repository.** `GAP10` and
  initiative 7 wait on the Requester's word: a published site is a copy of
  the models on a public address, and a host that runs the walk holds a
  working copy of the repository. Both repositories are public already, so
  neither discloses anything; the question is whether the Requester wants
  either to exist yet, and it is asked when the initiative that needs it
  reaches its gate. Nothing here assumes the answer.

## Resolved

- **What the hosted platform is expected to do.** The adopted interpretation
  — the host reads only, consuming the export or a synced checkout and
  editing nothing — was rejected by the Requester on 2026-09-06. The accepted
  answer: the host also runs the walk, the agent and the gates included, and
  the approval it collects lands in the scope document. Applied in
  [the target state](../6_transition/1_target-state.md#the-gaps) to `PLAT4`,
  `GAP11` and `GAP12`, and in [the sequence](../6_transition/2_sequence.md)
  to initiative 7.
