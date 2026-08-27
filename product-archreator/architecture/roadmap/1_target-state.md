# Target state

_[← Roadmap](./README.md) · [EA home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration. Where the model's
relationships are going, and what is missing between here and there.

**Status:** ● Validated at **Gate 1**, 2026-08-27 — the destination and the order,
approved as direction. It approves no work: every initiative below still stops at
its own Gate 2.

The method models the element and not the relationship. `BOBJ2` has an
identifier, a type, a level and a rule that it names what realizes it; the
relationship between two elements has none of that, and so it settled wherever
an author happened to write it. Today that is mostly inside a Mermaid diagram,
which is a **rendering** — and a fact whose only home is a rendering is a fact
`P1` says the method does not have.

Everything below is a consequence of that single omission. Nothing here
proposes a new capability: `CAP4` already exists to prove the model internally
consistent, and `G5` already commits the method to reaching readers who never
open a repository. What is missing is the relationship itself.

## How to read this document

```mermaid
flowchart LR
  plat[["≡ «Plateau» a state the model can be in"]]:::plateau
  gap(("⊘ «Gap» what is missing")):::gap

  gap -.->|closed to reach| plat

  classDef plateau fill:#ffe8e8,stroke:#d99b9b,color:#333
  classDef gap fill:#ffd6d6,stroke:#c98080,color:#333
```

| Glyph | Shape | Element | ID prefix | Reads as |
| ----- | ----- | ------- | --------- | -------- |
| `≡` | Subroutine | «Plateau» | `PLAT` | `PLAT1` = Plateau 1 |
| `⊘` | Circle | «Gap» | `GAP` | `GAP1` = Gap 1 |

Dashed edges throughout: none of these states is reached.

## The plateaus

```mermaid
flowchart LR
  plat1[["≡ Declared relationships [PLAT1]"]]:::plateau
  plat2[["≡ A walkable model [PLAT2]"]]:::plateau
  plat3[["≡ A federated graph [PLAT3]"]]:::plateau
  plat4[["≡ Checkable across the boundary [PLAT4]"]]:::plateau

  plat1 -.->|nothing to walk without it| plat2
  plat2 -.->|an index with no consumer| plat3
  plat3 -.->|nothing to resolve against| plat4

  classDef plateau fill:#ffe8e8,stroke:#d99b9b,color:#333
```

| ID | Plateau | The state it names | Status |
| -- | ------- | ------------------ | ------ |
| `PLAT1` | **Declared relationships** | Every relationship an element has is **stated** — in a catalogue column or a relationship table a Requester can read and a validator already checks — and the projection carries it as an edge that knows where it came from and whether it is live. Diagrams render; they no longer declare | **In flight** — [initiative 6](../scope/6_declare-the-relationships-and-let-the-graph-be-walked.md) |
| `PLAT2` | **A walkable model** | The projection has a visual reader: one static page, filters by layer and element type, and expansion outward from any node. No server, no deployed database | **In flight** — [initiative 7](../scope/7_walk-the-model.md) |
| `PLAT3` | **A federated graph** | Each project publishes its own projection at a stable URL. The topmost tree of a federation — the organization, or the parent business function where there is no organization — owns an **index** naming those URLs. The graph is the union, computed at read time and owned by nobody | Planned |
| `PLAT4` | **Checkable across the boundary** | A reference can name an element in another project, and something checks it. Decision 1's recorded consequence — "no validator crosses the repository boundary" — stops being true | Planned |

**`PLAT1` is the only one that is not optional.** The other three are worth
having; without `PLAT1` they are worth having *and impossible*, because each of
them is a consumer of a relationship set that does not currently exist.

**`PLAT3` deliberately has no central model.** A tree that held the union would
restate what another tree owns, which the tier rule in
`architecture-document-style` forbids in as many words, and would need approval
rights over elements it does not own. What is centralized is a list of URLs.
The graph is a view.

### Relationships

<!-- Transcribed from this document's diagrams. The identifier is
     authoritative; the description beside it is checked against the
     catalogue that defines the element. -->

| From | From element | To | To element | Relationship |
| ---- | ------------ | -- | ---------- | ------------ |
| `PLAT1` | «Plateau» Declared relationships | `PLAT2` | «Plateau» A walkable model | nothing to walk without it |
| `PLAT2` | «Plateau» A walkable model | `PLAT3` | «Plateau» A federated graph | an index with no consumer |
| `PLAT3` | «Plateau» A federated graph | `PLAT4` | «Plateau» Checkable across the boundary | nothing to resolve against |

## The gaps

Derived by subtracting today from the plateaus above, and measured against the
three trees in this repository on 2026-08-27.

```mermaid
flowchart TB
  subgraph P1G["Toward PLAT1"]
    gap1(("⊘ No home for a relationship [GAP1]")):::gap
    gap2(("⊘ 481 relationships as opaque text [GAP2]")):::gap
    gap3(("⊘ 164 relationships only in diagrams [GAP3]")):::gap
    gap4(("⊘ Pending reads as live [GAP4]")):::gap
  end
  subgraph P2G["Toward PLAT2"]
    gap5(("⊘ Nothing renders the graph [GAP5]")):::gap
    gap6(("⊘ Traversal would be written twice [GAP6]")):::gap
  end
  subgraph P3G["Toward PLAT3"]
    gap7(("⊘ The projection is never published [GAP7]")):::gap
    gap8(("⊘ No index of a federation [GAP8]")):::gap
  end
  subgraph P4G["Toward PLAT4"]
    gap9(("⊘ No reference crosses a project [GAP9]")):::gap
  end

  classDef gap fill:#ffd6d6,stroke:#c98080,color:#333
```

| ID | Gap | What is true today | Closes toward |
| -- | --- | ------------------ | ------------- |
| `GAP1` | **The relationship has no home in the model** | `BOBJ2` names the element. Nothing names the relationship, so no rule says where one is written, and no document owes one | `PLAT1` |
| `GAP2` | **Cross-layer relationships are opaque text** | 481 backticked identifiers sit in catalogue columns — `Realizes`, `Serves`, `Source`, `Provided by`, `Accessed by` — where `ACMP7` carries them into `attrs` as strings and `ACMP8` never makes an edge of them. 47% of `org-archreator`'s 184 elements have no edge at all | `PLAT1` |
| `GAP3` | **Peer relationships exist only inside diagrams** | 164 relationships are drawn in Mermaid and stated nowhere else. They are overwhelmingly **within one layer** — `CAP5 precedes CAP1`, `ACMP10 carries ACMP5`, `DRV1 evidenced by ASM1` — because a catalogue has one row per element and no column shape for a peer. The diagram was the only surface available | `PLAT1` |
| `GAP4` | **A pending relationship reads as a live one** | The notation says a dashed edge means Pending. `ACMP7`'s edge pattern matches the dashed arrow form and discards which form matched, so 24 pending relationships are indistinguishable from live ones in `DOBJ4`. Anything reading the projection as current state is wrong about them | `PLAT1` |
| `GAP5` | **Nothing renders the graph** | `ACMP14` prints text. A reader who is not in a terminal has the portal, which renders documents and draws no graph | `PLAT2` |
| `GAP6` | **Traversal would be written twice** | `ACMP14` walks `model.json` in Python. A web reader would walk `model.db` in the browser. Two implementations of one traversal is the drift `ACMP7` was created to prevent, one level up | `PLAT2` |
| `GAP7` | **The projection is never published** | `DOBJ4` is gitignored and local. Federation needs an interchange format, and `stack-selection` § A persisted projection needs one of four triggers names exactly this case — "an agent cannot `grep` a repository it has not cloned" | `PLAT3` |
| `GAP8` | **No index names the projects in a federation** | The fact exists in prose: `org-archreator`'s component catalogue carries a **Modeled in** column pointing at the tree that holds each component's detail. Nothing machine-readable carries it | `PLAT3` |
| `GAP9` | **No reference crosses a project** | `ACMP6` scopes every identifier to its project and rejects a foreign one as dangling. `ACMP14` stops at the same boundary, so "what would this change touch" silently excludes everything in another tree. Decision 1 records this consequence and accepts it as the price of the split | `PLAT4` |

## What is deliberately not here

**No relationship vocabulary.** `ACMP8` carries a Mermaid edge label verbatim
on the stated grounds that mapping it onto ArchiMate's vocabulary would be a
guess, and a wrong guess in a projection is worse than an honest string. That
reasoning does not change because the label moves into a table. The corpus
currently uses 111 distinct labels across 306 edges, 67 of them exactly once —
which is worth **reporting** so a project can converge on its own, and is not
worth a controlled list the method would then have to translate.

**No graph database.** At 345 elements and 306 edges across three trees, the
projection is 369 KB. `stack-selection` already settled this: at the scale a
model reaches, SQLite is the graph database. The point at which a model stops
being comprehensible to a person arrives long before the point at which it
stops fitting in a browser tab.

**No private-repository federation.** `PLAT3` works by fetching a published
URL, so it reaches public projects. That is enough to prove the shape.
