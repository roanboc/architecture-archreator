# Motivation

_[← Strategy layer](./README.md) · [EA home](../README.md)_

**ArchiMate viewpoint:** Motivation. Who has a stake in archreator, what
presses on them, what must become true, and the principles every change is
checked against.

The subject is **the method** — fifteen skills, the scaffold they emit, the
validators, and the plugin that ships them. The organization that publishes it
is modeled one tree up, in
[`org-archreator/`](../../../org-archreator/architecture/README.md).

## How to read this document

```mermaid
flowchart LR
  stk(["◍ «Stakeholder» whose interests the method serves"]):::stakeholder
  drv{{"✳ «Driver» what presses on them"}}:::driver
  asm>"⌕ «Assessment» what is true today"]:::assessment
  goal("◎ «Goal» what must become true"):::goal
  out[["◉ «Outcome» how we would know"]]:::outcome
  prin[/"⚑ «Principle» what every change is checked against"/]:::principle

  stk -->|concerned with| drv
  drv -->|evidenced by| asm
  drv -->|influences| goal
  goal -->|measured by| out
  prin -->|constrains| goal

  classDef stakeholder fill:#f4ecfc,stroke:#9575cd,color:#333
  classDef driver fill:#e6d6f5,stroke:#8e63c8,color:#333
  classDef assessment fill:#d8c3f0,stroke:#7e57c2,color:#333
  classDef goal fill:#c6aae9,stroke:#6f4bb2,color:#333
  classDef outcome fill:#b493e0,stroke:#5f3da0,color:#333
  classDef principle fill:#a37cd8,stroke:#4f318c,color:#333
```

| Glyph | Shape | Element | ID prefix | Reads as |
| ----- | ----- | ------- | --------- | -------- |
| `◍` | Stadium | «Stakeholder» | `STK` | `STK1` = Stakeholder 1 |
| `✳` | Hexagon | «Driver» | `DRV` | `DRV1` = Driver 1 |
| `⌕` | Flag | «Assessment» | `ASM` | `ASM1` = Assessment 1 |
| `◎` | Rounded rectangle | «Goal» | `G` | `G1` = Goal 1 |
| `◉` | Rectangle, double bars | «Outcome» | `OUT` | `OUT1` = Outcome 1 |
| `⚑` | Parallelogram | «Principle» | `P` | `P1` = Principle 1 |

The tone darkens along the chain, from the stakeholder who cares to the
principle that constrains.

## Stakeholders

```mermaid
flowchart LR
  stk1(["◍ Requester in an adopting project [STK1]"]):::stakeholder
  stk2(["◍ Agent in an adopting project [STK2]"]):::stakeholder
  stk3(["◍ Reviewer in an adopting project [STK3]"]):::stakeholder
  stk4(["◍ Method maintainer [STK4]"]):::stakeholder
  stk5(["◍ Reader outside the repository [STK5]"]):::stakeholder

  stk1 -->|delegates the modeling to| stk2
  stk2 -->|hands the branch to| stk3
  stk4 -->|changes what all three follow| stk1
  stk1 -->|shows the model to| stk5

  classDef stakeholder fill:#f4ecfc,stroke:#9575cd,color:#333
```

| ID | Stakeholder | What they want from the method | Where they meet it |
| -- | ----------- | ------------------------------ | ------------------ |
| `STK1` | **Requester in an adopting project** | To own a subject — a company, a department, an app — and have it modeled without doing the modeling. To decide at points they choose, and be shown enough to decide honestly | The gates, and whatever surface a gate is presented on |
| `STK2` | **Agent in an adopting project** | To know the business context before writing code, and to be stopped from acting on a fact that is no longer true. Usually an AI agent | The skills, the model, and the validators |
| `STK3` | **Reviewer in an adopting project** | To read a whole branch and see what it claims to change, against documents that were true before it started | The pull request and the scope document |
| `STK4` | **Method maintainer** | To change the method without silently falsifying the models built on it | The skill corpus and its own validator |
| `STK5` | **Reader outside the repository** | To read the architecture they are asked to agree with, fund or audit, without cloning anything or being taught where it lives | The portal, and the PDF |

