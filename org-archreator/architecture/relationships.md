# Relationships

_[← Front door](./README.md)_

Every relationship of this model, declared once: the source element, the target, the relationship as the diagrams name it, and a note where one is owed. A page draws and names its relationships; agents and validators read them here.

## Layer 0 — Business design

### [Value proposition canvas](./0_business-design/1_value-proposition-canvas.md)

| From | To | Relationship | Notes |
| ---- | -- | ------------ | ----- |
| `GAIN1` | `CS3` | strongest for |  |
| `GAIN2` | `CS2` | strongest for |  |
| `GAIN3` | `CS1` | strongest for |  |
| `GAIN4` | `CS2` | strongest for |  |
| `GAIN5` | `CS1` | strongest for |  |
| `GAIN6` | `CS3` | strongest for |  |
| `GCRE1` | `GAIN1` | creates |  |
| `GCRE2` | `GAIN2` | creates |  |
| `GCRE3` | `GAIN3` | creates |  |
| `GCRE4` | `GAIN4` | creates |  |
| `GCRE5` | `GAIN5` | creates |  |
| `GCRE6` | `GAIN6` | creates |  |
| `PAIN1` | `DRV1` | is the source of |  |
| `PAIN2` | `DRV2` | is the source of |  |
| `PAIN3` | `DRV3` | is the source of |  |
| `PAIN4` | `DRV4` | is the source of |  |
| `PAIN5` | `DRV5` | is the source of |  |
| `PAIN6` | `DRV7` | is the source of |  |
| `PREL1` | `PAIN1` | relieves |  |
| `PREL2` | `PAIN2` | relieves |  |
| `PREL3` | `PAIN3` | relieves |  |
| `PREL4` | `PAIN4` | relieves |  |
| `PREL5` | `PAIN5` | relieves |  |
| `PREL6` | `PAIN6` | relieves |  |
| `PROD1` | `CH1` | carried by |  |
| `PROD1` | `CH2` | carried by |  |
| `PROD1` | `CH3` | carried by |  |
| `PROD1` | `CR1` | contact is |  |
| `PROD1` | `CS1` | serves |  |
| `PROD1` | `CS2` | serves |  |
| `PROD1` | `GCRE1` | offers |  |
| `PROD1` | `GCRE2` | offers |  |
| `PROD1` | `GCRE3` | offers |  |
| `PROD1` | `GCRE4` | offers |  |
| `PROD1` | `GCRE5` | offers |  |
| `PROD1` | `GCRE6` | offers |  |
| `PROD1` | `PREL1` | offers |  |
| `PROD1` | `PREL2` | offers |  |
| `PROD1` | `PREL3` | offers |  |
| `PROD1` | `PREL4` | offers |  |
| `PROD1` | `PREL5` | offers |  |
| `PROD1` | `PREL6` | offers |  |
| `PROD1` | `RS1` | produces |  |
| `PROD1` | `RS2` | produces |  |
| `PROD2` | `CH4` | carried by |  |
| `PROD2` | `CR2` | contact is |  |
| `PROD2` | `CS3` | serves |  |
| `PROD2` | `GCRE1` | offers |  |
| `PROD2` | `GCRE5` | offers |  |
| `PROD2` | `PREL2` | offers |  |
| `PROD2` | `PREL5` | offers |  |
| `PROD2` | `RS3` | produces |  |

### [Business model canvas](./0_business-design/2_business-model-canvas.md)

| From | To | Relationship | Notes |
| ---- | -- | ------------ | ----- |
| `CH1` | `CS1` | reaches |  |
| `CH1` | `CS2` | reaches |  |
| `CH2` | `CS1` | reaches |  |
| `CH2` | `CS2` | reaches |  |
| `CH3` | `CS1` | reaches |  |
| `CH3` | `CS2` | reaches |  |
| `CH4` | `CS3` | reaches |  |
| `COST1` | `PROD1` | is spent on |  |
| `COST1` | `PROD2` | is spent on |  |
| `COST2` | `PROD1` | is spent on |  |
| `COST2` | `PROD2` | is spent on |  |
| `COST3` | `PROD1` | is spent on |  |
| `KA1` | `PROD1` | delivers |  |
| `KA2` | `PROD1` | delivers |  |
| `KA3` | `PROD2` | delivers |  |

