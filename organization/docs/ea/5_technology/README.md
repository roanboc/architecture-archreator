# Technology Layer — the organization behind archreator

_[← EA home](../README.md)_

The infrastructure this organization uses, and the fact that it operates none
of it.

## Analysis order

| # | Document | Elements | Question it answers | State |
| - | -------- | -------- | ------------------- | ----- |
| 1 | [1_technology-services.md](./1_technology-services.md) | Technology Services and the Nodes providing them | What infrastructure is used? | **Filled** — 5 services, 4 nodes, one of them Pending |
| 2 | [2_deployment.md](./2_deployment.md) | Artifacts and how they reach their nodes | How does the build get to where it runs? | **Filled** — 3 artifacts, and no build |

No stack decision was needed here. The stack is git, a static host and a
continuous-integration runner, all on one platform's free tier, and it was
chosen before this layer was ever written down — see the
`stack-selection` skill for the framework a project without that history
would use.
