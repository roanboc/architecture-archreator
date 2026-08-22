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
| 2   | `2_deployment.md`                   | Nodes, Artifacts, and the CI/CD deployment pipeline               | How does the build get to where it runs?  |

If no stack has been chosen yet — typical the first time this layer is
assessed for a new small project — use the `stack-selection` skill for a
decision framework and concrete defaults (static hosting vs. Supabase +
Vercel, etc.) before writing [1_technology-services.md](./1_technology-services.md).

## Layer view

Four nodes, none of them operated by the organization, and no edge between
any of them.

```mermaid
flowchart LR
  node1["⬒ Git hosting [NODE1]"]:::node
  node2["⬒ Continuous integration [NODE2]"]:::node
  node3["⬒ Static hosting [NODE3]"]:::node
  node4["⬒ The agent host platform [NODE4]"]:::node

  tsvc1(["⬯ Version control and review [TSVC1]"]):::technology
  tsvc2(["⬯ Checks on every change [TSVC2]"]):::technology
  tsvc3(["⬯ Public page delivery [TSVC3]"]):::technology
  tsvc4(["⬯ Skill execution [TSVC4]"]):::technology

  node1 -->|provides| tsvc1
  node2 -->|provides| tsvc2
  node3 -->|provides| tsvc3
  node4 -->|provides| tsvc4

  classDef node fill:#a9d68f,stroke:#4a7a35,color:#333
  classDef technology fill:#c9e7b7,stroke:#5a8a45,color:#333
```

**The absence of edges is the finding.** Nothing calls anything else at
request time, because nothing runs between requests — there are no requests.
That is what makes this layer four rows rather than a topology, and it is the
"no backend" case stated in full in
[1_technology-services.md](./1_technology-services.md).
