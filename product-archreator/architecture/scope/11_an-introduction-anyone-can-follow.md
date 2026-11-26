# Project Scope — An introduction anyone can follow

_[← Scope index](./README.md) · [Model home](../README.md)_

**ArchiMate viewpoint:** Implementation & Migration.
**Delivered as:** branches `ccr-89cc65be-vffo8n-site` and
`ccr-89cc65be-vffo8n-film` in
[`archreator`](https://github.com/roanboc/archreator), one pull request each.

The Requester asked for a proper web page that introduces the method to
anybody, without expecting them to know enterprise architecture: what it is
useful for, shown more than told, with a film that explains the loop and how a
repository is organized. This initiative rebuilds the landing page around
pictures a visitor can touch, and adds a two-minute narrated film drawn from
source.

## EA alignment (assessed top-down before implementing)

| Layer | Impact | Confirmed |
| ----- | ------ | --------- |
| 0_business-design | No change. In the organization's, the channel `CH2` already says the guidance site is where an owner evaluates the method before adopting; this makes that true for a reader with no background | — |
| 1_strategy | No change. The organization's `CAP2.1` Self-service adoption is what the page serves, and it stands as written | — |
| 2_business | `BSVC8` says what public guidance now delivers: the loop to step through, an example to select things in, a film, and where everything is kept | The shape — a visual page for anybody, a narrated film, the site first — by the owner, in conversation, 2026-11-25, and the wording, by the owner, in conversation, 2026-11-26 |
| 3_information | No change | — |
| 4_application | `ASVC9` and `ACMP12` restated. `ACMP15` The film source added | By the owner, in conversation, 2026-11-26 |
| 5_technology | No change. The site is still static files on the code host's pages | — |

## What the evidence said

| Source | What it said |
| ------ | ------------ |
| The page as it stood | Text from top to bottom, addressed to two named customers, with no picture of the method and nothing to try |
| The preview generator, [scope 10](./10_a-preview-comes-with-its-picture.md) | The method can now draw a change for somebody who never read the model. That drawing is the most direct answer to "what would I actually see", so the page shows a real one |
| The owner's own films | Narrated, drawn from source and voiced by a synthetic voice that says so. The same voice and the same practice are used here |
| A speech recognizer, run on the finished narration | It heard the script word for word, 98.7% matched; the only difference is the product's name, which it writes as two words. The voice reads the name by a respelling, and how the owner says it is theirs to settle |

**The page had to answer the question a stranger asks, in the order they ask
it.** So each section opens with that question, and the answer is a picture.

## Plateaus

| Plateau | State |
| ------- | ----- |
| **Baseline** | Two static pages and a stylesheet: a landing page of prose, and the install steps |
| **Target** | A landing page that reads as a conversation, with the loop to step through, a live example of a preview, a map of the repository and a two-minute film; the install steps unchanged in substance; the film kept as source beside it |

## Work packages and deliverables

### WP1 — The landing page

- **Deliverables:** `site/index.html`, `site/style.css`, `site/site.js`;
  `site/loop.js`, the loop drawn once as data; `site/demo/`, the example
  preview, which is the preview generator's own output for a made-up shop;
  `site/assets/fonts/`, three open-licensed faces served by the site itself;
  `site/start.html` moved onto the same shell;
  `tests/test_site_example.py`, which holds the example and the numbers
  quoted beside it to the tool.
- **Outcome:** a reader with no background sees what the method would do for
  them, and tries the part they would use.

### WP2 — The film

- **Deliverables:** `film/script.json`, `film/film.html`, `film/film.css`,
  `film/film.js`, `film/timeline.js`, `film/tools/voice.py`,
  `film/tools/render.js`, `film/README.md`; the film, its captions and its
  poster under `site/assets/film/`; the film's section and transcript on the
  landing page; `tests/test_film.py`, which holds the timeline, the captions
  and the transcript to the script.
- **Outcome:** two minutes that explain the loop and the layout of a
  repository, remade from source when the method changes.

### WP3 — These trees

- **Deliverables:** the elements named in the alignment table.
- **Outcome:** the product model describes the site and the film as they
  ship.

## In scope / out of scope

| In scope | Out of scope (gaps, candidate future work) |
| -------- | ------------------------------------------- |
| The landing page, its example, its repository map and the film | A Spanish page and a Spanish soundtrack |
| Serving the fonts from the site, so the page asks nothing of a third party | A custom domain |
| The film kept as source, with its words written once | Music under the narration |
| The example shop on one page, once [scope 10](./10_a-preview-comes-with-its-picture.md)'s last work package lands | |

## Gap notes

- **The film is a file in the repository.** About six megabytes, committed
  under `site/assets/film/` because the site is deployed from that folder.
  Every remake adds as much again to the history. Publishing it as a release
  asset and linking it would close that, and is how the owner's other films
  are kept.
- **How the name is said was settled by the owner**, 2026-11-26: "ar-kree-ay-ter",
  the "ch" said as a k. One line of `film/script.json` holds it.
- **The page speaks English only.** Its words are in the HTML, so a second
  language is a second page.
- **The example is made up.** It says so wherever it appears. A worked model
  of a real small business would serve a newcomer better, and belongs in
  this repository beside the two that are here.
