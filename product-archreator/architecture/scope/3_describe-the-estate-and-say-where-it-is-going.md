# Project Scope — Describe the estate, and say where it is going

_[← Scope index](./README.md) · [Model home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** the `claude/archreator-next-functionality-ta1tyx` branch in [`archreator`](https://github.com/roanboc/archreator), and the model changes this document holds the gate for.

The method could take a requirement down six layers and check that the result
was internally consistent. It could not describe an organization that existed
before anyone modeled it, and it could not say where that organization should
go. Both are the work an enterprise architect is actually hired for, and
neither had a procedure.

The gap was visible in the method's own worked models before it was named
here. A model built with archreator had its strategy layer approved and its
four lower layers left empty, with the note that filling them was "a later
initiative" — because every route into those layers began with a requirement,
and no requirement ever asks for the applications that were already running.

Three things close it. The estate can now be **described** from evidence
rather than from a change request; the model can now say where it is
**going**, in one folder that is the only part permitted to describe a future;
and the projection that had been built and read by nothing now has the
**consumer** it was waiting for.

## The gates were granted on a proposal, not on this document

The method says the scope document comes before the gate. Here the Requester
was presented with a written assessment naming the three items, their order
and the reasoning for each, approved it, and directed implementation in the
same reply — explicitly waiving a further presentation. This document was
written during the work.

That is worth recording rather than smoothing over. What was approved was real
and was approved before any of it was built; what it was approved *against*
was a proposal in the conversation rather than a numbered document, and the
Approvals table below says so.

## EA alignment (assessed top-down before implementing)

| Layer         | Impact                                              |
| ------------- | ---------------------------------------------------- |
| 0_business-design | Not used — the subject is a product, at Depth 1 |
| 1_strategy    | `ASM5` and `ASM6` added, naming the two gaps; `G6` added for the direction the model can now state; `CAP7` added for planning a transition; `VS1.6` added to the stream. `CAP1` widened to include the estate sweep, `CAP4` to include the grounding report, `G1` to answer `ASM5`, and `OUT1`'s honesty column now names the tool that narrows the search. `RES1` and `RES3` restated |
| 2_business    | `BSVC8` (model interrogation) and `BSVC9` (transition planning) added; `BSVC2` widened to cover the sweep |
| 3_information | `DOBJ2`'s prefix count restated — two prefixes and one group added; `DOBJ4` now names the consumer that reads it |
| 4_application | `ASVC10` and `ASVC11` added, `ACMP14` and `ACMP15` added, `ASVC2` and `ACMP2` widened. `ASVC8`'s edge to the business layer becomes solid: the projection has a consumer |
| 5_technology  | No change. The query tool is Python's standard library on the node the validators already run on, and needs nothing `NODE2` does not have |

**Two other trees carry a count this change moved.** `org-archreator`'s
`ACMP1` and the `site` tree's note on `BSVC2` each state how many skills the
method has, and both said fifteen. Correcting a number to what it now is keeps
a document true rather than changing what it claims, so it travels with this
initiative instead of waiting for one of its own — which is also why those
trees have no rows in the table above.

## Approvals

| Gate                     | Approved by | Date         | What was approved                          |
| ------------------------ | ----------- | ------------ | ------------------------------------------- |
| Gate 0 — Business model  | — | — | N/A — the subject is a product, not an organization |
| Gate 1 — Strategy        | Requester | 2026-08-24 | The written assessment of the three items, their order, and the reasoning: that landscape discovery must come first because it unblocks a model that is stuck today, that a target state needs a described baseline before a gap can be derived, and that the projection's missing consumer is the cheap third. Approved as direction, with implementation directed in the same reply |
| Gate 2 — Business        | Requester | 2026-08-24 | The same reply, which approved the architectural changes as well as the skills — the new capability, its business services, and the components realizing them |
| Gate 3 — Solution design | — | 2026-08-24 | N/A — waived. The Requester directed implementation "as I already understand what needs to be done", which declines the separate design review rather than omitting it |

## Plateaus

| Plateau                | State                     |
| ----------------------- | ------------------------- |
| **Baseline** (before)  | Fifteen skills. Layers 2–5 reachable only through a requirement; no way to state a target; a projection with no consumer and a grounding rule enforced by review alone |
| **Target** (delivered) | Seventeen skills. An estate describable from evidence with a declared boundary; a roadmap folder that is the only future-tense part of a model; a query tool that traverses the projection and reports what a catalogue leaves ungrounded |

## Work packages and deliverables

### WP1 — Describe an estate that predates the model

- **Deliverables:** `plugins/archreator/skills/discover-current-landscape/SKILL.md`; the `BPROC1.5` rows in `docs/process/1_level-1-macro-processes.md`, `2_level-2-processes.md` and `README.md`; the catalogue rows in `plugins/archreator/skills/README.md` and `plugins/archreator/scaffold/AGENTS.md`; handoff rows in `establish-project` and `discover-strategy`
- **Outcome:** the four layers below the strategy can be filled without inventing a requirement, and what the sweep did not reach is written where a reader of the layer will meet it

### WP2 — Say where the architecture is going

- **Deliverables:** `plugins/archreator/skills/plan-the-transition/SKILL.md`; the `BPROC5` macro process and its `BPROC5.1` child; `plugins/archreator/scaffold/architecture/6_transition/README.md`; the `PLAT` and `GAP` prefixes in `element-prefixes.json` and in the `architecture-document-style` table; the glyph, shape and colour rows in `scaffold/architecture/README.md`; the roadmap binding in `write-scope-document` and `restate-current-state`
- **Outcome:** a target, a derived gap register and a dependency-ordered sequence, in the one folder exempt from describing the present

### WP3 — Give the projection its consumer

- **Deliverables:** `plugins/archreator/scaffold/scripts/query_model.py` and its copy in `scripts/`; the `query_model.py` sections in both `scripts/README.md` files
- **Outcome:** "what would this change touch" is a traversal rather than a manual read of a hundred files, and the omissions the grounding rule cares about are listed rather than hunted

### WP4 — Repair the model the first three falsified

- **Deliverables:** the layer documents named in the alignment table above, and this scope document
- **Outcome:** the model of the method describes the method that now exists

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| The three skills and the tool, the process model, the scaffold, and the model repair | Running either new skill against a real subject |
| The `6_transition/` README the scaffold ships | The two numbered roadmap documents, which the skill writes per project, as every layer document is |
| The prefix registry in this repository and in the method | The same registry in `ea_bigview`, which carries its own copy |
| A grounding report | A grounding gate |

## Gap notes

- **Neither new skill has been run against a real subject.** They are written
  from the shape of the problem and from what the existing skills established,
  not from an engagement that exercised them. `discover-current-landscape` in
  particular claims an evidence order — repositories, licences, identity
  entries, runbooks — whose usefulness is a hypothesis until an estate is
  swept. The first real run is the test, and `run-retrospective` is where what
  it teaches goes.
- **`ea_bigview` gets none of this until it asks for it.** It carries its own
  copies of the scripts and its own prefix registry, and it is a live model in
  another language with its own Requester and its own gates. Propagating a
  method change into it is that project's initiative, not this one's — and it
  is the most likely first user of `discover-current-landscape`, since it is
  the model whose empty lower layers made the gap visible.
- **`CAP4` is still narrower than the grounding rule.** The report closes the
  half that needs no judgement — a blank cell beside filled ones. Whether a
  filled cell names a path that still exists remains unchecked, and remains a
  step in the change process rather than something a script can do.
- **The roadmap has no validator of its own.** `check_model.py` will resolve
  its element references like any other layer's, but nothing checks that a gap
  names a baseline element, or that a plateau names a goal. Those are rules in
  a skill and prose in a README. Whether they need mechanizing is a question
  for after the first roadmap exists.
- **Two identifiers now run out of order** — `BPROC5` runs second, `VS1.6`
  runs between `VS1.2` and `VS1.3`. That is the never-reuse rule working as
  written, and it is a small readability cost paid on every future reading of
  those two pages. It was accepted rather than overlooked.

## Open questions

- None. The Requester approved the assessment directly and directed the
  implementation, and nothing was adopted on an interpretation of what they
  meant.
