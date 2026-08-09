# Application Components

_[← Application layer](./README.md) · [EA home](../README.md)_

**ArchiMate elements:** Application Service, Application Component.

## How to read this document

```mermaid
flowchart LR
  asvc(["⬮ «Application Service»<br>what the software offers"]):::appservice
  acmp["⊞ «Application Component»<br>a page that provides it"]:::component
  bsvc(["⬭ «Business Service»<br>what the business offers"]):::business

  acmp -->|realizes| asvc
  asvc -->|realizes| bsvc

  classDef appservice fill:#c2f0ff,stroke:#2a8fb0,color:#333
  classDef component fill:#9adcf0,stroke:#1a6f8c,color:#333
  classDef business fill:#fffbb5,stroke:#b8a200,color:#333
```

| Glyph | Shape | Element | ID prefix | Reads as |
| ----- | ----- | ------- | --------- | -------- |
| `⬮` | Stadium | «Application Service» | `ASVC` | `ASVC1` = Application Service 1 |
| `⊞` | Rectangle | «Application Component» | `ACMP` | `ACMP1` = Application Component 1 |
| `⬭` | Stadium (yellow) | «Business Service» — context, from [layer 2](../2_business/2_business-services.md) | `BSVC` | `BSVC1` = Business Service 1 |

**The glyph rides on every node; the «stereotype» word appears once.**

## `ASVC1` — Guidance publishing

```mermaid
flowchart TB
  bsvc1(["⬭ «Business Service» BSVC1<br>EA-first method guidance"]):::business
  asvc1(["⬮ «Application Service» ASVC1<br>Guidance publishing"]):::appservice

  acmp1["⊞ «Application Component» ACMP1<br>Landing page"]:::component
  acmp2["⊞ ACMP2<br>Setup page"]:::component
  acmp3["⊞ ACMP3<br>Guide page"]:::component
  acmp4["⊞ ACMP4<br>Walkthrough page"]:::component
  acmp5["⊞ ACMP5<br>Architecture page"]:::component
  acmp6["⊞ ACMP6<br>Shared stylesheet"]:::component

  acmp1 --> asvc1
  acmp2 --> asvc1
  acmp3 --> asvc1
  acmp4 --> asvc1
  acmp5 --> asvc1
  acmp6 --> acmp1
  acmp6 --> acmp2
  acmp6 --> acmp3
  acmp6 --> acmp4
  acmp6 --> acmp5
  asvc1 --> bsvc1

  classDef business fill:#fffbb5,stroke:#b8a200,color:#333
  classDef appservice fill:#c2f0ff,stroke:#2a8fb0,color:#333
  classDef component fill:#9adcf0,stroke:#1a6f8c,color:#333
```

Page edges read **realizes**; `ACMP6`'s read **serves**. **`ACMP6` is the
only shared component and it is a stylesheet** — which is the whole coupling
story of this application. Change it and every page changes; change any
page and nothing else moves.

| ID | Application service | Realizes | Provided by |
| -- | ------------------- | -------- | ----------- |
| `ASVC1` | **Guidance publishing** — the pages, served statically, in two language editions | `BSVC1`, the [EA-first method guidance](../2_business/2_business-services.md) business service | `ACMP1`–`ACMP6` |

Provided by six components:

| ID | Component | Realizes | Source file |
| -- | --------- | -------- | ----------- |
| `ACMP1` | **Landing page** | Entry point: states the one rule, the Requester → Agent → Reviewer loop, links onward | [`public/index.html`](../../../public/index.html) |
| `ACMP2` | **Setup page** | A beginner's zero-to-first-change setup guide: create a GitHub account, copy the template, pick an AI agent (free-first, no editor install) | [`public/start.html`](../../../public/start.html) |
| `ACMP3` | **Guide page** | Reference for the EA-first process and the human/AI/hybrid actor notation | [`public/guide.html`](../../../public/guide.html) |
| `ACMP4` | **Walkthrough page** | One requirement climbing the layers end to end (Requester vs. Agent at each step), plus dedicated coverage of the situational `stack-selection` and `story-sharding` skills | [`public/walkthrough.html`](../../../public/walkthrough.html) |
| `ACMP5` | **Architecture page** | Renders this project's own filled EA layers as the concrete "what finished looks like" example | [`public/architecture.html`](../../../public/architecture.html) |
| `ACMP6` | **Shared stylesheet** | The self-contained CSS diagram components (`archi-*`, `node`, the `loop` and `ladder`) that render this project's ArchiMate diagrams without a diagramming library | [`public/styles.css`](../../../public/styles.css) |


Each component ships in **two language editions**: the English page listed
above and a Spanish edition with the same filename under
[`public/es/`](../../../public/es/index.html) (`G4`,
[1_strategy/1_motivation.md](../1_strategy/1_motivation.md)). The Spanish
edition mirrors its English counterpart's structure, element `id`s, and
source links, and every page's header carries an EN ⇄ ES switcher linking
the two editions of the same page; `<link rel="alternate" hreflang>` tags
declare the pairing to search engines. See
[3_information/1_data-objects.md](../3_information/1_data-objects.md) for
which edition wins when they disagree.

All ten pages share `ACMP6`. None of the pages build or fetch anything at request
time — no external scripts, fonts, or stylesheets — so deployment is a
direct copy of `public/` (see
[5_technology/2_deployment.md](../5_technology/README.md)). The site's
diagrams are a *derived* rendering of the canonical Mermaid diagrams in
`docs/ea/`; the choice to render them in CSS rather than load a library is
recorded in
[decision 2 — how the site renders its diagrams](../../decisions/2_site-diagram-rendering.md).
