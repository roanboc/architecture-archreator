# Business

_[← Front door](../README.md)_

What the product does for an adopting project, as services. The actors are
the adopting project's own three roles, defined as stakeholders in
[motivation](../1_strategy/1_motivation.md).

**ArchiMate viewpoint:** Business: Business Service.

## Documents

| # | Document | Elements | Question it answers |
| - | -------- | -------- | ------------------- |
| 1 | [Business services](./1_business-services.md) | The eight services, what each delivers, and which components realize it | What does the product do for an adopting project? |

## Metamodel

```mermaid
flowchart LR
  %% legend
  bsvc(["⬭ «Business Service» what the product does for an adopting project [BSVC#]"]):::business
  other(["⬭ «Business Service» another service it serves or flows to [BSVC#]"]):::business
  acmp["⊞ «Application Component» the piece that realizes it, from the application layer [ACMP#]"]:::component

  bsvc -->|serves| other
  bsvc -->|realized by| acmp

  classDef business fill:#fffbb5,stroke:#c8c04a,color:#333
  classDef app fill:#c2f0ff,stroke:#0288d1,color:#333
  classDef component fill:#9adcf0,stroke:#0277bd,color:#333
```

The component is a visitor from the application layer and keeps its cyan.

## Layer view

```mermaid
flowchart LR
  b8(["⬭ Public guidance [BSVC8]"]):::business
  b5(["⬭ Method distribution [BSVC5]"]):::business
  b2(["⬭ Subject discovery [BSVC2]"]):::business
  b1(["⬭ Gated change alignment [BSVC1]"]):::business
  b3(["⬭ Model validation [BSVC3]"]):::business
  c1["⊞ The skill corpus [ACMP1]"]:::component

  b8 -->|serves| b5
  b5 -->|serves| b2
  b2 -->|flows to| b1
  b3 -->|serves| b1
  b1 -->|realized by| c1

  classDef business fill:#fffbb5,stroke:#c8c04a,color:#333
  classDef app fill:#c2f0ff,stroke:#0288d1,color:#333
  classDef component fill:#9adcf0,stroke:#0277bd,color:#333
```

Guidance leads to distribution, distribution to discovery, and discovery
flows into the gated alignment where the method happens; validation serves
it, and the skill corpus realizes it.
