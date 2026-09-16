# Application

_[← Front door](../README.md)_

Which software realizes each service. Everything here is a path in the
[archreator repository](https://github.com/roanboc/archreator).

**ArchiMate viewpoint:** Application: Application Service, Application
Component.

## Documents

| # | Document | Elements | Question it answers |
| - | -------- | -------- | ------------------- |
| 1 | [Application services](./1_application-services.md) | The nine services the software offers, and the business service each one serves | What does the software do for the business layer? |
| 2 | [Application components](./2_application-components.md) | The thirteen pieces that do it, each naming its path | Which components provide those services? |

## Metamodel

```mermaid
flowchart LR
  %% legend
  acmp["⊞ «Application Component» the piece that does it [ACMP#]"]:::component
  other["⊞ «Application Component» a piece it imports, checks or aggregates [ACMP#]"]:::component
  asvc(["⬮ «Application Service» what the software does [ASVC#]"]):::app
  bsvc(["⬭ «Business Service» who it does it for, from the business layer [BSVC#]"]):::business

  acmp -->|realizes| asvc
  asvc -->|serves| bsvc
  acmp -->|imports| other

  classDef business fill:#fffbb5,stroke:#c8c04a,color:#333
  classDef app fill:#c2f0ff,stroke:#0288d1,color:#333
  classDef component fill:#9adcf0,stroke:#0277bd,color:#333
```

The cyan ramps from service to component; the business service is a visitor
and keeps its yellow.

## Layer view

```mermaid
flowchart LR
  c8["⊞ The scaffold [ACMP8]"]:::component
  c2["⊞ The link checker [ACMP2]"]:::component
  c3["⊞ The element-ID validator [ACMP3]"]:::component
  c4["⊞ The model parser [ACMP4]"]:::component
  c13["⊞ The prose validator [ACMP13]"]:::component
  a3(["⬮ Self-checking [ASVC3]"]):::app
  b3(["⬭ Model validation [BSVC3]"]):::business

  c8 -->|aggregates| c2
  c8 -->|aggregates| c3
  c8 -->|aggregates| c4
  c8 -->|aggregates| c13
  c2 -->|imports| c4
  c3 -->|imports| c4
  c4 -->|realizes| a3
  a3 -->|serves| b3

  classDef business fill:#fffbb5,stroke:#c8c04a,color:#333
  classDef app fill:#c2f0ff,stroke:#0288d1,color:#333
  classDef component fill:#9adcf0,stroke:#0277bd,color:#333
```

The scaffold ships three validators and the parser two of them import; the
self-checking service they realize is what the business layer sells as model
validation.