**`STK1` and `STK3` are usually the same person, and that is not a
redundancy.** They want different things at different moments: one decides
before the work, the other checks after it. Collapsing them would lose the
distinction that makes the second reading worth doing.

**`STK2` is the stakeholder the method is written for.** The documents are
Markdown in git rather than a modeling tool's file format because that is what
an agent reads natively.

**`STK5` decides nothing, and that is what separates them from `STK1`.** A
Requester is shown a change and grants a gate; a reader is shown the model and
has to be able to follow it. The same documents serve both, which is why
reaching `STK5` is a rendering rather than a second model.

## Drivers and assessments

```mermaid
flowchart LR
  drv1{{"✳ Agents build faster than anyone can specify [DRV1]"}}:::driver
  drv2{{"✳ The context an agent needs is not written down [DRV2]"}}:::driver
  drv3{{"✳ Documentation stops being true when code moves [DRV3]"}}:::driver

  asm1>"⌕ Requirements reach code without passing through architecture [ASM1]"]:::assessment
  asm2>"⌕ An agent cannot tell a deleted element from a live one [ASM2]"]:::assessment
  asm3>"⌕ Modeling tools produce files agents cannot read or diff [ASM3]"]:::assessment
  asm4>"⌕ AI is modeled as a tool, so its decisions have no owner [ASM4]"]:::assessment

  drv1 -->|evidenced by| asm1
  drv2 -->|evidenced by| asm3
  drv2 -->|evidenced by| asm4
  drv3 -->|evidenced by| asm2

  classDef driver fill:#e6d6f5,stroke:#8e63c8,color:#333
  classDef assessment fill:#d8c3f0,stroke:#7e57c2,color:#333
```

| ID | Driver | Why it presses | Concerns |
| -- | ------ | -------------- | -------- |
| `DRV1` | **Agents build faster than anyone can specify** | The constraint on delivery has moved from writing code to deciding what should be written. A requirement handed straight to an agent produces working software nobody agreed to | `STK1`, `STK2` |
| `DRV2` | **The context an agent needs is not written down** | Who the customers are, what the organization is trying to do, which rules bind a change — an agent with none of this fills the gap with something plausible | `STK2` |
| `DRV3` | **Documentation stops being true when code moves** | A model describing last quarter is worse than no model, because it is trusted | `STK2`, `STK3` |

| ID | Assessment | What it means for the method |
| -- | ---------- | --------------------------- |
| `ASM1` | **Requirements reach code without passing through architecture** | The ladder from strategy to technology exists in every methodology and is skipped in most projects, because nothing stops the skip. Something has to stop it |
| `ASM2` | **An agent cannot tell a deleted element from a live one** | An agent reading a claim that one element relieves another has no cheap way to notice the second was removed three initiatives ago, and will reason confidently from it. This is the failure agents are worst at unaided |
| `ASM3` | **Modeling tools produce files agents cannot read or diff** | An architecture kept in a tool's own format is invisible to the reader who most needs it, and invisible to code review |
| `ASM4` | **AI is modeled as a tool, so its decisions have no owner** | When an agent is drawn as a box rather than an actor, nothing records what it may decide alone, or who it escalates to |

## Goals and outcomes

```mermaid
flowchart LR
  g1("◎ An agent reads the business context natively [G1]"):::goal
  g2("◎ A person approves before code exists [G2]"):::goal
  g3("◎ The model still describes today after the merge [G3]"):::goal
  g4("◎ An adopter starts without learning a tool [G4]"):::goal
  g5("◎ The model reaches the people who never open the repository [G5]"):::goal

  out1[["◉ Every element names what realizes it [OUT1]"]]:::outcome
  out2[["◉ Every gate is recorded with what was shown [OUT2]"]]:::outcome
  out3[["◉ No reference resolves to something deleted [OUT3]"]]:::outcome

  g1 -->|measured by| out1
  g2 -->|measured by| out2
  g3 -->|measured by| out3
  g4 -->|measured by| out1

  classDef goal fill:#c6aae9,stroke:#6f4bb2,color:#333
  classDef outcome fill:#b493e0,stroke:#5f3da0,color:#333
```

