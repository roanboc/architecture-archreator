# Project Scope — Previews in the conversation

_[← Scope index](./README.md) · [Model home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** branch `ccr-a18fcfba-bdmhgn` here and in
[`archreator`](https://github.com/roanboc/archreator), taking the method to
0.7 together with [scope 8](./8_intention-first-realization-handed-over.md).

The Requester asked that people understand what they are doing, and that the
experience stay in the chat: the agent shows what matters there — previews,
diagrams, tables, questions — instead of sending the Requester to the
repository, and the important thing is checked and approved there. This
initiative adds a rulebook for what a preview holds and when one is due, and
makes the Requester's confirmation, not the merge, what validates a document.

## EA alignment (assessed top-down before implementing)

| Layer | Impact | Confirmed |
| ----- | ------ | --------- |
| 0_business-design | No change to this tree, which does not use the layer. In the organization's, `PREL5` names the confirmation, not the merge, as what keeps a human in the loop | The direction — a confirmation validates, the merge records it — by the owner, in conversation, 2026-09-29. The rest not yet |
| 1_strategy | `G2` restated as **A person confirms what reaches the model**, realized by the preview; `OUT2` restated to check who confirmed each validated document; `ASM7` and `G6` reworded to match. In the organization's, `P1` names the confirmation as what makes it structural, and `OUT2` checks that the preview is generated from the documents on the branch | Not yet |
| 2_business | `BSVC1`, `BSVC2` and `BSVC4` restated for the preview and the confirmation. In the organization's, `ACT2` never decides whether a claim is confirmed, `BPROC1.2` has `ACT1` confirming the preview, and `VS1.5` names the confirmation | Not yet |
| 3_information | `DOBJ2.2` in both trees records who confirmed what; the organization's no longer names an Approvals table, retired in 0.6 | Not yet |
| 4_application | `ACMP1` restated for the new rulebook | Not yet |
| 5_technology | No change | — |

## What the evidence said

Read across the three projects outside these trees that run on the method.

| Project | What a Requester met |
| ------- | -------------------- |
| [`dbx-master-data-manager`](https://github.com/roanboc/dbx-master-data-manager), on 0.6 | A request of 440 words and five answers became about 6,600 lines of model citing 221 element identifiers, in four pull requests merged within three days. The agent recorded about thirty-three calls of its own. Nobody reads and agrees to that at that speed; the calls are what a person needs to see |
| [`ea_bigview`](https://github.com/roanboc/ea_bigview), a company whose Requester is its CEO | The CEO never opens the repository. The loop runs through working sessions, whose notes are filed as reference documents, and a PDF for the board; the architect merges every pull request |
| [`dbx-enterprise-architecture`](https://github.com/roanboc/dbx-enterprise-architecture) | Its own initiatives 24 and 25 already built the pattern as a product feature: the assistant asks a few questions at a time, each tied to one row and offering the choices the model allows, top-down, and shows the impact and a drawing before anything is applied |

**The merge had stopped being evidence that anyone understood.** A merge
says the work was accepted; it does not say the claims were read. The
research behind this initiative found the same gap named elsewhere as
comprehension and intent debt, and no enterprise-architecture tool that
measures it.

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (0.6) | The merge is the only approval. The Requester meets the change in a pull request, and a document moves to `●` when it merges |
| **Target** (0.7) | The agent previews what changed and every call it took, where the Requester is. Their confirmation moves a document to `●`, naming who and when; the merge lands it, and a merge alone validates nothing |

## Work packages and deliverables

### WP1 — The rulebook

- **Deliverables:** `plugins/archreator/skills/conversation-previews/SKILL.md`,
  invoked by name: what a preview holds, when one is due, how a question is
  put, the two carriers (the conversation, a one-page session pack), and how a
  confirmation is written into the documents; its row in the skill
  catalogue and in the process model's rulebooks.
- **Outcome:** one place says how every process meets its Requester.

### WP2 — The confirmation validates

- **Deliverables:** `architecture-document-style` § Document status (the `●`
  line names who confirmed it); `align-change-through-layers` (§ Where this
  stops, Step 8 now "Preview, then open the pull request");
  `discover-business-model`, `discover-strategy`, `discover-current-landscape`,
  `model-domains`, `plan-the-transition`, `restate-current-state`,
  `write-scope-document` (a `Confirmed` column), `write-pr-description`,
  `record-decision`, `establish-project`; both pull-request templates (a
  **Confirmed** section); the scaffold's `AGENTS.md`, `README.md` and
  `architecture/README.md`; `assets/CONTRIBUTING.md`; `docs/method.md` (two
  loops, the Requester's and the Reviewer's), `docs/process/`,
  `docs/standards-alignment.md`, `docs/migrating.md` (§ 0.7), the README, the
  site and the manifests at 0.7.0.
- **Outcome:** nothing in the method says the merge is the approval.

### WP3 — These trees

- **Deliverables:** the elements named in the alignment table; `AGENTS.md`,
  `CONTRIBUTING.md`, the README and this index at 0.7.
- **Outcome:** both models describe the method as it now works.

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| The rule, the rulebook, and every skill and document that stated the old rule | A preview generator: `build_brief.py` could produce the one-screen preview from the branch, and `export_pdf.py` could render its diagram as an image for a conversation that shows pictures |
| Both carriers — the conversation and the session pack | Measuring comprehension — whether a Requester can say back what changed — which the pilot should record |
| Restating the elements whose claims the rule changed | Moving these trees' own documents to `●`: none is confirmed yet, which is what the rule now says |

## Gap notes

- **No tool generates the preview yet.** The rulebook requires it to be
  generated from the branch; today the agent writes it from the files. A
  `preview` focus for the brief generator closes this.
- **The pilot is still to run.** The next story of `dbx-master-data-manager`,
  previewing its adopted calls, is the first test of the rule on a real
  Requester.
