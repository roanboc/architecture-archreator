# Contributing

The owner of this repository says what should change, reviews the branch and
merges it. An agent, or a person, does the work in between. **The merge is
the approval**; nothing else records one.

## What kind of change is this?

| The change | What it needs |
| ---------- | ------------- |
| **A change to a model** — new elements, a changed relationship, a corrected description | Walk the layers top-down and edit the ones the change touches. Write a short note under [`product-archreator/architecture/scope/`](./product-archreator/architecture/scope/README.md) saying what changed, why, and what was left out — one note per change, whichever trees it spans. Open a pull request |
| **A change to the method itself** | The wrong repository — it belongs in [`archreator`](https://github.com/roanboc/archreator). Its *consequences* for these models land here |
| **A pure correction** — a broken link, a typo, a stale path | Fix it, and fix whatever else it falsifies |

## Before pushing

```bash
python3 scripts/check_links.py
python3 scripts/check_model.py
```

Both must be green. CI runs the same two on every pull request. `make smoke`
runs them and every reading tool over both trees — see the README.

## The rules that catch people out

- **A merged scope note is never rewritten.** It records what changed and
  when. The model moves on; the note does not. If it later names an element
  that no longer exists, that is correct — which is why the validators
  deliberately skip `scope/`, `decisions/`, `reviews/`, `engagements/` and
  `reference/`.
- **An identifier is never reused** once the element it names has been
  merged. Before that it is a draft, and renumbering to close a gap is fine.
- **The documentation describes its subject, not its own construction.** No
  "this used to say", no notes about how many elements were consolidated, no
  narration of a rebuild. The change log is the scope note.
