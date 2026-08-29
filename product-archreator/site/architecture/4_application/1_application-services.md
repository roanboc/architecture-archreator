# Application services

_[← Application layer](./README.md) · [EA home](../README.md)_

**ArchiMate viewpoint:** Application. What software does for the business
layer.

**Status:** ● Validated — **Gate 3** declined at Gate 2 ([scope document 1](../scope/1_model-the-site-on-the-current-method.md), 2026-08-22), which routed the application and technology layers to pull-request review.

**One service, and it is the smallest one a layer can have.** The page is
static: nothing computes, nothing queries, nothing decides. What the software
does is hand over bytes that were already correct when they were written.

That is not a gap to be filled later. A site with an application layer worth
several elements would have acquired the build, the framework and the
maintenance that `G2` exists to refuse.

## How to read this document

```mermaid
flowchart LR
  asvc(["⬮ «Application Service» what the software offers"]):::service
  bsvc(["⬭ «Business Service» — context, from the business layer"]):::business

  asvc -->|realizes| bsvc

  classDef service fill:#c2f0ff,stroke:#0288d1,color:#333
  classDef business fill:#efe57d,stroke:#b8ad3f,color:#333
```

| Glyph | Shape | Element | ID prefix | Reads as |
| ----- | ----- | ------- | --------- | -------- |
| `⬮` | Stadium | «Application Service» | `ASVC` | `ASVC1` = Application Service 1 |
| `⬭` | Stadium (yellow) | «Business Service» — context, from [2_business/2_business-services.md](../2_business/2_business-services.md) | `BSVC` | `BSVC1` = Business Service 1 |

## The service

```mermaid
flowchart LR
  asvc1(["⬮ Page delivery [ASVC1]"]):::service

  bsvc1(["⬭ Explain the problem and the answer [BSVC1]"]):::business
  bsvc2(["⬭ Say what an adopter receives [BSVC2]"]):::business
  bsvc3(["⬭ Give the two install commands [BSVC3]"]):::business
  bsvc4(["⬭ Send the reader to the right repository [BSVC4]"]):::business

  asvc1 -->|realizes| bsvc1
  asvc1 -->|realizes| bsvc2
  asvc1 -->|realizes| bsvc3
  asvc1 -->|realizes| bsvc4

  classDef service fill:#c2f0ff,stroke:#0288d1,color:#333
  classDef business fill:#efe57d,stroke:#b8ad3f,color:#333
```

| ID | Application service | What it does | Realizes | Provided by |
| -- | ------------------- | ------------ | -------- | ----------- |
| `ASVC1` | **Page delivery** | Returns one HTML document over HTTPS. No request is interpreted, no parameter is read, and no two responses differ | `BSVC1`, `BSVC2`, `BSVC3`, `BSVC4` | `ACMP1` |

**Four business services and one application service is the right shape**, not
a modelling shortcut. The four are distinctions a *reader* makes — sections
they scroll past for different reasons. The software makes none of them: it
cannot tell which section anyone read, and would behave identically if three
of the four were deleted.

## No collaborations, no interfaces, no contracts

There is one component and nothing for it to collaborate with. The application
interface a reader meets is the URL, and that is modeled where it belongs — as
`BIF1`, the published page, in the business layer.
