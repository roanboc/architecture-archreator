# Value Stream — the organization behind archreator

_[← Strategy layer](./README.md) · [EA home](../README.md)_

**ArchiMate elements:** Value Stream.

One stream, six stages, from a stakeholder who has never heard of the method
to value returning to the organization. Derived from the key activities
(`KA1`–`KA4`) and channels (`CH1`–`CH5`) on the
[business model canvas](../0_business-design/2_business-model-canvas.md).

## How to read this document

```mermaid
flowchart LR
  s1[["«Value Stream» stage<br>a step in the flow"]]:::stage
  s2[["the next step"]]:::stage
  cap["«Capability»<br>what makes the step possible"]:::capability
  bif["«Business Interface»<br>where the stakeholder<br>meets it"]:::interface

  s1 -->|triggers| s2
  cap -->|serves| s1
  bif -->|serves| s1

  classDef stage fill:#eed4a0,stroke:#c8a24a,color:#333
  classDef capability fill:#f5deaa,stroke:#c8a24a,color:#333
  classDef interface fill:#fffbb5,stroke:#b8a200,color:#333
```

A value stream is a sequence of **stages**, each one a step that moves the
stakeholder closer to the value. Stages are served by capabilities — what the
organization must be able to do at that point — and, at the ends, by the
interfaces the stakeholder actually touches.

| Shape | Element | ID prefix | Reads as |
| ----- | ------- | --------- | -------- |
| Rectangle with double bars | «Value Stream» stage | `VS` | `VS1` = Value Stream 1; its stages are numbered inside it |
| Rectangle | «Capability» — context, from [2_capabilities-and-resources.md](./2_capabilities-and-resources.md) | `CAP` | `CAP1` = Capability 1 |
| Rectangle (yellow) | «Business Interface» — context, from [the business layer](../2_business/2_business-services.md) | `BIF` | `BIF1` = Business Interface 1 |

Stages carry a slightly deeper sand than capabilities, so the flow reads as
one band and the things serving it as another. Business interfaces keep the
Business yellow they have in their own layer.

**The «stereotype» label appears on the first node of each type in a
diagram** and is dropped on the rest; the legend carries it for the whole
document.

## The stream

```mermaid
flowchart LR
  s1[["«Value Stream» stage<br>1 Reach"]]:::stage
  s2[["2 Frame"]]:::stage
  s3[["3 Approve"]]:::stage
  s4[["4 Model"]]:::stage
  s5[["5 Build"]]:::stage
  s6[["6 Feed back"]]:::stage

  s1 -->|triggers| s2
  s2 -->|triggers| s3
  s3 -->|triggers| s4
  s4 -->|triggers| s5
  s5 -->|triggers| s6
  s6 -.->|flow: a better method| s2

  classDef stage fill:#eed4a0,stroke:#c8a24a,color:#333
```

**The stream closes**, which is the one thing worth seeing before the detail:
stage 6 returns to stage 2 as a better method. That loop is `RS1` (Revenue
Stream 1 — continuous improvement) drawn as a flow rather than listed as a
table row. It is also the reason `PROD1` is free — a closed loop needs volume
through it, and a price on the open method would throttle the only
non-monetary return this organization has.

| ID | Value stream | Stages |
| -- | ------------ | ------ |
| `VS1` | **From first contact to a delivered outcome, and back** | Six, below — the sixth returns to the second |

## What serves each stage

