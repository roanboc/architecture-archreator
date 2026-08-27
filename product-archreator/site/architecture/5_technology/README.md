# Technology Layer

_[← EA home](../README.md)_

The runtimes, tooling, and infrastructure that the
[application layer](../4_application/README.md) executes on.

## Analysis order

Files are numbered in the order they are analyzed: first _which technology
services exist and what provides them_, then _how the built artifacts reach
their runtime nodes_.

| #   | Document                                               | Elements                                                          | Question it answers                       |
| --- | --------------------------------------------------------| --------------------------------------------------------------------| --------------------------------------------- |
| 1   | [1_technology-services.md](./1_technology-services.md) | Technology Services and the nodes/system software providing them | What infrastructure services are used?    |
| 2   | [2_deployment.md](./2_deployment.md)                   | Nodes, Artifacts, and the CI/CD deployment pipeline               | How does the build get to where it runs?  |

If no stack has been chosen yet — typical the first time this layer is
assessed for a new small project — use the `stack-selection` skill for a
decision framework and concrete defaults (static hosting vs. Supabase +
Vercel, etc.) before writing [1_technology-services.md](./1_technology-services.md).

## Layer view

```mermaid
flowchart LR
  node2["⬒ GitHub Actions [NODE2]"]:::technology
  node1["⬒ GitHub Pages [NODE1]"]:::technology
  art1[/"⎔ The site directory [ART1]"/]:::technology

  node2 -->|uploads| art1
  art1 -->|deployed on| node1

  classDef technology fill:#c9e7b7,stroke:#558b2f,color:#333
```

**The only edge is a deployment.** It happens when something merges, never
while anyone is reading — at request time the two nodes have nothing to do
with each other.

### Relationships

<!-- Transcribed from this document's diagrams. The identifier is
     authoritative; the description beside it is checked against the
     catalogue that defines the element. -->

| From | From element | To | To element | Relationship |
| ---- | ------------ | -- | ---------- | ------------ |
| `NODE2` | «Node» GitHub Actions | `ART1` | «Artifact» The site directory | uploads |
