# 6 — The portability boundary: what may be provider-specific

_[← Decisions](./README.md)_

**Status:** Accepted
**Date:** 2026-08-12
**Touches:** `P6`, `RULE9`, `CH3`, `ACMP2`,
[`2_business-model-canvas.md`](../../../org-archreator/architecture/0_business-design/2_business-model-canvas.md#open-questions)
open question 2

## Context

archreator is distributed today as a Claude Code plugin, and the skills are
written for it. `P6` — _generic by design, one implementation at a time_ —
commits to the method being transferable instructions with provider-specific
packaging, but records that _"its exact boundary is still open"_. The
organization's Business Model Canvas states the condition precisely: a
decision record is needed _"before anything provider-specific enters a skill
body"_, and _"before the question is settled by accident"_.

The accident was imminent. [Scope document 9](../scope/9_the-repository-says-what-it-is.md)
proposed moving the project scaffold into `.claude/templates/` — which would
have placed method content, the thing `P6` protects, inside the directory that
exists for one provider's packaging. The boundary had to be drawn before the
move, not after it.

## Options considered

| Option | Consequence |
| ------ | ----------- |
| **Leave the boundary undrawn** | The status quo. Every layout choice settles a bit of it silently, which is the outcome the canvas explicitly warns about |
| **Draw the boundary by tier, with a test** | Each artifact is assignable to a tier by a question a reader can answer alone. Costs one document and some relocation; enforces nothing mechanically |
| **Answer by porting to a second platform now** | Demonstrates portability instead of asserting it. But it widens `CS1` — the customer segment is defined as "already working in an agent" — which makes it a strategy change requiring Gate 1, not a boundary decision |

## Decision

**Three tiers, assigned by one test.**

| Tier | What it holds | Rule |
| ---- | ------------- | ---- |
| **Method content** | Skill bodies, templates, conventions, gates, document style | Must be portable. Plain markdown that assumes nothing about which agent reads it. No provider's tool names, directory conventions, or CLI mechanics in the prose |
| **Discovery metadata** | `SKILL.md` frontmatter — `name`, `description` | Kept as-is. Portability here comes from it being plain text with trivial structure, not from a formal cross-vendor specification existing |
| **Packaging** | `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, the `.claude/` location itself, `CH3` | Provider-specific and disposable. One set per supported platform |

**The test that assigns the tier:** _if Claude Code vanished tomorrow, would
this file need **editing**, or just **moving**?_ Method content and discovery
metadata move. Packaging gets rewritten. Anything in a skill body that would
need editing is a `P6` violation.

**Claude Code is the first packaging target, not the only one.** Further
targets are additive — each adds a manifest, and none forks the method.

## Why

**`P6` already made the commitment; what was missing was the line.** This
record does not change the principle's posture, it supplies the boundary the
principle says is open. That is why this is a decision and not a Gate 1
strategy change.

**The asymmetry decides the shape.** Packaging is small, mechanical and
cheap to duplicate. Method content is large, carefully worded, and the whole
value of the product. A boundary that lets the small disposable part be
duplicated per platform, while the large part stays single, is the only split
where adding a platform is a manifest rather than a fork.

**`P2` is what makes it work.** _Everything is in the repository, as text_ —
portability is a property of the method being markdown, not of any agent
vendor's cooperation. The tiers just keep it that way.

**A test beats a rule.** "Don't be provider-specific" is unenforceable
because nobody agrees where it starts. "Would this file need editing or just
moving?" is answerable about a specific file by one person in a few seconds,
which is the most enforcement an unautomated rule can get.

## Consequences

- **`RULE9` is a packaging constraint, not a method rule**, and should be
  satisfied structurally rather than by convention. It exists because a plugin
  is copied to a cache and outbound links die — a fact about one provider that
  currently shapes how every skill is written.
- **Templates live inside the skill that emits them**, not in a provider
  directory. A skill is already a directory of files, so the template travels
  with its skill as one portable unit and `RULE9` is satisfied by structure.
  This reverses the `.claude/templates/` placement scope document 9 first
  proposed.
- **`CH3` gains siblings rather than being replaced.** The Claude Code plugin
  marketplace stays the distribution channel; a second platform's registry
  would be `CH4`, not a migration.
- **Nothing enforces any of this.** The test is applied by a person. A check
  that greps skill bodies for provider-specific tokens would close most of the
  gap cheaply, and is the obvious follow-up if the boundary starts eroding.
- **Open question 2 is answered** and moves out of the canvas's Pending table.

## What would reopen this

A target platform whose skill format is **not** markdown with simple
frontmatter — which would make the discovery-metadata tier non-portable and
force either a translation step or a genuine second format. That is a real
possibility and it would be a strategy question, not a layout one.
