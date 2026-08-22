# Contributing

## Actors

| Role | Who | Does |
| ---- | --- | ---- |
| **Requester** | The repository owner | Says what should change, and **grants the gate approvals** before any work is done |
| **Agent** | An AI agent, or a person | Aligns the change through the layers, stops at each gate, writes the scope document, implements, opens the PR |
| **Reviewer** | The repository owner | Reviews the whole branch and merges |

Nothing here assumes a human fills the middle role.

## What kind of change is this?

| The change | What it needs |
| ---------- | ------------- |
| **A change to a model** — new elements, a changed relationship, a corrected description | The full process: aligned through the layers, gates recorded in a scope document under that tree's `architecture/scope/` |
| **A decision smaller than an initiative** | A record in that tree's `architecture/decisions/`, not a scope document |
| **A change to the method itself** | The wrong repository — it belongs in [`archreator`](https://github.com/roanboc/archreator). Its *consequences* for these models land here |
| **A pure correction** — a broken link, a typo, a stale path | No gates. Fix it, and fix whatever else it falsifies |

## Before pushing

```bash
python3 scripts/check_links.py
python3 scripts/check_model.py
```

Both must be green. CI runs the same two on every pull request.

## The rules that catch people out

- **A merged scope document is never rewritten.** It records what was approved
  and when. The model moves on; the document does not. If it later names an
  element that no longer exists, that is correct — which is why the validators
  deliberately skip `scope/`, `decisions/`, `reviews/` and `engagements/`.
- **An approval that isn't recorded didn't happen.** Gates go in the scope
  document's Approvals table, with who approved and what they were shown. A
  gate that did not apply gets an `N/A — <why>` row rather than being deleted.
- **An identifier is never reused** once the gate approving its element has
  passed. Before that it is draft, and renumbering to close a gap is fine.
- **The documentation describes its subject, not its own construction.** No
  "this used to say", no notes about how many elements were consolidated.
  The change log is the scope document.
