#!/usr/bin/env python3
"""Check that relative Markdown links in this repo resolve to real files.

Two categories of link are deliberately not flagged:

- Links inside fenced code blocks or inline code spans — skill files quote
  illustrative link syntax (e.g. `./<n>_*.md`) as examples, not real links.
- Links under docs/ea/ whose target is a numbered EA content file
  (`<n>_kebab-name.md`) that doesn't exist yet — layer READMEs deliberately
  forward-reference the numbered docs a downstream project will write; a
  pure, unfilled template (like this repo's own main branch) is expected to
  have every one of these unresolved.
"""
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")
NUMBERED_EA_DOC_RE = re.compile(r"^\d+_[\w.-]+\.md$")


def is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:", "#"))


def strip_code(text: str) -> str:
    text = FENCE_RE.sub("", text)
    text = INLINE_CODE_RE.sub("", text)
    return text


def is_expected_forward_reference(resolved: Path) -> bool:
    try:
        resolved.relative_to(REPO_ROOT / "docs" / "ea")
    except ValueError:
        return False
    return bool(NUMBERED_EA_DOC_RE.match(resolved.name))


def check_file(md_file: Path) -> list[str]:
    errors = []
    text = strip_code(md_file.read_text(encoding="utf-8"))
    for match in LINK_RE.finditer(text):
        target = match.group(1).strip()
        if not target or is_external(target):
            continue
        path_part = target.split("#", 1)[0]
        if not path_part:
            continue
        resolved = (md_file.parent / path_part).resolve()
        if resolved.exists() or is_expected_forward_reference(resolved):
            continue
        errors.append(f"{md_file.relative_to(REPO_ROOT)}: broken link -> {target}")
    return errors


def main() -> int:
    all_errors = []
    for md_file in REPO_ROOT.rglob("*.md"):
        if ".git" in md_file.parts:
            continue
        all_errors.extend(check_file(md_file))
    if all_errors:
        print("Broken relative links found:")
        for error in all_errors:
            print(f"  {error}")
        return 1
    print("All relative Markdown links resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
