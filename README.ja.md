# 🔒 ラグのない VPN サブスクリプション — 検閲を回避

<p align="center">
  <a href="https://hidashimora.github.io/free-vpn-anti-rkn/">
    <img src="https://img.shields.io/badge/Open_the_site—lag--free_subscriptions-06b6d4?style=for-the-badge&labelColor=0c4a6e" alt="サイトを開く" height="120" />
  </a>
</p>

[Русский](README.md) | [English](README.en.md) | **日本語**

---

<a id="s-sources"></a>
## ⚠️ ソースの状態 — 利用前に必ずお読みください

リスト **1–26** は、以前は `AvenCores/goida-vpn-configs` リポジトリから収集していました。
**このアカウントとリポジトリは現在存在しません**。`repos/AvenCores/goida-vpn-configs` と
`users/AvenCores` はどちらも **HTTP 404** を返します (アカウントが削除されたか名前が変更されました)。そのため、
リスト 1–26 は **2026 年 9 月 24 日以降更新されていませんでした** (最後の実質的な変更: コミット `0e713e240`、
2026-09-24T10:02:47Z)。

**対応内容:** リスト 1–26 は現在、同じプロジェクトの稼働中のミラー
[**aneek0/goida-vpn-configs**](https://github.com/aneek0/goida-vpn-configs) から取得しています。このミラーは
同一の構成 (`githubmirror/1.txt` … `githubmirror/26.txt`) と **同じリストの順序**
(1 = OpenRay、2 = 5ubscrpt10n、3 = proxy-minging、… 26 = SNI/CIDR 回避) を維持しており、更新も続いています
(最終 push 2026-11-09T00:05:31Z、26 ファイルすべてあり)。**リスト 1–26 の更新は再開されています。**

| ソース | 提供内容 | 状態 |
|---|---|---|
| `AvenCores/goida-vpn-configs` | リスト 1–26 (以前) | ❌ **404、アカウントに到達不可** — 現在は使用していません |
| [`aneek0/goida-vpn-configs`](https://github.com/aneek0/goida-vpn-configs) | リスト 1–26 (現在) | ✅ 稼働中、更新中 |
| [`igareck/vpn-configs-for-russia`](https://github.com/igareck/vpn-configs-for-russia) | リスト 27–34 | ✅ 稼働中、更新中 |

別件として、**リスト 31** のソース (`Vless-Reality-White-Lists-Rus-Mobile-2.txt`) は
`igareck/vpn-configs-for-russia` から削除され、現在は **404** を返します。リスト 31 は **最後に取得に成功した
コピー** を引き続き提供しており、`stale` としてマークされています — 今後は更新されません。
ソースごと・リストごとの正確な状態は、機械可読な
[`configs/sources.json`](configs/sources.json) に記録されています。

---

## 📑 目次

- [このプロジェクトについて](#s-desc)
- [⚠️ ソースの状態](#s-sources)
- [🗂 リポジトリの構成](#s-structure)
- [🚀 クイックスタート](#s-quickstart)
- [📋 サブスクリプションリンク (1–34)](#s-links)
- [📱 クライアントと設定](#s-clients)
- [📊 統計](#s-stats)
- [⚙️ 自動更新の仕組み](#s-updates)
- [🤝 貢献](#s-contribute)
- [⚠️ 免責事項](#s-disclaimer)

---

<a id="s-desc"></a>
## 💡 このプロジェクトについて

これらのサブスクリプションに含まれる VPN サーバーを使うと、プロバイダによって制限されているサイト、メッセンジャー、
サービスの **ブロックを回避** できます。サブスクリプション設定とは、`vless`、`trojan`、
`vmess`、`shadowsocks` (`ss`)、`hysteria` (`hy2`) プロトコルを使うこうしたサーバーの一覧です。

人気のある公開リストには、**数千ものノード** が含まれていることがよくあります。これほど大量のデータを読み込むと
クライアントに大きな負荷がかかり、UI が重くなったり、リストの読み込みに時間がかかったり、アプリがクラッシュしたりすることがあります。

そのため、ここではソースごとに **専用の短縮ファイル** を用意しています。

- **短縮** リスト (`N.1.txt`) — 最大 **300** サーバー
- **拡張** リスト (`N.2.txt`) — 最大 **500** サーバー (ソース 1–26 と 28、32、33 で利用可能)

サーバーは **ソースのリスト全体から均等に** 選ばれ、重複は削除されます。`vless`、`trojan`、`vmess`、`ss`、`hy2`
を使う行のみが対象です。ノード数が少ないほどクライアントの負荷が減り、動作が安定します。

---

<a id="s-structure"></a>
## 🗂 リポジトリの構成

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

> `configs/` には **旧命名規則のレガシーファイル** (サフィックスなしの `1.txt` … `34.txt`、
> `1.3.txt` … `1.26.txt`、`vpn.txt`) も含まれています。これらは **もう更新されておらず**、古い
> リンクが引き続き機能するように残しているだけです。使用しないでください。一部は空です (ヘッダー行のみ)。

---

<a id="s-quickstart"></a>
## 🚀 クイックスタート

1. [プロジェクトのサイト](https://hidashimora.github.io/free-vpn-anti-rkn/) を開くか、
   [サブスクリプションの表](#s-links) からリンクをコピーします。
2. VPN クライアントで、URL からサブスクリプションを追加します (「Subscription」/「Import from link」)。
3. リストを更新し、必要に応じて遅延 (ping) テストを実行します。
4. サーバーを選んで接続します。うまくいかない場合は、サブスクリプションを更新して別のサーバーを試してください。

---

<a id="s-links"></a>
<a id="subscription-links-134"></a>
## 📋 サブスクリプションリンク (1–34)

ベース URL: `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/`

| # | ソース | 短縮 (≤300) | 拡張 (≤500) |
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
| 26 | SNI/CIDR 回避 (`.ru` なし) | [26.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/26.1.txt) | [26.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/26.2.txt) |
| 27 | Shadowsocks + All (ブラック) | [27](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/27.txt) | — |
| 28 | VLESS 全部 (ブラック) | [28.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/28.1.txt) | [28.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/28.2.txt) |
| 29 | VLESS モバイル (ブラック) | [29](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/29.txt) | — |
| 30 | VLESS Reality ホワイト モバイル | [30](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/30.txt) | — |
| 31 | VLESS Reality ホワイト モバイル 2 | [31](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/31.txt) ⚠️ **stale** | — |
| 32 | WHITE-CIDR-RU-all | [32.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/32.1.txt) | [32.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/32.2.txt) |
| 33 | WHITE-CIDR-RU-checked | [33.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/33.1.txt) | [33.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/33.2.txt) |
| 34 | WHITE-SNI-RU-all | [34](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/34.txt) | — |

**どれを選ぶか。** 普段使いには **短縮** リスト (`N.1`) を選んでください — クライアントへの負荷が
軽くなります。リスト **27–31** は「ブラック」(検閲回避) グループ、**32–34** は「ホワイト」
(制限回避) グループに属します。ほとんどのユーザーには短縮リストが 2 つほどあれば十分です。すべてを
一度に有効にしないでください。

---

<a id="s-clients"></a>
## 📱 クライアントと設定

サブスクリプションは単なるリンクです。コピーして、単一の設定としてではなく **サブスクリプション** として
クライアントに追加してください。

**Android / iOS / デスクトップ (クロスプラットフォーム)**

1. [Hiddify](https://github.com/hiddify/hiddify-app) または
   [NekoBox for Android](https://github.com/MatsuriDayo/NekoBoxForAndroid) をインストールします。
2. 「サブスクリプションの追加」ダイアログを開き、リンクを貼り付けます (または「Import from clipboard」)。
3. サブスクリプションを更新し、遅延テストを実行して、遅延順に並べ替えます。
4. サーバーを選んで接続します。

> 旧 **NekoRay** (`MatsuriDayo/nekoray`) はアーカイブされています — 代わりに Hiddify または Throne を使用してください。

**Android**

1. [v2rayNG](https://github.com/2dust/v2rayNG) をインストールします。
2. 「+」→「Add subscription」をタップし、リンクを貼り付けます。
3. リストを更新し、「Test group profiles」を実行して、ノードを選びます。

**Windows / Linux**

1. [v2rayN](https://github.com/2dust/v2rayN) または [Throne](https://github.com/throneproj/Throne) をインストールします。
2. 「Profiles」→「Add profile from URL」(またはクリップボードから)。
3. 遅延をテストし、必要に応じて TUN モードを有効にして接続します。

**iOS / iPadOS**

1. サブスクリプションと `vless` / `trojan` / `vmess` / `ss` / `hy2` プロトコルに対応したクライアント
   (例: V2Box、v2RayTun、**Streisand**) をインストールします。
2. サブスクリプション URL の欄にリンクを貼り付け、リストを読み込んでサーバーを選びます。

**macOS**

1. [Hiddify](https://github.com/hiddify/hiddify-app) をインストールします。
2. 「New profile」→ サブスクリプションのリンクを貼り付けます。
3. ルーティングモードを選択し、サービスとサーバーを有効にします。

**`hysteria` (`hy2`) と `shadowsocks` (`ss`) について。** どちらもリストに含まれていますが、すべてのクライアントが
対応しているわけではありません。`hy2` には別のコア (Hysteria2) が必要で、`ss` は別の
サブスクリプション形式として扱われることがあります。クライアントが未対応の形式だと警告する場合、それらのノードは単に
除外されます。

---

<a id="s-stats"></a>
## 📊 統計

直近の更新時のスナップショット (`2026-11-09T03:36:56Z`、`counts.json` / `sources.json` より):

| 指標 | 値 |
|---|---|
| 公開リスト数 | **63** |
| サブスクリプション番号 (グループ) | 34 |
| ユニークなサーバー数 (重複なし) | **約 10 200** (直近の実行で 9 894–10 272) |
| 全リストの合計行数 (リスト間の重複を含む) | 約 17 800 |
| 正常に更新されたリスト | 62 |
| `stale` としてマーク (ソース利用不可) | 1 (`31`) |

> サーバー数は **更新のたびに変わります** — 上流のリストは常に入れ替わっているため、正確な値は必ず
> `counts.json` で確認してください。安定しているのは構成 (63 リスト、34 グループ) と上限 (300 / 500)
> だけです。

> これらの数値は更新のたびに変わります。**正式な値は常に以下にあります:**
> [`configs/counts.json`](configs/counts.json) (ファイルごとのサーバー数と `totalUnique`) と
> [`configs/sources.json`](configs/sources.json) (ソースの状態、HTTP コード、設定数、最後に
> 取得に成功した日時)。サイトは `counts.json` から数値を自動的に取得します。

---

<a id="s-updates"></a>
## ⚙️ 自動更新の仕組み

処理は GitHub Actions が行うため、自前のサーバーは必要ありません。

- **スケジュール:** `23 */4 * * *` — **4 時間ごと**。以前は `* * * * *` (「毎分」) でしたが、
  GitHub はこのようなスケジュールを大幅に制限するため、実際には 1 日あたり約 6 回、不規則な
  時刻にしか実行されていませんでした。4 時間ごとにすれば実際の頻度は同じで、正直かつ予測可能になります。
- **コード:** [`.github/scripts/update_configs.py`](.github/scripts/update_configs.py) — サードパーティの
  依存関係はなく、ローカルでも実行できます: `python3 .github/scripts/update_configs.py`
- **チェック:** [`.github/scripts/verify_configs.py`](.github/scripts/verify_configs.py) が設定ファイル、
  `counts.json`、`sources.json` を照合します。不一致があれば何もコミットされません。

**フェイルセーフ:** リストが空の結果や不自然に短い結果で置き換えられることは **決して** ありません。ソースに
到達できない場合や不正なデータが返された場合、ファイルは最後に動作していたコピーを保持し、`sources.json` に
理由 (HTTP コード、エラー) とともに `stale` の状態が記録されます。さらに、重複は削除され、対応プロトコルの
行のみが残され、リスト 26 では (従来どおり) `.ru` を含むエントリが除外されます。

---

<a id="s-contribute"></a>
## 🤝 貢献

- **Issue。** 動作しないサーバーや壊れたソースは
  [Issues](https://github.com/Hidashimora/free-vpn-anti-rkn/issues) で報告してください。なお、サーバーは
  サードパーティのものであり、一部は常に利用できない状態にあります — これは想定どおりです。
  [issue #5](https://github.com/Hidashimora/free-vpn-anti-rkn/issues/5) をご覧ください。
- **Pull Request。** README、クライアントの手順、スクリプト、リストの修正を歓迎します。
  PR を作成する前に、以下を実行してください。

  ```bash
  python3 .github/scripts/update_configs.py
  python3 .github/scripts/verify_configs.py
  ```

- **ソースの追加。** `update_configs.py` 内の `MIRROR_LISTS` / `IGARECK_LISTS` に上流の URL とともに
  記述し、`published_plan()` に追加して、`verify_configs.py` が通ることを確認してください。
- **フォーク。** ワークフローは、フォークが上流へ push しようとしないように設定されています。

---

<a id="s-disclaimer"></a>
## ⚠️ 免責事項

**このプロジェクトは決して VPN の広告ではありません。** 作者は、掲載されている VPN 設定のいずれも所有、開発、提供
していません。これは独立した情報提供のための概要であり、公開されているサブスクリプションをまとめたものです。

**すべての設定はサードパーティのものです。** 作者はその可用性、安全性、匿名性を検証しておらず、
動作することも一切保証しません。ノードは現れては消え、どの時点でも一部は到達できません。**ここで見つけたノードを
通じて機密情報を送信しないでください** — ノードの運営者は技術的にあなたの通信を見ることができます。自己責任でご利用ください。

違法な目的での使用は禁止されています。すべての情報は「現状のまま」提供され、いかなる種類の保証もありません。
これらの設定の使用についてはご自身が責任を負います。お住まいの地域の法律に従って使用してください。
この情報を見たくない場合は、このページを閉じてください。

### 作者を支援する

BNB Smart Chain (BEP20): `0x78187a5efaefa1a790be883492c4f0952a167c4a`
Tron (TRC20): `TBynQEXksZzCcx5KC52i7VyjRKvmv6DrjV`
Ethereum (ERC20): `0x78187a5efaefa1a790be883492c4f0952a167c4a`
