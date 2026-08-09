# Value Stream

_[← Strategy layer](./README.md) · [EA home](../README.md)_

**ArchiMate elements:** Value Stream.

## How to read this document

```mermaid
flowchart LR
  s1[["⇉ «Value Stream» stage<br>a step toward adopting"]]:::stage
  s2[["⇉ the next step"]]:::stage
  acmp["⊞ «Application Component»<br>the page that realizes it"]:::component

  s1 -->|triggers| s2
  acmp -->|realizes| s1

  classDef stage fill:#eed4a0,stroke:#c8a24a,color:#333
  classDef component fill:#c2f0ff,stroke:#2a8fb0,color:#333
```

| Glyph | Shape | Element | ID prefix | Reads as |
| ----- | ----- | ------- | --------- | -------- |
| `⇉` | Rectangle, double bars | «Value Stream» stage | `VS` | `VS1` = Value Stream 1; its stages are numbered inside it |
| `⊞` | Rectangle (cyan) | «Application Component» — context, from [layer 4](../4_application/2_application-components.md) | `ACMP` | `ACMP1` = Application Component 1 |

**The glyph rides on every node; the «stereotype» word appears once.**

## The stream

```mermaid
flowchart LR
  s1[["⇉ «Value Stream» stage<br>1 Discover — lands on the site"]]:::stage
  s2[["⇉ 2 Understand — reads the method<br>and the actor-notation example"]]:::stage
  s3[["⇉ 3 Adopt — uses 'Use this template'"]]:::stage

  acmp1["⊞ «Application Component» ACMP1<br>Landing page"]:::component
  acmp3["⊞ ACMP3/ACMP4<br>Guide and walkthrough pages"]:::component
  acmp2["⊞ ACMP2/ACMP5<br>Setup and architecture pages"]:::component

  acmp1 --> s1
  acmp3 --> s2
  acmp2 --> s3

  s1 -->|triggers| s2
  s2 -->|triggers| s3

  classDef stage fill:#eed4a0,stroke:#c8a24a,color:#333
  classDef component fill:#c2f0ff,stroke:#2a8fb0,color:#333
```

Component edges read **realizes**. **The stream does not close.** Unlike the
organization's, nothing returns from Adopt to Discover — this site has no
feedback path, which is honest rather than an omission: it is five static
pages with no way for a reader to report anything back.

| ID | Value stream | Stages |
| -- | ------------ | ------ |
| `VS1` | **Discover → Understand → Adopt** | Three, below |

| # | Stage | Realized by |
| - | ----- | ----------- |
| 1 | **Discover** | [`public/index.html`](../../../public/index.html) — landing page, states the one rule and links onward |
| 2 | **Understand** | [`public/guide.html`](../../../public/guide.html) — the EA-first process and the human/AI/hybrid actor notation as reference — and [`public/walkthrough.html`](../../../public/walkthrough.html) — one requirement walked through the layers end to end, plus the situational skills |
| 3 | **Adopt** | [`public/start.html`](../../../public/start.html) — a beginner's zero-to-first-change setup guide (create an account, copy the template, pick an AI agent — free-first, no editor install), and [`public/architecture.html`](../../../public/architecture.html) — this project's own filled EA layers, as the concrete "what it looks like when finished," plus a direct link to the parent template's "Use this template" flow |

The stages are language-independent: each realizing page above also
ships a Spanish edition under [`public/es/`](../../../public/es/index.html)
(`G4`, [1_motivation.md](./1_motivation.md)), so a Spanish-speaking
visitor moves through the same three stages without switching language.

This value stream is realized end to end by `BSVC1`, the
[EA-first method guidance](../2_business/2_business-services.md) business
service.
