# Information

_[← Front door](../README.md)_

What the organization knows, who owns each part, and where it lives.

**ArchiMate viewpoint:** Information: Data Object, with the domain as its
level 1 and the object as its level 2.

## Documents

| # | Document | Elements | Question it answers |
| - | -------- | -------- | ------------------- |
| 1 | [Information domains and objects](./1_information-domains-and-objects.md) | The two domains the organization masters, the one it defers to the product, and the objects inside each | What does the organization know, who owns it, and where does it live? |

## Metamodel

```mermaid
flowchart LR
  %% legend
  domain["▦ «Data Object» a domain, who owns this information [DOBJ#]"]:::domain
  obj["▦ «Data Object» what is known inside it [DOBJ#.#]"]:::info
  act(["⚇ «Business Actor» who owns a domain outright, from the business layer [ACT#]"]):::business
  role["⚉ «Business Role» the hat it is owned under, from the business layer [ROLE#]"]:::role

  act -->|owns| domain
  role -->|owns| domain
  domain -->|composed of| obj
  obj -->|flows to| domain

  classDef info fill:#c2f0ff,stroke:#0288d1,color:#333
  classDef domain fill:#9adcf0,stroke:#0277bd,color:#333
  classDef business fill:#fffbb5,stroke:#c8c04a,color:#333
  classDef role fill:#f7f099,stroke:#b8ad3f,color:#333
  classDef ext fill:#e8f7fd,stroke:#0288d1,color:#333,stroke-dasharray: 4 3
```

The actor and the role are visitors from the business layer and keep their
yellow; the darker cyan marks a domain, and a dashed box is a domain the
product owns.

## Layer view

```mermaid
flowchart TB
  subgraph d1["▦ Engagement knowledge [DOBJ1]"]
    d12["▦ Engagement notes [DOBJ1.2]"]:::info
  end
  subgraph d2["▦ The organization's own model [DOBJ2]"]
    d21["▦ The canvases and layer documents [DOBJ2.1]"]:::info
  end
  d3["▦ Method and guidance content, the product's [DOBJ3]"]:::ext
  r2["⚉ Consultant [ROLE2]"]:::role
  a1(["⚇ The Requester [ACT1]"]):::business

  r2 -->|owns| d1
  a1 -->|owns| d2
  d12 -->|flows to| d3
  d3 -->|influences| d21

  classDef info fill:#c2f0ff,stroke:#0288d1,color:#333
  classDef domain fill:#9adcf0,stroke:#0277bd,color:#333
  classDef business fill:#fffbb5,stroke:#c8c04a,color:#333
  classDef role fill:#f7f099,stroke:#b8ad3f,color:#333
  classDef ext fill:#e8f7fd,stroke:#0288d1,color:#333,stroke-dasharray: 4 3
```

What the organization masters it owns outright. What it uses most, the method
itself, belongs to the product, and the loop closes anyway: engagement notes
become method and come back as the shape of the organization's own model.
