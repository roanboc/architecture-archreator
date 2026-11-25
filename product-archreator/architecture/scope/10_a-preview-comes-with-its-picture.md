# Project Scope — A preview comes with its picture

_[← Scope index](./README.md) · [Model home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** branch `ccr-89cc65be-vffo8n` here and in
[`archreator`](https://github.com/roanboc/archreator), taking the method to
0.9.

The Requester asked to be shown a change as diagrams in the conversation, so
they understand what it does and confirm it there, without going back
through the pull request. A preview already said what changed, in words.
This initiative gives it a picture drawn from the branch, in the subject's
own words, and a page to read it on.

## EA alignment (assessed top-down before implementing)

| Layer | Impact | Confirmed |
| ----- | ------ | --------- |
| 0_business-design | No change | — |
| 1_strategy | `G2` names the generated views beside the preview. `OUT6` added: a Requester confirms what a change claims without opening its pull request | The shape — views generated from the branch, the same on every host, with a page where a host can show one, private to the Requester — by the owner, in conversation, 2026-11-25. The wording not yet |
| 2_business | `BSVC1` says the preview carries a picture of what changed. `BSVC1` and `BSVC2` are realized by the preview generator as well as by the skills | Not yet |
| 3_information | No change | — |
| 4_application | `ASVC10` Change preview and `ACMP14` The preview generator added | Not yet |
| 5_technology | No change | — |

## What the evidence said

| Source | What it said |
| ------ | ------------ |
| The method's own rulebook | `conversation-previews` required every fact in a preview to come from the branch, and nothing generated one. The agent wrote it by reading the files and drew its diagram by hand, where it drew one at all |
| The brief generator | Its views carry identifiers, glyphs and layer names. That is right for a reader of the model, and exactly what a preview may not show |
| The hosts | A conversation renders what it renders: one shows a page, another a picture, another a diagram from its source, a terminal none of them. No single carrier reaches every Requester, and which chat renders what moves between versions |
| This repository | Scope 9 was previewed as a list in the conversation. The owner confirmed it, and then asked for this |

**The rule was already written; the tool behind it was missing.** A preview
generated from the branch cannot drift from the branch. One an agent writes
from what it remembers reading can, and a picture drawn by hand is the part
most likely to.

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (0.8) | A preview is prose and a table the agent writes after reading the branch, with a diagram where the agent thinks to draw one |
| **Target** (0.9) | A preview's views are generated from the branch: what is new, changed and taken away, and what each touches, as a page, a picture and a diagram's source, with no identifier and no notation in any of them |

## Work packages and deliverables

### WP1 — The drawing

- **Deliverables:** `plugins/archreator/scripts/plain_view.py`: bands by the
  question each element answers, an element's type in an everyday word, what
  the change did to it written on the mark as a word; one drawing as a
  picture, as a diagram's source, and inside a self-contained page that
  follows the reader's light or dark setting.
- **Outcome:** a model can be drawn for the person it is about.

### WP2 — The preview generator

- **Deliverables:** `plugins/archreator/scripts/build_preview.py` and its
  tests: the branch compared with the commit it left the default branch at;
  the views, each change as before and after, every adopted call lifted out
  of its row, the one question and the answers the model allows; a change too
  large for one screen drawn one question at a time.
  `tests/example_project.py`, a made-up shop with a base and a branch.
- **Outcome:** what a preview shows is what the branch says.

### WP3 — The rule

- **Deliverables:** `conversation-previews` (the views are generated; the
  richest form the conversation renders; a page only the Requester can open
  is still the conversation); `align-change-through-layers` Step 8;
  `write-pr-description`; `docs/method.md`; `docs/adopting.md` § Seeing a
  change before it lands; `docs/migrating.md`; the manifests at 0.9.0.
- **Outcome:** the Requester is never sent to the pull request to find out
  what changed.

### WP4 — These trees

- **Deliverables:** the elements named in the alignment table.
- **Outcome:** the product model names the tool that draws it.

### WP5 — The whole model on one page

- **Deliverables:** `plugins/archreator/scripts/build_overview.py`, in a pull
  request of its own: the same drawing over a whole model, one question at a
  time, as one self-contained page.
- **Outcome:** a project on a private repository shows its model to its own
  people without publishing a site.

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| The views, the page, and the rule that they are generated | An answer given on the page; it is read there and answered in the conversation |
| A recipe per host for showing the page, in the method's guidance | The method publishing a page itself; the host does, and the agent asks first when anyone but the Requester could open it |
| A made-up example the tests and the public site share | Questions and everyday type names in a language other than English |

## Gap notes

- **The words around the model are English.** A model written in another
  language keeps its own names and cells, under English headings and type
  names. A word list the project translates, as it does the prose
  validator's, would close it.
- **Nothing proves a preview was shown.** The tool writes the views; whether
  the agent showed them is recorded only by the confirmation in the scope
  document.
- **A call recorded on a relationship is not lifted out.** Only a row of an
  element carries an adopted call the generator can find.
