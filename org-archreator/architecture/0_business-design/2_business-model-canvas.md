# Business model canvas

_[← Business design](./README.md) · [Front door](../README.md)_

**Not an ArchiMate layer.** How the organization around
[archreator, the open method [PROD1]](./1_value-proposition-canvas.md) and
[Consulting [PROD2]](./1_value-proposition-canvas.md) actually operates and
pays for itself.

**Status:** ◐ Draft catalogue — rebuilt on method 0.2 from the validated
pre-0.2 canvas, not yet re-approved. **Direction** covers this layer.

## The nine blocks

```mermaid
flowchart TB
  subgraph left[" "]
    kp["⧉ AI model providers [KP1] · The code host [KP2]"]:::block
    ka{{"⚙ Improve the method [KA1] · Publish guidance [KA2] · Deliver with clients [KA3]"}}:::block
    kr[("▤ The Requester's knowledge and time [KR1] · The method [KR2] · The guidance site [KR3]")]:::block
  end
  subgraph mid[" "]
    vp["▣ archreator, the open method [PROD1] · Consulting [PROD2]"]:::vp
  end
  subgraph right[" "]
    cr[["⇄ Self-service [CR1] · Personal and direct [CR2]"]]:::block
    ch["⊸ Repository [CH1] · Guidance site [CH2] · Plugin marketplace [CH3] · Referral [CH4]"]:::block
    cs(["◍ Independent builder [CS1] · Enterprise architect [CS2] · Business owner [CS3]"]):::block
  end
  cost[/"▼ Requester's time [COST1] · AI inference [COST2] · Hosting [COST3]"\]:::cost
  rs[\"▲ Continuous improvement [RS1] · Mission progress [RS2] · Consulting fees [RS3]"/]:::rs

  left --- mid --- right
  cost --- rs

  classDef block fill:#fffbb5,stroke:#c8c04a,color:#333
  classDef vp fill:#efe57d,stroke:#b8ad3f,color:#333
  classDef cost fill:#ffd6d6,stroke:#d99b9b,color:#333
  classDef rs fill:#c9e7b7,stroke:#558b2f,color:#333
```

A compact view of the tables below, in the traditional arrangement. The
tables are the source; resolve any mismatch in their favour.

## Channels

| ID | Channel | Carries | Reaches | State |
| -- | ------- | ------- | ------- | ----- |
| `CH1` | The public repository | `PROD1` | `CS1`, `CS2` — they find it as code, not as marketing | Live |
| `CH2` | The guidance site | `PROD1` | `CS1`, `CS2`, and any owner evaluating the method | Live |
| `CH3` | The plugin marketplace | `PROD1` | `CS1`, `CS2`, already working inside an agent | Live |
| `CH4` | Referral and direct approach | `PROD2` | `CS3` | Live |

## Customer relationships

| ID | Relationship | For | Costs |
| -- | ------------ | --- | ----- |
| `CR1` | Self-service | `PROD1` | Near zero per user |
| `CR2` | Personal and direct — the Requester individually | `PROD2` | Their whole available time |

## Key activities

| ID | Activity | For | Performed by |
| -- | -------- | --- | ------------ |
| `KA1` | Developing and improving the method | `PROD1` | The Requester, with an AI agent at co-pilot autonomy |
| `KA2` | Publishing guidance | `PROD1` | The Requester, with an AI agent |
| `KA3` | Running discovery and delivery with clients | `PROD2` | The Requester |

## Key resources

| ID | Resource | Kind | State |
| -- | -------- | ---- | ----- |
| `KR1` | The Requester's knowledge and time | People | **Constrained — the binding limit on the whole organization** |
| `KR2` | The method: skills, conventions, gates | Knowledge | Held, and improving |
| `KR3` | The published guidance site | Asset | Held |

## Key partners

| ID | Partner | Provides | Note |
| -- | ------- | -------- | ---- |
| `KP1` | AI model providers | The inference every product ultimately runs on | **Substitutable by design.** The method is provider-agnostic prose; only the packaging names a platform |
| `KP2` | The code host | Repository, plugin distribution, site hosting | Replaceable, and free at this scale |

## Revenue streams and cost structure

| ID | Revenue stream | Kind | From | Note |
| -- | -------------- | ---- | ---- | ---- |
| `RS1` | **Continuous improvement** — feedback and real usage flowing back into the method | Non-monetary | `PROD1` | Grows with adoption; the method improves because people use it where the Requester is not |
| `RS2` | **Mission progress** — people building better things with AI while human knowledge improves rather than being delegated away | Non-monetary | `PROD1` | The reason the organization exists |
| `RS3` | Consulting fees | Monetary | `PROD2` | Hourly; bounded by one person's available time |

| ID | Cost | For | Note |
| -- | ---- | --- | ---- |
| `COST1` | **The Requester's time** | `PROD1`, `PROD2` | **Dominant, and the binding constraint on everything** |
| `COST2` | AI inference | `PROD1`, `PROD2` | Each adopter carries their own; the organization pays only for its own use |
| `COST3` | Hosting the repository and site | `PROD1` | Effectively zero — free tiers |

**The Requester appears three times** — a key resource, the dominant cost,
and a stakeholder with wants of their own. That triple entry is the
organization's central fact, not a modelling accident.

## From canvas to ArchiMate

Stated once, here; the [strategy layer](../1_strategy/README.md) cites it
per element rather than restating it.

| Canvas block | Becomes | In |
| ------------ | ------- | -- |
| Customer segment | «Stakeholder» | [Motivation](../1_strategy/1_motivation.md) |
| Pain | «Driver» and its «Assessment» | Motivation |
| Job, gain | «Goal» and its «Outcome» | Motivation |
| Key activity, pain reliever, gain creator | «Capability» | [Capabilities](../1_strategy/2_capabilities-and-value-stream.md) |
| Key resource | «Resource» | Capabilities |
| Channel, relationship | The service's access, on the business layer | [Business](../2_business/README.md) |
