# Federation

_[← Front door](./README.md)_

```mermaid
flowchart LR
  subgraph parent["ORG · org-archreator — Depth 2, Organization"]
    p1(["◍ «Stakeholder» the segments, seen from outside a project [ORG.CS#, ORG.STK#]"]):::pstake
    p2{{"✳ «Driver» the general pressure [ORG.DRV#]"}}:::pdriver
    p3("◎ «Goal» what the organization must achieve [ORG.G#]"):::pgoal
  end

  subgraph child["PRD_MTD · product-archreator — Depth 1, Application"]
    c1(["◍ «Stakeholder» the same person, inside one adopting project [STK#]"]):::stake
    c2{{"✳ «Driver» the pressure sharpened for this product [DRV#]"}}:::driver
    c3("◎ «Goal» what the method must achieve [G#]"):::goal
  end

  c1 -->|refines| p1
  c2 -->|sharpens| p2
  c3 -->|serves| p3

  classDef pstake fill:#f4ecfc,stroke:#9575cd,color:#333
  classDef pdriver fill:#e6d6f5,stroke:#8e63c8,color:#333
  classDef pgoal fill:#c6aae9,stroke:#6f4bb2,color:#333
  classDef stake fill:#f4ecfc,stroke:#9575cd,color:#333
  classDef driver fill:#e6d6f5,stroke:#8e63c8,color:#333
  classDef goal fill:#c6aae9,stroke:#6f4bb2,color:#333
```

**Every arrow points the same way, and that is the contract.** The models
this one cites, each by its **federation ID** — the short uppercase code the
model declares on its own front door. The ID leads a qualified reference —
`ORG.G#` — and resolves against that model's own definitions, because both
live in this repository. Three kinds of element cross the boundary and no
others: a stakeholder refines a segment, a driver sharpens a driver, a goal
serves a goal.

| ID | Model | Level | Where | Relationship |
| -- | ----- | ----- | ----- | ------------ |
| `ORG` | `org-archreator` | Organization | [`../../org-archreator/architecture/`](../../org-archreator/architecture/README.md) | The organization that publishes this product; the product's goals serve its goals |

Read by position: cell 1 the federation ID, cell 2 the model's key — its
tree name, backticked.

References run one way: this model cites the organization's elements, never
the reverse — a new product needs to know its parent, and the parent needs
to know nothing about it.
