# Business

_[← Front door](../README.md)_

Who does what, which services the organization offers, and how the work
flows.

**ArchiMate viewpoint:** Business: Business Actor, Business Role, Contract,
Business Service, Business Process.

## Documents

| # | Document | Elements | Question it answers |
| - | -------- | -------- | ------------------- |
| 1 | [Business architecture](./1_business-architecture.md) | Two actors, one of them an AI, three roles, two contracts, three services and the process map in its four bands | Who does what, which services are offered, and how does the work flow? |

## Metamodel

```mermaid
flowchart LR
  %% legend
  act(["⚇ «Business Actor» who acts [ACT#]"]):::business
  actAI(["⚇ «Business Actor (AI)» an agent that assists a role [ACT#]"]):::ai
  role["⚉ «Business Role» the hat they wear [ROLE#]"]:::role
  ctr[/"❒ «Contract» what binds them [CTR#]"/]:::contract
  bsvc(["⬭ «Business Service» what is offered [BSVC#]"]):::service
  bproc{{"⚙ «Business Process» how the work runs [BPROC#, BPROC#.#]"}}:::business
  cap["✦ «Capability» what the service delivers, from the strategy layer [CAP#]"]:::capability
  ch["⊸ «Channel» how it is reached, from the canvas [CH#]"]:::channel
  kp{{"⧉ «Key Partner» who the contract binds us to, from the canvas [KP#]"}}:::partner

  act -->|fills| role
  actAI -->|assists in| role
  ctr -->|binds| act
  ctr -->|binds| kp
  role -->|performs| bproc
  bproc -->|owned by| role
  bproc -->|realizes| bsvc
  bsvc -->|delivers| cap
  bsvc -->|reached through| ch

  classDef business fill:#fffbb5,stroke:#c8c04a,color:#333
  classDef ai fill:#c2f0ff,stroke:#0288d1,color:#333
  classDef role fill:#f7f099,stroke:#b8ad3f,color:#333
  classDef service fill:#efe57d,stroke:#b8ad3f,color:#333
  classDef contract fill:#d9cc4a,stroke:#a89a34,color:#333
  classDef capability fill:#f5deaa,stroke:#c8a24a,color:#333
  classDef channel fill:#e5d95f,stroke:#a89a34,color:#333
  classDef partner fill:#f7f099,stroke:#b8ad3f,color:#333
```

An AI actor takes the application cyan, so a reader never mistakes it for a
person. The capability, the channel and the key partner are visitors from the
strategy layer and the canvases and keep their colours.

## Layer view

```mermaid
flowchart LR
  act1(["⚇ The Requester (Human) [ACT1]"]):::business
  act2(["⚇ The AI agent (AI) [ACT2]"]):::ai
  role1["⚉ Method maintainer [ROLE1]"]:::role
  ctr1[/"❒ Model provider subscription and usage terms [CTR1]"/]:::contract
  kp1{{"⧉ AI model providers [KP1]"}}:::partner
  p1{{"⚙ Deliver the product [BPROC1]"}}:::business
  b1(["⬭ The method, published and installable [BSVC1]"]):::service
  c1["✦ Method development [CAP1]"]:::capability
  ch1["⊸ The public repository [CH1]"]:::channel

  act1 -->|fills| role1
  act2 -->|assists in| role1
  ctr1 -->|binds| act1
  ctr1 -->|binds| kp1
  p1 -->|owned by| role1
  p1 -->|realizes| b1
  b1 -->|delivers| c1
  b1 -->|reached through| ch1

  classDef business fill:#fffbb5,stroke:#c8c04a,color:#333
  classDef ai fill:#c2f0ff,stroke:#0288d1,color:#333
  classDef role fill:#f7f099,stroke:#b8ad3f,color:#333
  classDef service fill:#efe57d,stroke:#b8ad3f,color:#333
  classDef contract fill:#d9cc4a,stroke:#a89a34,color:#333
  classDef capability fill:#f5deaa,stroke:#c8a24a,color:#333
  classDef channel fill:#e5d95f,stroke:#a89a34,color:#333
  classDef partner fill:#f7f099,stroke:#b8ad3f,color:#333
```

One person fills every role and an agent assists in two of them. One process
realizes the two services that scale; one role performs the service that does
not.
