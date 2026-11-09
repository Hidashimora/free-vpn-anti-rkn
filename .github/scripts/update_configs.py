#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fail-safe updater for the published VPN subscription lists of
https://github.com/Hidashimora/free-vpn-anti-rkn

Why this script exists
----------------------
The previous implementation was a single shell step inside
.github/workflows/update-vpn-config.yml. It had two fatal flaws:

1. It reused one shared temporary file (`full.txt`) for every iteration and
   called `curl -sLf ... -o full.txt || true`. When the upstream returned an
   error (404/429/...) curl left the *previously written* `full.txt` untouched
   and `touch full.txt` did not truncate it either. The following `grep`
   therefore re-read the previous loop's data and wrote it to every output
   file. On 2026-11-09T02:32Z (commit 4184c16d1) this overwrote
   configs/1.2.txt .. configs/26.2.txt with the 7 leftover lines of igareck's
   WHITE-SNI-RU-all.txt.

2. It wrote output files unconditionally, so an empty fetch replaced a good,
   non-empty list and "last known good" was destroyed.

This script fixes both: every fetch is independent (no shared temp state), the
result is validated *before* anything is written, and a list that cannot be
refreshed keeps its last known good content and is reported as `stale`.

Outputs
-------
  configs/<id>.txt     refreshed subscription lists (never emptied)
  configs/counts.json  per-list server counts + totalUnique
  configs/sources.json machine-readable provenance / health report

