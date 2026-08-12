# Skills

_[← Repository README](../../README.md)_

Claude Code picks these up automatically from their `description:`
frontmatter — they aren't invoked by name in normal use. This file is a
directory listing for humans browsing the folder; see the
[root README](../../README.md#how-everything-fits-together) for the
core-vs-supporting breakdown and how each skill relates to `architecture/` and
`scope/`.

This folder is also the root of the **`archreator` plugin** — its manifest
is `.claude/.claude-plugin/plugin.json`, and the marketplace that publishes
it is `.claude-plugin/marketplace.json` at the repository root. The same
files therefore serve both distribution paths: auto-loaded from `.claude/`
in a project created from the template, and installed via
`/plugin install archreator@archreator` into a project that already exists.

That dual role constrains how skills link. **A skill may only link to files
inside this folder.** Installing a plugin copies its directory to a cache,
so a relative link out of it (`../../../architecture/README.md`) resolves to
nothing for a plugin user. Skills refer to a consuming project's documents
by naming the path in a code span — `` `architecture/README.md` `` — which reads
correctly on both paths and is what `ea-doc-style` § Links requires.

| Skill | `SKILL.md` |
| ----- | ---------- |
| `project-bootstrap` | [project-bootstrap/SKILL.md](./project-bootstrap/SKILL.md) |
| `ea-first-change` | [ea-first-change/SKILL.md](./ea-first-change/SKILL.md) |
| `operating-model-discovery` | [operating-model-discovery/SKILL.md](./operating-model-discovery/SKILL.md) |
| `domain-modeling` | [domain-modeling/SKILL.md](./domain-modeling/SKILL.md) |
| `restate-current-state` | [restate-current-state/SKILL.md](./restate-current-state/SKILL.md) |
| `strategy-discovery` | [strategy-discovery/SKILL.md](./strategy-discovery/SKILL.md) |
| `ea-doc-style` | [ea-doc-style/SKILL.md](./ea-doc-style/SKILL.md) |
| `scope-doc` | [scope-doc/SKILL.md](./scope-doc/SKILL.md) |
| `pr-description` | [pr-description/SKILL.md](./pr-description/SKILL.md) |
| `decision-record` | [decision-record/SKILL.md](./decision-record/SKILL.md) |
| `stack-selection` | [stack-selection/SKILL.md](./stack-selection/SKILL.md) |
| `story-sharding` | [story-sharding/SKILL.md](./story-sharding/SKILL.md) |
| `engagement-retrospective` | [engagement-retrospective/SKILL.md](./engagement-retrospective/SKILL.md) |
