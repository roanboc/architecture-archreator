# Project Scope — Skills by name, and a lighter listing

_[← Scope index](./README.md) · [Model home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** branch `claude/archreator-validation-feedback-gt00b7` across
the four repositories on the method.

A host loads every skill's name and description at the start of every session,
against a budget of one percent of the context window, and when the budget
overflows it drops the descriptions of the skills used least. The eighteen
descriptions measured 7,678 characters — about 96 percent of that budget on
their own — so on any machine with a second skill pack installed, the method
was the first thing to fall out of context, and it fell out fastest where it
was newest. The Requester asked for the skills to be invoked by name except
the key ones. This initiative takes the method to **0.4** by doing that, and
adds the report that says whether the method is doing what it claims.

## EA alignment (assessed top-down before implementing)

| Layer | Impact |
| ----- | ------ |
| 0_business-design | No change |
| 1_strategy | No change. `G1` holds as written; the listing cut serves the organization's *cheaper to run the longer it runs* [`ORG.G7`] |
| 2_business | No change. `BSVC1` and `BSVC3` do the same work through a different door |
| 3_information | The skill corpus [`DOBJ1.1`] is still eighteen skills; two gain a reference file, fifteen gain a frontmatter key |
| 4_application | The skill corpus [`ACMP1`] is reached two ways — three skills listed for the agent, fifteen invoked by name; the corpus validator [`ACMP7`] checks which is which; the model reader [`ACMP5`] gains `health`; `ASVC4` and `ASVC7` restated for both |
| 5_technology | The agent host platform [`NODE4`]: a host that reads the by-name key loads three skills, one that ignores it loads all eighteen as before |

## What the evidence said

| Measure | Before | After |
| ------- | ------ | ----- |
| Descriptions loaded into every session | 18, at 7,678 characters | 3, at 291 |
| Share of the default listing budget, at a 200k context | about 96 percent | about 4 percent |
| Lines loaded on nearly every change — the three listed bodies | 932 | 856 |
| Skills an agent can reach without being told | 18 | 3 — the spine, and the two rulebooks every edit obeys |

The three that stay listed are the only ones whose *forgetting* silently
breaks a model: a requirement that skips `align-change-through-layers` skips
the layers, and an edit that skips a style rulebook has the wrong shape. Every
other skill is a step somebody starts by name, or one the spine reaches.

## Work packages and deliverables

### WP1 — Fifteen skills leave the listing

- **Deliverables:** `disable-model-invocation: true` on fifteen skills, an
  argument hint on the two that take one; every description rewritten — the
  three listed to at most 140 characters, the fifteen by name to at most 300,
  keyword-rich because they cost nothing and are still the trigger on a host
  that ignores the key; every **Hands off to** section opening with the one
  sentence that says a hand-off is a file beside this one, read when it
  applies; the catalogue's **Invoke** column; every page that said skills
  surface on their own made true.
- **Outcome:** what a session loads falls from 7,678 characters to 291.

### WP2 — The corpus validator knows the rule

- **Deliverables:** a `listing` check naming the three, requiring the key on
  every other skill and holding both lengths; `--report`, which prints what
  each skill costs and what the listing spends; four tests.
- **Outcome:** a skill cannot drift back into the listing unnoticed.

### WP3 — What is read on some activations leaves what is read on every one

- **Deliverables:** *When a document or a table outgrows a page* moves out of
  `architecture-document-style` and *Presenting a gate* out of
  `align-change-through-layers`, each into a reference its skill links by
  name; every citation of the moved headings still resolves.
- **Outcome:** the three always-loaded bodies fall from 932 lines to 856.

### WP4 — `model.py health`

- **Deliverables:** one command that prints, per model, the elements and
  documents by status, the dated approval rows across its scope documents,
  whether any of them moved a document to `●`, and how many elements name
  what realizes them. Language-independent: a status is a glyph, a grant is a
  dated row, an initiative is a file.
- **Outcome:** the number the method's own claim rests on is printed rather
  than counted by hand — see the gap note.

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| The method at 0.4, and the entry points of the four projects on it | Merging `document-style` into `architecture-document-style`, which would drop the listed set to two |
| The product model corrected for what changed | Any change to the organization's model: the intent behind the method stands |
| The health report, and the gap it surfaces | Closing that gap — a promotion is a gate presentation, and belongs to the initiative that presents it |

## Gap notes

- **A granted gate has never moved a status line, in any model on the
  method.** `health` counts thirteen dated approval rows across the eight
  scope documents of one project and one across the eight of another, and
  zero documents at `●` in either — or in either tree here. The rule *a
  granted gate moves a status line* has been written since 0.2 and has never
  fired; until it does, nothing built on this method is built on an approved
  fact. Naming the gap is this initiative's; closing it is the next one's.
- **Copilot's handling of the by-name key is unverified.** The Claude Code
  documentation says what the key does; Copilot's could not be reached from
  where this was built. The design holds either way — a host that ignores the
  key loads every skill as before, which is why the fifteen keep a description
  worth triggering on.
- **A hand-off names the host's variable.** `${CLAUDE_SKILL_DIR}` is
  substituted by one host and read as a path by the rest. It is the one place
  a skill body names a host, and the portability rule now says so.

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| | | | |

<!--
  Nothing here has been granted. At Depth 1 the change meets Understanding;
  the row is written when it is granted, and not before.
-->
