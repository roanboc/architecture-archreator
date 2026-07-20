# archreator

An **EA-first project template**: the enterprise-architecture guidelines,
Claude Code skills, and procedural scaffolding that every new project should
start from, distilled from two working projects
([`junta_usatama`](https://github.com/roanboc/junta_usatama), a Next.js +
Supabase app, and [`fractal-tree-generator`](https://github.com/roanboc/fractal-tree-generator),
a static TypeScript web app + CLI) that independently converged on the same
method. This repo carries no application code — it's the starting point you
copy, not a library you install.

## The method, in one paragraph

**Strategy and business architecture are validated before any other
layer.** A change in requirements is never coded directly: it is aligned
top-down through five numbered ArchiMate layers
(`docs/ea/1_strategy` → `2_business` → `3_information` → `4_application` →
`5_technology`), recorded in a scope document (`docs/scope/`), and only then
implemented. Every EA element names the code artifact that realizes it (or
is marked "Pending"), so the architecture stays verifiable against the code
at any time. Full write-up: [CONTRIBUTING.md](./CONTRIBUTING.md) and
[docs/scope/README.md](./docs/scope/README.md).

## What's in here

| Where                                          | What                                                                                          |
| ------------------------------------------------| ------------------------------------------------------------------------------------------------ |
| [docs/ea/](./docs/ea/README.md)                | The 5-layer EA skeleton: numbering, notation conventions, ArchiMate-on-Mermaid palette, per-layer analysis order and a fill-in-the-blank layer view for each |
| [docs/scope/](./docs/scope/README.md)          | The scope-document index, the EA-first change process, and the optional open-questions log      |
| [CONTRIBUTING.md](./CONTRIBUTING.md)           | The working method and a definition-of-done checklist                                            |
| [CLAUDE.md](./CLAUDE.md)                       | Agent entry point — the one rule, pointers to layout/commands/conventions to fill in            |
| `.claude/skills/`                               | Four Claude Code skills that operationalize the method for an agent (see below)                 |
| `.github/pull_request_template.md`             | PR body shaped to match a scope document's alignment table                                      |

### The four skills

- **`ea-first-change`** — the process itself: walk the EA layers top-down,
  write a scope document, implement, verify alignment, write the PR.
- **`ea-doc-style`** — numbering, ArchiMate-on-Mermaid notation, the
  grounding rule, link conventions for anything under `docs/`.
- **`scope-doc`** — the scope-document template and the rules for filling
  it in (every layer gets a verdict, deliverables are concrete, out-of-scope
  matters as much as in-scope).
- **`pr-description`** — PR bodies describe the whole branch, not just the
  latest commit, and follow the template.

These are near-verbatim across both source projects — the parts worth
keeping generic — with the project-specific glossaries, business rules, and
diagrams stripped back out to placeholders.

## Using this as a template for a new project

This repo is meant to be the **first commit** of a new project, not
something you reference from afar. Two ways to start a new repo from it:

1. **GitHub template repository (recommended).** In this repo's Settings,
   enable "Template repository." Then, for each new project, click
   **"Use this template" → "Create a new repository"** on GitHub (or
   `gh repo create <new-repo> --template roanboc/archreator`). This gives
   the new repo its own clean git history — no shared ancestry, no
   accidental push-back into archreator — which is the right relationship
   here: every downstream project immediately diverges (real stakeholders,
   real stack, real code), so there's nothing to keep in sync afterward.
2. **One-off copy.** `npx degit roanboc/archreator my-new-project` (or a
   plain clone + `rm -rf .git && git init`) if you don't want to flip the
   template flag or don't have admin rights on this repo.

Avoid a git submodule/subtree relationship or trying to keep new projects
"pinned" to archreator — the docs here are explicitly placeholders meant to
be overwritten with project-specific content on day one, not a shared
dependency that updates in place. If the *method* changes later (a skill
gets a new step, the layer set changes), pull that specific improvement
into each project by hand — treat archreator as the reference copy, not a
live upstream.

### First-commit checklist for a new project

1. Fill in `README.md` and `CLAUDE.md` with the real project name,
   description, layout, and commands.
2. Write `docs/ea/1_strategy/1_motivation.md` first — stakeholders, drivers,
   goals, and the Principles that will later gate every change — then work
   down through the layers as far as the project's current understanding
   goes. Layers with nothing to say yet still get their README's table row
   acknowledged as "not started."
3. Decide the documentation language once, and note it in `CLAUDE.md` (see
   `ea-doc-style`).
4. Delete `docs/scope/open-questions.md` if there's no external stakeholder
   who needs a running index of unconfirmed interpretations.
5. Write scope document `1_...md` for the initial build, retrospectively if
   needed, so the initiative index isn't empty on day one.
