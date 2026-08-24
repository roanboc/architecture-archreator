# Application services

_[← Application layer](./README.md) · [EA home](../README.md)_

**ArchiMate viewpoint:** Application. What the software offers the business
layer, and which business service each one realizes.

**Status:** ● Validated — **Gate 3** declined at Gate 2 ([scope document 1](../scope/1_rebuild-the-models-on-the-current-method.md), 2026-08-22), which routed the layers below the business layer to pull-request review.

## How to read this document

```mermaid
flowchart LR
  asvc(["⬮ «Application Service» what the software offers"]):::service
  bsvc(["⬭ «Business Service» — context, from the business layer"]):::business

  asvc -->|realizes| bsvc

  classDef service fill:#c2f0ff,stroke:#0288d1,color:#333
  classDef business fill:#efe57d,stroke:#b8ad3f,color:#333
```

| Glyph | Shape | Element | ID prefix | Reads as |
| ----- | ----- | ------- | --------- | -------- |
| `⬮` | Stadium | «Application Service» | `ASVC` | `ASVC1` = Application Service 1 |
| `⬭` | Stadium (yellow) | «Business Service» — context, from [2_business/2_business-services.md](../2_business/2_business-services.md) | `BSVC` | `BSVC1` = Business Service 1 |

## The services

```mermaid
flowchart LR
  asvc1(["⬮ Layer-by-layer alignment [ASVC1]"]):::service
  asvc2(["⬮ Guided discovery [ASVC2]"]):::service
  asvc3(["⬮ Document generation [ASVC3]"]):::service
  asvc4(["⬮ Reference and link checking [ASVC4]"]):::service
  asvc5(["⬮ Corpus self-check [ASVC5]"]):::service
  asvc6(["⬮ Project emission [ASVC6]"]):::service
  asvc7(["⬮ Plugin distribution [ASVC7]"]):::service
  asvc8(["⬮ Model projection [ASVC8]"]):::service
  asvc9(["⬮ Model publication [ASVC9]"]):::service
  asvc10(["⬮ Model interrogation [ASVC10]"]):::service
  asvc11(["⬮ Transition planning [ASVC11]"]):::service

  bsvc1(["⬭ Gated change alignment [BSVC1]"]):::business
  bsvc2(["⬭ Subject discovery [BSVC2]"]):::business
  bsvc3(["⬭ Model validation [BSVC3]"]):::business
  bsvc4(["⬭ Decision and scope recording [BSVC4]"]):::business
  bsvc5(["⬭ Method distribution [BSVC5]"]):::business
  bsvc7(["⬭ Model publication [BSVC7]"]):::business
  bsvc8(["⬭ Model interrogation [BSVC8]"]):::business
  bsvc9(["⬭ Transition planning [BSVC9]"]):::business

  asvc1 -->|realizes| bsvc1
  asvc2 -->|realizes| bsvc2
  asvc3 -->|realizes| bsvc4
  asvc4 -->|realizes| bsvc3
  asvc5 -->|realizes| bsvc3
  asvc6 -->|realizes| bsvc5
  asvc7 -->|realizes| bsvc5
  asvc8 -->|realizes| bsvc8
  asvc10 -->|realizes| bsvc8
  asvc11 -->|realizes| bsvc9
  asvc9 -->|realizes| bsvc7

  classDef service fill:#c2f0ff,stroke:#0288d1,color:#333
  classDef business fill:#efe57d,stroke:#b8ad3f,color:#333
```

| ID | Application service | What it does | Realizes | Provided by |
| -- | ------------------- | ------------ | -------- | ----------- |
| `ASVC1` | **Layer-by-layer alignment** | Walks a requirement down the six layers, decides which gates apply, and stops at each one | `BSVC1` | `ACMP1` |
| `ASVC2` | **Guided discovery** | Runs the canvas and strategy conversations, the domain split, and the sweep of an estate that was already running, each ending at a gate | `BSVC2` | `ACMP2` |
| `ASVC3` | **Document generation** | Produces the scope document, the decision record and the pull-request body from templates with fixed sections | `BSVC4` | `ACMP1`, `ACMP3` |
| `ASVC4` | **Reference and link checking** | Resolves every element identifier and every relative link and anchor in a model, per project, and requires a declared status on every document that defines an element | `BSVC3` | `ACMP5`, `ACMP6`, `ACMP7` |
| `ASVC5` | **Corpus self-check** | Checks the skill corpus against the process model and its own format rules | `BSVC3` | `ACMP9` |
| `ASVC6` | **Project emission** | Copies the scaffold into a new project and turns it into that project | `BSVC5` | `ACMP2`, `ACMP10` |
| `ASVC7` | **Plugin distribution** | Publishes the corpus so a host platform can install it | `BSVC5` | `ACMP11` |
| `ASVC8` | **Model projection** | Reads a model and writes it as nodes and edges for a consumer that cannot read Markdown | `BSVC8` | `ACMP7`, `ACMP8` |
| `ASVC9` | **Model publication** | Renders a model as a website and prints it as one document, both from the Markdown, and gives every page a route back to the file it came from. Publishes no source document — the portal hands a reader the model, and a transcript carries the rest of the room | `BSVC7` | `ACMP12`, `ACMP13` |
| `ASVC10` | **Model interrogation** | Walks the projected graph outward from one element to say what a change would touch, and reports which catalogue rows name no realizing artifact while their neighbours do | `BSVC8` | `ACMP14` |
| `ASVC11` | **Transition planning** | Turns approved goals and a described baseline into target plateaus, a derived gap register and a dependency-ordered sequence, ending at a gate | `BSVC9` | `ACMP15` |

**`ASVC8`'s edge is solid, and `ASVC10` is what made it so.** The projection
was built, worked, and was consumed by nothing for as long as the only
candidate was the published view — and `ASVC9` does not read it, because
rendering documents means rendering the documents, and a renderer fed the
projection would publish a second-hand copy of what is already Markdown.

The consumer the dash was waiting for was named in advance: one that asks graph
questions — coverage, and blast radius. `ASVC10` asks exactly those two, which
is why it reads `.model/` rather than importing the parser. Importing the parser
would have been simpler and would have left this edge dashed, because a
projection nothing reads is not a projection.

**`ASVC9` renders and never summarizes.** A page it publishes says exactly
what the file says, which is what makes the rendering safe to hand to someone
who will never see the file. `RULE7` is the constraint, and every page carries
its source path so a reader can check it.

**`ASVC4` and `ASVC5` both realize `BSVC3`, and neither is redundant.** One
checks a model an adopter wrote; the other checks the method itself. They
share no code and run in different repositories — the first ships in the
scaffold, the second deliberately does not, because a downstream project has
no skills to check.

**No service realizes `BSVC6`.** Model restatement and the engagement
retrospective are procedures a person or an agent follows, with no component
behind them beyond the skill text itself. That is a real gap in the sense that
nothing can be automated about them today, and not a gap in the sense that
something is missing — some work is judgement, and the method says so rather
than inventing a component to fill the row.
