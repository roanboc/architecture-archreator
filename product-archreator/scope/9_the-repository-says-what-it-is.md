# Project Scope — The repository says what it is

_[← Scope index](./README.md) · [EA home](../architecture/README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** branch `claude/product-1-roadmap-74giay`.

This repository holds four things — the method, the organization that
publishes it, the guidance site, and the empty scaffold a cloner inherits —
and its directory names identify none of them. `docs/` is a template, `product-archreator/`
is the method, `org-archreator/` is the business, and `site/` is a channel. A
reader cannot tell which is which without opening them, and neither can the
process: [`ea-first-change`](../../.claude/skills/ea-first-change/SKILL.md)
step 1a reads the declared modeling depth from `CLAUDE.md`, and the only
`CLAUDE.md` at the root still says _"This project has not been bootstrapped
yet"_ with depth _"not yet declared"_. This initiative names the parts, moves
the scaffold to where it is actually used, and draws the portability boundary
that `P6` has been deferring.

## Why now

Three questions already open in the model converge on the same change, and
one of them is explicitly time-sensitive:

| Log | Question | What this initiative does to it |
| --- | -------- | ------------------------------- |
| [`product-archreator/open-questions.md`](../open-questions.md) #1 | Should the template repository be **generated** from the plugin, or hand-maintained alongside it? | **Answers it — generated.** The scaffold moves inside the skills that emit it, so the two cannot drift |
| [`product-archreator/open-questions.md`](../open-questions.md) #5 (Resolved) | Where should archreator record its own architecture, given that `docs/` must stay blank for cloners? | **Supersedes it.** The premise dissolves — once the scaffold ships inside the skills, `docs/` no longer has to stay blank, and the reason `product-archreator/` exists under that name goes with it |
| [`2_business-model-canvas.md`](../../org-archreator/architecture/0_business-design/2_business-model-canvas.md#open-questions) #2 | How far should provider neutrality go in practice? | **Answers it.** The canvas says a decision record is needed _"before anything provider-specific enters a skill body"_ and _"before the question is settled by accident"_ — and the scaffold move would settle it by accident if taken first |

The ordering matters. Moving the scaffold under `.claude/` without deciding
the boundary would push method content inside provider-specific packaging,
which is the failure `P6` names. The boundary is therefore WP1, and every
other work package complies with it.

## EA alignment (assessed top-down before implementing)

The subject is **the method**, so this document lives in `product-archreator/scope/` — the
same call [scope document 8](./8_the-engagement-retrospective-skill.md) made.
The organization's model is touched only where it records artifact paths as
fact; that impact is tabled separately below.

| Layer | Impact |
| ----- | ------ |
| 1_strategy | **No change to elements.** `P6` is fulfilled rather than altered — it already states the boundary is open and points at the question this closes. `P2` (everything in the repository, as text) is what makes the portable tier portable |
| 2_business | **No change to elements.** `RULE9` (a skill links only within `.claude/skills/`) gains a stated reason and a scope: it is a packaging constraint, not a method rule, and WP4 satisfies it structurally instead of by convention |
| 3_information | **No change** |
| 4_application | **`ACMP2` (Bootstrap) gains a realizing artifact** — `templates/`, the scaffold it emits. The scaffold was never modeled as a component of its own and does not become one: it is what `ACMP2` produces, and `P4`/`P5` argue against inventing an element for it. **`ACMP13` and `ACMP15` changed** — both check scripts key on the model directory name and must learn the new one |
| 5_technology | **No change to nodes.** `NODE1` loads skills exactly as before; the plugin manifest keeps its location and role |
| domains | **No change.** Depth 3 is not in use by any of this repository's models — `domains/` exists only inside the scaffold |

### Impact on the organization's model

| Document | Change |
| -------- | ------ |
| [`2_business-services.md`](../../org-archreator/architecture/2_business/2_business-services.md) | `BSVC2`'s realizing artifacts are recorded as "`site/`, `product-archreator/`, and this tree". Those are current-state facts stated as paths, so they change with the paths |
| [`2_business-model-canvas.md`](../../org-archreator/architecture/0_business-design/2_business-model-canvas.md) | Open question 2 moves from Pending to answered, pointing at the decision record from WP1. `CH3` gains its tier: the marketplace is packaging, and a second one is additive |

Everything else across the two models is a **path repair**, not a claim
change. Merged scope documents are repaired under `scope-doc` § Rules — _"update
the link targets so they still resolve, and leave every word alone"_ — which
keeps `RULE6` intact.

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — the subject is the method at Depth 1, not an organization |
| Gate 1 — Strategy | — | — | **N/A** — no Stakeholder, Driver, Goal or Principle is added or modified; `P6` is fulfilled, not changed |
| Gate 2 — Business | Requester | 2026-08-12 | This document, [decision 6](../decisions/6_the-portability-boundary.md) and [decision 7](../decisions/7_one-tree-per-federated-project.md) |
| Gate 3 — Solution design | — | — | **N/A** — declined at Gate 2; layers 4–5 covered by PR review |

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** (before) | Four things in one repository, none of them named after what it is. The root `CLAUDE.md` is the template's placeholder, so no project tree except `site/` declares a modeling depth and step 1a cannot be executed as written. The scaffold at `docs/` is hand-maintained against the skills, with nothing detecting drift. `P6`'s boundary is undrawn |
| **Target** (delivered) | `org-archreator/` and `product-archreator/` (with `site/` nested inside it), each declaring its depth. The scaffold ships inside the skills that emit it. The portability boundary is written down and testable. The root holds archreator's own `CLAUDE.md` and `README.md`, not the template's |

## Work packages and deliverables

### WP1 — Draw the two boundaries

- **Deliverables:** `product-archreator/decisions/6_the-portability-boundary.md` — the
  three-tier split (method content · discovery metadata · packaging), the
  test that assigns a tier (_if Claude Code vanished tomorrow, does this file
  need editing, or just moving?_), and Claude Code named as the first
  packaging target with others additive.
  `product-archreator/decisions/7_one-tree-per-federated-project.md` — the top-level layout
  rule, and why it is **not** the per-product split that
  [decision 5](../decisions/5_no-per-product-strategy-folders.md) forbids.
- **Outcome:** the two calls that every later work package depends on are
  recorded before anything moves, which is the sequencing the canvas asked
  for.

### WP2 — Name the trees, and declare their depths

- **Deliverables:** `org-archreator/` → `org-archreator/`; `product-archreator/` →
  `product-archreator/`; `site/` → `product-archreator/site/`. A `CLAUDE.md`
  in each tree declaring its depth — **Depth 2** for the organization,
  **Depth 1** for the method and for the site (the site already declares it).
  The root `CLAUDE.md` and `README.md` become archreator's own.
- **Outcome:** step 1a of `ea-first-change` can be executed against this
  repository, and a reader can tell the four things apart from the root
  listing.

### WP3 — Rename the model directory

- **Deliverables:** `architecture/` → `architecture/` in all three project trees,
  with `scope/`, `decisions/` and the open-questions log rising to sit beside
  it rather than under `docs/`. All 182 in-repository references repaired
  across the 56 files that carry them, including skill bodies and merged
  scope documents.
- **Outcome:** the directory says what it holds. "Docs" was never what the
  layered model was.

### WP4 — Move the scaffold into the skills that emit it

- **Deliverables:** the contents of `docs/` relocated to
  [`.claude/skills/project-bootstrap/templates/`](../../.claude/skills/project-bootstrap/templates/CLAUDE.md),
  which also gains the `CLAUDE.md` and `README.md` placeholders its layer
  READMEs already linked to. Root `docs/` retired. `project-bootstrap`
  Step 2 rewritten to **emit** the scaffold, and its "delete what you didn't
  inherit" step removed — nothing is inherited any more.
  `scope-doc` and `decision-record` get no `templates/`: their shapes are
  inline in the skill bodies, checked and confirmed during WP4.
- **Outcome:** `product-archreator/open-questions.md` #1 is answered — the scaffold is
  generated from the plugin, travels with the skill that writes it, and
  cannot drift from it.

### WP5 — Teach the checks the new shape

- **Deliverables:** [`scripts/check_model.py`](../../scripts/check_model.py)
  — project discovery currently defines a project as the directory containing
  an `ea/` folder; it learns the new name. [`scripts/check_links.py`](../../scripts/check_links.py)
  — the unresolved-numbered-file rule is keyed on `architecture/` and follows.
  Both run clean across all three trees.
- **Outcome:** the model stays machine-checkable, and this becomes the first
  initiative in this repository to change code as well as documents.

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| The portability boundary, written down and testable | **Actually running on a second agent platform.** That widens `CS1` and is a Gate 1 initiative of its own |
| Renaming and relocating the four trees | Extracting `product-archreator/site/` into its own repository — the nesting is deliberate and extraction is a later, separate move |
| The scaffold moving inside the skills | Generating a project *automatically* on install. `project-bootstrap` still copies on request |
| Path repair across merged scope documents | Any rewording of them. `RULE6` holds — link targets change, claims do not |
| Both check scripts learning the new layout | Enforcing the tier split mechanically. Nothing will detect provider-specific prose entering a skill body |

## Gap notes

- **Nothing enforces the portability boundary.** WP1 produces a test a person
  can apply, not one a script runs. This is the same shape as `RULE2` and the
  confidentiality rule in scope document 8 — a rule the method states and
  review carries. A check that greps skill bodies for provider-specific tokens
  would close most of it cheaply, and is the obvious follow-up if the boundary
  starts eroding.
- **The `product-` prefix is one misreading away from the split decision 5
  forbids.** WP1's second record exists precisely to draw that line, but the
  line lives in a document rather than in the structure. An adopter who copies
  the layout without reading it may well conclude that products get folders.
  Worth watching once anyone adopts the pattern.
- **Renaming the organization would cost what this initiative cost.** The
  `org-` and `product-` prefixes embed a name that three products do not all
  share, which is the same shape that eventually renamed Facebook to Meta.
  Mitigated by having `project-bootstrap` generate the folder from a prompted
  organization name rather than hardcoding it, so an adopter's rename is not
  archreator's problem — but archreator's own rename would still be a
  directory move plus 180-odd link repairs.
- **The scaffold ships no tooling and no `CONTRIBUTING.md`.** A generated
  project gets `CLAUDE.md`, `README.md` and the three model folders, but not
  `scripts/check_links.py` or `check_model.py`, so nothing validates its
  links or element IDs. The scaffold's one reference to the process document
  now points at archreator's published copy rather than a file the project
  owns. Both are defensible — the checks are Python, and a project may not
  be — but it means "the method ships its own enforcement" is still not true
  for anyone but archreator.
- **`site/` nested inside `product-archreator/` is harder to reason about at
  Depth 1.** Two project trees now sit one inside the other. The check scripts
  discover nested projects without complaint, but a reader may expect the
  site's model to be part of the method's rather than beside it.

## Open questions

- **Should the site keep its own model once nested, or fold into the
  method's?** Adopted interpretation: **keep its own.** `BSVC2` is realized by
  the site *and* the method *and* the organization's tree, so the site has
  content of its own to model, and it is intended to become a separate
  repository later. Applied in WP2. Mirrored to
  [`product-archreator/open-questions.md`](../open-questions.md).
