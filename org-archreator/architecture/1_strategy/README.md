# Strategy & Motivation Layer

_[← EA home](../README.md)_

The top-down business context: who has a stake in the project, why it
exists, which capabilities it needs, and the value stream it delivers. This
layer motivates everything below it — each capability is realized by
business services in the [business layer](../2_business/README.md).

**If [0_business-design/](../0_business-design/README.md) is filled in, this
layer is derived from it, not invented alongside it.** On the company track
the canvases come first and every element here traces back to a canvas
block — the `Source` column below says which. On the application track
layer 0 stays empty, the `Source` column is left blank, and this layer is
where discovery starts.

## Analysis order

Files are numbered in the order they are analyzed: first _who wants what
and why_, then _what we must be able to do_, and only then _how value
flows_.

| #   | Document                                                             | Elements                                                         | Question it answers                                | Source (company track)                             |
| --- | ---------------------------------------------------------------------| ------------------------------------------------------------------ | ---------------------------------------------------- | ---------------------------------------------------- |
| 1   | [1_motivation.md](./1_motivation.md)                                 | Stakeholders, Drivers, Assessments, Goals, Outcomes, Principles | Who cares, what pressures them, what must be true?  | Customer Segments, Jobs, Pains, Gains               |
| 2   | [2_capabilities-and-resources.md](./2_capabilities-and-resources.md) — capabilities split into a folder of one document per level once leveled | Capabilities, Resources, Courses of Action                      | What must we be able to do, and with what?          | Pain Relievers, Gain Creators, Key Resources, Key Activities |
| 3   | [3_value-stream.md](./3_value-stream.md)                             | Value Stream and its stage mapping                               | How does value flow end-to-end?                     | Key Activities, Channels                             |

The `Source` column names the canvas blocks each document is derived from;
the block-by-block element mapping lives in
[0_business-design/](../0_business-design/README.md#from-canvas-to-archimate)
and is not restated here. Principles are the exception — they have no canvas
block, and are discovered directly with the Requester in either track.

**Capabilities are leveled here** — three areas at level 1 and seven
capabilities at level 2, with identifiers that carry the level (`CAP1`, then
`CAP1.2`). **Nothing goes to a third level**, because no named pain justifies
one yet, and a branch left undetailed says so rather than looking forgotten.

The map was drafted against what the organization actually does and confirmed
item by item rather than recalled from a blank page. The
`process-and-capability-levels` skill holds the rule, the safeguard that keeps
a reference model a proposal rather than an answer, and the distinction that
keeps this document honest: capabilities are nouns, processes are verbs.

[1_motivation.md](./1_motivation.md) is where **Principles** live — the constraints that a
proposed change is checked against in step 1 of `align-change-through-layers` before
anything else. Keep them few, load-bearing, and testable (e.g. "role
determines access", not "be secure").

## Layer view

```mermaid
flowchart TB
  stakeholder(["◍ Established business owners [STK2]"]):::motivation
  driver{{"✳ Architectural expertise is priced out of reach [DRV4]"}}:::motivation
  goal("◎ Quality without scarce expertise [G4]"):::motivation

  vs[["⇉ Reach → Frame → Approve → Model → Build → Feed back [VS1]"]]:::strategy
  cap["✦ Delivery from design [CAP3]"]:::strategy
  res[("▤ The Requester's knowledge and time [RES1]")]:::strategy

  stakeholder -->|concerned with| driver
  driver -->|influences| goal
  goal -->|realized by| vs
  vs -->|requires| cap
  cap -->|uses| res

  classDef motivation fill:#e6d6f5,stroke:#7e57c2,color:#333
  classDef strategy fill:#f5deaa,stroke:#c8a24a,color:#333
```

A cross-layer view, so it uses the flat layer palette rather than the tone
ramps the single-layer documents use. Thirty-one motivation elements do not
fit one honest diagram; each section carries its own.

### Relationships

<!-- Transcribed from this document's diagrams. The identifier is
     authoritative; the description beside it is checked against the
     catalogue that defines the element. -->

| From | From element | To | To element | Relationship |
| ---- | ------------ | -- | ---------- | ------------ |
| `DRV4` | «Driver» Architectural expertise is priced out of reach | `G4` | «Goal» Architectural quality without scarce expertise | influences |
| `G4` | «Goal» Architectural quality without scarce expertise | `VS1` | «Value Stream» From first contact to a delivered outcome, and back | realized by |
| `VS1` | «Value Stream» From first contact to a delivered outcome, and back | `CAP3` | «Capability» Delivery from design | requires |
| `CAP3` | «Capability» Delivery from design | `RES1` | «Resource» The Requester's knowledge and time | uses |
