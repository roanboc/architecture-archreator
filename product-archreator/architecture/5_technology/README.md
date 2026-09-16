# Technology

_[← Front door](../README.md)_

What runs it all, and where each part lives and deploys.

**ArchiMate viewpoint:** Technology: Node, Technology Service, Artifact.

## Documents

| # | Document | Elements | Question it answers |
| - | -------- | -------- | ------------------- |
| 1 | [Technology and deployment](./1_technology-and-deployment.md) | Five nodes, none of them operated by the organization, five services, one artifact and the path a merged change takes | What runs it all, and how does a change reach where it runs? |

## Metamodel

```mermaid
flowchart LR
  %% legend
  node["⬒ «Node» what runs it [NODE#]"]:::tech
  other["⬒ «Node» another node it triggers or serves [NODE#]"]:::tech
  tsvc(["⬯ «Technology Service» what it provides [TSVC#]"]):::tsvc
  art[/"⎔ «Artifact» what is deployed onto it [ART#]"/]:::art
  dobj["▦ «Data Object» what a run writes and throws away, from the information layer [DOBJ#.#]"]:::info

  node -->|provides| tsvc
  art -->|deployed to| node
  node -->|triggers| other
  node -->|accesses| dobj

  classDef tech fill:#a9d68f,stroke:#558b2f,color:#333
  classDef tsvc fill:#c9e7b7,stroke:#558b2f,color:#333
  classDef art fill:#dcefd0,stroke:#7aa860,color:#333
  classDef info fill:#c2f0ff,stroke:#0288d1,color:#333
```

Green is technology; the data object is a visitor from the information layer
and keeps its cyan.

## Layer view

```mermaid
flowchart LR
  n1["⬒ Git hosting, GitHub today [NODE1]"]:::tech
  n2["⬒ Continuous integration [NODE2]"]:::tech
  n3["⬒ Static hosting [NODE3]"]:::tech
  n4["⬒ The agent host platform [NODE4]"]:::tech
  n5["⬒ The Python runtime [NODE5]"]:::tech
  a1[/"⎔ The installable plugin [ART1]"/]:::art
  t4(["⬯ Skill execution [TSVC4]"]):::tsvc

  n1 -->|triggers| n2
  n1 -->|flows to| n3
  n1 -->|flows to| a1
  a1 -->|deployed to| n4
  n5 -->|serves| n2
  n5 -->|serves| n4
  n4 -->|provides| t4

  classDef tech fill:#a9d68f,stroke:#558b2f,color:#333
  classDef tsvc fill:#c9e7b7,stroke:#558b2f,color:#333
  classDef art fill:#dcefd0,stroke:#7aa860,color:#333
  classDef info fill:#c2f0ff,stroke:#0288d1,color:#333
```

A merge fans out to the checks, the site and the plugin an adopter installs;
the Python runtime serves the checks and the agent host, and nothing calls
anything else.
