# Scripts

_[← Project home](../README.md)_

Two validators that keep this repository's architecture documents honest, and
four tools — one for the reader who queries a model, three for the readers a
repository does not reach. They came with the
scaffold, so this repository has had the validators since its first commit,
and CI runs both on every pull request.

```bash
python3 scripts/check_links.py    # relative links and HTML anchors resolve
python3 scripts/check_model.py    # element-ID references resolve
python3 scripts/build_model.py    # project a model into .model/
python3 scripts/query_model.py coverage           # what is grounded, and what is not
python3 scripts/query_model.py trace CAP5 --project product-archreator
python3 scripts/build_docs.py --project <tree>    # that model as a website
python3 scripts/export_pdf.py  --project <tree>   # that model as one PDF
```

Both validators exit `0` when everything resolves and `1` otherwise, printing
what failed. The other four are tools rather than gates: nothing has to be
green for them, and nothing breaks if they are never run.

**The two publishing tools take a `--project`, and that is not optional here.**
They act on one model at a time, and this repository holds three — each with
its own `mkdocs.yml` beside its `architecture/`. Run without it, they list the
trees and stop rather than guessing:

```bash
python3 scripts/build_docs.py --project org-archreator
python3 scripts/build_docs.py --project product-archreator --serve
python3 scripts/export_pdf.py --project product-archreator/site
```

| File | What it is |
| ---- | ---------- |
| `check_links.py` | Executable. Every relative Markdown link and every HTML `href`, `src` and `#fragment` points at something that exists |
| `check_model.py` | Executable. Every backticked element ID resolves to a definition, none is defined twice, none is both live and retired, and a levelled ID has its parent defined |
| `build_model.py` | Executable. Writes `.model/model.json` and `.model/model.db` — the model as nodes and edges, for a rendered view or a report. `--inventory` prints one line per element instead |
| `query_model.py` | Executable. Reads the projection and answers the two questions a table cannot. `trace <ID>` follows relationships outward and says what a change to one element would touch; `coverage` reports what names a realizing artifact, what is explicitly Pending, and what its own catalogue leaves blank beside grounded neighbours. Builds the projection first if it is missing. **Three trees each own a `CAP1`**, so `trace` takes `--project` when an ID is not unique — it says so rather than picking one |
| `build_docs.py` | Executable. Stages one tree's documents into `<tree>/.docs/src/` and builds its portal into `<tree>/.docs/site/`. `--serve` rebuilds as the model is edited. Also the staging hook each `mkdocs.yml` runs |
| `export_pdf.py` | Executable. Prints that portal's single-page view to `<tree>/.docs/architecture.pdf` with a headless browser, and checks that the diagrams were drawn rather than left as source text. What a PDF leaves out is the `print-site` `exclude` list in the tree's `mkdocs.yml` |
| `model_graph.py` | Library, imported by the others. The single parse of the document convention — element IDs, catalogue tables, Mermaid edges |
| `element-prefixes.json` | Data, read by `model_graph.py`. The element-ID prefixes and what each stands for |

## The projection is derived, and stays that way

The Markdown under `architecture/` is the source of truth. `build_model.py`
writes a second representation of it, which is a thing worth being uneasy
about — a derived store that falls behind the source is exactly the drift the
one-fact-one-place rule exists to prevent.

Three things keep it honest. It is **regenerated** from scratch on every run,
never hand-edited. It is **gitignored**, so no stale copy can be committed.
And **nothing reads it that could have read the Markdown instead** — an agent
reads the documents natively, so this exists for the consumers that cannot: a
dashboard, a report, and `query_model.py`, whose traversals are the reason a
graph is worth materializing at all.

Delete `.model/` and nothing is lost.

## `query_model.py` reports; it never fails a build

Every element must name what realizes it, and that is the one rule the
validators do not enforce: telling a repository path from a team name is fuzzy,
and a check that fails wrongly teaches people to ignore the checks that do not.

So `coverage` prints and **always exits 0**, and there is no `--strict`. It
judges by catalogue table rather than by element — a table grounding none of
its rows is not modeling realization at all, and reporting each of its elements
is how a report becomes noise. What it reports is a table that grounds some
rows and leaves others blank.

It cannot say what nothing points at. The projection drops a reference made
inside the document that defines the element, so an element named only by its
own neighbours looks unreferenced, and answering the question properly would
mean re-reading the Markdown.

## So is the portal, and one thing it cannot do

Everything under `<tree>/.docs/` is the same arrangement: a staged copy of the
Markdown, the portal built from it, and the PDF that portal printed. All three
are rebuilt on every run, all three are gitignored, and none holds a sentence
the documents do not. Every page carries the path of the file that produced it
— `RULE7` in `product-archreator`.

**A portal covers one tree, and the trees cite each other.** Twenty-one links
across the three models point at a document in a sibling tree; in the
repository they resolve, and in a portal built from a single tree they do not.
Nothing is lost — the reader is one directory up from the answer in git — but
a portal handed to somebody is not self-contained, and that is worth knowing
before handing one over.

The shared parts sit at the repository root and are pointed at, not copied:
one `scripts/`, one `overrides/`, and one `mkdocs.yml` per tree naming both.

## What each one cannot do

`check_model.py` verifies that a *reference* resolves. `check_links.py`
verifies that a *link* resolves. **Neither reads what a "Realized by" cell
claims about a path**, so a cell naming a directory that no longer exists
passes both silently. Checking that is a step in the change process, not
something these scripts can do for you.

`build_model.py` reads structure from the identifier, the numbered folder and
the notation — all of which survive translation, so it works the same on a
model written in any language. **The one exception is its `realized_by`
column**, which has to guess which heading names a realization and is empty
when it cannot. The full row is always in `attrs`, so consult that rather than
trusting the guess. It also reports rows where the cell after the ID does not
look like a name, which is a finding about the document rather than an error.

## `element-prefixes.json`

It is data, not configuration — regenerated from the method rather than
hand-edited. Adding a prefix here does not make it part of the method's
vocabulary; it makes `check_model.py` stop objecting to one the method does
not have.

If this project genuinely needs an element type the method does not define,
that is a decision worth recording rather than a line worth adding quietly.
