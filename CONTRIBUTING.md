# Contributing

## Actors

| Role | Who | Does |
| ---- | --- | ---- |
| **Requester** | The repository owner | Says what should change, in plain words. **Merging the pull request is the approval** — nothing else records one |
| **Agent** | An AI agent, or a person | Works out which layers the change touches, edits them, writes the scope note, implements, opens the PR |
| **Reviewer** | The repository owner | Reviews the whole branch and merges |

## What kind of change is this?

| The change | What it needs |
| ---------- | ------------- |
| **A change to a model** — new elements, a changed relationship, a corrected description | Walk the layers top-down and edit the ones the change touches. Write a short note under [`product-archreator/architecture/scope/`](./product-archreator/architecture/scope/README.md) saying what changed, why, and what was left out — one note per change, whichever trees it spans. Open a pull request |
| **A decision smaller than an initiative** | A record in `architecture/decisions/`, not a scope document |
| **A change to the method itself** | The wrong repository — it belongs in [`archreator`](https://github.com/roanboc/archreator). Its *consequences* for these models land here |
| **A pure correction** — a broken link, a typo, a stale path | Fix it, and fix whatever else it falsifies |

## Before pushing

```bash
python3 scripts/check_links.py
python3 scripts/check_model.py
python3 scripts/check_prose.py
```

All three must be green. CI runs the same three on every pull request.

## The rules that catch people out

- **A merged scope document is never rewritten.** It records what was approved
  and when. The model moves on; the document does not, and it may name an
  element that no longer exists — the validators skip `scope/`, `decisions/`,
  `reviews/` and `engagements/`. The one edit it accepts is repairing a link
  target so it still resolves; every word, link text included, is left alone.
- **The merge is the only approval that exists.** Nothing records one before
  it — no gate, no signature inside a document — so a pull request left open
  has not been approved, however long it sits.
- **A question reaches the Requester only when the answer changes what gets
  built now and nothing in the model settles it.** Everything else is the
  agent's call — taken, applied, and written into the row it changes with that
  row's `Source` cell reading `adopted — <the call>`, in a document still
  marked `◐`. Never ask about a state that does not exist yet.
- **An identifier is never reused** once the change that introduced it merges.
  Before that, renumbering to close a gap is fine.
- **The documentation describes its subject, not its own construction,
  governance or layout.** No "this used to say", no notes about how many
  elements were consolidated, no "Direction covers this document", no "the
  table below". The change log is the scope document, and
  `scripts/check_prose.py` names the sentence that breaks this, from a word
  list tuned to these models.
- **A relationship is declared once, in the tree's
  `architecture/relationships.md`.** A page draws it and names it in prose;
  a table a person reads carries no bare identifier list, and a layer README
  has one shape: title, one sentence, the viewpoint line, Documents,
  Metamodel, Layer view.
