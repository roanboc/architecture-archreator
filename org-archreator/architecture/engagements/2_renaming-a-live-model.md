# 2 — Renaming a live model, and the trees nobody checked

**Date:** 2026-08-12
**Kind:** initiative — one, plus the correction that followed it
**Delivered:** [scope document 9](../../../product-archreator/architecture/scope/9_the-repository-says-what-it-is.md)
in `product-archreator/`, merged as PR #18

The first note written the way this mechanism intends: against work that was
finished before the retrospective started, by whoever did it, while the
improvising was still recent.

## What the method did not cover

**Which *other* model a change falsifies.** `architecture-first-change` walks one
model's layers. This initiative changed two — the method's and the
organization's — and no step asks what current-state statements elsewhere
have just become false. The scope document named the one organization
element it expected to touch; six more were falsified and nobody looked.

**A gate-approved document that turns out to be wrong about existing state.**
Step 6 covers implementation *diverging* from the plan, and says to take the
delta back to the Requester if it touches what a gate approved. It does not
cover the approved document simply being mistaken — here, naming the wrong
element as the one the initiative would redefine. That is not a divergence to
renegotiate; it is an error to fix.

**Repairing links in immutable documents at scale.** `scope-doc` § Rules
permits repairing a merged document's link *targets* while its words stay
fixed. It does not say how, and at 910 links across 135 files with three
trees changing depth, "how" is the entire problem.

**Whether a scaffold's links resolve here or at the destination.** Once the
project template moved inside the skill that emits it, `../CONTRIBUTING.md`
in a layer README stopped having one meaning. Nothing in the method
distinguishes a link that must resolve in place from one that must resolve
after the template is copied.

## What was done instead, and why

Links were repaired by **resolving each one against its old location and
recomputing it from the new one**, with the checkers as the safety net —
never by pattern replacement. The first attempt did use pattern replacement
and silently normalised 344 `./` prefixes out of existence, editing immutable
records to no purpose. The convention was then re-established by *measuring*
it — 342 links carried `./` at the previous commit and none did not — rather
than by assuming which form was house style.

The wrong element in the approved scope document was **corrected in place and
the correction recorded** in the commit and in the document, without
reopening the gate. The reasoning: the gate approved a decision, and the
decision was unaffected. What changed was a statement of fact about the model
that had been wrong when written, and leaving it standing to protect the
record would have made the record less true rather than more.

For the scaffold, the first two attempts were wrong in the same way — they
tried to make the *checker* tolerate links that did not resolve. The third
made the scaffold ship the root files its own READMEs point at, so the links
resolve in both places. The checker exemption would have hidden a real
defect: the shipped scaffold linked out to archreator's own documents, which
dangles for every adopter.

Nothing was done about the falsified organization model, because it was never
noticed. It surfaced two days later when the Requester asked an unrelated
question that required opening that layer.

## Does it generalize?

| Moment | Verdict |
| ------ | ------- |
| Which other model a change falsifies | **Yes, and it is the most valuable finding here.** Any federated model — the Depth 2 → Depth 1 shape this method recommends to every adopter — has the same hole. It is not a judgement call that happened to work; it is a defect that reached `main` |
| An approved document wrong about existing state | **Yes.** The distinction between "the plan changed" and "the document was mistaken" is general, and only the first needs the Requester |
| Repairing links at scale | **Yes.** Any project that renames a tree hits it, and the reasoning — resolve against the old location, measure the convention before restoring it — transfers whole |
| Scaffold link semantics | **Specific to this**, in its particulars: only a project that ships a template has two resolution contexts. The general half is that **an exemption which silences a failing check can hide the defect the check found** |

## What surprised us

**The Requester rejected the question, not the answer.** The site's model
sitting three levels deep was presented as a choice between folding it in and
leaving it alone. The Requester declined both and said the real problem is
that nothing states how much design detail belongs at which tier — and that
whether an implementation lives in the same tree or a child one is a
legitimate preference, either way. A structural question turned out to be a
granularity question. The symptom had been offered as the problem, and it
took a third party to see it.

**The model already knew the rule the method was missing.** The
organization's own layer 4 states it in prose — *"the organization's layer 4
names that an application exists; a Depth 1 model says how it is built.
Neither restates the other"* — and nothing in `.claude/skills/` carries it.
A fact discovered while modeling had been written where it was discovered and
never lifted into the method.

## Deliberately not recorded

Nothing. Internal work on a public repository again, so the confidentiality
boundary remains **completely unexercised** across both notes to date. Worth
repeating rather than leaving as silence: the rule this mechanism exists to
police has still never been tested against a real client engagement.

## Proposed

**A note on how much of this will recur.** The Requester's calibration, given
when these proposals were reviewed: *structural churn is a founding-phase
phenomenon, not the steady state.* A repository whose shape has been settled
properly should not be renaming trees every other initiative. Proposals 4 and
5 are both about moving structure around, so if that judgement holds they are
not "waiting for a second sighting" — they are waiting for a recurrence that
probably should never come, and the method is better off without rules for
it. Proposal 1 is not structural: any change touching two models hits it, and
that is ordinary work.

| # | Skill or document | The sentence it would add | Raised as |
| - | ----------------- | ------------------------- | --------- |
| 1 | `architecture-first-change` § Step 7 | Name every other model in the repository whose current state this change falsifies, and correct it in the same change — the grounding rule is not enforced across models by any tool | **Act now**, approved by the Requester. Seen once, not twice. The justification is that the evidence is a shipped defect rather than an improvisation that worked — which is a *third* standard, neither the one this skill states nor the one note 1 applied. See proposal 6 |
| 2 | `architecture-doc-style` | A tier may refine what the tier above exposed, never restate it, and every refining element names its parent; business and information layers below the owning tier cite their parent and detail only what the implementation requires | **Act now**, requested directly by the Requester, and already stated informally in `org-archreator/architecture/4_application/` |
| 3 | `architecture-first-change` § Step 6 | A gate-approved document that states something false about existing state is corrected in place and the correction recorded; only a change to what was *decided* returns to the Requester | Wait — one case |
| 4 | `scope-doc` § Rules | When a tree moves, repair a merged document's links by resolving each against its old location and recomputing it, never by pattern replacement | Wait, and probably forever. Structural churn should not recur once a repository is shaped properly |
| 5 | `architecture-doc-style` or a decision | What happens to element identifiers when two models **merge** — the inverse of [decision 2](../../../product-archreator/architecture/decisions/2_no-renumbering-on-domain-split.md), which refuses renumbering on a split | Wait, same reasoning as 4. Surfaced while planning, never attempted |
| 6 | `engagement-retrospective` § Following through | State whether "two" means two **notes** or two **occurrences** — the skill says notes, note 1 counted occurrences within a single note, and note 2 argued from one occurrence with a demonstrated defect | **Ready on any reading.** Three different standards have now been applied across two notes, which is itself the recurrence |
