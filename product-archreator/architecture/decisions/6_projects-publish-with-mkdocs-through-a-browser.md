# Decision 6 — Projects publish with MkDocs, rendered through a browser

_[← Decisions index](./README.md)_

**Status:** Proposed
**Date:** 2026-08-22
**Touches:** [4_application/2_application-components.md § The components](../4_application/2_application-components.md)

## Context

An adopting project's model is Markdown in git; the people who approve it at
the gates are not. A commercial strategist reads, highlights and annotates a
Portable Document Format (PDF) file, and will not clone a repository to do it.
`P3` — an approval that is not recorded did not happen — needs what they
approved to be a citable document rather than a branch they never opened.

So the scaffold, `ACMP10`, needs to render a project's `architecture/` tree as
a site and as documents. What decides *how* is the notation. The
[`architecture-document-style`](https://github.com/roanboc/archreator/blob/main/plugins/archreator/skills/architecture-document-style/SKILL.md)
rulebook writes every diagram as ArchiMate-on-Mermaid, and Mermaid draws
itself in the browser, from JavaScript, after the page loads. A renderer that
executes no JavaScript emits documents with the diagrams missing — and for a
reviewer at Gate 2, the diagrams are the document.

This concerns projects that adopt the method. archreator's own repository
publishes a hand-written page and has no model tree to render.

## Options considered

| Option | Why not (or why) |
| ------ | ---------------- |
| **MkDocs with a print engine** — `mkdocs-with-pdf`, on WeasyPrint | The obvious first pick, and it cannot draw a Mermaid diagram: WeasyPrint runs no JavaScript, so every diagram arrives as a code fence or as nothing. It also needs GTK and Pango native libraries, which is the one part of the toolchain that is genuinely unpleasant to install on Windows |
| **MkDocs with a browser exporter** — `mkdocs-exporter` on Playwright, or `mkdocs-print-site-plugin` printed from headless Chromium | The renderer is a real browser, so the diagrams render exactly as they do on the site, and one engine produces both outputs. Chromium installs the same way on every operating system |
| **Pandoc straight to PDF** | Produces a document without producing a site, so the searchable view has to be built a second way. Mermaid needs a filter that shells out to a browser regardless, and a LaTeX toolchain is heavier than the model it renders |
| **A hosted portal** — Confluence, Backstage | Contradicts the shape of [5_technology](../5_technology/README.md), which has no server, no database and no accounts on purpose. The reviewer also still ends up being mailed a file, so the portal is added infrastructure that does not remove the step it was bought for |
| **Print to PDF by hand from the rendered site** | Free today and drifts tomorrow. No cover, no contents, no page numbers, and no way to say which commit a signed-off document was |

## Decision

**A project publishes its `architecture/` tree with MkDocs, and the PDF is
produced by a headless browser rather than a print engine.** The scaffold
carries the configuration; the documents stay ordinary Markdown.

## Consequences

- **It commits every adopting project to a build.** [5_technology](../5_technology/1_technology-services.md)
  records that archreator has none — "`ART1` is the repository contents at a
  ref". That stays true of the method and stops being true of a project using
  it, which now has a Python environment, a pinned plugin set and a Chromium
  download in continuous integration.
- **The notation and the renderer are now one choice.** Keeping
  ArchiMate-on-Mermaid is what rejected the print engine; the reverse also
  holds, and a future renderer that cannot run JavaScript would force the
  method's diagram notation to change rather than merely its build.
- **All renderer specificity stays in the configuration file, never in a
  document.** This is `P5` applied to a second platform: delete `mkdocs.yml`
  and every Markdown file is untouched. It also makes the pipeline optional,
  which a project modelling a single application will want it to be.
- **The link conventions have to be proved against the renderer.**
  [`document-style`](https://github.com/roanboc/archreator/blob/main/plugins/archreator/skills/document-style/SKILL.md)
  requires links to a specific file, keeping anchors, and MkDocs rewrites
  exactly those paths — so `mkdocs build --strict` runs beside `check_links.py`
  rather than instead of it, and the raw-git reading path stays supported.
- **It commits the project to versioning what it hands over.** A PDF carries
  the commit it was built from, and is built at a gate rather than on every
  merge; an annotated copy coming back from a reviewer is a competing version
  of the model until someone transcribes it.
- **It does not give `ASVC8` its consumer.** The published view renders the
  Markdown, not the projection, so model projection keeps its dashed edge and
  the gap stays honest.
