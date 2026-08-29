# Project Scope — Inspect a diagram

_[← Scope index](./README.md) · [Model home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** the corresponding change in `archreator` and this model alignment.
**Prior art:** [`ea_bigview` PR #6](https://github.com/roanboc/ea_bigview/pull/6).

A focused diagram can still be the densest thing on its page. Browser zoom
also scales the prose and navigation, while the reader needs room for the
diagram alone. BigView proved that Material's closed Mermaid shadow root does
not prevent this: move the rendered host into an overlay, then return that
exact node to its source position.

## The design

### 1. Inspect the rendering; never create a second one

Clicking a Mermaid diagram, or focusing it and pressing Enter, opens the
already-rendered host in a full-screen modal. Wheel or `+`/`−` zooms, pointer
drag pans, **Fit** or `0` restores the frame, and `Esc` closes it. The viewer
does not read the closed shadow root, clone an SVG, parse Mermaid or fetch a
library.

### 2. The interaction belongs to the portal only

The overlay is absent from `print_page`, so PDF output does not move. GitHub
continues to render the same Markdown. The viewer adds no model content,
dependency, service, generated file or network request.

### 3. Generalize the proven implementation for the scaffold

The scaffold version separates markup, CSS and JavaScript under `overrides/`.
It adds dialog semantics, keyboard opening, focus containment and restoration,
and follows Material's instant-navigation lifecycle. Controls default to
English and can be translated through `extra.diagram_zoom` in `mkdocs.yml`.

## EA alignment

| Layer | Impact |
| ----- | ------ |
| 0_business-design | **Not used** — Depth 1 |
| 1_strategy | **No change.** The viewer serves the existing goal of readable architecture |
| 2_business | **`BSVC7` and `BIF5` restated.** The portal interface gains diagram inspection; the PDF remains static |
| 3_information | **No change.** No model or projection data changes |
| 4_application | **`ASVC9` and `ACMP12` restated.** The portal builder ships the accessible viewer as theme assets |
| 5_technology | **No change.** No dependency, renderer, runtime or network service is added |

## Approvals

| Gate | Approved by | Date | What was approved |
| ---- | ----------- | ---- | ----------------- |
| Gate 0 — Business model | — | — | **N/A** — Depth 1 |
| Gate 1 — Strategy | Requester | 2026-08-29 | No strategy change; improve human diagram reading without weakening agent-readable Markdown |
| Gate 2 — Business | Requester | 2026-08-29 | Incorporate the BigView full-screen zoom interaction into ArChreator's published portal |
| Gate 3 — Solution design | Requester | 2026-08-29 | No dependency; move the rendered host; keep PDF out; generalize language, accessibility and navigation behavior |

## Work packages

1. Add configurable dialog markup to `overrides/main.html`.
2. Add separate CSS and JavaScript assets for zoom, pan, fit, close, keyboard and focus behavior.
3. Document the interaction and non-English label configuration.
4. Build and exercise the real portal, including instant navigation and print exclusion.

## In scope / out of scope

| In scope | Out of scope |
| -------- | ------------ |
| Portal diagrams rendered by Mermaid | GitHub's Mermaid renderer |
| Mouse, keyboard and pointer interaction | Editing or rearranging the architecture |
| Configurable interface labels | Automatic translation |
| Light, dark and responsive portal styles | Changing diagram layout or selection |
| Print-page exclusion | Interactive PDF diagrams |
