# Business services

_[← Business layer](./README.md) · [Front door](../README.md)_

**ArchiMate viewpoint:** Business — Business Service.

**Status:** ◐ Draft catalogue — not yet approved at a gate. **Understanding**
covers this document.

## How to read this document

```mermaid
flowchart LR
  bsvc(["⬭ «Business Service» what the product does for an adopting project [BSVC#]"]):::business

  classDef business fill:#fffbb5,stroke:#c8c04a,color:#333
```

## The services

```mermaid
flowchart LR
  b8(["⬭ Public guidance [BSVC8]"]):::business
  b5(["⬭ Method distribution [BSVC5]"]):::business

  subgraph guided["The guided route — the builder explains, the agent runs the method"]
    b2(["⬭ Subject discovery [BSVC2]"]):::business
    b1(["⬭ Gated change alignment [BSVC1]"]):::business
    b6(["⬭ Restatement and learning [BSVC6]"]):::business
  end

  subgraph expert["The expert route — the same model, no agent required"]
    b3(["⬭ Model validation [BSVC3]"]):::business
    b7(["⬭ Reading beyond the repository [BSVC7]"]):::business
  end

  b4(["⬭ Decision and scope recording [BSVC4]"]):::business

  b8 -->|serves| b5
  b5 -->|serves| b2
  b2 -->|flows to| b1
  b4 -->|serves| b1
  b6 -->|serves| b1
  b3 -->|serves| b1
  b7 -->|serves| b1

  classDef business fill:#fffbb5,stroke:#c8c04a,color:#333
```

**Five of the eight services point at one.** `BSVC1` is where the method
happens and everything else exists to reach it, feed it, record it or read
what it produced — which is also why a change to it is the most expensive
change in this model.



| ID | Service | Delivers | Realized by |
| -- | ------- | -------- | ----------- |
| `BSVC1` | **Gated change alignment** | A requirement walked top-down through the layers, stopped at every gate that applies, each layer changed or explicitly declared unchanged | `ACMP1` |
| `BSVC2` | **Subject discovery** | A company or an application turned into canvases, a strategy and — where one already runs — a described estate, each approved before the next begins | `ACMP1` |
| `BSVC3` | **Model validation** | Mechanical proof that references resolve, identifiers are never reused, links point at something, and every defining document declares how far it has been validated — offline, with no plugin | `ACMP2`, `ACMP3`, `ACMP4` |
| `BSVC4` | **Decision and scope recording** | A durable record of what was approved, by whom, and what they were shown — and of the calls too small to be initiatives | `ACMP1` |
| `BSVC5` | **Method distribution** | An installable plugin, and a scaffold that is a working project on its first commit — eleven files, every one of them used | `ACMP8`, `ACMP9`, `ACMP10`, `ACMP11` |
| `BSVC6` | **Restatement and learning** | A model that stopped reading as a description of today turned back into one, and what the method failed to cover captured before it evaporates | `ACMP1` |
| `BSVC7` | **Reading beyond the repository** | Answers a table cannot give — what a change would touch, what names no realizing artifact — plus a portal generated on request and a brief for one question, converted to PDF by the agent when a reader asks | `ACMP5`, `ACMP6` |
| `BSVC8` | **Public guidance** | Why the method exists, what an adopter receives, and the two install commands — for the reader who has not adopted anything yet | `ACMP12` |

**Two ways in, one model.** `BSVC1`, `BSVC2` and `BSVC6` are the guided
route — the independent builder explains the business and the agent runs the
method. `BSVC3` and `BSVC7` serve the expert route just as well without an
agent in the loop: an enterprise architect navigates the standard structure
directly, and the validators and readers answer to them too.

## Relationships

What the diagram above draws: seven dependencies between peers in one layer,
which a catalogue with one row per service has no column shape for.

| From | From element | To | To element | Relationship |
| ---- | ------------ | -- | ---------- | ------------ |
| `BSVC8` | ⬭ «Business Service» Public guidance | `BSVC5` | ⬭ «Business Service» Method distribution | serves |
| `BSVC5` | ⬭ «Business Service» Method distribution | `BSVC2` | ⬭ «Business Service» Subject discovery | serves |
| `BSVC2` | ⬭ «Business Service» Subject discovery | `BSVC1` | ⬭ «Business Service» Gated change alignment | flows to |
| `BSVC4` | ⬭ «Business Service» Decision and scope recording | `BSVC1` | ⬭ «Business Service» Gated change alignment | serves |
| `BSVC6` | ⬭ «Business Service» Restatement and learning | `BSVC1` | ⬭ «Business Service» Gated change alignment | serves |
| `BSVC3` | ⬭ «Business Service» Model validation | `BSVC1` | ⬭ «Business Service» Gated change alignment | serves |
| `BSVC7` | ⬭ «Business Service» Reading beyond the repository | `BSVC1` | ⬭ «Business Service» Gated change alignment | serves |
