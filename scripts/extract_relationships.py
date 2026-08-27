#!/usr/bin/env python3
"""Transcribe the relationships drawn in diagrams into relationship tables. Once.

**This is a migration tool, not a component.** It exists because
[initiative 6] moved the relationship out of Mermaid and into `BOBJ7`, and 164
relationships in this corpus were drawn and stated nowhere else. Retyping them
by hand is how a migration loses one; this reads them and writes the tables,
and a person reads what it wrote.

It is deleted in the pull request that runs it. A script that converts a
corpus once has no place in a catalogue of things the method ships, and
leaving it behind would invite somebody to run it again against documents that
have moved on.

    python3 scripts/extract_relationships.py           # print what it would add
    python3 scripts/extract_relationships.py --apply   # append the sections

**Only what is not already declared.** A diagram edge whose two ends are
already joined by a catalogue column — in either direction — is the same fact
rendered, and transcribing it would create the duplicate the initiative exists
to remove.

**The description cells are filled from the catalogue**, never invented, so
the name check in `check_model.py` is green the moment this lands. If it is
not, this script has a bug and that is exactly what the check is for. The
glyph is left off: `element-prefixes.json` types a prefix but does not carry
its glyph, and the notation makes the glyph optional in a table cell.
"""
import argparse
import sys
from collections import defaultdict
from pathlib import Path

from model_graph import (
    PREFIX_TYPES,
    REPO_ROOT,
    find_projects,
    mermaid_edges,
    model_files,
    parse_project,
    prefix_of,
    qualifier_of,
    strip_code,
)

HEADING = "## Relationships"
NOTE = (
    "<!-- Transcribed from this document's diagrams. The identifier is\n"
    "     authoritative; the description beside it is checked against the\n"
    "     catalogue that defines the element. -->"
)


def describe(element: str, names: dict[str, str]) -> str:
    """`«Capability» Learn from an engagement` — the archetype and the name."""
    stereotype = PREFIX_TYPES.get(prefix_of(element), "")
    name = names.get(element, "")
    return " ".join(part for part in (f"«{stereotype}»" if stereotype else "", name) if part)


def proposals(project: Path) -> dict[str, list[tuple[str, str, str]]]:
    """Document -> the (source, target, label) triples it draws and never states."""
    parsed = parse_project(project, detail=True)
    declared = {
        frozenset((edge.src, edge.dst))
        for edge in parsed.edges
        if edge.origin in ("catalogue", "table")
    }
    found: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
    for md_file in model_files(project):
        raw = md_file.read_text(encoding="utf-8")
        doc = str(md_file.relative_to(REPO_ROOT)).replace("\\", "/")
        scope = ""
        parts = md_file.relative_to(project).parts
        segments = [parts[i + 1] for i, part in enumerate(parts[:-1]) if part == "domains"]
        if segments:
            scope = ".".join(s.upper() for s in segments)
        seen: set[tuple[str, str]] = set()
        for source, target, label in mermaid_edges(raw):
            src = source if qualifier_of(source) or not scope else f"{scope}.{source}"
            dst = target if qualifier_of(target) or not scope else f"{scope}.{target}"
            if src not in parsed.elements or dst not in parsed.elements:
                continue
            if frozenset((src, dst)) in declared or (src, dst) in seen:
                continue
            # A parent-to-child edge with no label is the decomposition the
            # identifier already carries. `model_graph` drops it; so does this.
            if not label and parsed.elements[dst].parent == src:
                continue
            seen.add((src, dst))
            found[doc].append((src, dst, label or "relates to"))
    return found


def table(rows: list[tuple[str, str, str]], names: dict[str, str]) -> str:
    lines = [
        HEADING,
        "",
        NOTE,
        "",
        "| From | From element | To | To element | Relationship |",
        "| ---- | ------------ | -- | ---------- | ------------ |",
    ]
    for src, dst, label in rows:
        lines.append(
            f"| `{src}` | {describe(src, names)} | `{dst}` | "
            f"{describe(dst, names)} | {label} |"
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):  # pragma: no cover
            pass
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--apply", action="store_true", help="append the sections")
    args = parser.parse_args()

    total = 0
    for project in find_projects():
        parsed = parse_project(project, detail=True)
        if not parsed.elements:
            continue
        names = {key: element.name for key, element in parsed.elements.items()}
        for doc, rows in sorted(proposals(project).items()):
            total += len(rows)
            body = table(rows, names)
            if not args.apply:
                print(f"\n===== {doc} — {len(rows)} relationship(s) =====\n{body}")
                continue
            path = REPO_ROOT / doc
            text = path.read_text(encoding="utf-8")
            joiner = "" if text.endswith("\n\n") else ("\n" if text.endswith("\n") else "\n\n")
            path.write_text(text + joiner + body, encoding="utf-8")
            print(f"  {doc}: +{len(rows)} relationship(s)")
    print(f"\n{total} relationship(s) {'written' if args.apply else 'to transcribe'}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