## Layer 1 — Strategy

### [Motivation](./1_strategy/1_motivation.md)

| From | To | Relationship | Notes |
| ---- | -- | ------------ | ----- |
| `ASM1` | `PAIN1` | derived from |  |
| `ASM2` | `PAIN2` | derived from |  |
| `ASM3` | `PAIN3` | derived from |  |
| `ASM4` | `PAIN4` | derived from |  |
| `ASM5` | `PAIN5` | derived from |  |
| `ASM6` | `PAIN6` | derived from |  |
| `DRV1` | `ASM1` | evidenced by |  |
| `DRV2` | `ASM2` | evidenced by |  |
| `DRV3` | `ASM3` | evidenced by |  |
| `DRV4` | `ASM4` | evidenced by |  |
| `DRV5` | `ASM5` | evidenced by |  |
| `DRV7` | `ASM6` | evidenced by |  |
| `OUT1` | `G1` | measures |  |
| `OUT1` | `GAIN1` | derived from |  |
| `OUT2` | `G1` | measures |  |
| `OUT2` | `G3` | measures |  |
| `OUT2` | `GAIN2` | derived from |  |
| `OUT3` | `G2` | measures |  |
| `OUT3` | `GAIN3` | derived from |  |
| `OUT4` | `G3` | measures |  |
| `OUT4` | `GAIN4` | derived from |  |
| `OUT5` | `G4` | measures |  |
| `OUT5` | `GAIN5` | derived from |  |
| `OUT6` | `G5` | measures |  |
| `OUT6` | `GAIN6` | derived from |  |
| `OUT7` | `G7` | measures |  |
| `OUT7` | `PREL6` | derived from |  |
| `STK1` | `CS1` | derived from |  |
| `STK1` | `DRV1` | concerned with |  |
| `STK1` | `DRV2` | concerned with |  |
| `STK1` | `DRV5` | concerned with |  |
| `STK1` | `DRV7` | concerned with |  |
| `STK2` | `CS2` | derived from |  |
| `STK2` | `DRV2` | concerned with |  |
| `STK2` | `DRV3` | concerned with |  |
| `STK2` | `DRV5` | concerned with |  |
| `STK3` | `CS3` | derived from |  |
| `STK3` | `DRV1` | concerned with |  |
| `STK3` | `DRV3` | concerned with |  |
| `STK3` | `DRV4` | concerned with |  |
| `STK4` | `COST1` | derived from |  |
| `STK4` | `DRV5` | concerned with |  |
| `STK4` | `DRV6` | concerned with |  |
| `STK4` | `KR1` | derived from |  |

### [Capabilities and the value stream](./1_strategy/2_capabilities-and-value-stream.md)

