# architecture-archreator

The worked models of the [archreator](https://github.com/roanboc/archreator)
method — the method applied to its own organization and to itself as a
product, so a prospective adopter can read a filled-in model rather than an
empty scaffold.

```mermaid
flowchart LR
  method["⊞ archreator — the method: skills, scaffold, validators"]:::ext

  subgraph repo["This repository — the worked models"]
    org(["◍ org-archreator — the organization, Depth 2"]):::org
    prod(["◍ product-archreator — the method as a product, Depth 1"]):::prod
    scripts["⊞ scripts/ — two validators and the parse they share"]:::tool
  end

  method -->|installed as a plugin, writes| org
  method -->|and| prod
  prod -->|cites, one way only| org
  scripts -->|checks both on every change| org
  scripts -->|and| prod
  prod -->|describes| method

  classDef ext fill:#9adcf0,stroke:#0277bd,color:#333
  classDef org fill:#f5deaa,stroke:#c8a24a,color:#333
  classDef prod fill:#efe57d,stroke:#b8ad3f,color:#333
  classDef tool fill:#a9d68f,stroke:#558b2f,color:#333
```

| Tree | Subject |
| ---- | ------- |
| [`org-archreator/`](./org-archreator/architecture/README.md) | The organization that publishes archreator |
| [`product-archreator/`](./product-archreator/architecture/README.md) | archreator the method, as a product |
| [`scripts/`](./scripts/README.md) | The two validators and the parse they share, one copy for both trees |

The models run on method 0.2. Start at either tree's
`architecture/README.md` — the front door says, per layer, what is modeled,
what is deliberately not, and how far each document has been validated.
Contributions follow [`CONTRIBUTING.md`](./CONTRIBUTING.md).
