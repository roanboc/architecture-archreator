# Scripts

_[← Project home](../README.md)_

Two validators that keep this repository's architecture documents honest, and
three tools for the readers a repository does not reach. They came with the
scaffold, so this repository has had the validators since its first commit,
and CI runs both on every pull request.

```bash
python3 scripts/check_links.py    # relative links and HTML anchors resolve
python3 scripts/check_model.py    # element-ID references resolve
python3 scripts/build_model.py    # project a model into .model/
python3 scripts/build_docs.py --project <tree>    # that model as a website
python3 scripts/export_pdf.py  --project <tree>   # that model as one PDF
```

Both validators exit `0` when everything resolves and `1` otherwise, printing
what failed. The other three are tools rather than gates: nothing has to be
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
published view of the model, a dashboard, a report.

Delete `.model/` and nothing is lost.

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
