# product-archreator

The architecture model of **archreator the method** — the fifteen skills, the
scaffold they emit, the validators that keep a model honest, and the plugin
that ships them.

The method's source lives in
[`archreator`](https://github.com/roanboc/archreator). This tree is the model
of it: why it exists, who it serves, what it offers, and which file realizes
each piece.

| Read | For |
| ---- | --- |
| [`architecture/README.md`](./architecture/README.md) | The notation — glyphs, shapes, layer colours |
| [`architecture/1_strategy/`](./architecture/1_strategy/README.md) | Why the method exists and what it must be able to do |
| [`architecture/2_business/`](./architecture/2_business/README.md) | What it offers, to whom, and the rules that bind it |
| [`architecture/4_application/`](./architecture/4_application/README.md) | Which skill or script realizes each service |
| [`architecture/scope/`](./architecture/scope/README.md) | One document per initiative, with its gate approvals |
| [`architecture/decisions/`](./architecture/decisions/README.md) | Calls smaller than an initiative |

**Modeling depth: 1 — Application.** The organization that publishes the
method is modeled one tree up, in
[`org-archreator/`](../org-archreator/architecture/README.md).
