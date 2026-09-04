# Application services

_[← Application layer](./README.md) · [Front door](../README.md)_

**ArchiMate viewpoint:** Application — Application Service.

**Status:** ◐ Draft catalogue — not yet approved at a gate. **Understanding**
covers this document.

## How to read this document

```mermaid
flowchart LR
  asvc(["⬮ «Application Service» what the software does [ASVC#]"]):::app
  bsvc(["⬭ «Business Service» who it does it for — defined in the business layer [BSVC#]"]):::business
  acmp["⊞ «Application Component» the piece that ships it — catalogued next door [ACMP#]"]:::component

  acmp -->|realizes| asvc
  asvc -->|serves| bsvc

  classDef app fill:#c2f0ff,stroke:#0288d1,color:#333
  classDef business fill:#fffbb5,stroke:#c8c04a,color:#333
  classDef component fill:#9adcf0,stroke:#0277bd,color:#333
```

## The services

```mermaid
flowchart LR
  a1(["⬮ Method execution [ASVC1]"]):::app
  a2(["⬮ Document generation [ASVC2]"]):::app
  a3(["⬮ Self-checking [ASVC3]"]):::app
  a4(["⬮ Corpus self-checking [ASVC4]"]):::app
  a5(["⬮ Project emission [ASVC5]"]):::app
  a6(["⬮ Plugin distribution [ASVC6]"]):::app
  a7(["⬮ Model interrogation [ASVC7]"]):::app
  a8(["⬮ Portal configuration [ASVC8]"]):::app
  a9(["⬮ Public guidance serving [ASVC9]"]):::app

  b1(["⬭ Gated change alignment [BSVC1]"]):::business
  b2(["⬭ Subject discovery [BSVC2]"]):::business
  b3(["⬭ Model validation [BSVC3]"]):::business
  b4(["⬭ Decision and scope recording [BSVC4]"]):::business
  b5(["⬭ Method distribution [BSVC5]"]):::business
  b6(["⬭ Restatement and learning [BSVC6]"]):::business
  b7(["⬭ Reading beyond the repository [BSVC7]"]):::business
  b8(["⬭ Public guidance [BSVC8]"]):::business

  a1 -->|serves| b1
  a1 -->|serves| b2
  a1 -->|serves| b6
  a2 -->|serves| b4
  a3 -->|serves| b3
  a4 -->|serves| b3
  a5 -->|serves| b5
  a6 -->|serves| b5
  a7 -->|serves| b7
  a8 -->|serves| b7
  a9 -->|serves| b8

  classDef app fill:#c2f0ff,stroke:#0288d1,color:#333
  classDef business fill:#fffbb5,stroke:#c8c04a,color:#333
```

**This is where the two layers meet, and it is not one-to-one in either
direction.** One application service carries three business services on its
own — `ASVC1` is the skills doing what skills do — while three business
services each need two application services behind them. Every business
service is served; nothing here is built for nobody.

The `Realized by` column below points on to
[the components](./2_application-components.md), which is the next link in
the same chain and is drawn there rather than repeated here.

| ID | Service | Does | Serves | Realized by |
| -- | ------- | ---- | ------ | ----------- |
| `ASVC1` | **Method execution** | Walks a requirement through the layers, runs the discovery conversations, decides which gates apply and stops at each — the skills, doing what skills do | `BSVC1`, `BSVC2`, `BSVC6` | `ACMP1` |
| `ASVC2` | **Document generation** | Produces the scope document, the decision record and the pull-request body from templates with fixed sections | `BSVC4` | `ACMP1` |
| `ASVC3` | **Self-checking** | Resolves every identifier, link and anchor in a project's model and requires a declared status on every defining document — offline, with no plugin installed | `BSVC3` | `ACMP2`, `ACMP3`, `ACMP4` |
| `ASVC4` | **Corpus self-checking** | Checks the skill corpus against the process model, the citation forms, the asset bindings and its own format rules | `BSVC3` | `ACMP7` |
| `ASVC5` | **Project emission** | Copies the eleven-file scaffold into a new project and turns it into that project; emits an asset the first time a skill has content for it | `BSVC5` | `ACMP8`, `ACMP9` |
| `ASVC6` | **Plugin distribution** | Publishes the corpus so a host platform can install it, and copies the skills for a host that installs no plugin | `BSVC5` | `ACMP10`, `ACMP11` |
| `ASVC7` | **Model interrogation** | Reads a project fresh — nothing cached — and answers what a change would touch, what names no realizing artifact, and one focused question as a disposable brief | `BSVC7` | `ACMP5`, `ACMP6` |
| `ASVC8` | **Portal configuration** | Writes a stock MkDocs Material configuration for one project into its gitignored work area, on request — the method owns the boundary, not a site builder | `BSVC7` | `ACMP5` |
| `ASVC9` | **Public guidance serving** | The landing page and the get-started page, telling the two customers what the method is and how to install it | `BSVC8` | `ACMP12` |
