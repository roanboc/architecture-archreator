# Order

_[← Where the product is going](./README.md) · [Features](./1_target-state.md) · [Front door](../README.md)_

**Status:** ◐ Draft — not yet marked as reviewed by the owner.

The order the missing pieces in [Features](./1_target-state.md) are closed
in, and what each step needs first. No dates: a step waits on the step before
it, not on a calendar.

| # | Change | Closes | Reaches | Needs first | Status |
| - | ------ | ------ | ------- | ----------- | ------ |
| 2 | **Say where the product is going, and put the tools on the bench** — [scope note 2](../scope/2_say-where-the-product-is-going.md) | `GAP2`, `GAP4`, `GAP5` | `PLAT2`, in part | — | **In progress** |
| 3 | **Declare the method version, and walk it as an ordinary change** — the front door says which method version the models are written against and a bench check compares it with the plugin's; the change is walked from a filed request to a merged pull request, which is the record the first feature asks for | `GAP1`, `GAP6` | `PLAT1` | 2 — the bench runs the check | **Planned** |
| 4 | **Teach the readers a two-tree repository** — the marker is read at the start of a cell in the coverage report, as the parse already reads it, and `--project` narrows a brief to its own tree | `GAP7` | — | 2 — the smoke run proves the fix on both trees | **Planned** — a change to the method |
| 5 | **Read the impact before the review, and check the ground** — the walk shows what a change would touch before the pull request is opened, and a bench check opens every path a `Lives at` cell names against the method checkout | `GAP3`, `GAP8` | `PLAT2` | 2 and 3 | **Planned** — half of it a change to the method |
| 6 | **One site for both models** — one portal configuration over both trees, so every link between them resolves | `GAP9` | `PLAT3` | 2 — the portal builds on the bench | **Planned** |

**Why this order.** The bench first, because every later step ends in
something the bench checks. The ordinary change second, because it is the
product's argument and the cheapest thing to show: one line on the front
door, one comparison on the bench, and the walk that puts them there is the
record. The method's fixes before the site, because a site renders what the
readers read. Steps 4 and 5 can be one change in the method's repository if
that is easier.
