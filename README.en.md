# 🔒 Lag-free VPN subscriptions — bypassing censorship

<p align="center">
  <a href="https://hidashimora.github.io/free-vpn-anti-rkn/">
    <img src="https://img.shields.io/badge/Open_the_site—lag--free_subscriptions-06b6d4?style=for-the-badge&labelColor=0c4a6e" alt="Open the site" height="120" />
  </a>
</p>

[Русский](README.md) | **English**

---

<a id="s-sources"></a>
## ⚠️ Source status — read this before using anything

Lists **1–26** used to be collected from the `AvenCores/goida-vpn-configs` repository.
**That account and repository are gone**: both `repos/AvenCores/goida-vpn-configs` and
`users/AvenCores` now answer **HTTP 404** (the account was deleted or renamed). Because of that,
lists 1–26 **had not been updated since 24 September 2026** (last real change: commit `0e713e240`,
2026-09-24T10:02:47Z).

**What has been done:** lists 1–26 now come from a live mirror of the same project —
[**aneek0/goida-vpn-configs**](https://github.com/aneek0/goida-vpn-configs). It keeps the identical
layout (`githubmirror/1.txt` … `githubmirror/26.txt`) and **the same list order**
(1 = OpenRay, 2 = 5ubscrpt10n, 3 = proxy-minging, … 26 = SNI/CIDR bypass), and it is being updated
(last push 2026-11-09T00:05:31Z, all 26 files present). **Updates for lists 1–26 are running again.**

| Source | What it serves | Status |
|---|---|---|
| `AvenCores/goida-vpn-configs` | lists 1–26 (previously) | ❌ **404, account unreachable** — no longer used |
| [`aneek0/goida-vpn-configs`](https://github.com/aneek0/goida-vpn-configs) | lists 1–26 (now) | ✅ alive, updating |
| [`igareck/vpn-configs-for-russia`](https://github.com/igareck/vpn-configs-for-russia) | lists 27–34 | ✅ alive, updating |

Separately: the source of **list 31** (`Vless-Reality-White-Lists-Rus-Mobile-2.txt`) was removed from
`igareck/vpn-configs-for-russia` and now returns **404**. List 31 keeps serving its **last successful
copy** and is flagged `stale` — it is no longer refreshed.
Exact per-source and per-list statuses live in the machine-readable
[`configs/sources.json`](configs/sources.json).

---

## 📑 Contents

- [What this project is](#s-desc)
- [⚠️ Source status](#s-sources)
- [🗂 Repository layout](#s-structure)
- [🚀 Quick start](#s-quickstart)
- [📋 Subscription links (1–34)](#s-links)
- [📱 Clients and setup](#s-clients)
- [📊 Statistics](#s-stats)
- [⚙️ How auto-updating works](#s-updates)
- [🤝 Contributing](#s-contribute)
- [⚠️ Disclaimer](#s-disclaimer)

---

<a id="s-desc"></a>
## 💡 What this project is

VPN servers from these subscriptions let you **bypass blocks** on sites, messengers and services
restricted by your ISP. A subscription config is a list of such servers using the `vless`, `trojan`,
`vmess`, `shadowsocks` (`ss`) and `hysteria` (`hy2`) protocols.

Popular public lists often contain **many thousands of nodes**. Loading that much data puts a heavy
load on the client: the UI slows down, the list takes a long time to load, and the app may crash.

That is why every source here gets its **own shortened file**:

- **short** list (`N.1.txt`) — **at most 300** servers;
- **extended** list (`N.2.txt`) — **at most 500** servers (available for sources 1–26, plus 28, 32, 33).

Servers are picked **evenly across the whole source list** and duplicates are removed. Only lines
using `vless`, `trojan`, `vmess`, `ss` or `hy2` are counted. Fewer nodes means less client load and
more stable operation.

---

<a id="s-structure"></a>
## 🗂 Repository layout

```
.github/
├── workflows/update-vpn-config.yml   # scheduled auto-update
└── scripts/
    ├── update_configs.py             # fail-safe list refresh
    └── verify_configs.py             # consistency check (runs in CI)

configs/
├── 1.1.txt … 26.1.txt   # short lists for sources 1–26 (max 300)
├── 1.2.txt … 26.2.txt   # extended lists for sources 1–26 (max 500)
├── 27.txt, 29.txt, 30.txt, 31.txt, 34.txt            # short igareck lists
├── 28.1.txt, 28.2.txt, 32.1.txt, 32.2.txt, 33.1.txt, 33.2.txt   # short + extended
├── counts.json          # servers per file + totalUnique
└── sources.json         # source status: URL, HTTP code, config count, update time

index.html             # GitHub Pages site with all subscription links
README.md              # Russian version
README.en.md           # this file
```

> `configs/` also contains **legacy files from the old naming scheme** (`1.txt` … `34.txt` without a
> suffix, `1.3.txt` … `1.26.txt`, `vpn.txt`). They are **no longer updated** and are kept only so old
> links keep working. Do not use them. Some are empty (header line only).

---

<a id="s-quickstart"></a>
## 🚀 Quick start

1. Open the [project site](https://hidashimora.github.io/free-vpn-anti-rkn/) or copy a link from the
   [subscription table](#s-links).
2. In your VPN client, add the subscription by URL ("Subscription" / "Import from link").
3. Refresh the list and, optionally, run a latency (ping) test.
4. Pick a server and connect. If it does not work, refresh the subscription and try another one.

---

<a id="s-links"></a>
<a id="subscription-links-134"></a>
## 📋 Subscription links (1–34)

Base URL: `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/`

| # | Source | Short (≤300) | Extended (≤500) |
|---|--------|--------------|-----------------|
| 1 | sakha1370/OpenRay | [1.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/1.1.txt) | [1.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/1.2.txt) |
| 2 | sevcator/5ubscrpt10n | [2.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/2.1.txt) | [2.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/2.2.txt) |
| 3 | yitong2333/proxy-minging | [3.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/3.1.txt) | [3.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/3.2.txt) |
| 4 | acymz/AutoVPN | [4.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/4.1.txt) | [4.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/4.2.txt) |
| 5 | miladtahanian/V2RayCFGDumper | [5.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/5.1.txt) | [5.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/5.2.txt) |
| 6 | roosterkid/openproxylist | [6.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/6.1.txt) | [6.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/6.2.txt) |
| 7 | Epodonios/v2ray-configs | [7.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/7.1.txt) | [7.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/7.2.txt) |
| 8 | ShatakVPN/ConfigForge-V2Ray | [8.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/8.1.txt) | [8.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/8.2.txt) |
| 9 | mohamadfg-dev/telegram-v2ray-configs-collector | [9.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/9.1.txt) | [9.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/9.2.txt) |
| 10 | mheidari98/.proxy | [10.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/10.1.txt) | [10.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/10.2.txt) |
| 11 | youfoundamin/V2rayCollector | [11.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/11.1.txt) | [11.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/11.2.txt) |
| 12 | VOID-Anonymity/V.O.I.D-VPN_Bypass | [12.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/12.1.txt) | [12.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/12.2.txt) |
| 13 | cbusifabcap/daily_free_vpn | [13.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/13.1.txt) | [13.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/13.2.txt) |
| 14 | LalatinaHub/Mineral | [14.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/14.1.txt) | [14.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/14.2.txt) |
| 15 | miladtahanian/Config-Collector | [15.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/15.1.txt) | [15.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/15.2.txt) |
| 16 | Pawdroid/Free-servers | [16.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/16.1.txt) | [16.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/16.2.txt) |
| 17 | MhdiTaheri/V2rayCollector_Py | [17.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/17.1.txt) | [17.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/17.2.txt) |
| 18 | free18/v2ray | [18.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/18.1.txt) | [18.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/18.2.txt) |
| 19 | MhdiTaheri/V2rayCollector | [19.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/19.1.txt) | [19.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/19.2.txt) |
| 20 | Argh94/Proxy-List | [20.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/20.1.txt) | [20.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/20.2.txt) |
| 21 | shabane/kamaji | [21.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/21.1.txt) | [21.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/21.2.txt) |
| 22 | wuqb2i4f/xray-config-toolkit | [22.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/22.1.txt) | [22.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/22.2.txt) |
| 23 | igareck BLACK_VLESS_RUS | [23.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/23.1.txt) | [23.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/23.2.txt) |
| 24 | Mr-Meshky/vify | [24.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/24.1.txt) | [24.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/24.2.txt) |
| 25 | V2RayRoot/V2RayConfig | [25.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/25.1.txt) | [25.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/25.2.txt) |
| 26 | SNI/CIDR bypass (no `.ru`) | [26.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/26.1.txt) | [26.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/26.2.txt) |
| 27 | Shadowsocks + All (black) | [27](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/27.txt) | — |
| 28 | VLESS all (black) | [28.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/28.1.txt) | [28.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/28.2.txt) |
| 29 | VLESS mobile (black) | [29](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/29.txt) | — |
| 30 | VLESS Reality white mobile | [30](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/30.txt) | — |
| 31 | VLESS Reality white mobile 2 | [31](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/31.txt) ⚠️ **stale** | — |
| 32 | WHITE-CIDR-RU-all | [32.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/32.1.txt) | [32.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/32.2.txt) |
| 33 | WHITE-CIDR-RU-checked | [33.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/33.1.txt) | [33.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/33.2.txt) |
| 34 | WHITE-SNI-RU-all | [34](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/34.txt) | — |

**Which one to pick.** For everyday use take the **short** lists (`N.1`) — they are easier on the
client. Lists **27–31** belong to the "black" (censorship-bypass) group, **32–34** to the "white"
(restriction-bypass) group. For most users a couple of short lists is plenty; do not enable all of
them at once.

---

<a id="s-clients"></a>
## 📱 Clients and setup

A subscription is just a link. Copy it and add it to your client as a **subscription**, not as a
single config.

**Android / iOS / Desktop (cross-platform)**

1. Install [Hiddify](https://github.com/hiddify/hiddify-app) or
   [NekoBox for Android](https://github.com/MatsuriDayo/NekoBoxForAndroid).
2. Open the "add subscription" dialog and paste the link (or "Import from clipboard").
3. Refresh the subscription, run a latency test, sort by latency.
4. Pick a server and connect.

> The old **NekoRay** (`MatsuriDayo/nekoray`) is archived — use Hiddify or Throne instead.

**Android**

1. Install [v2rayNG](https://github.com/2dust/v2rayNG).
2. Tap "+" → "Add subscription" and paste the link.
3. Refresh the list, run "Test group profiles", pick a node.

**Windows / Linux**

1. Install [v2rayN](https://github.com/2dust/v2rayN) or [Throne](https://github.com/throneproj/Throne).
2. "Profiles" → "Add profile from URL" (or from clipboard).
3. Test latency, enable TUN mode if needed, connect.

**iOS / iPadOS**

1. Install a client that supports subscriptions and the `vless` / `trojan` / `vmess` / `ss` / `hy2`
   protocols (for example V2Box, v2RayTun, **Streisand**).
2. Paste the link into the subscription URL field, load the list, pick a server.

**macOS**

1. Install [Hiddify](https://github.com/hiddify/hiddify-app).
2. "New profile" → paste the subscription link.
3. Choose your routing mode, enable the service and a server.

**About `hysteria` (`hy2`) and `shadowsocks` (`ss`).** Both appear in the lists, but not every client
supports them: `hy2` needs a separate core (Hysteria2) and `ss` is sometimes exposed as a different
subscription type. If your client complains about an unsupported format, those nodes are simply
filtered out.

---

<a id="s-stats"></a>
## 📊 Statistics

Snapshot from the most recent update (`2026-11-09T03:36:56Z`, taken from `counts.json` / `sources.json`):

| Metric | Value |
|---|---|
| Published lists | **63** |
| Subscription numbers (groups) | 34 |
| Unique servers (no repeats) | **≈10 200** (9 894–10 272 across neighbouring runs) |
| Total lines across lists (with repeats between lists) | ≈17 800 |
| Lists refreshed successfully | 62 |
| Flagged `stale` (source unavailable) | 1 (`31`) |

> The server count **changes on every update** — the upstream lists rotate constantly, so always read
> the exact value from `counts.json`. Only the structure (63 lists, 34 groups) and the caps (300 / 500)
> are stable.

> These numbers change on every update. **The authoritative values always live here:**
> [`configs/counts.json`](configs/counts.json) (servers per file and `totalUnique`) and
> [`configs/sources.json`](configs/sources.json) (source status, HTTP codes, config counts, last
> successful download time). The site pulls its numbers from `counts.json` automatically.

---

<a id="s-updates"></a>
## ⚙️ How auto-updating works

GitHub Actions does the work — you do not need your own server.

- **Schedule:** `23 */4 * * *` — **every 4 hours**. It used to be `* * * * *` ("every minute"), but
  GitHub throttles such schedules heavily: in practice only ~6 runs per day happened, at random
  times. Every 4 hours gives the same real frequency, but honestly and predictably.
- **Code:** [`.github/scripts/update_configs.py`](.github/scripts/update_configs.py) — no third-party
  dependencies; you can also run it locally: `python3 .github/scripts/update_configs.py`.
- **Check:** [`.github/scripts/verify_configs.py`](.github/scripts/verify_configs.py) cross-checks the
  config files, `counts.json` and `sources.json`. If anything disagrees, nothing is committed.

**Fail-safe:** a list is **never** replaced by an empty or suspiciously shorter result. If a source is
unreachable or returns garbage, the file keeps its last working copy and `sources.json` records a
`stale` status with the reason (HTTP code, error). On top of that, duplicates are removed, only lines
with supported protocols are kept, and for list 26 (as before) entries containing `.ru` are excluded.

---

<a id="s-contribute"></a>
## 🤝 Contributing

- **Issues.** Report dead servers and broken sources in
  [Issues](https://github.com/Hidashimora/free-vpn-anti-rkn/issues). Note that the servers are
  third-party and some are always unavailable — that is expected, see
  [issue #5](https://github.com/Hidashimora/free-vpn-anti-rkn/issues/5).
- **Pull requests.** Fixes to the README, client instructions, scripts and lists are welcome.
  Before opening a PR, run:

  ```bash
  python3 .github/scripts/update_configs.py
  python3 .github/scripts/verify_configs.py
  ```

- **Adding a source.** Describe it in `MIRROR_LISTS` / `IGARECK_LISTS` inside `update_configs.py`
  together with its upstream URL, add it to `published_plan()`, and make sure `verify_configs.py`
  passes.
- **Forks.** The workflow is configured so that forks never try to push back upstream.

---

<a id="s-disclaimer"></a>
## ⚠️ Disclaimer

**This project is in no way an advertisement for VPNs.** The author does not own, develop or provide
any of the listed VPN configurations. This is an independent informational overview and an
aggregation of public subscriptions.

**All configurations are third-party.** The author does not verify their availability, security or
anonymity, and does not guarantee that they work at all: nodes appear and disappear, and some are
unreachable at any given moment. **Do not send anything confidential through a node you found here** —
the node operator can technically see your traffic. Use at your own risk.

Use for illegal purposes is forbidden. All information is provided "as is", without warranty of any
kind. You are responsible for any use of these configurations. Use them in accordance with your local
law. If this information is not something you want to see, close this page.

### Support The Author

BNB Smart Chain (BEP20): `0x78187a5efaefa1a790be883492c4f0952a167c4a`
Tron (TRC20): `TBynQEXksZzCcx5KC52i7VyjRKvmv6DrjV`
Ethereum (ERC20): `0x78187a5efaefa1a790be883492c4f0952a167c4a`