| From | To | Relationship | Notes |
| ---- | -- | ------------ | ----- |
| `CAP1` | `CAP2` | its output is published by |  |
| `CAP1` | `CAP3` | its output is delivered by |  |
| `CAP1` | `KA1` | derived from |  |
| `CAP1` | `VAL1` | delivers |  |
| `CAP1` | `VAL2` | delivers |  |
| `CAP1` | `VAL3` | delivers |  |
| `CAP1` | `VAL4` | delivers |  |
| `CAP1` | `VAL5` | delivers |  |
| `CAP1` | `VS1.2` | serves |  |
| `CAP1` | `VS1.3` | serves |  |
| `CAP1` | `VS1.4` | serves |  |
| `CAP1` | `VS1.5` | serves |  |
| `CAP1.3` | `VS1.6` | serves |  |
| `CAP2` | `CAP1` | brings the use that feeds |  |
| `CAP2` | `KA2` | derived from |  |
| `CAP2` | `VAL4` | delivers |  |
| `CAP2` | `VS1.1` | serves |  |
| `CAP3` | `CAP1` | feeds experience back to |  |
| `CAP3` | `KA3` | derived from |  |
| `CAP3` | `VAL1` | delivers |  |
| `CAP3` | `VAL2` | delivers |  |
| `CAP3.1` | `VS1.2` | serves |  |
| `CAP3.2` | `VS1.5` | serves |  |
| `VAL1` | `STK1` | strongest for |  |
| `VAL1` | `STK3` | strongest for |  |
| `VAL2` | `STK1` | strongest for |  |
| `VAL2` | `STK3` | strongest for |  |
| `VAL3` | `STK2` | strongest for |  |
| `VAL3` | `STK3` | strongest for |  |
| `VAL4` | `STK1` | strongest for |  |
| `VAL4` | `STK3` | strongest for |  |
| `VAL5` | `STK3` | strongest for |  |
| `VS1.1` | `VS1.2` | flows to |  |
| `VS1.2` | `VS1.3` | flows to |  |
| `VS1.3` | `VS1.4` | flows to |  |
| `VS1.4` | `VS1.5` | flows to |  |
| `VS1.5` | `VS1.6` | flows to |  |
| `VS1.6` | `VS1.2` | real use changes the method |  |

## Layer 2 — Business

### [Business architecture](./2_business/1_business-architecture.md)

| From | To | Relationship | Notes |
| ---- | -- | ------------ | ----- |
| `ACT1` | `DOBJ2` | owns |  |
| `ACT1` | `ROLE1` | fills |  |
| `ACT1` | `ROLE2` | fills |  |
| `ACT1` | `ROLE3` | fills |  |
| `ACT2` | `ROLE1` | assists in |  |
| `ACT2` | `ROLE2` | assists in |  |
| `BPROC1` | `BPROC2` | real use feeds |  |
| `BPROC1` | `BSVC1` | realizes |  |
| `BPROC1` | `BSVC2` | realizes |  |
| `BPROC1` | `ROLE1` | owned by |  |
| `BPROC1.1` | `BPROC1.2` | triggers |  |
| `BPROC1.1` | `ROLE1` | owned by |  |
| `BPROC1.2` | `BPROC1.3` | triggers |  |
| `BPROC1.2` | `ROLE1` | owned by |  |
| `BPROC1.3` | `BPROC2.1` | triggers |  |
| `BPROC1.3` | `ROLE1` | owned by |  |
| `BPROC2` | `BPROC1` | method changes re-enter |  |
| `BPROC2` | `ROLE1` | owned by |  |
| `BPROC2.1` | `BPROC2.2` | triggers |  |
| `BPROC2.1` | `ROLE1` | owned by |  |
| `BPROC2.2` | `BPROC1.1` | triggers |  |
| `BPROC2.2` | `ROLE1` | owned by |  |
| `BSVC1` | `CAP1` | delivers |  |
| `BSVC1` | `CH1` | reached through |  |
| `BSVC1` | `CH3` | reached through |  |
| `BSVC2` | `CAP2` | delivers |  |
| `BSVC2` | `CH1` | reached through |  |
| `BSVC2` | `CH2` | reached through |  |
| `BSVC3` | `CAP3` | delivers |  |
| `BSVC3` | `CH4` | reached through |  |
| `CTR1` | `ACT1` | binds |  |
| `CTR1` | `KP1` | binds |  |
| `CTR2` | `ACT1` | binds |  |
| `CTR2` | `KP2` | binds |  |
| `ROLE2` | `BSVC3` | performs |  |
| `ROLE2` | `DOBJ1` | owns |  |
| `ROLE3` | `BPROC1.1` | triggers |  |

## Layer 3 — Information

### [Information domains and objects](./3_information/1_information-domains-and-objects.md)

| From | To | Relationship | Notes |
| ---- | -- | ------------ | ----- |
| `DOBJ1.2` | `DOBJ3` | flows to |  |
| `DOBJ3` | `DOBJ2.1` | influences |  |
