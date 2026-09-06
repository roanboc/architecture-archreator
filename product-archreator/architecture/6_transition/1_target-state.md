# Target state

_[← Roadmap](./README.md) · [Front door](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration — Plateau, Gap.

**Status:** ◐ Draft catalogue — the destination is drafted, not yet approved.
**Direction** covers this document, and approving it approves the states and
their order, never the work.

Where the product should be, measured against the model as it stands, and
what stands between here and there. Every plateau is a state the product can
be in, named for what is true on arrival; every gap names the element it is
measured from and the plateau that closes it. The source of every row is
[the Requester's request](../reference/2026-09-06-poc-features-request.md).

## How to read this document

```mermaid
flowchart LR
  plat[["≡ «Plateau» a state the product can be in [PLAT#]"]]:::plateau
  gap(("⊘ «Gap» what stands between today and it [GAP#]")):::gap
  goal("◎ «Goal» what the state serves — defined in motivation [G#]"):::goal
  stk(["◍ «Stakeholder» who it is worth most to — defined there too [STK#]"]):::stakeholder

  gap -->|closed to reach| plat
  plat -->|serves| goal
  plat -->|strongest for| stk

  classDef plateau fill:#ffe8e8,stroke:#d99b9b,color:#333
  classDef gap fill:#ffd6d6,stroke:#c98080,color:#333
  classDef goal fill:#c6aae9,stroke:#6f4bb2,color:#333
  classDef stakeholder fill:#f4ecfc,stroke:#9575cd,color:#333
```

## The plateaus

```mermaid
flowchart LR
  p2[["≡ The tools are on the bench and drift is caught [PLAT2]"]]:::plateau
  p1[["≡ A change arrives as text and leaves as an approved diff [PLAT1]"]]:::plateau
  p3[["≡ The federation reads as one site [PLAT3]"]]:::plateau
  p4[["≡ The walk runs wherever the Requester is [PLAT4]"]]:::plateau

  g2("◎ A person approves before code exists [G2]"):::goal
  g3("◎ The model still describes today after the merge [G3]"):::goal
  g4("◎ An adopter starts without learning a tool [G4]"):::goal
  g5("◎ The model reaches people who never open the repository [G5]"):::goal
  g7("◎ What the model is worth is written on the model [G7]"):::goal

  p2 -->|serves| p1
  p2 -->|serves| p3
  p2 -->|serves| p4
  p1 -->|serves| g2
  p1 -->|serves| g7
  p2 -->|serves| g3
  p2 -->|serves| g4
  p3 -->|serves| g5
  p4 -->|serves| g5
  p4 -->|serves| g2

  classDef plateau fill:#ffe8e8,stroke:#d99b9b,color:#333
  classDef goal fill:#c6aae9,stroke:#6f4bb2,color:#333
```

**Three of the four hang off the bench, and the bench is the one in flight.**
The walk on record is checked on it, the site is built on it, and a walk
hosted elsewhere is a walk first run here — which is why the least visible
plateau is the first one closed.

| ID | Plateau | Serves | Strongest for | Status |
| -- | ------- | ------ | ------------- | ------ |
| `PLAT1` | **A change arrives as text and leaves as an approved diff** — the request is filed as it was received, walked through the layers with a verdict on every one, scoped before its gate, approved by a reply on the pull request and transcribed into the Approvals table, and the model's diff is the whole of the change; an adopter reads one such walk here end to end, and it is an ordinary change rather than a rebuild | `G2`, `G7` | `STK1`, `STK3` | **Planned** |
| `PLAT2` | **The tools are on the bench and drift is caught** — one command, run before every push, runs the validators and every reading tool over both trees with nothing installed, and fails when the validators here differ from the scaffold's or the method no longer reads these models; the method version the models are written against is declared where a tool can read it | `G3`, `G4` | `STK2`, `STK4` | **In flight** — initiative 2 |
| `PLAT3` | **The federation reads as one site** — a reader who will not open a repository opens one site carrying both trees, every link between them resolves, and what is published is a rendering, never a second copy | `G5` | `STK5` | **Planned** |
| `PLAT4` | **The walk runs wherever the Requester is** — a Requester who is not in a terminal proposes a change in text on the hosted platform, and the agent there runs the same skills against a working copy of the repository, presents the gates there, and lands every approval in the scope document; a question is answered from the current revision, and a change leaves as a pull request, so the host holds a working copy and never a second model | `G5`, `G2` | `STK1`, `STK5` | **Planned** |

**The first plateau is the product's whole argument.** Proposing a change to
an architecture with a sentence and a document, the agent doing the modeling
and a person deciding at the gate, is what the method offers in place of a
modeling tool; the model describes that service as
[Gated change alignment [BSVC1]](../2_business/1_business-services.md), and
the one initiative on record is a rebuild rather than a change, so nobody
evaluating the method can read the service being delivered here. That is the
first gap below, and the reason the ordinary change is the second thing on
the sequence rather than the last.

**Read down the Strongest-for column and the product's readers appear in the
order they meet it.** The Requester and the Reviewer of an adopting project
[STK1, STK3] want the walk; the agent and the maintainer [STK2, STK4] want
the bench; the reader outside the repository [STK5] wants the site; and then
the Requester who never opens a terminal wants the walk itself to come to
them. No plateau is for the method alone.

**None of the four serves the goal that the model says where the subject is
going [G6], and none needs to.** This folder is what that goal asks for, and
the product had none until now — the one goal the product's own model failed,
closed by writing the page rather than by planning to.

### Relationships

What the diagram draws between the plateaus and no row can carry: the bench
serves the other three states, because each of them is checked, built or
proven on it.

| From | From element | To | To element | Relationship |
| ---- | ------------ | -- | ---------- | ------------ |
| `PLAT2` | ≡ «Plateau» The tools are on the bench and drift is caught | `PLAT1` | ≡ «Plateau» A change arrives as text and leaves as an approved diff | serves |
| `PLAT2` | ≡ «Plateau» The tools are on the bench and drift is caught | `PLAT3` | ≡ «Plateau» The federation reads as one site | serves |
| `PLAT2` | ≡ «Plateau» The tools are on the bench and drift is caught | `PLAT4` | ≡ «Plateau» The walk runs wherever the Requester is | serves |

## The gaps

Derived by subtracting today from the plateaus above, measured against the
two trees of this repository at the revision this document was drafted on.

```mermaid
flowchart TB
  subgraph P1G["Toward PLAT1 — the change as text"]
    gap1(("⊘ No ordinary change is on record [GAP1]")):::gap
    gap2(("⊘ The request has no home [GAP2]")):::gap
    gap3(("⊘ Impact is read after the change, not before [GAP3]")):::gap
  end
  subgraph P2G["Toward PLAT2 — the bench"]
    gap4(("⊘ The reading tools have no address [GAP4]")):::gap
    gap5(("⊘ Drift is found by hand [GAP5]")):::gap
    gap6(("⊘ The method version is prose [GAP6]")):::gap
    gap7(("⊘ The readers stumble on two trees [GAP7]")):::gap
    gap8(("⊘ A Lives-at path is never opened [GAP8]")):::gap
  end
  subgraph P3G["Toward PLAT3 — one site"]
    gap9(("⊘ The portal renders one tree [GAP9]")):::gap
    gap10(("⊘ Nothing publishes the models [GAP10]")):::gap
  end
  subgraph P4G["Toward PLAT4 — the walk, anywhere"]
    gap11(("⊘ A gate granted elsewhere has no path into the record [GAP11]")):::gap
    gap12(("⊘ The walk has no surface but a terminal [GAP12]")):::gap
  end

  classDef gap fill:#ffd6d6,stroke:#c98080,color:#333
```

**Five of the twelve are the bench's, and two of the twelve are the method's
to close.** A gap closed by changing the plugin is closed in the archreator
repository with its scope document here; the roadmap names it so the Requester
can carry it across, and so the initiative that closes it has a row to mark.

| ID | Gap | Measured from | Closes toward | Status |
| -- | --- | ------------- | ------------- | ------ |
| `GAP1` | **No ordinary change is on record** — the one initiative recorded is a rebuild with its three gates still open; nothing here shows one requirement becoming a scoped, gated, merged diff, which is the service the product exists to deliver | `BSVC1` | `PLAT1` | **Planned** — initiative 3 |
| `GAP2` | **The request has no home** — what the Requester provides lives in the conversation it was said in; no `reference/` folder exists, so no Source cell can cite it | `DOBJ2.2` | `PLAT1` | **In flight** — initiative 2 |
| `GAP3` | **Impact is read after the change, not before** — `trace` and the impact brief answer what a change would touch, and the alignment walk never asks; a gate is presented with documents and no blast radius | `ASVC7` | `PLAT1` | **Planned** — initiative 5, in the method |
| `GAP4` | **The reading tools have no address** — the repository rules name `model.py` and `build_brief.py` and nothing says where they are; they live in the plugin, installed per host or not at all | `ACMP5`, `ACMP6` | `PLAT2` | **In flight** — initiative 2 |
| `GAP5` | **Drift between the method and the models is found by hand** — the validators here are copies of the scaffold's and nothing compares them; nothing runs the readers over these trees unless somebody remembers to, so a method change that broke `trace`, `coverage`, a brief or the portal here would wait to be noticed | `ACMP3`, `TSVC2` | `PLAT2` | **In flight** — initiative 2 |
| `GAP6` | **The method version is prose** — "0.2" is a sentence on the front door and `0.2.0` a field in the plugin manifest; nothing reads either, so no tool can say that these models were written against a method the plugin has moved past | `ACMP10` | `PLAT2` | **Planned** — initiative 3 |
| `GAP7` | **The readers stumble on a two-tree repository** — `coverage` reports two rows as not true yet because it matches the marker anywhere in a row, where the parse anchors it to the start of a cell; a brief named with `--project` still stops on an identifier both trees own until `--scope` repeats the tree | `ACMP5`, `ACMP6` | `PLAT2` | **Planned** — initiative 4, in the method |
| `GAP8` | **A path in a `Lives at` cell is never opened** — twelve components name a path in the method's repository and no check opens one; a moved directory passes both validators silently, as the scripts' own README says | `ACMP2`, `ACMP3` | `PLAT2` | **Planned** — initiative 5 |
| `GAP9` | **The portal renders one tree** — the configuration the method writes covers one model; built for the product, seven links into the organization's tree, the repository rules and the scripts resolve to nothing | `ASVC8` | `PLAT3` | **Planned** — initiative 6 |
| `GAP10` | **Nothing publishes the models** — the static host serves the guidance site and nothing else; no workflow deploys a portal of these trees, and publishing a model is the Requester's decision, never a default | `NODE3`, `TSVC3` | `PLAT3` | **Planned** — initiative 6, on the Requester's authorization |
| `GAP11` | **A gate granted off the repository has no path into the record** — an approval is transcribed by hand from a reply on a pull request or a sentence in a session; a host where the Requester approves would have to carry the approval into the scope document itself, and nothing does | `BSVC4`, `DOBJ2.2` | `PLAT4` | **Planned** — initiative 7 |
| `GAP12` | **The walk has no surface but a terminal** — the skills run where the adopter's coding agent runs, and a host that is none of those platforms runs nothing; the Requester outside a terminal has neither the terminal nor the plugin | `NODE4`, `TSVC4` | `PLAT4` | **Planned** — initiative 7 |

## What is deliberately not a gap

- **A graph to explore.** A reader arrives with a question, not at a graph;
  the product answers with a brief, and a navigator would answer a question
  nobody asked.
- **A second model on the host.** The host that runs the walk holds a working
  copy of the repository, and every change it makes leaves as a pull request.
  A host that edited a copy of its own would be the second model, which is the
  thing the product exists to prevent.
- **A converter on the bench.** One brief or one scope document per PDF,
  converted by the agent with whatever the environment offers, is the
  method's rule; a converter here would be a dependency for a job any agent
  already does.
- **The organization's roadmap.** Its front door keeps the stated gap: where
  the organization is going is decided there, by the Requester, and never
  derived from where the product is going.
