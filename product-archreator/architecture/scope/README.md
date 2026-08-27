# Project Scope Documents

_[← Repository README](../../README.md) · [Enterprise architecture](../README.md)_

One document per delivered (or in-flight) initiative, numbered
chronologically. While the [EA docs](../README.md) describe the
**current** state of the system, each scope document describes one
**change**: what plateau it started from, what it delivered, and what it
deliberately left out.

**ArchiMate viewpoint:** Implementation & Migration (Work Package,
Deliverable, Plateau, Gap).

## The EA-first change process

Every change in requirements follows the same order — the same order the EA
folders are numbered in:

1. **Align the EA first.** Walk the layers top-down and record what the
   change means for each: [1_strategy](../1_strategy/README.md) (does it
   serve an existing goal, or introduce a new driver?) →
   [2_business](../2_business/README.md) (new/changed services,
   processes, rules?) → [3_information](../3_information/README.md)
   (new/changed data objects, flows, storage?) →
   [4_application](../4_application/README.md) (which services,
   components, ports change?) → [5_technology](../5_technology/README.md)
   (any runtime, build, or hosting impact?). Update the affected EA
   documents in the same change. If the strategy layer is still template
   placeholders, or the change adds/modifies a stakeholder, driver, goal,
   or principle, the initiative becomes **strategy discovery** first — a
   docs-only, question-driven initiative ending at **Gate 1 — Strategy**
   approval (see the `discover-strategy` skill); implementation
   follows as a separate initiative. If the subject is an **organization**
   rather than an application, the walk starts one layer earlier, at
   [0_business-design](../0_business-design/README.md) — the value
   proposition and business model canvases, approved at **Gate 0 —
   Business model** (see the `discover-business-model` skill)
   before layers 1–2 are derived from them.
2. **Document the scope.** Add the next-numbered file to this folder
   describing plateaus, work packages, in/out of scope, gaps, and gate
   approvals — before implementation starts, refined as it proceeds.
3. **Pass the gates.** Before any code, the Requester approves the
   strategy, business, and information changes (**Gate 2 — Business**) and
   chooses whether to also review the solution design before it is coded
   (**Gate 3 — Solution design**, optional). Approvals are recorded in the
   scope document's Approvals table — who approved, when, and what was
   shown, with `N/A — <why>` for the gates that didn't apply. Which gate
   applies to which initiative is defined in exactly one place,
   the `align-change-through-layers` skill § The gates, which also says **where**
   an approval can be granted — the conversation, or a reply on the pull
   request for a Requester who doesn't work in a terminal.
4. **Implement.** Only then write the code, keeping the scope document and
   EA docs in sync with what is actually delivered.

Agent guidance for this process lives in the `align-change-through-layers`,
`discover-strategy`, and `write-scope-document` skills; PR descriptions follow
`.github/pull_request_template.md` (see the `write-pr-description` skill) and
must cover the whole branch.

If the project needs a single running index of adopted interpretations that
still need sign-off from a stakeholder who can't be consulted synchronously,
keep it in [open-questions.md](./open-questions.md) — optional, see the
`write-scope-document` skill.

If a work package is too large or long-running to implement in one sitting,
shard it into self-contained story files instead of leaving it as one
inline task list — see the `shard-stories` skill.

For a single consequential call smaller than a full initiative — most
often why an AI actor's autonomy level or decision rights were set the way
they were — see [docs/decisions/](../decisions/README.md) (optional) and
the `record-decision` skill.

Scope documents accumulate. After a run of initiatives the EA can be
accurate line by line and no longer read as a description of *today* —
shipped work still marked "Pending", elements that were replaced but never
retired, questions answered in a conversation nobody recorded. The
`restate-current-state` skill compacts that, as its own initiative with its
own Gate 2. It changes the current-state documents only: **a merged scope
document is never rewritten**, because it is the record of what was
approved on a date and against what information.

## Initiatives

| #   | Scope document | Delivered as | Summary |
| --- | --------------- | ------------ | ------- |
| 1 | [Rebuild the models on the current method](./1_rebuild-the-models-on-the-current-method.md) | The `rebuild` branch | Three trees rebuilt from an empty branch against the current method, with the previous corpus preserved at the tag `pre-rebuild-2026-08` |
| 2 | [Publish the model beyond the repository](./2_publish-the-model-beyond-the-repository.md) | [`archreator` PR #33](https://github.com/roanboc/archreator/pull/33), and the model changes it makes necessary | The method learned to render a model as a portal and print it as one PDF; the four layers that describe it are repaired to match |
| 3 | [Describe the estate, and say where it is going](./3_describe-the-estate-and-say-where-it-is-going.md) | The `claude/archreator-next-functionality-ta1tyx` branch in `archreator`, and the model changes it makes necessary | The method learned to describe an estate that predates the model, to state a target and a sequence, and to answer graph questions from the projection that nothing had been reading |
| 4 | [Say what a document is worth, and keep what it came from](./4_say-what-a-document-is-worth-and-keep-what-it-came-from.md) | The same branch | Every document that defines an element declares how far it has been validated, and the transcripts and documents a model was built from are kept beside it, dated and indexed |
| 5 | [Ask where the project lives, and let it publish](./5_ask-where-the-project-lives-and-let-it-publish.md) | [`archreator` PR #39](https://github.com/roanboc/archreator/pull/39) | Bootstrap asks which repository a project lives in, and a public GitHub answer activates the checks and publishing workflows the scaffold now ships inert |
| 6 | [Declare the relationships, and let the graph be walked](./6_declare-the-relationships-and-let-the-graph-be-walked.md) | The `claude/graph-navigator-architecture-m2fr9j` branch in `archreator`, and the model changes it makes necessary | The relationship becomes a modeled object with a home of its own, declared in catalogues and relationship tables rather than drawn in diagrams, and the projection carries where each one came from |
| 7 | [Walk the model](./7_walk-the-model.md) | The same branch | The graph gets a reader: one static page over the projection, filtered by layer and walked outward from any node, with the traversal shared with `query_model.py` rather than written twice |
| 8 | [Federate the graph](./8_federate-the-graph.md) | The same branch | Every published project offers its projection at a documented path; the topmost tree names the federation in a document a gate approves; the navigator reads that index and shows what it names |
