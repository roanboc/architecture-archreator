# Information domains and objects

_[← Information layer](./README.md) · [Front door](../README.md)_

**ArchiMate viewpoint:** Information — Data Object. A domain is the level-1
row of the catalogue; its objects extend the identifier, so the hierarchy is
readable from the ID and no new element kind is needed.

**Status:** ◐ Draft catalogue — not yet approved at a gate. **Understanding**
covers this document.

## How to read this document

```mermaid
flowchart LR
  dobj["▦ «Data Object» what is known [DOBJ#, DOBJ#.# per level]"]:::info
  act(["⚇ «Business Actor» who owns a domain outright — defined in the business layer [ACT#]"]):::business
  role["⚉ «Business Role» the hat it is owned under — defined there too [ROLE#]"]:::role

  act -->|owns| dobj
  role -->|owns| dobj

  classDef info fill:#c2f0ff,stroke:#0288d1,color:#333
  classDef business fill:#fffbb5,stroke:#c8c04a,color:#333
  classDef role fill:#f7f099,stroke:#b8ad3f,color:#333
```

## Level 1 — the domains

```mermaid
flowchart TB
  subgraph d1["▦ Engagement knowledge [DOBJ1]"]
    d11["▦ The client's model [DOBJ1.1]"]:::info
    d12["▦ Engagement notes [DOBJ1.2]"]:::info
  end
  subgraph d2["▦ The organization's own model [DOBJ2]"]
    d21["▦ The canvases and layer documents [DOBJ2.1]"]:::info
    d22["▦ The initiative records [DOBJ2.2]"]:::info
  end
  subgraph d3["▦ Method and guidance content [DOBJ3] — the product's"]
    d3note["Its objects are the product's to define"]:::ext
  end

  r2["⚉ Consultant [ROLE2]"]:::role
  a1(["⚇ The Requester [ACT1]"]):::business

  r2 -->|owns| d1
  a1 -->|owns| d2

  d12 -->|lessons flow into| d3
  d3 -->|shapes| d21

  classDef info fill:#c2f0ff,stroke:#0288d1,color:#333
  classDef business fill:#fffbb5,stroke:#c8c04a,color:#333
  classDef role fill:#f7f099,stroke:#b8ad3f,color:#333
  classDef ext fill:#e8f7fd,stroke:#0288d1,color:#333,stroke-dasharray: 4 3
```

**Two owners, and the third domain has neither of them.** What the
organization masters it owns outright; what it uses most — the method
itself — belongs to the product, and the loop closes anyway: engagement
notes leave this tree, become method, and come back as the shape of the
model.

| ID | Domain | Owner | Mastered in |
| -- | ------ | ----- | ----------- |
| `DOBJ1` | **Engagement knowledge** — what working with a client produces and teaches | `ROLE2` | The client's own repository for their model; this repository for what the method learns |
| `DOBJ2` | **The organization's own model** — what this tree says about the organization | `ACT1` | This repository |
| `DOBJ3` | **Method and guidance content** — what the method is made of | The product — [its information layer](../../../product-archreator/architecture/3_information/1_data-domains-and-objects.md) models it in full | The archreator repository |

## Level 2 — the objects

Only the domains this organization masters decompose here; the product's
objects are the product's to define.

| ID | Object | Is | Classification |
| -- | ------ | -- | -------------- |
| `DOBJ1.1` | **The client's model** | The architecture the engagement builds, in the client's repository — theirs, referenced from here and never copied | The client's call |
| `DOBJ1.2` | **Engagement notes** | What the method did not cover, captured by `Capture what real use exposed [BPROC2.1]`; none exist yet — the first lands with the next retrospective | Internal |
| `DOBJ2.1` | **The canvases and layer documents** | The model proper — this tree | Public |
| `DOBJ2.2` | **The initiative records** | Scope documents and their Approvals tables — the durable trail of who approved what | Public |

## Relationships

The two edges the map draws between domains, which no catalogue row can
carry: a level-2 object feeding a domain the product owns, and that domain
shaping a level-2 object here.

| From | From element | To | To element | Relationship |
| ---- | ------------ | -- | ---------- | ------------ |
| `DOBJ1.2` | ▦ «Data Object» Engagement notes | `DOBJ3` | ▦ «Data Object» Method and guidance content | flows to |
| `DOBJ3` | ▦ «Data Object» Method and guidance content | `DOBJ2.1` | ▦ «Data Object» The canvases and layer documents | influences |

