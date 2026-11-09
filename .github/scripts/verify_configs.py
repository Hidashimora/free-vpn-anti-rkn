#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Consistency checker for the published subscription lists.

Run it after update_configs.py (the workflow does this automatically) or by
hand before opening a pull request:

    python3 .github/scripts/verify_configs.py

It fails with a non-zero exit code when the repository is internally
inconsistent, which is what guards against the class of bug that produced the
"7 identical configs in every N.2 file" incident:

  * a published list is empty or contains only its header line
  * a published line is not a supported URI scheme
  * a list contains duplicates
  * configs/counts.json disagrees with the actual file contents
  * counts.json lists a file that does not exist, or misses a published file
  * configs/sources.json reports a list as `ok` whose file is empty
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = REPO_ROOT / "configs"

SCHEME_RE = re.compile(r"^(vless|trojan|vmess|ss|hy2)://")
HEADER_PREFIX = "#"

errors: list[str] = []
warnings: list[str] = []


def load_json(name: str) -> dict:
    path = CONFIG_DIR / name
    if not path.is_file():
        errors.append(f"missing file: configs/{name}")
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"configs/{name} is not valid JSON: {exc}")
        return {}


def read_uris(path: Path) -> list[str]:
    return [
        line.strip()
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines()
        if SCHEME_RE.match(line.strip())
    ]


def check_index_html(published: dict[str, int]) -> None:
    """Every subscription the site links to must exist and have a count.

    index.html builds its links as `<base><id>.txt` and looks counts up in
    configs/counts.json, so a stale id in its Alpine arrays would render a dead
    link on GitHub Pages.
    """
    path = REPO_ROOT / "index.html"
    if not path.is_file():
        warnings.append("index.html not found; skipped the site consistency check")
        return

    html = path.read_text(encoding="utf-8", errors="replace")

    short_block = re.search(r"configs:\s*\[(.*?)\],\s*fullConfigs:", html, re.S)
    full_block = re.search(r"fullConfigs:\s*\[(.*?)\n\s*\],", html, re.S)

    if not short_block or not full_block:
        warnings.append("index.html: could not locate the configs/fullConfigs arrays; skipped")
        return

    short_ids = []
    for quoted, plain in re.findall(r"\{\s*id:\s*(?:'([^']+)'|(\d+))\s*\}", short_block.group(1)):
        short_ids.append(quoted or plain)
    full_ids = re.findall(r"\{\s*id:\s*'([^']+)'", full_block.group(1))

    if not short_ids:
        warnings.append("index.html: no short-list ids parsed; skipped")

    for lid in short_ids + full_ids:
        if lid not in published:
            errors.append(f"index.html links configs/{lid}.txt but counts.json has no such list")
        elif not (CONFIG_DIR / f"{lid}.txt").is_file():
            errors.append(f"index.html links configs/{lid}.txt but the file does not exist")
        elif published[lid] == 0:
            errors.append(f"index.html links configs/{lid}.txt which is empty")

    # the raw base URL used by the site must point at this repository
    base_match = re.search(r"base:\s*'([^']+)'", html)
    if base_match and "Hidashimora/free-vpn-anti-rkn" not in base_match.group(1):
        errors.append(f"index.html uses an unexpected base URL: {base_match.group(1)}")

    # the removed upstream must not be linked as a live source any more
    if "github.com/AvenCores/goida-vpn-configs" in html.replace("github.com/AvenCores`", ""):
        if re.search(r'href="https://github\.com/AvenCores/goida-vpn-configs"', html):
            errors.append("index.html still contains a clickable link to the removed AvenCores repository")

    print(f"index.html ids  : {len(short_ids)} short + {len(full_ids)} extended")


def main() -> int:
    counts = load_json("counts.json")
    sources = load_json("sources.json")

    published = {k: v for k, v in counts.items() if k != "totalUnique" and isinstance(v, int)}
    if not published:
        errors.append("counts.json has no published list entries")

    actual: dict[str, int] = {}
    for lid in published:
        path = CONFIG_DIR / f"{lid}.txt"
        if not path.is_file():
            errors.append(f"counts.json lists '{lid}' but configs/{lid}.txt does not exist")
            continue
        lines = read_uris(path)
        actual[lid] = len(lines)

        # header line present and everything else a valid URI
        raw_lines = [
            l for l in path.read_text(encoding="utf-8", errors="replace").splitlines() if l.strip()
        ]
        body = [l for l in raw_lines if not l.lstrip().startswith(HEADER_PREFIX)]
        bad = [l for l in body if not SCHEME_RE.match(l.strip())]
        if bad:
            errors.append(f"configs/{lid}.txt has {len(bad)} non-URI line(s), e.g. {bad[0][:80]!r}")
        if not lines:
            errors.append(f"configs/{lid}.txt is empty (header only) — a published list must not be empty")
        if len(set(lines)) != len(lines):
            errors.append(f"configs/{lid}.txt contains duplicates ({len(lines) - len(set(lines))})")
        if published[lid] != actual[lid]:
            errors.append(
                f"counts.json says {lid}={published[lid]} but configs/{lid}.txt has {actual[lid]} servers"
            )

    # files present but not published (frozen legacy files)
    published_files = {f"{lid}.txt" for lid in published}
    for path in sorted(CONFIG_DIR.glob("*.txt")):
        if path.name in published_files:
            continue
        n = len(read_uris(path))
        if n == 0:
            warnings.append(f"legacy file configs/{path.name} is empty (header only)")

    # totalUnique must match the union of the published files
    union: set[str] = set()
    for lid in published:
        path = CONFIG_DIR / f"{lid}.txt"
        if path.is_file():
            union.update(read_uris(path))
    reported_total = counts.get("totalUnique")
    if reported_total != len(union):
        errors.append(
            f"counts.json totalUnique={reported_total} but the union of published files is {len(union)}"
        )

    # ---- index.html must only reference files that exist --------------------
    check_index_html(published)

    # sources.json must not claim `ok` for an empty file
    lists_report = sources.get("lists", {}) if isinstance(sources, dict) else {}
    for lid, entry in lists_report.items():
        if entry.get("written") and actual.get(lid) == 0:
            errors.append(f"sources.json reports '{lid}' as written but configs/{lid}.txt is empty")
    summary = sources.get("summary", {}) if isinstance(sources, dict) else {}
    stale = summary.get("staleIds", []) or []
    for lid in stale:
        if published.get(lid, 0) == 0:
            errors.append(f"'{lid}' is reported stale but its file is empty (no last known good)")

    print(f"published lists : {len(published)}")
    print(f"servers (union) : {len(union)}")
    print(f"stale lists     : {', '.join(stale) if stale else 'none'}")
    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")

    if errors:
        print(f"\nFAILED: {len(errors)} error(s)")
        return 1
    print("\nOK: configs/, counts.json and sources.json are consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