```mermaid
flowchart TB
  bif1["«Business Interface»<br>BIF1–BIF3 Repository,<br>site, marketplace"]:::interface
  bif4["BIF4 Referral and<br>direct approach"]:::interface

  s1[["«Value Stream» stage<br>1 Reach"]]:::stage
  s2[["2 Frame"]]:::stage
  s3[["3 Approve"]]:::stage
  s4[["4 Model"]]:::stage
  s5[["5 Build"]]:::stage
  s6[["6 Feed back"]]:::stage

  cap1["«Capability»<br>CAP1 Gated<br>discovery"]:::capability
  cap2["CAP2 Design-to-delivery<br>continuity"]:::capability
  cap3["CAP3 One documented<br>model"]:::capability
  cap4["CAP4 A shared<br>architectural language"]:::capability
  cap5["CAP5 Method-carried<br>competence"]:::capability
  cap6["CAP6 Layered change<br>absorption"]:::capability

  bif1 --> s1
  bif4 --> s1
  cap1 --> s2
  cap1 --> s3
  cap3 --> s4
  cap4 --> s4
  cap2 --> s5
  cap5 --> s5
  cap6 --> s6

  s1 --> s2 --> s3 --> s4 --> s5 --> s6

  classDef stage fill:#eed4a0,stroke:#c8a24a,color:#333
  classDef capability fill:#f5deaa,stroke:#c8a24a,color:#333
  classDef interface fill:#fffbb5,stroke:#b8a200,color:#333
```

Every capability and interface edge reads **serves**.

| # | Stage | What happens | Capability | Reached through |
| - | ----- | ------------ | ---------- | --------------- |
| 1 | **Reach** | Someone finds the method, or the Requester is approached directly | — | `CH1` the repository, `CH2` the site, `CH3` the plugin marketplace, `CH4` referral |
| 2 | **Frame** | Discovery: the business model and strategy are drawn out by questions, and the frame is tested rather than recorded | `CAP1` | `KA1`, `KA3` |
| 3 | **Approve** | The Requester of that project grants the gate, against documents they were given links to | `CAP1` | `KA1`, `KA3` |
| 4 | **Model** | The layers are derived from what was approved, in one place, in one language | `CAP3`, `CAP4` | `KA1` |
| 5 | **Build** | The approved design is what an agent implements from | `CAP2`, `CAP5` | `KA3` |
| 6 | **Feed back** | Real use exposes what the method gets wrong, and the method changes | `CAP6` | `KA1`, `KA2` |

**Stage 1 is the only stage no capability serves.** Being found is not
something this organization is currently able to do — it is something that
happens to it. That is visible in the diagram as two interfaces feeding a
stage with nothing above it, and it is the gap the next section is about.

## Where the stream is weak

```mermaid
flowchart TB
  s1[["«Value Stream» stage<br>1 Reach"]]:::stage
  s6[["6 Feed back"]]:::stage

  bif5["«Business Interface»<br>BIF5 The web, self-serve<br>— Pending"]:::interface

  coa2{{"«Course of Action»<br>COA2 Build the portal"}}:::action
  coa3{{"COA3 Instrument the<br>adoption measure"}}:::action

  res1[("«Resource»<br>RES1 The Requester's<br>knowledge and time")]:::resource

  coa2 -.->|would create| bif5
  bif5 -.->|would serve| s1
  coa3 -.->|would instrument| s6
  res1 -->|assigned to| s1
  res1 -->|assigned to| s6

  classDef stage fill:#eed4a0,stroke:#c8a24a,color:#333
  classDef interface fill:#fffbb5,stroke:#b8a200,color:#333
  classDef action fill:#d9ad5c,stroke:#8a6a2a,color:#333
  classDef resource fill:#faf0d5,stroke:#c8a24a,color:#333
```

Dashed edges are Pending; solid ones are true today. Three weaknesses, and
the diagram shows that two of them have a named response and one does not.

- **Stage 1 reaches only people already looking.** `CH1`–`CH3` cost nothing
  and find only those close to the tooling. `BIF5`, the interface that would
  change it, is Pending on `COA2`.
- **Stage 6 has no instrumentation.** Feedback arrives if someone chooses to
  give it; nothing counts whether stage 5 was ever reached. That is `COA3`.
- **Stages 2–5 all draw on `RES1`.** For `PROD2` the Requester performs them
  personally; for `PROD1` an adopter performs them with an agent, but the
  method they follow is still authored by one person. **No course of action
  addresses this at the stream level** — `COA1` would, and it needs more AI
  maturity than exists today.