| ID | Goal | Answers | Realized by |
| -- | ---- | ------- | ----------- |
| `G1` | **An agent reads the business context natively** | `DRV2`, `ASM3` | The model is Markdown in git — nothing has to be exported before it can be used |
| `G2` | **A person approves before code exists** | `DRV1`, `ASM1` | The gates, and the rule that an unrecorded approval did not happen |
| `G3` | **The model still describes today after the merge** | `DRV3`, `ASM2` | The validators, and the rule that a change updates whatever it falsifies |
| `G4` | **An adopter starts without learning a tool** | `ASM3` | A scaffold of Markdown and two scripts, installed as a plugin |
| `G5` | **The model reaches the people who never open the repository** | `ASM3` | The portal and the PDF, both rendered from the Markdown, both thrown away and rebuilt |

| ID | Outcome | How it is checked | Happening today? |
| -- | ------- | ----------------- | ---------------- |
| `OUT1` | **Every element names what realizes it, or says it is Pending** | Review. No validator can tell a repository path from a team name, and a wrong failure in CI teaches people to ignore CI | Partly — the convention holds, the check does not exist |
| `OUT2` | **Every gate is recorded with who approved and what they were shown** | The Approvals table in the scope document | Yes, by convention |
| `OUT3` | **No reference resolves to something that was deleted** | `check_model.py`, on every pull request | Yes, mechanically |

**`G1` and `G5` are the two halves of `ASM3`.** An architecture in a tool's
own format is unreadable by the agent that must build from it *and* by the
person who must agree to it. Markdown in git answers the first directly; the
second is answered by rendering the same files, never by keeping a second copy.

**`G5` is measured by no outcome, because nothing here can measure it.** The
repository knows whether a page can be traced back to its source; it cannot
know whether anyone read it. An outcome invented to fill the row would be
checked by nobody.

**`OUT1` is the weakest of the three, and deliberately so.** Grounding is the
rule that makes the model verifiable, and it is the one the tooling cannot
enforce — distinguishing a path from a description is fuzzy, and a check that
fails wrongly is worse than no check.

## Principles

Constraints every proposed change is tested against, before anything else.
They are few on purpose: a principle nobody could violate is a slogan.

- **P1 — Each fact has exactly one home.** Every other place that needs it
  points there rather than restating it. A second copy is a second thing to
  drift, and the drift is always silent. Where a copy is unavoidable, a check
  holds the two in step.
- **P2 — Every element names what realizes it.** A skill file, a script, a
  written procedure — or an explicit `Pending — future initiative`. An element
  grounded in nothing is a claim, and a model of claims cannot be verified.
- **P3 — An approval that is not recorded did not happen.** The Requester's
  decision lives in the scope document's Approvals table, with what they were
  shown. A gate that did not apply is marked `N/A` with its reason rather than
  deleted, so a skipped gate is distinguishable from a forgotten one.
- **P4 — Consolidate before enumerating.** A new rule, element or document
  must earn its place against the ones that already exist. The method is read
  by people who are busy; length is a cost paid by every future reader.
- **P5 — Method content is portable; packaging is disposable.** The test for
  any file is whether it would need *editing* if the host platform vanished
  tomorrow, or merely *moving*. Anything that would need editing is packaging,
  and packaging is allowed to be thrown away.

**`P1` and `P4` pull the same way from different ends** — one forbids saying a
thing twice, the other forbids saying it at all unless it earns the space.
Together they are why this document is short.

## Notes

`0_business-design/` is empty in this tree and stays that way. The canvases
describe an organization's customers and economics, and this subject has
neither of its own. They are filled one tree up.
