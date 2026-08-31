# Data domains and objects

_[← Information layer](./README.md) · [Front door](../README.md)_

**ArchiMate viewpoint:** Information — Data Object. A domain is the level-1
row of the same catalogue; its objects extend the identifier, so the
hierarchy is readable from the ID and no new element kind is needed.

**Status:** ◐ Draft catalogue — not yet approved at a gate. **Understanding**
covers this document.

## How to read this document

```mermaid
flowchart LR
  dobj["▦ «Data Object» a domain, or an object extending its ID [DOBJ#, DOBJ#.# per level]"]:::info

  classDef info fill:#c2f0ff,stroke:#0288d1,color:#333
```

## Level 1 — the domains

```mermaid
flowchart TB
  subgraph d1["▦ Method content [DOBJ1]"]
    d11["▦ The skill corpus [DOBJ1.1]"]:::info
    d12["▦ The process model [DOBJ1.2]"]:::info
    d13["▦ The scaffold and assets [DOBJ1.3]"]:::info
  end
  subgraph d2["▦ Project models [DOBJ2]"]
    d21["▦ Layer documents [DOBJ2.1]"]:::info
    d22["▦ Records [DOBJ2.2]"]:::info
  end
  subgraph d3["▦ Generated output [DOBJ3]"]
    d31["▦ Briefs and portal builds [DOBJ3.1]"]:::info
  end

  d1 -->|shapes| d2
  d2 -->|is read into| d3

  classDef info fill:#c2f0ff,stroke:#0288d1,color:#333
```

| ID | Domain | Owner | Mastered in |
| -- | ------ | ----- | ----------- |
| `DOBJ1` | **Method content** — what the method itself is made of | The method maintainer | The archreator repository |
| `DOBJ2` | **Project models** — what each adopting project knows about itself | Each adopting project's Requester | That project's repository, always |
| `DOBJ3` | **Generated output** — what the tools produce on request | Nobody — disposable by design | Nowhere: gitignored under `.archreator/`, regenerated fresh, never committed |

## Level 2 — the objects

| ID | Object | Is | Classification |
| -- | ------ | -- | -------------- |
| `DOBJ1.1` | The skill corpus | Eighteen skills and their references, one Markdown file each | Public |
| `DOBJ1.2` | The process model | The macro processes and their level-2 children, beside the skills that realize them | Public |
| `DOBJ1.3` | The scaffold and assets | The eleven files a project starts with, and the templates emitted when a skill first has content for them | Public |
| `DOBJ2.1` | Layer documents | The model proper — catalogues, relationship tables, diagrams, each declaring how far it is validated | The project's call |
| `DOBJ2.2` | Records | Scope documents, decisions, engagement notes — the durable trail of who approved what | The project's call |
| `DOBJ3.1` | Briefs and portal builds | One question answered, or the model rendered for a reader — stamped with the revision they came from and thrown away | Derived — never a source of truth |

**The whole layer in one sentence:** method content shapes project models,
project models are read fresh into generated output, and only the first two
are ever a source of truth.
