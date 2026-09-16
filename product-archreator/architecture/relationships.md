# Relationships

_[← Front door](./README.md)_

Every relationship of this model, declared once: the source element, the target, the relationship as the diagrams name it, and a note where one is owed. A page draws and names its relationships; agents and validators read them here.

## Layer 1 — Strategy

### [Motivation](./1_strategy/1_motivation.md)

| From | To | Relationship | Notes |
| ---- | -- | ------------ | ----- |
| `ASM1` | `DRV1` | evidences |  |
| `ASM2` | `DRV3` | evidences |  |
| `ASM3` | `DRV2` | evidences |  |
| `ASM4` | `DRV2` | evidences |  |
| `ASM5` | `DRV2` | evidences |  |
| `ASM6` | `DRV1` | evidences |  |
| `ASM7` | `DRV3` | evidences |  |
| `ASM8` | `DRV3` | evidences |  |
| `DRV1` | `ORG.DRV5` | sharpens |  |
| `DRV1` | `STK1` | pressing on |  |
| `DRV1` | `STK3` | pressing on |  |
| `DRV2` | `ORG.DRV3` | sharpens |  |
| `DRV2` | `STK2` | pressing on |  |
| `DRV3` | `ORG.DRV3` | sharpens |  |
| `DRV3` | `STK2` | pressing on |  |
| `DRV3` | `STK3` | pressing on |  |
| `G1` | `ASM3` | against |  |
| `G1` | `ASM5` | against |  |
| `G1` | `ORG.G3` | serves |  |
| `G2` | `ASM1` | against |  |
| `G2` | `ORG.G1` | serves |  |
| `G3` | `ASM2` | against |  |
| `G3` | `ASM7` | against |  |
| `G3` | `ASM8` | against |  |
| `G3` | `ORG.G3` | serves |  |
| `G4` | `ASM3` | against |  |
| `G4` | `ORG.G4` | serves |  |
| `G5` | `ASM3` | against |  |
| `G5` | `ORG.G3` | serves |  |
| `G6` | `ASM6` | against |  |
| `G6` | `ORG.G5` | serves |  |
| `G7` | `ASM7` | against |  |
| `G7` | `ASM8` | against |  |
| `G7` | `ORG.G1` | serves |  |
| `STK1` | `ORG.CS1` | refines |  |
| `STK1` | `ORG.CS3` | refines |  |
| `STK2` | `ORG.CS1` | refines |  |
| `STK2` | `ORG.CS2` | refines |  |
| `STK3` | `ORG.CS1` | refines |  |
| `STK3` | `ORG.CS2` | refines |  |
| `STK4` | `ORG.STK4` | refines |  |
| `STK5` | `ORG.CS3` | refines |  |

## Layer 2 — Business

### [Business services](./2_business/1_business-services.md)

| From | To | Relationship | Notes |
| ---- | -- | ------------ | ----- |
| `BSVC1` | `ACMP1` | realized by |  |
| `BSVC2` | `ACMP1` | realized by |  |
| `BSVC2` | `BSVC1` | flows to |  |
| `BSVC3` | `ACMP2` | realized by |  |
| `BSVC3` | `ACMP3` | realized by |  |
| `BSVC3` | `ACMP4` | realized by |  |
| `BSVC3` | `ACMP13` | realized by |  |
| `BSVC3` | `BSVC1` | serves |  |
| `BSVC4` | `ACMP1` | realized by |  |
| `BSVC4` | `BSVC1` | serves |  |
| `BSVC5` | `ACMP10` | realized by |  |
| `BSVC5` | `ACMP11` | realized by |  |
| `BSVC5` | `ACMP8` | realized by |  |
| `BSVC5` | `ACMP9` | realized by |  |
| `BSVC5` | `BSVC2` | serves |  |
| `BSVC6` | `ACMP1` | realized by |  |
| `BSVC6` | `BSVC1` | serves |  |
| `BSVC7` | `ACMP5` | realized by |  |
| `BSVC7` | `ACMP6` | realized by |  |
| `BSVC7` | `BSVC1` | serves |  |
| `BSVC8` | `ACMP12` | realized by |  |
| `BSVC8` | `BSVC5` | serves |  |

