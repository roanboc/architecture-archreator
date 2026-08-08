---
name: ea-doc-style
description: Use when creating or editing any document under docs/ea/ or docs/scope/ — numbering, ArchiMate-on-Mermaid notation, grounding rules, and link conventions for this repo's documentation.
---

# EA documentation style

## Language

Pick one documentation language for the project and use it consistently
across `docs/ea/`, `docs/scope/`, commit messages, and code identifiers
(see the project's `CLAUDE.md`). Whatever language is chosen, **folder and
file names stay plain ASCII** (no accents, no non-Latin punctuation) even
if the prose inside is written in a language that uses them — this avoids
cross-platform path and URL-encoding issues. If ArchiMate stereotypes are
translated, keep a correspondence table to the standard English element
names near the top of `docs/ea/README.md`.

## Numbering

- Layer folders are numbered in assessment order and never reordered:
  `1_strategy`, `2_business`, `3_information`, `4_application`,
  `5_technology` (translate the words if the project's doc language isn't
  English, but keep the numbers and the order). Projects that model an
  organization also have `0_business-design`, holding the canvases the rest
  is derived from — it is not an ArchiMate layer, and application-only
  projects leave it empty.
- Files inside a layer carry a numeric prefix giving the **logical analysis
  order**, which each layer README explains in an "Analysis order" table.
  A new file gets the next number, plus a row in that table; only renumber
  when the analysis order genuinely changes.
- Scope documents (`docs/scope/`) are numbered **chronologically** per
  initiative.

## Element IDs

Every element in an inventory table carries a short **ID** in its own first
column: a type prefix followed by an integer, no separator — `G1`, `CAP3`,
`PROD2`. IDs are how one document refers to an element in another without
restating it, and they are what lets the model be exported mechanically
later (see `stack-selection` § The model as data).

| Where | Prefixes |
| ----- | -------- |
| Motivation | `STK` Stakeholder · `DRV` Driver · `ASM` Assessment · `G` Goal · `OUT` Outcome · `P` Principle |
| Strategy | `CAP` Capability · `RES` Resource · `COA` Course of Action · `VS` Value Stream |
| Business | `ACT` Actor · `ROLE` Role · `BCOL` Business Collaboration · `PROD` Product · `BSVC` Business Service · `BPROC` Business Process · `BOBJ` Business Object · `BIF` Business Interface · `CTR` Contract · `RULE` Business Rule · `VAL` Value |
| Information | `DOBJ` Data Object |
| Application | `ASVC` Application Service · `ACMP` Application Component |
| Technology | `TSVC` Technology Service · `NODE` Node · `ART` Artifact |
| Canvas (VPC) | `JOB` Job · `PAIN` Pain · `GAIN` Gain · `PREL` Pain Reliever · `GCRE` Gain Creator |
| Canvas (BMC) | `KP` Key Partner · `KA` Key Activity · `KR` Key Resource · `VP` Value Proposition · `CR` Customer Relationship · `CH` Channel · `CS` Customer Segment · `RS` Revenue Stream · `COST` Cost |

Rules: an ID is assigned once and **never reused** after the element is
removed (a dangling reference should fail loudly, not silently point at
something else); numbering is per prefix, not global; and an element's ID
never changes when it is renamed. Referencing an element in prose or a
table cell means writing its ID — `relieves PAIN2` — not repeating its
description.

### Namespacing across domains

A project modeling multiple domains (see the `domain-modeling` skill and
`docs/ea/domains/README.md`) qualifies
IDs by domain, the way a module path qualifies a symbol:

| Where the reference is written | How the ID is written | Example |
| ------------------------------- | ---------------------- | -------- |
| Inside the domain that owns the element | bare | `BSVC3` |
| From another domain, or from the enterprise level | `<DOMAIN>.` prefix, domain in upper case | `SALES.BSVC3` |
| An element owned at the enterprise level | always bare | `G1` |

The domain segment is the folder name under `docs/ea/domains/`, upper-cased
(`domains/sales/` → `SALES.`). A subdomain chains it — `SALES.EMEA.BSVC2` —
which is also why the tree is capped at three levels; beyond that the IDs
stop being readable, and the thing being modeled is a team, not a domain.

Numbering stays per prefix **per domain**: two domains may both own a
`BSVC3`, and the qualifier is what tells them apart. This is deliberate —
domains are meant to be modeled independently, and forcing globally unique
numbers would make every new domain a merge conflict against every other.

Only a domain's **exposed** services (the ones in its charter) may be
referenced from outside it. Referencing another domain's internal process or
resource by ID reaches through the contract and is a modeling error — take
it up with that domain's charter instead.

## Canvas notation

The canvases in `0_business-design/` are Strategyzer artifacts, not
ArchiMate, so they are written as **tables, one per canvas**, not as
diagrams — a nine-block grid is unreadable in Mermaid and a table diffs
cleanly. Each canvas gets its own `###` heading naming the segment or
product it belongs to.

Where a canvas *is* drawn — a layer view showing fit — use the canvas
block name as the stereotype (`«Pain»`, `«Gain Creator»`, `«Customer
Segment»`) with the Motivation fill for the customer profile and the
Strategy fill for the value map, as in
`docs/ea/0_business-design/README.md` § Layer view.
The canvas-block-to-ArchiMate-element mapping lives in that same README and
is not restated anywhere else.

## Grounding rule (the most important one)

Every EA element must name the code artifact that realizes it — a page, a
module path, a pipeline file. If you cannot point at the realizing
artifact, either the element doesn't belong in the docs, or the code is
missing and the element should be marked explicitly **"Pending — future
initiative"** (ideally linked to the initiative that will deliver it). This
keeps the whole set verifiable against the code at any time — an outsider
should be able to open any EA document and check it against the repo.

## ArchiMate on Mermaid

ArchiMate has no native Mermaid profile, so these documents encode
ArchiMate semantics onto Mermaid flowcharts with two rules:

1. **Element type as a «stereotype»** in the first line of each node label,
   e.g. `«Business Service»`, `«Data Object»`, `«Capability»`.
2. **One `classDef` per layer**, using the per-layer palette. The exact
   fills (Motivation, Strategy, Business, Application, Technology,
   Implementation & Migration) live in exactly one place —
   `docs/ea/README.md` § Notation conventions.
   Copy the `classDef` lines from there rather than re-tabulating the hexes
   here, so the palette never drifts between documents.

Relationships are labeled with their ArchiMate name (**serves**,
**realizes**, **assigned to**, **accesses**, **triggers**, **flow**,
**aggregates**, **influences**); where Mermaid arrowheads can't distinguish
relation types, the label is authoritative.

## Actors: human, AI, and hybrid

`«Business Actor»` and `«Business Role»` nodes name **who** — and in a
system where an AI can hold a role, "who" is no longer implicitly human.
State the actor's kind on the same line as the stereotype:
`«Business Actor (Human)»`, `«Business Actor (AI)»`, or
`«Business Actor (Hybrid)»` (a human and an AI sharing one role, e.g. a
co-pilot pattern). Default to `(Human)` only when the actor is provably
never an AI system acting with delegated authority — don't omit the
qualifier to save space.

When populating `2_business/1_business-actors-and-roles.md`, explicitly
ask, for every role: **does an AI system perform or assist this role, and
at what autonomy?** — don't let "actor" default to human by omission. For
every `(AI)` or `(Hybrid)` actor, the actors table carries three extra
columns beyond the usual name/description:

| Column | Answers |
| ------ | ------- |
| Autonomy level | One of: **advisory** (suggests, a human decides and acts), **co-pilot** (acts, a human reviews before it takes effect), **autonomous with checkpoint** (acts independently, a human is notified and can intervene after the fact), **fully autonomous** (acts independently, no routine human checkpoint) |
| Decision rights | What this actor is actually authorized to decide or change, in concrete terms — not "helps with X" |
| Escalation path | Who/what it hands off to when it's outside its authority or confidence — a Business Role, not a vague "a human" |

If an initiative changes an AI actor's autonomy level or decision rights,
that's exactly the kind of call the `decision-record` skill is for.

## Document skeleton

- Title (`# …`), then a nav line:
  `_[← <Layer> layer](./README.md) · [EA home](../README.md)_`
  (scope docs link to the scope index instead).
- State the **ArchiMate elements/viewpoint** covered near the top.
- Prefer tables for element inventories, Mermaid for relationships, and
  prose only for rationale (the "why", not the "what" — the diagrams and
  tables already say what).

## Links

- Always relative, always to a specific file (`../2_business/README.md`,
  not `../2_business/`), keeping `#anchors` when pointing at a section.
- Human-readable link text (`[solution design](…)`), not raw paths.
- Each fact lives in exactly one document; everything else links to it. If
  you are about to restate a table or diagram, link instead.
- When renaming or moving a doc, grep the whole repo for the old path and
  fix every reference in the same change.
- **Skill files are the exception: they link only within `.claude/skills/`.**
  A skill points at a consuming project's documents by naming the path in a
  code span — `` `docs/ea/README.md` § Modeling depth `` — never as a
  relative link. Skills ship as a plugin, and installing one copies its
  directory to a cache, so a link reaching outside that directory resolves
  to nothing for anyone who installed rather than cloned.
