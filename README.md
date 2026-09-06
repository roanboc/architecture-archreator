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

## Working locally

The two validators need nothing but Python. The reading tools live in the
[archreator](https://github.com/roanboc/archreator) plugin and read a tree
through `--project`, so the `Makefile` carries one target for each and fetches
the plugin under gitignored `.archreator/method/` — nothing has to be
installed to try them:

| Target | Does |
| ------ | ---- |
| `make check` | The two validators, exactly as CI runs them |
| `make method` | Fetches the method, or refreshes it; `METHOD_REF=<branch or tag>` pins it |
| `make sync` | Fails when a validator here differs from the scaffold's copy, byte for byte |
| `make trace E=ACMP4` · `make coverage` · `make inventory` · `make export` | The model reader — `trace` on tree `P` (default `product-archreator`), the other three over every tree |
| `make brief E=BSVC1 F=impact` | One disposable brief, under `<tree>/.archreator/work/briefs/` |
| `make portal` · `make serve` | The tree as a MkDocs site, built or served from `<tree>/.archreator/work/portal/`; needs `uv` |
| `make smoke` | All of the above, non-interactively, over both trees; run it before pushing |

`make` and `uv` are all the bench asks for beyond Python. On Windows, run it
from Git Bash or WSL, or paste the command a target prints.
