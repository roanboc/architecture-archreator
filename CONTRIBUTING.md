# Contributing

## The working method: EA first

This repo practices **architecture-first development**: strategy and
business architecture are validated before information, application, and
technology — and all of it before code. The full process is described in
[docs/scope/README.md](./docs/scope/README.md); in short, for any change in
requirements:

1. **Align the EA** — walk [docs/ea/](./docs/ea/README.md) top-down
   (`1_strategy` → `5_technology`), updating the affected documents.
2. **Document the scope** — add the next-numbered initiative document to
   [docs/scope/](./docs/scope/README.md).
3. **Implement** — keeping docs and code in sync in the same change set.

Bug fixes that change no documented behavior can go straight to step 3.
Agent-oriented guidance for the same process lives in `.claude/skills/`.

Pull requests follow `.github/pull_request_template.md`: the body links the
scope document, gives every EA layer a verdict, and describes **all**
changes on the branch (`git diff main...HEAD`), not just the latest commit —
and is kept updated as the branch grows.

## Development workflow

<!--
  TEMPLATE — replace with the project's real workflow once a stack is
  chosen. Keep the shape: an install step, a dev-loop command, and the
  exact commands CI runs (so a contributor can reproduce a CI failure
  locally verbatim). For example:

  ```bash
  npm install
  npm run dev
  ```

  Before pushing (CI runs exactly these):

  ```bash
  npm run lint && npm run typecheck && npm test && npm run build
  ```
-->

## Definition of done

A change is done when:

- the project's verification commands (lint, typecheck, tests, build, or
  whatever this stack defines) pass;
- the affected EA documents ([docs/ea/](./docs/ea/README.md)) still
  describe the system as it now is — services, rules, data objects, and
  their realizations (or explicit "Pending") are up to date;
- the initiative's scope document reflects what was actually delivered;
- cross-links resolve and diagrams render;
- any new interpretation of a requirement is recorded as an open question
  with its adopted interpretation (see the `scope-doc` skill).
