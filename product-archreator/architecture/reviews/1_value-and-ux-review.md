# Review — value, and whether the workflows land for a new user

_[← meta index](../../README.md) · [Repository README](../../../README.md)_

**Date:** 2026-08-08 · **Subject:** archreator at commit `58c369f` (29
commits, 84 files, ~9,800 lines) · **Acted on by:**
[scope/1_repo-value-and-fractal-domains.md](../scope/1_repo-value-and-fractal-domains.md)

Three questions: does archreator add real value over comparable tools; are
its workflows and documentation clear enough for a new user; and what should
improve. The frame for the third is the stated goal — companies model their
enterprise landscape, model each business line vertically, and the repository
becomes the organizational brain and eventually an executer of AI-assisted
processes with humans in the loop.

## 1. Value against comparable tools

### The differentiator, stated plainly

**archreator models to implement; the comparable frameworks model to
document.** That is the thesis the rest of this section tests, and it is
also the reason for the ArchiMate-over-TOGAF choice that a reader might
otherwise take as arbitrary.

TOGAF is a process framework — the ADM governs how an architecture practice
runs, and its output is a deliverable catalogue. ArchiMate is a modeling
language whose elements denote things that exist. archreator takes the
language and skips the process framework, then adds the one rule that keeps
a model honest: **the grounding rule**, under which every element names the
artifact realizing it or is explicitly Pending.

The consequence is testable, which is the point. Open any document under
`docs/ea/` and check it against the repository or against the people doing
the work. A documentation framework has no answer to that question; here it
is the definition of done.

This should be said in the README, which previously left the ArchiMate
choice unexplained and let a reader assume it was notation preference.

### Against BMAD-METHOD — different altitude, no overlap to defend

[BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) is project-scoped
SDLC: analysis → planning → solutioning → implementation, with agent personas
(PM, architect, developer, QA) and context-engineered story files. It carries
no persistent organizational model, no enterprise layers, and no business
sign-off gates. archreator operates one level up — the model outlives the
project, and the organization can be the subject rather than the software.

The one thing archreator borrowed, `story-sharding`, is already credited to
BMAD in the skill itself. There is nothing else to compare.

### Against ArcKit — the real comparable, and the thinner margin

