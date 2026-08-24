# Business objects

_[← Business layer](./README.md) · [EA home](../README.md)_

**ArchiMate viewpoint:** Business. The things the method's services create,
read and hand to each other.

**Status:** ● Validated at **Gate 2**, 2026-08-22.

Every object here is a **Markdown file in git**, and that is the point rather
than an implementation detail: it is what makes the model readable by the
agent the method is written for, diffable in review, and versioned by
something nobody has to operate.

## How to read this document

```mermaid
flowchart LR
  bobj["▧ «Business Object» something the services handle"]:::object
  bsvc(["⬭ «Business Service» — context, from services"]):::service

  bsvc -->|accesses| bobj

  classDef object fill:#fffbb5,stroke:#c8c04a,color:#333
  classDef service fill:#efe57d,stroke:#b8ad3f,color:#333
```

| Glyph | Shape | Element | ID prefix | Reads as |
| ----- | ----- | ------- | --------- | -------- |
| `▧` | Rectangle | «Business Object» | `BOBJ` | `BOBJ1` = Business Object 1 |
| `⬭` | Stadium | «Business Service» — context, from [2_business-services.md](./2_business-services.md) | `BSVC` | `BSVC1` = Business Service 1 |

## The objects

```mermaid
flowchart TB
  bobj1["▧ The architecture model [BOBJ1]"]:::object
  bobj2["▧ The element [BOBJ2]"]:::object
  bobj3["▧ The scope document [BOBJ3]"]:::object
  bobj4["▧ The decision record [BOBJ4]"]:::object
  bobj5["▧ The gate approval [BOBJ5]"]:::object
  bobj6["▧ The skill [BOBJ6]"]:::object

  bobj1 -->|composed of| bobj2
  bobj3 -->|records| bobj5
  bobj3 -->|changes| bobj1
  bobj4 -->|explains a row of| bobj1
  bobj6 -->|produces| bobj3

  classDef object fill:#fffbb5,stroke:#c8c04a,color:#333
```

| ID | Business object | What it is | On disk | Accessed by |
| -- | --------------- | ---------- | ------- | ----------- |
| `BOBJ1` | **The architecture model** | Six numbered layers describing one subject as it is today, in assessment order | `architecture/0_*` … `architecture/5_*` | `BSVC1`, `BSVC2`, `BSVC3`, `BSVC6` |
| `BOBJ2` | **The element** | One identified thing in the model — a stakeholder, a capability, a service — carrying a type prefix, a number, a name, and what realizes it | A row in an inventory table, or a bolded lead-in | `BSVC1`, `BSVC3` |
| `BOBJ3` | **The scope document** | One initiative: what changes at each layer, what was approved, what was deliberately left out | `architecture/scope/<n>_<slug>.md` | `BSVC1`, `BSVC4` |
| `BOBJ4` | **The decision record** | One call too small to be an initiative, with the option that was rejected | `architecture/decisions/<n>_<slug>.md` | `BSVC4` |
| `BOBJ5` | **The gate approval** | Which gate, who approved, when, and what they were shown | A row in `BOBJ3`'s Approvals table | `BSVC1`, `BSVC4` |
| `BOBJ6` | **The skill** | One procedure, template or rulebook, in a fixed section format, bound by its frontmatter to the process it realizes | `plugins/archreator/skills/<name>/SKILL.md` | `BSVC5` |

**`BOBJ5` has no file of its own, and that is deliberate.** An approval is a
row inside the document it approves, so a reader who has the initiative has
its approvals, and nobody can find one without the other. Giving it a file
would make an approval something that could go missing from the thing it
authorized.

**`BOBJ2` is the object every validator is really about.** `BSVC3` checks that
elements resolve, are not defined twice, and do not outlive their retirement.
That is the whole of what can be checked mechanically, and it is checked
because an agent reasoning from a deleted element fails silently.

**`BOBJ3` and `BOBJ4` are immutable once merged.** They record what was true
and approved at a moment; the model moves on and they do not. This is why the
validators skip `scope/` and `decisions/` entirely — reference-checking a
frozen document is incoherent rather than merely awkward.