No third-party dependencies: standard library only, so it behaves identically
on GitHub Actions runners and on a local machine.
"""

from __future__ import annotations

import base64
import datetime
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

# --------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = REPO_ROOT / "configs"

USER_AGENT = "free-vpn-anti-rkn-updater/2.0 (+https://github.com/Hidashimora/free-vpn-anti-rkn)"

# Only lines starting with a supported scheme are published.
SCHEME_RE = re.compile(r"^(vless|trojan|vmess|ss|hy2)://")

# Caps. These bound client load and the size of every commit: the repository is
# public and large, so the published payload must not grow without a limit.
MAX_SHORT = 300   # <id>.1 files (and single-file lists)
MAX_FULL = 500    # <id>.2 files

# Safety net: never replace a non-empty list with a much smaller one.
MIN_SHRINK_RATIO = 0.5
MIN_SHRINK_FLOOR = 20

HTTP_TIMEOUT = 240
HTTP_ATTEMPTS = 3

# --------------------------------------------------------------------------
# Sources
# --------------------------------------------------------------------------
# The original upstream, https://github.com/AvenCores/goida-vpn-configs, no
# longer resolves: the repository and the whole account answer HTTP 404, so its
# configs stopped updating for us. Lists 1..26 are therefore served by the
# surviving mirror of the same project, which keeps the identical
# `githubmirror/<n>.txt` layout and the same list order (1 = OpenRay,
# 2 = 5ubscrpt10n, ... 26 = Обход SNI/CIDR). Per-source upstream URLs are kept
# as a fallback in case the mirror disappears too.

MIRROR_REPO = "aneek0/goida-vpn-configs"
MIRROR_BASE = f"https://raw.githubusercontent.com/{MIRROR_REPO}/refs/heads/main/githubmirror"

AVENCORES_NOTE = "AvenCores/goida-vpn-configs is unreachable (HTTP 404); served by the {mirror} mirror".format(
    mirror=MIRROR_REPO
)


def mirror_url(n: int) -> str:
    return f"{MIRROR_BASE}/{n}.txt"


# list number -> (human label, upstream fallback URL or None)
MIRROR_LISTS: dict[int, tuple[str, str | None]] = {
    1: ("sakha1370/OpenRay", "https://github.com/sakha1370/OpenRay/raw/refs/heads/main/output/all_valid_proxies.txt"),
    2: ("sevcator/5ubscrpt10n", "https://raw.githubusercontent.com/sevcator/5ubscrpt10n/main/protocols/vl.txt"),
    3: ("yitong2333/proxy-minging", "https://raw.githubusercontent.com/yitong2333/proxy-minging/refs/heads/main/v2ray.txt"),
    4: ("acymz/AutoVPN", "https://raw.githubusercontent.com/acymz/AutoVPN/refs/heads/main/data/V2.txt"),
    5: ("miladtahanian/V2RayCFGDumper", "https://raw.githubusercontent.com/miladtahanian/V2RayCFGDumper/refs/heads/main/sub.txt"),
    6: ("roosterkid/openproxylist", "https://raw.githubusercontent.com/roosterkid/openproxylist/main/V2RAY_RAW.txt"),
    7: ("Epodonios/v2ray-configs", "https://github.com/Epodonios/v2ray-configs/raw/main/Splitted-By-Protocol/trojan.txt"),
    8: ("ShatakVPN/ConfigForge-V2Ray", "https://github.com/ShatakVPN/ConfigForge-V2Ray/raw/refs/heads/main/configs/vless.txt"),
    9: ("mohamadfg-dev/telegram-v2ray-configs-collector", "https://raw.githubusercontent.com/mohamadfg-dev/telegram-v2ray-configs-collector/refs/heads/main/category/vless.txt"),
    10: ("mheidari98/.proxy", "https://raw.githubusercontent.com/mheidari98/.proxy/refs/heads/main/vless"),
    11: ("youfoundamin/V2rayCollector", "https://raw.githubusercontent.com/youfoundamin/V2rayCollector/main/mixed_iran.txt"),
    12: ("VOID-Anonymity/V.O.I.D-VPN_Bypass", "https://github.com/VOID-Anonymity/V.O.I.D-VPN_Bypass/raw/refs/heads/main/url_work.txt"),
    13: ("cbusifabcap/daily_free_vpn", "https://github.com/cbusifabcap/daily_free_vpn/raw/refs/heads/main/Z.txt"),
    14: ("LalatinaHub/Mineral", "https://github.com/LalatinaHub/Mineral/raw/refs/heads/master/result/nodes"),
    15: ("miladtahanian/Config-Collector", "https://raw.githubusercontent.com/miladtahanian/Config-Collector/refs/heads/main/mixed_iran.txt"),
    16: ("Pawdroid/Free-servers", "https://raw.githubusercontent.com/Pawdroid/Free-servers/refs/heads/main/sub"),
    17: ("MhdiTaheri/V2rayCollector_Py", "https://github.com/MhdiTaheri/V2rayCollector_Py/raw/refs/heads/main/sub/Mix/mix.txt"),
    18: ("free18/v2ray", "https://raw.githubusercontent.com/free18/v2ray/refs/heads/main/v.txt"),
    19: ("MhdiTaheri/V2rayCollector", "https://github.com/MhdiTaheri/V2rayCollector/raw/refs/heads/main/sub/mix"),
    20: ("Argh94/Proxy-List", "https://github.com/Argh94/Proxy-List/raw/refs/heads/main/All_Config.txt"),
    21: ("shabane/kamaji", "https://raw.githubusercontent.com/shabane/kamaji/master/hub/merged.txt"),
    22: ("wuqb2i4f/xray-config-toolkit", "https://raw.githubusercontent.com/wuqb2i4f/xray-config-toolkit/main/output/base64/mix-uri"),
    23: ("igareck/vpn-configs-for-russia (BLACK_VLESS_RUS)", "https://github.com/igareck/vpn-configs-for-russia/raw/refs/heads/main/BLACK_VLESS_RUS.txt"),
    24: ("Mr-Meshky/vify", "https://github.com/Mr-Meshky/vify/raw/refs/heads/main/configs/vless.txt"),
    25: ("V2RayRoot/V2RayConfig", "https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/refs/heads/main/Config/vless.txt"),
    # 26 is generated by the mirror project itself ("Обход SNI/CIDR белых
    # списков") and has no independent upstream, so it mirrors itself.
    26: ("Обход SNI/CIDR белых списков", None),
}

IGARECK_REPO = "igareck/vpn-configs-for-russia"
IGARECK_BASE = f"https://raw.githubusercontent.com/{IGARECK_REPO}/main"

# list number -> (label, upstream filename)
IGARECK_LISTS: dict[int, tuple[str, str]] = {
    27: ("Shadowsocks + All (чёрный список)", "BLACK_SS%2BAll_RUS.txt"),
    28: ("VLESS все (чёрный список)", "BLACK_VLESS_RUS.txt"),
    29: ("VLESS mobile (чёрный список)", "BLACK_VLESS_RUS_mobile.txt"),
    30: ("VLESS Reality white lists mobile", "Vless-Reality-White-Lists-Rus-Mobile.txt"),
    # igareck removed Vless-Reality-White-Lists-Rus-Mobile-2.txt: the URL now
    # answers HTTP 404, so list 31 keeps its last known good content and is
    # reported as `stale` in sources.json.
    31: ("VLESS Reality white lists mobile 2", "Vless-Reality-White-Lists-Rus-Mobile-2.txt"),
    32: ("WHITE-CIDR-RU-all", "WHITE-CIDR-RU-all.txt"),
    33: ("WHITE-CIDR-RU-checked", "WHITE-CIDR-RU-checked.txt"),
    34: ("WHITE-SNI-RU-all", "WHITE-SNI-RU-all.txt"),
}

# Behaviour that must be preserved from the original pipeline: list 26 excludes
# hosts matching ".ru" (the published 26.1.txt contains 0 such entries).
EXCLUDE_SUBSTRINGS: dict[int, tuple[str, ...]] = {
    26: (".ru",),
}

# Human-readable role of every upstream host, used in configs/sources.json.
SOURCE_ROLES: dict[str, str] = {
    MIRROR_REPO: "serves lists 1-26 (mirror of the repository whose AvenCores account disappeared)",
    IGARECK_REPO: "serves lists 27-34",
    "unavailable": "upstream file removed; last known good content is being served",
}


# --------------------------------------------------------------------------
# Published-file plan
# --------------------------------------------------------------------------

def published_plan() -> list[dict]:
    """Ordered list of the subscription files this repository publishes."""
    plan: list[dict] = []
    for n in range(1, 27):
        label = MIRROR_LISTS[n][0]
        plan.append({"id": f"{n}.1", "num": n, "label": label, "cap": MAX_SHORT})
        plan.append({"id": f"{n}.2", "num": n, "label": label, "cap": MAX_FULL})
    for n in (27, 29, 30, 31, 34):
        plan.append({"id": str(n), "num": n, "label": IGARECK_LISTS[n][0], "cap": MAX_SHORT})
    for n in (28, 32, 33):
        plan.append({"id": f"{n}.1", "num": n, "label": IGARECK_LISTS[n][0], "cap": MAX_SHORT})
        plan.append({"id": f"{n}.2", "num": n, "label": IGARECK_LISTS[n][0], "cap": MAX_FULL})
    return plan


# --------------------------------------------------------------------------
# HTTP / parsing helpers
# --------------------------------------------------------------------------

def http_get(url: str) -> dict:
    """Fetch a URL once (with retries on transient errors)."""
    last_err = None
    for attempt in range(HTTP_ATTEMPTS):
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as resp:
                return {
                    "ok": True,
                    "status": resp.status,
                    "body": resp.read(),
                    "last_modified": resp.headers.get("Last-Modified"),
                    "error": None,
                }
        except urllib.error.HTTPError as exc:
            # Deterministic HTTP error (404, 403, ...): retrying will not help.
            return {"ok": False, "status": exc.code, "body": b"", "last_modified": None,
                    "error": f"HTTP {exc.code}"}
        except Exception as exc:  # noqa: BLE001 - network errors vary
            last_err = f"{type(exc).__name__}: {exc}"
            if attempt < HTTP_ATTEMPTS - 1:
                time.sleep(2 * (attempt + 1))
    return {"ok": False, "status": None, "body": b"", "last_modified": None, "error": last_err}


def extract_uris(text: str) -> list[str]:
    out: list[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if SCHEME_RE.match(line):
            out.append(line)
    return out


def _b64decode(data: str) -> str | None:
    compact = "".join(data.split())
    if len(compact) < 16:
        return None
    try:
        padded = compact + "=" * (-len(compact) % 4)
        return base64.b64decode(padded, validate=False).decode("utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        return None


def parse_configs(body: bytes) -> tuple[list[str], bool]:
    """Extract subscription URIs; returns (uris, used_base64).

    Some upstreams publish base64-encoded subscription payloads, so a direct
    scan runs first and base64 decoding is the fallback.
    """
    text = body.decode("utf-8", errors="replace")
    direct = extract_uris(text)
    if direct:
        return direct, False

    whole = _b64decode(text)
    if whole:
        decoded = extract_uris(whole)
        if decoded:
            return decoded, True

    collected: list[str] = []
    for raw in text.splitlines():
        decoded = _b64decode(raw)
        if decoded:
            collected.extend(extract_uris(decoded))
    return collected, bool(collected)


def dedupe(items: list[str]) -> list[str]:
    """Drop byte-identical duplicates, preserving order.

    Several upstreams ship the same line more than once; publishing duplicates
    would waste the per-list cap and contradict the "no repeats" promise of the
    site.
    """
    seen: set[str] = set()
    out: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


def sample_evenly(items: list[str], target: int) -> list[str]:
    """Deterministically keep at most `target` items, evenly spread."""
    n = len(items)
    if n <= target:
        return list(items)
    return [items[(k * n) // target] for k in range(target)]


def count_uris(path: Path) -> int:
    if not path.is_file():
        return 0
    try:
        return len(extract_uris(path.read_text(encoding="utf-8", errors="replace")))
    except OSError:
        return 0


def write_text_lf(path: Path, content: str) -> None:
    """UTF-8 without BOM, LF line endings."""
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(content)


def utcnow() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_previous_report() -> dict:
    path = CONFIG_DIR / "sources.json"
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except Exception:  # noqa: BLE001
        return {}


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main() -> int:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    plan = published_plan()
    previous = load_previous_report()
    prev_lists = previous.get("lists", {}) or {}

    fetch_cache: dict[str, dict] = {}
    source_cache: dict[int, dict] = {}

    def load_source(num: int) -> dict:
        """Fetch and parse one upstream list number (cached)."""
        if num in source_cache:
            return source_cache[num]

        if num in MIRROR_LISTS:
            label, fallback = MIRROR_LISTS[num]
            candidates = [(MIRROR_REPO, "mirror of the removed AvenCores repo", mirror_url(num))]
            if fallback and fallback != mirror_url(num):
                candidates.append((label, "original upstream source", fallback))
        else:
            label, filename = IGARECK_LISTS[num]
            candidates = [(IGARECK_REPO, "lists 27-34", f"{IGARECK_BASE}/{filename}")]

        result: dict = {"attempts": [], "source": None, "label": None, "url": None, "uris": []}
        for source_id, source_role, url in candidates:
            if url not in fetch_cache:
                fetch_cache[url] = http_get(url)
            res = fetch_cache[url]
            attempt = {"url": url, "httpStatus": res["status"], "error": res["error"]}
            if res["ok"]:
                found, used_b64 = parse_configs(res["body"])
                for token in EXCLUDE_SUBSTRINGS.get(num, ()):
                    found = [u for u in found if token not in u]
                found = dedupe(found)
                attempt["upstreamValid"] = len(found)
                if used_b64:
                    attempt["base64"] = True
                if found:
                    attempt["error"] = None
                    result.update({
                        "source": source_id,
                        "label": source_role,
                        "url": url,
                        "upstreamValid": len(found),
                        "uris": found,
                    })
                    result["attempts"].append(attempt)
                    break
                attempt["error"] = "no valid configs in response"
            result["attempts"].append(attempt)

        source_cache[num] = result
        return result

    report_lists: dict[str, dict] = {}
    final_counts: dict[str, int] = {}
    stale_ids: list[str] = []
    refused_ids: list[str] = []

    by_num: dict[int, list[dict]] = {}
    for item in plan:
        by_num.setdefault(item["num"], []).append(item)

    for num in sorted(by_num):
        items = sorted(by_num[num], key=lambda d: d["cap"])  # short first
        info = load_source(num)
        uris: list[str] = info["uris"]
        full_cap = max(d["cap"] for d in items)
        # The short list is always a subset of the full list.
        selected = sample_evenly(uris, full_cap) if uris else []

        for item in items:
            out_path = CONFIG_DIR / f"{item['id']}.txt"
            old_count = count_uris(out_path)
            lines = selected if item["cap"] == full_cap else sample_evenly(selected, item["cap"])

            entry: dict = {
                "source": info.get("source"),
                "httpStatus": info["attempts"][-1]["httpStatus"] if info["attempts"] else None,
                "upstreamValid": info.get("upstreamValid", 0),
            }
            if info.get("url"):
                entry["url"] = info["url"]

            status = "ok"
            if not lines:
                status = "stale"
                entry["reason"] = "no data from upstream; kept last known good"
            elif old_count >= MIN_SHRINK_FLOOR and len(lines) < old_count * MIN_SHRINK_RATIO:
                status = "stale"
                entry["reason"] = (
                    f"refused shrink {old_count} -> {len(lines)} "
                    f"(< {int(MIN_SHRINK_RATIO * 100)}%); kept last known good"
                )
                refused_ids.append(item["id"])

            if status == "ok":
                write_text_lf(
                    out_path,
                    f"# Подписка {item['id']} | {item['label']}\n" + "\n".join(lines) + "\n",
                )
                entry["written"] = len(lines)
            else:
                entry["written"] = old_count
                stale_ids.append(item["id"])

            entry["servers"] = count_uris(out_path)
            entry["lastSuccess"] = (
                utcnow() if status == "ok"
                else (prev_lists.get(item["id"]) or {}).get("lastSuccess")
            )
            # Only keep the per-attempt trail when it carries information: a
            # single successful attempt duplicates the fields above, and this
            # file is committed on every run.
            if len(info["attempts"]) > 1 or status != "ok":
                entry["attempts"] = info["attempts"]
            report_lists[item["id"]] = entry
            final_counts[item["id"]] = entry["servers"]

    # ---- counts.json -------------------------------------------------------
    uniq: set[str] = set()
    for item in plan:
        path = CONFIG_DIR / f"{item['id']}.txt"
        if path.is_file():
            uniq.update(extract_uris(path.read_text(encoding="utf-8", errors="replace")))
    total_unique = len(uniq)

    counts_out = ["{"]
    for item in plan:
        counts_out.append(f'  "{item["id"]}": {final_counts.get(item["id"], 0)},')
    counts_out.append(f'  "totalUnique": {total_unique}')
    counts_out.append("}")
    write_text_lf(CONFIG_DIR / "counts.json", "\n".join(counts_out) + "\n")

    # ---- legacy / frozen file inventory -----------------------------------
    published_files = {f"{item['id']}.txt" for item in plan}
    legacy: dict[str, dict] = {}
    for path in sorted(CONFIG_DIR.glob("*.txt")):
        if path.name in published_files:
            continue
        n = count_uris(path)
        legacy[path.name] = {"servers": n, "published": False, "empty": n == 0}

    # ---- sources.json ------------------------------------------------------
    sources_summary: dict[str, dict] = {}
    for item in plan:
        entry = report_lists[item["id"]]
        key = entry.get("source") or "unavailable"
        bucket = sources_summary.setdefault(
            key, {"role": SOURCE_ROLES.get(key, "unknown"), "lists": 0, "ok": 0, "stale": 0}
        )
        bucket["lists"] += 1
        bucket["stale" if item["id"] in stale_ids else "ok"] += 1

    report = {
        "generatedAt": utcnow(),
        "generator": ".github/scripts/update_configs.py (workflow: update-vpn-config.yml)",
        "policy": {
            "schemes": ["vless", "trojan", "vmess", "ss", "hy2"],
            "maxShort": MAX_SHORT,
            "maxFull": MAX_FULL,
            "failSafe": "a published list is never replaced by an empty or suspiciously smaller result",
            "exclusions": {str(k): list(v) for k, v in EXCLUDE_SUBSTRINGS.items()},
        },
        "notes": {
            "avencores": AVENCORES_NOTE,
            "list26": "list 26 excludes entries containing '.ru' (behaviour preserved from the shell pipeline)",
            "list31": f"{IGARECK_LISTS[31][1]} was removed upstream and answers HTTP 404",
        },
        "sources": sources_summary,
        "lists": report_lists,
        "summary": {
            "lists": len(plan),
            "ok": len(plan) - len(stale_ids),
            "stale": len(stale_ids),
            "staleIds": stale_ids,
            "refusedShrink": refused_ids,
            "totalUnique": total_unique,
        },
        "legacyFiles": legacy,
    }
    write_text_lf(
        CONFIG_DIR / "sources.json",
        json.dumps(report, ensure_ascii=False, indent=1) + "\n",
    )

    # ---- console summary ---------------------------------------------------
    print(f"published lists: {len(plan)}  ok: {report['summary']['ok']}  stale: {len(stale_ids)}")
    if stale_ids:
        print(f"  stale: {', '.join(stale_ids)}")
    if refused_ids:
        print(f"  refused shrink: {', '.join(refused_ids)}")
    print(f"totalUnique: {total_unique}")
    for item in plan:
        entry = report_lists[item["id"]]
        print(f"  {item['id']:>5}: {entry['servers']:>4} servers  <- "
              f"{entry.get('source')} [{entry.get('httpStatus')}]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