[ArcKit](https://github.com/tractorjuice/arc-kit) is 75+ slash commands for
enterprise-architecture governance: traceability chains, Wardley maps,
compliance packs (UK Service Standard, TCOP, DPIA), ServiceNow integration.
It targets regulated and public-sector environments that need audit trails.
It is distributed as a Claude Code plugin and a `pip`-installable scaffolder.

archreator's differentiation against it is real but currently undersold:

| # | The differentiator | Where it lives today |
| - | ------------------ | -------------------- |
| 1 | **AI actors as first-class modeled organization members** — `«Business Actor (AI)»` carrying a mandatory autonomy level (advisory / co-pilot / autonomous-with-checkpoint / fully autonomous), decision rights, and an escalation path | [`ea-doc-style` § Actors](../../../.claude/skills/ea-doc-style/SKILL.md) |
| 2 | **A standing ArchiMate model as the deliverable**, not generated governance artifacts | [`meta/ea/`](../README.md) |
| 3 | **The grounding rule** — every element names the artifact realizing it, or is explicitly "Pending", so the model is falsifiable against the repository | [`ea-doc-style` § Grounding rule](../../../.claude/skills/ea-doc-style/SKILL.md) |
| 4 | **Reasoning-first skills, not a command catalogue** — the skill states the *what*, the model reasons the *how* | [`.claude/skills/`](../../../.claude/skills/README.md) |

Differentiator 1 is the strongest and the most defensible: neither BMAD nor
ArcKit models the AI as part of the organization. It is also the seed of the
executer ambition — an actor with a declared autonomy level, decision rights,
and an escalation path is already most of a machine-readable delegation
contract.

Differentiator 3 is the one that separates the two intents. ArcKit's
traceability runs sideways — document to document, with citation markers
linking artifacts to sources — which is exactly right when the deliverable
is audit evidence. archreator's runs downward, from element to realizing
artifact, because the deliverable is a working system. Both are traceability;
they point in different directions because they are for different jobs.

**The positioning problem.** The README led with "vibe coders and AI-first
builders … burned by drift." That sells differentiators 1–3 short and aims at
an audience whose problem is a single application, not an enterprise
landscape. The company track existed but sat as a subsection of an
application-shaped document.

## 2. The stated principles, assessed

Well served already, and worth protecting: everything-as-code; humans in
charge of strategy and business with explicit gates; markdown as first-class
documentation with narratives and diagrams; a small skill surface where the
model supplies the *how*. On the last point specifically — ArcKit ships 15
plugins and 165 prompt files. Nine skills is a feature, not a shortfall.

Three critiques:

**The enterprise graph is load-bearing, not a nice-to-have.**
[`ea-doc-style` § Element IDs](../../../.claude/skills/ea-doc-style/SKILL.md)
already mandates the full prefix scheme, and
[`stack-selection` § The model as data](../../../.claude/skills/stack-selection/SKILL.md)
already specifies the exact `nodes`/`edges` SQLite schema. The design is
finished; the implementation is zero. Today
[`check_links.py`](../../../.claude/skills/project-bootstrap/templates/scripts/check_links.py) catches a broken file link
but nothing catches a dangling `PAIN2` reference. At one organization that is
survivable; across twenty business lines the markdown drifts silently and no
human can verify it. This is the highest-value item left in the backlog.

**Fractal domains and multi-agent were absent, not partial.** `docs/ea/` was
flat and single-organization, with no notion of a business line owning its
own model. The only occurrence of "parallel" outside the examples was a
warning *against* it.

**Don't build the executer.** Going from modeled processes to AI-executed
processes needs a runtime, and that is a product, not a documentation
convention. Build the *contract* instead: make business processes carry
enough structure — inputs, outputs, actor assignment, autonomy level,
escalation — that an agent can pick one up and run it, and let the runtime be
Claude Code plus skills to begin with. The autonomy notation is already that
seed.

## 3. Ten verified new-user defects

The documentation is unusually consistent — gate names are byte-identical
across fourteen files, and the single-source-of-truth discipline on the
colour palette and the canvas mapping holds without exception. The defects
below are journey defects, not writing defects.

| # | Defect | Evidence |
| - | ------ | -------- |
| D1 | `story-sharding` was an orphan — **zero** inbound references from any skill. `ea-first-change` Step 6 is exactly where it should fire and didn't. | Only the README, `docs/scope/README.md`, and the skills index mentioned it |
| D2 | On both discovery tracks the scope document was unreachable. Creating it is `ea-first-change` Step 3, but both discovery verdicts occur at Step 1 and hand off to another skill. Both discovery skills then said "record the approval in the scope document's Approvals table" — a document nothing told you to create, number, or index. | The `CONTRIBUTING.md` process flow's discovery branch never touched the `scopedoc` node |
| D3 | Gate 2 applicability was stated three contradictory ways. | "Every initiative" vs "at minimum for any change in documented behavior" vs `example-company`'s "Gate 2 does not apply" |
| D4 | The Approvals template hard-coded **only a Gate 2 row**, so an agent on a discovery initiative copied a table shaped for the wrong gate. | `scope-doc` § Template |
| D5 | `CLAUDE.md` was advertised as "Start here if you're an agent" but shipped as `<placeholder>` prose naming 6 of 9 skills. | README's orientation table |
| D6 | No skill covered bootstrap. The first-commit checklist was human-only prose, so an agent dropped into a fresh clone matched `ea-first-change`, hit the placeholder trigger, and dived into strategy discovery — skipping project name, documentation language, and folder pruning. | No skill description mentioned bootstrap except `stack-selection`, covering one of six steps |
| D7 | No skill linked back to `README.md` or `CONTRIBUTING.md`. Onboarding flowed README → skills, never the reverse. | All nine `SKILL.md` files |
| D8 | A stray `RN-xx` rule ID (Spanish *Regla de Negocio*, left from a translated ancestor) matched nothing. Root cause: the element-ID table had **no prefix for business rules at all**, though the rules table is mandatory. «Value» and «Business Collaboration» were missing too. | `story-sharding`; `ea-doc-style` § Element IDs |
| D9 | Link text disagreed with link target in two places, violating the repository's own link rule. | `stack-selection`; `README.md` |
| D10 | archreator did not follow its own process for its own development — 29 commits, zero scope documents — because `docs/scope/` must stay blank for cloners. A real tension, previously unstated. | `docs/scope/` held only templates |

All ten are addressed by
[scope/1_repo-value-and-fractal-domains.md](../scope/1_repo-value-and-fractal-domains.md).

## 4. Distribution: the packaging was hiding a structural flaw

The template-repository model bundled three things with different lifecycles
into a single clone:

| | What | Lifecycle |
| - | ---- | --------- |
| **Method** | the skills, the PR templates, the link checker | versionable software — wants upgrades |
| **Scaffold** | layer READMEs, document templates, `CLAUDE.md`, `CONTRIBUTING.md` | seed content, overwritten on day one |
| **Examples** | `site/`, `example-company/` | read-only reference — should never be cloned |

Forcing all three into one bundle is *why* the README needed a section
explaining that downstream projects must not submodule or pin, and why method
improvements had to be hand-ported into every existing project. Those were
symptoms of the packaging, not quirks of the method.

Splitting them — the method as an installable, versioned Claude Code plugin;
the scaffold written by a bootstrap skill; the examples left on GitHub — makes
`/plugin update` propagate method improvements, which the README previously
documented as impossible.

## 5. Non-technical adoption is not a packaging problem

A plugin install and a template clone both require a GitHub account, git, a
terminal, and Claude Code. Neither packaging reaches a non-technical user, so
the choice between them is not the lever.

The role model already solves this, and it was simply not exploited:

| Role | Technical skill required |
| ---- | ------------------------ |
| **Requester** — says what should change, approves at the gates | **none** |
| **Agent** — walks the layers, drafts, implements | it is the AI |
| **Reviewer** — approves and merges the PR | some |

A non-technical user should never install anything. Someone technical sets
the repository up once; the non-technical person participates only as
Requester. The real gap was that `ea-first-change` said "present to the
Requester, in one message" and never said *where* — and for a non-technical
Requester, that unstated surface is the entire product experience. Three
surfaces now named in the skill: Claude Code on the web for the discovery
conversation, **PR comments for the gates** (durable and auditable for free,
which fits the existing "an approval that isn't recorded didn't happen"
rule), and a published read-only site for stakeholders who never open GitHub.

## 6. Backlog, in priority order

Everything above the line is delivered by
[scope/1_repo-value-and-fractal-domains.md](../scope/1_repo-value-and-fractal-domains.md).
Below the line is what it deliberately left out.

| # | Item | Why this order |
| - | ---- | -------------- |
| 1 | **Graph exporter and ID validator** — the `nodes`/`edges` projection, plus CI failing on a dangling element reference | The design is already written and the IDs already exist. It converts a convention into an enforced invariant, which is what makes the model survive twenty business lines. Namespaced domain IDs were designed to map onto this schema one-for-one |
| 2 | **Multi-agent orchestration** — running agents in parallel across horizontal layers or vertical business-service slices | Depends on 1 for a shared queryable state and on the federation rule for ownership boundaries. Attempting it before those exist produces merge conflicts, not throughput |
| 3 | **Executable process contracts** — business processes carrying inputs, outputs, actor assignment, autonomy, and escalation in a machine-readable shape | The path to the executer ambition. Build the contract, not the runtime |
| 4 | **A Requester-facing surface that is not GitHub** — a rendered model view with gate approvals inline | Only worth building once 1 exists to generate it |
