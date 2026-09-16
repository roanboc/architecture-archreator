# Information

_[← Front door](../README.md)_

What information exists, who owns it, and where it lives.

**ArchiMate viewpoint:** Information: Data Object, with the domain as its
level 1 and the object as its level 2.

## Documents

| # | Document | Elements | Question it answers |
| - | -------- | -------- | ------------------- |
| 1 | [Data domains and objects](./1_data-domains-and-objects.md) | The three domains and their owners, and the objects inside each | What information exists, who owns it, and where does it live? |

## Metamodel

```mermaid
flowchart LR
  %% legend
  domain["▦ «Data Object» a domain, who owns this information [DOBJ#]"]:::domain
  other["▦ «Data Object» another domain it shapes or flows to [DOBJ#]"]:::domain
  obj["▦ «Data Object» what exists inside a domain [DOBJ#.#]"]:::info
  node["⬒ «Node» what writes or reads it, from the technology layer [NODE#]"]:::tech

  domain -->|composed of| obj
  domain -->|influences| other
  node -->|accesses| obj

  classDef info fill:#c2f0ff,stroke:#0288d1,color:#333
  classDef domain fill:#9adcf0,stroke:#0277bd,color:#333
  classDef business fill:#fffbb5,stroke:#c8c04a,color:#333
  classDef role fill:#f7f099,stroke:#b8ad3f,color:#333
  classDef ext fill:#e8f7fd,stroke:#0288d1,color:#333,stroke-dasharray: 4 3
  classDef tech fill:#a9d68f,stroke:#558b2f,color:#333
```

The darker cyan marks a domain; the node is a visitor from the technology
layer and keeps its green.

## Layer view

```mermaid
flowchart LR
  d1["▦ Method content [DOBJ1]"]:::domain
  d2["▦ Project models [DOBJ2]"]:::domain
  d3["▦ Generated output [DOBJ3]"]:::domain
  d31["▦ Briefs and portal builds [DOBJ3.1]"]:::info
  n5["⬒ The Python runtime [NODE5]"]:::tech

  d1 -->|influences| d2
  d2 -->|flows to| d3
  d3 -->|composed of| d31
  n5 -->|accesses| d31

  classDef info fill:#c2f0ff,stroke:#0288d1,color:#333
  classDef domain fill:#9adcf0,stroke:#0277bd,color:#333
  classDef business fill:#fffbb5,stroke:#c8c04a,color:#333
  classDef role fill:#f7f099,stroke:#b8ad3f,color:#333
  classDef ext fill:#e8f7fd,stroke:#0288d1,color:#333,stroke-dasharray: 4 3
  classDef tech fill:#a9d68f,stroke:#558b2f,color:#333
```

Method content shapes project models, project models are read fresh into
generated output, and only the first two are ever a source of truth.
