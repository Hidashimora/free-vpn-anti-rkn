# 🔒 VPN подписки без лагов — обход блокировок

<p align="center">
  <a href="https://hidashimora.github.io/free-vpn-anti-rkn/">
    <img src="https://img.shields.io/badge/Перейти_на_сайт—подписки_без_лагов-06b6d4?style=for-the-badge&labelColor=0c4a6e" alt="Перейти на сайт" height="120" />
  </a>
</p>

**Русский** | [English](README.en.md)

---

<a id="s-sources"></a>
## ⚠️ Статус источников — прочитайте перед использованием

Ранее списки **1–26** собирались из репозитория `AvenCores/goida-vpn-configs`.
**Этот аккаунт и репозиторий больше недоступны**: и `repos/AvenCores/goida-vpn-configs`, и
`users/AvenCores` отдают **HTTP 404** (аккаунт удалён или переименован). Из-за этого списки 1–26
**не обновлялись с 24 сентября 2026** (последнее реальное изменение — коммит `0e713e240`,
2026-09-24T10:02:47Z).

**Что сделано сейчас:** списки 1–26 переведены на живое зеркало того же проекта —
[**aneek0/goida-vpn-configs**](https://github.com/aneek0/goida-vpn-configs). Оно сохранило ту же
структуру (`githubmirror/1.txt` … `githubmirror/26.txt`) и **тот же порядок списков**
(1 = OpenRay, 2 = 5ubscrpt10n, 3 = proxy-minging, … 26 = Обход SNI/CIDR), и обновляется
(последний push — 2026-11-09T00:05:31Z, все 26 файлов на месте). **Обновление списков 1–26
возобновлено.**

| Источник | Что обслуживает | Статус |
|---|---|---|
| `AvenCores/goida-vpn-configs` | списки 1–26 (раньше) | ❌ **404, аккаунт недоступен** — больше не используется |
| [`aneek0/goida-vpn-configs`](https://github.com/aneek0/goida-vpn-configs) | списки 1–26 (сейчас) | ✅ жив, обновляется |
| [`igareck/vpn-configs-for-russia`](https://github.com/igareck/vpn-configs-for-russia) | списки 27–34 | ✅ жив, обновляется |

Отдельно: источник **списка 31** (`Vless-Reality-White-Lists-Rus-Mobile-2.txt`) удалён из
`igareck/vpn-configs-for-russia` и отдаёт **404**. Список 31 продолжает отдавать **последнюю
успешную копию** и помечен как `stale` — актуальным он больше не обновляется.
Точные статусы всех источников и списков лежат в машиночитаемом файле
[`configs/sources.json`](configs/sources.json).

---

## 📑 Содержание

- [Описание проекта](#s-desc)
- [⚠️ Статус источников](#s-sources)
- [🗂 Структура репозитория](#s-structure)
- [🚀 Быстрый старт](#s-quickstart)
- [📋 Ссылки на подписки (1–34)](#s-links)
- [📱 Клиенты и установка](#s-clients)
- [📊 Статистика](#s-stats)
- [⚙️ Как работает автообновление](#s-updates)
- [🤝 Как помочь проекту](#s-contribute)
- [⚠️ Дисклеймер](#s-disclaimer)

---

<a id="s-desc"></a>
## 💡 Описание проекта

VPN-серверы из подписок позволяют **обходить блокировки** доступа к сайтам, мессенджерам и сервисам,
ограниченным провайдером. Подписочные конфиги — это списки таких серверов в форматах `vless`,
`trojan`, `vmess`, `shadowsocks` (`ss`), `hysteria` (`hy2`).

В популярных открытых списках нередко содержится **много тысяч узлов**. При загрузке такого объёма
клиентское приложение испытывает повышенную нагрузку: замедляется интерфейс, долго подгружается
список, возможны сбои и завершение работы приложения.

Поэтому для каждого источника здесь подготовлен **отдельный укороченный файл**:

- **короткий** список (`N.1.txt`) — **не более 300** серверов;
- **расширенный** список (`N.2.txt`) — **не более 500** серверов (доступен для источников 1–26, а
  также 28, 32, 33).

Серверы отбираются **равномерно по всему исходному списку**, дубликаты удаляются. Учитываются только
строки с протоколами `vless`, `trojan`, `vmess`, `ss`, `hy2`. Меньше узлов — меньше нагрузка на
клиент и стабильнее работа.

---

<a id="s-structure"></a>
## 🗂 Структура репозитория

```
.github/
├── workflows/update-vpn-config.yml   # автообновление (расписание)
└── scripts/
    ├── update_configs.py             # fail-safe обновление списков
    └── verify_configs.py             # проверка целостности (запускается в CI)

configs/
├── 1.1.txt … 26.1.txt   # короткие списки по источникам 1–26 (до 300)
├── 1.2.txt … 26.2.txt   # расширенные списки по источникам 1–26 (до 500)
├── 27.txt, 29.txt, 30.txt, 31.txt, 34.txt            # короткие списки igareck
├── 28.1.txt, 28.2.txt, 32.1.txt, 32.2.txt, 33.1.txt, 33.2.txt   # короткий + расширенный
├── counts.json          # число серверов в каждом файле + totalUnique
└── sources.json         # статус источников: URL, HTTP-код, число конфигов, время обновления

index.html             # страница GitHub Pages со ссылками на все подписки
README.md              # этот файл (русский)
README.en.md           # English version
```

> В `configs/` также лежат **устаревшие файлы старой схемы** (`1.txt` … `34.txt` без суффикса,
> `1.3.txt` … `1.26.txt`, `vpn.txt`). Они **не обновляются** и оставлены только для совместимости со
> старыми ссылками. Не используйте их. Часть из них пуста (содержит только заголовок).

---

<a id="s-quickstart"></a>
## 🚀 Быстрый старт

1. Откройте [страницу проекта](https://hidashimora.github.io/free-vpn-anti-rkn/) или скопируйте нужную
   ссылку из таблицы [«Ссылки на подписки»](#s-links).
2. В VPN-клиенте добавьте подписку по URL (меню «Подписка» / «Subscription» / «Импорт по ссылке»).
3. Выполните обновление списка, при необходимости запустите проверку задержки (пинга).
4. Выберите сервер и подключитесь. Если сервер не работает — обновите подписку и выберите другой.

---

<a id="s-links"></a>
<a id="ссылки-на-подписки-1-34"></a>
## 📋 Ссылки на подписки (1–34)

Базовый URL: `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/`

| № | Источник | Короткий (≤300) | Расширенный (≤500) |
|---|----------|-----------------|--------------------|
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
| 26 | Обход SNI/CIDR (без `.ru`) | [26.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/26.1.txt) | [26.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/26.2.txt) |
| 27 | Shadowsocks + All (чёрный) | [27](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/27.txt) | — |
| 28 | VLESS все (чёрный) | [28.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/28.1.txt) | [28.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/28.2.txt) |
| 29 | VLESS mobile (чёрный) | [29](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/29.txt) | — |
| 30 | VLESS Reality white mobile | [30](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/30.txt) | — |
| 31 | VLESS Reality white mobile 2 | [31](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/31.txt) ⚠️ **stale** | — |
| 32 | WHITE-CIDR-RU-all | [32.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/32.1.txt) | [32.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/32.2.txt) |
| 33 | WHITE-CIDR-RU-checked | [33.1](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/33.1.txt) | [33.2](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/33.2.txt) |
| 34 | WHITE-SNI-RU-all | [34](https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/34.txt) | — |

**Что выбрать.** Для обычного использования берите **короткие** списки (`N.1`) — они легче для
клиента. Списки **27–31** относятся к «чёрному» (обход блокировок), **32–34** — к «белому» списку
(обход ограничений). Для большинства пользователей достаточно нескольких коротких списков; не
подключайте все сразу.

---

<a id="s-clients"></a>
## 📱 Клиенты и установка

Подписка — обычная ссылка. Скопируйте её и добавьте в клиент как «подписку» (subscription),
а не как отдельный конфиг.

**Android / iOS / Desktop (мультиплатформенные)**

1. Установите [Hiddify](https://github.com/hiddify/hiddify-app) или
   [NekoBox for Android](https://github.com/MatsuriDayo/NekoBoxForAndroid).
2. Откройте раздел добавления подписки и вставьте ссылку (или «Импорт из буфера обмена»).
3. Обновите подписку, при необходимости проверьте задержку и отсортируйте узлы.
4. Выберите сервер и подключитесь.

> Старый **NekoRay** (`MatsuriDayo/nekoray`) переведён в архив — используйте Hiddify или Throne.

**Android**

1. Установите [v2rayNG](https://github.com/2dust/v2rayNG).
2. Нажмите «+» → «Добавить подписку» и вставьте ссылку.
3. Обновите список, выполните «Проверка профилей группы», выберите узел.

**Windows / Linux**

1. Установите [v2rayN](https://github.com/2dust/v2rayN) или [Throne](https://github.com/throneproj/Throne).
2. «Профили» → «Добавить профиль из URL» (или из буфера обмена).
3. Протестируйте задержку, включите режим TUN при необходимости, подключитесь.

**iOS / iPadOS**

1. Установите клиент, поддерживающий подписки и протоколы `vless` / `trojan` / `vmess` / `ss` / `hy2`
   (например, V2Box, v2RayTun, **Streisand**).
2. Добавьте ссылку в поле URL подписки, загрузите список, выберите сервер.

**macOS**

1. Установите [Hiddify](https://github.com/hiddify/hiddify-app).
2. «Новый профиль» → вставьте ссылку подписки.
3. Выберите маршрутизацию, включите сервис и узел.

**Про `hysteria` (`hy2`) и `shadowsocks` (`ss`).** Эти протоколы есть в списках, но не все клиенты
их поддерживают: `hy2` требует отдельного ядра (Hysteria2), `ss` иногда вынесен в отдельный тип
подписки. Если клиент жалуется на неподдерживаемый формат — часть узлов просто отфильтруется.

---

<a id="s-stats"></a>
## 📊 Статистика

Снимок на момент последнего обновления (`2026-11-09T03:36:56Z`, из `counts.json` / `sources.json`):

| Показатель | Значение |
|---|---|
| Опубликованных списков | **63** |
| Номеров подписок (групп) | 34 |
| Уникальных серверов (без повторов) | **≈10 200** (9 894–10 272 в соседних прогонах) |
| Суммарно строк в списках (с повторами между списками) | ≈17 800 |
| Списков, обновившихся успешно | 62 |
| Помечены `stale` (источник недоступен) | 1 (`31`) |

> Число серверов **меняется при каждом обновлении** — исходные списки постоянно ротируются,
> поэтому точное значение всегда смотрите в `counts.json`. Стабильны только структура (63 списка,
> 34 группы) и лимиты (300 / 500).

> Цифры меняются при каждом обновлении. **Актуальные значения всегда здесь:**
> [`configs/counts.json`](configs/counts.json) (число серверов по каждому файлу и `totalUnique`) и
> [`configs/sources.json`](configs/sources.json) (статус источников, HTTP-коды, число конфигов,
> время последней удачной загрузки). Числа на сайте подтягиваются из `counts.json` автоматически.

---

<a id="s-updates"></a>
## ⚙️ Как работает автообновление

Обновление выполняет GitHub Actions — собственный сервер не нужен.

- **Расписание:** `23 */4 * * *` — **раз в 4 часа**. Раньше стояло `* * * * *` («каждую минуту»),
  но GitHub сильно ограничивает такие расписания: фактически выходило ~6 запусков в сутки в
  случайное время. Раз в 4 часа даёт ту же реальную частоту, но честно и предсказуемо.
- **Код:** [`.github/scripts/update_configs.py`](.github/scripts/update_configs.py) — без сторонних
  зависимостей, его можно запустить и локально: `python3 .github/scripts/update_configs.py`.
- **Проверка:** [`.github/scripts/verify_configs.py`](.github/scripts/verify_configs.py) сверяет файлы,
  `counts.json` и `sources.json`. Если что-то не сходится — коммит не создаётся.

**Fail-safe:** список **никогда** не перезаписывается пустым или подозрительно коротким результатом.
Если источник недоступен или отдал мусор, файл сохраняет последнюю рабочую копию, а в
`sources.json` появляется статус `stale` с причиной (HTTP-код, ошибка). Дополнительно: дубликаты
удаляются, отбираются только строки с поддерживаемыми протоколами, а для списка 26 (как и раньше)
исключаются узлы с `.ru` в адресе.

---

<a id="s-contribute"></a>
## 🤝 Как помочь проекту

- **Issues.** Сообщайте о нерабочих серверах и о упавших источниках в
  [Issues](https://github.com/Hidashimora/free-vpn-anti-rkn/issues). Обратите внимание: серверы
  сторонние, часть из них недоступна всегда — это ожидаемо, см. [issue #5](https://github.com/Hidashimora/free-vpn-anti-rkn/issues/5).
- **Pull requests.** Правки README, клиентов, скриптов и списков приветствуются.
  Перед PR запустите проверку:

  ```bash
  python3 .github/scripts/update_configs.py
  python3 .github/scripts/verify_configs.py
  ```

- **Новый источник.** Если добавляете список — опишите его в `MIRROR_LISTS` / `IGARECK_LISTS` внутри
  `update_configs.py` вместе с upstream-URL, добавьте в `published_plan()` и проверьте, что
  `verify_configs.py` проходит.
- **Форки.** Workflow настроен так, что в форках он не пытается пушить в upstream.

---

<a id="s-disclaimer"></a>
## ⚠️ Дисклеймер

**Данный проект ни в коем случае не является рекламой VPN.** Автор не является владельцем,
разработчиком или поставщиком перечисленных VPN-конфигураций. Это независимый информационный обзор
и агрегация публичных подписок.

**Все конфигурации — сторонние.** Автор не проверяет их работоспособность, безопасность, анонимность
и не гарантирует, что они работают вообще: узлы появляются и исчезают, часть недоступна в любой
момент времени. **Не передавайте через найденные узлы ничего конфиденциального**: оператор узла
технически может видеть ваш трафик. Доверяйте на свой риск.

Запрещено использование в незаконных целях. Вся информация предоставлена «как есть», без каких-либо
гарантий. Ответственность за любое применение данных конфигураций лежит на пользователе. Используйте
в соответствии с местным законодательством. Если вам такая информация не подходит — закройте эту
страницу.

### Support The Author

BNB Smart Chain (BEP20): `0x78187a5efaefa1a790be883492c4f0952a167c4a`
Tron (TRC20): `TBynQEXksZzCcx5KC52i7VyjRKvmv6DrjV`
Ethereum (ERC20): `0x78187a5efaefa1a790be883492c4f0952a167c4a`
