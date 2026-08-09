# Deployment — the organization behind archreator

_[← Technology layer](./README.md) · [EA home](../README.md)_

**ArchiMate elements:** Artifact, Node.

How the built things reach where they run. There is very little pipeline,
and the reason is structural rather than immature.

## How to read this document

```mermaid
flowchart LR
  art[/"⎔ «Artifact»<br>what is produced"/]:::artifact
  node["⬒ «Node»<br>where it lands"]:::node
  tsvc(["⬯ «Technology Service»<br>what carries it"]):::techservice

  art -->|deployed on| node
  tsvc -->|serves| art

  classDef artifact fill:#dcefd0,stroke:#5a8a45,color:#333
  classDef node fill:#a9d68f,stroke:#4a7a35,color:#333
  classDef techservice fill:#c9e7b7,stroke:#5a8a45,color:#333
```

| Glyph | Shape | Element | ID prefix | Reads as |
| ----- | ----- | ------- | --------- | -------- |
| `⎔` | Parallelogram | «Artifact» | `ART` | `ART1` = Artifact 1 |
| `⬒` | Rectangle | «Node» — from [1_technology-services.md](./1_technology-services.md) | `NODE` | `NODE1` = Node 1 |
| `⬯` | Stadium | «Technology Service» — same document | `TSVC` | `TSVC1` = Technology Service 1 |

**The glyph rides on every node; the «stereotype» word appears once.**

## What gets deployed, and to where

```mermaid
flowchart LR
  art1[/"⎔ «Artifact» ART1<br>The repository at a commit"/]:::artifact
  art2[/"⎔ ART2<br>The published site"/]:::artifact
  art3[/"⎔ ART3<br>The plugin, as the manifest resolves it"/]:::artifact

  node1["⬒ «Node» NODE1<br>GitHub"]:::node
  node2["⬒ NODE2<br>The adopter's machine"]:::adopter

  art1 --> node1
  art2 --> node1
  art3 --> node2
  art1 -->|cloned as| node2

  classDef artifact fill:#dcefd0,stroke:#5a8a45,color:#333
  classDef node fill:#a9d68f,stroke:#4a7a35,color:#333
  classDef adopter fill:#c9e7b7,stroke:#5a8a45,color:#333
```

| ID | Artifact | Produced by | Deployed on | How it gets there |
| -- | -------- | ----------- | ----------- | ----------------- |
| `ART1` | **The repository at a commit** — the method, the scaffold and the validators as text | A merge to the default branch | `NODE1`, and `NODE2` on clone | `git push`; the adopter pulls |
| `ART2` | **The published site** — `ACMP2`'s pages | The Pages workflow | `NODE1` | Automatic on merge |
| `ART3` | **The plugin, as the manifest resolves it** | Nothing — the manifest points at the repository | `NODE2` | `/plugin install`, then `/plugin update` |

## There is no build

`ART1` and `ART3` are **not compiled, bundled or versioned artifacts** —
they are the source, read where it lies. `ART2` is the only thing produced
by a process, and that process copies static files.

The whole deployment story is therefore: merge to the default branch, and
the three artifacts are current. What passes for release engineering here is
`TSVC2`, the continuous checks, which run `ACMP3` and stop a merge that would
leave the model inconsistent.

**That is a consequence of `P2`** — everything in the repository, as text. A
method distributed as source has no packaging step to get wrong, and the
cost is that there is no version boundary either: an adopter who pulls gets
whatever the default branch says today. Nobody has needed more than that, and
the moment someone does, this document is where it would be recorded.

`COA2` would introduce the first real deployment: `NODE4` needs something
built, shipped and rolled back.