## Layer 3 — Information

### [Data domains and objects](./3_information/1_data-domains-and-objects.md)

| From | To | Relationship | Notes |
| ---- | -- | ------------ | ----- |
| `DOBJ1` | `DOBJ2` | influences |  |
| `DOBJ2` | `DOBJ3` | flows to |  |

## Layer 4 — Application

### [Application services](./4_application/1_application-services.md)

| From | To | Relationship | Notes |
| ---- | -- | ------------ | ----- |
| `ASVC1` | `ACMP1` | realized by |  |
| `ASVC1` | `BSVC1` | serves |  |
| `ASVC1` | `BSVC2` | serves |  |
| `ASVC1` | `BSVC6` | serves |  |
| `ASVC2` | `ACMP1` | realized by |  |
| `ASVC2` | `BSVC4` | serves |  |
| `ASVC3` | `ACMP2` | realized by |  |
| `ASVC3` | `ACMP3` | realized by |  |
| `ASVC3` | `ACMP4` | realized by |  |
| `ASVC3` | `ACMP13` | realized by |  |
| `ASVC3` | `BSVC3` | serves |  |
| `ASVC4` | `ACMP7` | realized by |  |
| `ASVC4` | `BSVC3` | serves |  |
| `ASVC5` | `ACMP8` | realized by |  |
| `ASVC5` | `ACMP9` | realized by |  |
| `ASVC5` | `BSVC5` | serves |  |
| `ASVC6` | `ACMP10` | realized by |  |
| `ASVC6` | `ACMP11` | realized by |  |
| `ASVC6` | `BSVC5` | serves |  |
| `ASVC7` | `ACMP5` | realized by |  |
| `ASVC7` | `ACMP6` | realized by |  |
| `ASVC7` | `BSVC7` | serves |  |
| `ASVC8` | `ACMP5` | realized by |  |
| `ASVC8` | `BSVC7` | serves |  |
| `ASVC9` | `ACMP12` | realized by |  |
| `ASVC9` | `BSVC8` | serves |  |

### [Application components](./4_application/2_application-components.md)

| From | To | Relationship | Notes |
| ---- | -- | ------------ | ----- |
| `ACMP1` | `ACMP9` | emits from |  |
| `ACMP2` | `ACMP4` | imports |  |
| `ACMP3` | `ACMP4` | imports |  |
| `ACMP4` | `ASVC7` | realizes |  |
| `ACMP5` | `ACMP4` | imports |  |
| `ACMP6` | `ACMP4` | imports |  |
| `ACMP7` | `ACMP1` | checks |  |
| `ACMP8` | `ACMP2` | aggregates |  |
| `ACMP8` | `ACMP3` | aggregates |  |
| `ACMP8` | `ACMP4` | aggregates |  |
| `ACMP8` | `ACMP13` | aggregates |  |

## Layer 5 — Technology

### [Technology and deployment](./5_technology/1_technology-and-deployment.md)

| From | To | Relationship | Notes |
| ---- | -- | ------------ | ----- |
| `ART1` | `NODE4` | deployed to |  |
| `NODE1` | `ART1` | flows to | Resolved from the marketplace manifest at install time |
| `NODE1` | `NODE2` | triggers | Every push and pull request runs the three validators |
| `NODE1` | `NODE3` | flows to | The guidance site is deployed by the method repository's own workflow |
| `NODE1` | `TSVC1` | provides |  |
| `NODE2` | `TSVC2` | provides |  |
| `NODE3` | `TSVC3` | provides |  |
| `NODE4` | `TSVC4` | provides |  |
| `NODE5` | `DOBJ3.1` | accesses | Written into the project's gitignored work area, and thrown away |
| `NODE5` | `NODE2` | serves | The validators are Python and nothing else |
| `NODE5` | `NODE4` | serves | The reading tools run wherever the adopter already works |
| `NODE5` | `TSVC5` | provides |  |
