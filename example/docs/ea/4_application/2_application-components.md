# Application Components

_[← Application layer](./README.md) · [EA home](../README.md)_

**ArchiMate elements:** Application Service, Application Component.

## Guidance publishing (Application Service)

Realizes the [EA-first method guidance](../2_business/README.md) business
service. Provided by three components:

| Component | Realizes | Source file |
| --------- | -------- | ------------ |
| Landing page | Entry point: states the one rule, links onward | [`site/index.html`](../../../site/index.html) |
| Guide page | Walks the EA-first process and the human/AI/hybrid actor notation step by step | [`site/guide.html`](../../../site/guide.html) |
| Architecture page | Renders this project's own filled EA layers as the concrete "what finished looks like" example | [`site/architecture.html`](../../../site/architecture.html) |

All three share [`site/styles.css`](../../../site/styles.css). None of
them build or fetch anything at request time — deployment is a direct copy
of `site/` (see
[5_technology/2_deployment.md](../5_technology/README.md)).
