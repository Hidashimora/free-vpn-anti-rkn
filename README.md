# 🔒 VPN подписки без лагов — обход блокировок

> Укороченные списки VPN-серверов для обхода блокировок. 26 укороченных списков вместо тонны нод. Скопировал ссылку — вставил в клиент — и всё работает без тормозов и вылетов.
>
> Автоматически обновляемая коллекция публичных VPN-конфигов (V2Ray / VLESS / Hysteria / Trojan / VMess / Reality / Shadowsocks) для быстрого обхода блокировок. Каждый конфиг — это TXT-подписка, которую можно импортировать практически в любой современный клиент (v2rayNG, NekoRay, Throne, v2rayN, V2Box, v2RayTun, Hiddify и др.). Списки обновляются раз в минуту с помощью GitHub Actions, поэтому ссылки из раздела «📋 Ссылки на подписки (1–26)» всегда актуальны.

---

## 📑 Содержание

- [Описание проекта](#-описание-проекта)
- [🗂 Структура репозитория](#-структура-репозитория)
- [🚀 Быстрый старт](#-быстрый-старт)
- [📋 Ссылки на подписки (1–26)](#ссылки-на-подписки-1-26)
- [📱 Гайды по установке](#-гайды-по-установке)
- [🔗 Полные списки (оригинал)](#-полные-списки-оригинал)
- [⚙️ Обновление](#️-обновление)

---

## 💡 Описание проекта

VPN-серверы из подписок позволяют **обходить блокировки** доступа к сайтам, мессенджерам и сервисам, ограниченным провайдером. Подписочные конфиги представляют собой списки таких серверов в форматах vless, trojan, vmess, shadowsocks, hysteria и других.

В популярных открытых списках нередко содержится **более тысячи узлов**. При загрузке и обработке такого объёма данных клиентское приложение испытывает повышенную нагрузку: замедляется интерфейс, долго подгружается список, возможны сбои и завершение работы приложения.

В данном репозитории для каждого из 26 списков проекта **[AvenCores/goida-vpn-configs](https://github.com/AvenCores/goida-vpn-configs)** подготовлен **отдельный укороченный файл**: в него входит примерно четверть серверов (каждая 4‑я строка), но не более 300. Уменьшение числа конфигов снижает нагрузку на клиент и обеспечивает стабильную работу без задержек. Обновление списков выполняется **автоматически** — проверка исходных данных выполняется раз в минуту, поэтому изменения появляются вскоре после обновления исходного репозитория.

---

## 🗂 Структура репозитория

```
.github/workflows/
├── update-vpn-config.yml    # запуск по расписанию (раз в минуту)

configs/
├── 1.txt … 26.txt           # укороченные подписки (1/4 серверов, макс. 300)

index.html                   # страница со ссылками на все конфиги
README.md
```

---

## 🚀 Быстрый старт

1. Откройте [главную страницу](https://hidashimora.github.io) или скопируйте нужную ссылку из таблицы в разделе «Ссылки на подписки».
2. В VPN-клиенте добавьте подписку по URL (меню «Подписка» / «Subscription» / «Импорт по ссылке»).
3. Выполните обновление списка; при необходимости запустите проверку задержки (пинга).
4. Выберите сервер и установите подключение.

---

<a id="ссылки-на-подписки-1-26"></a>
## 📋 Ссылки на подписки (1–26)

В каждом файле — не более 300 конфигов из соответствующего списка репозитория [AvenCores/goida-vpn-configs](https://github.com/AvenCores/goida-vpn-configs): если в исходном списке меньше 300 — сохраняются все; иначе примерно четверть (каждая 4‑я строка), но не более 300. Учитываются только строки с конфигурациями протоколов **vless**, **trojan**, **vmess**, **ss**, **hy2**. Для **обхода блокировок по SNI/CIDR** (белые списки) предназначен список **№26**. Списки №1–№25 соответствуют разным источникам и наборам серверов; описание источников приведено в указанном репозитории.

| № | Raw-ссылка |
|---|------------|
| 1 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/configs/1.txt` |
| 2 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/configs/2.txt` |
| 3 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/configs/3.txt` |
| 4 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/configs/4.txt` |
| 5 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/configs/5.txt` |
| 6 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/configs/6.txt` |
| 7 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/configs/7.txt` |
| 8 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/configs/8.txt` |
| 9 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/configs/9.txt` |
| 10 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/configs/10.txt` |
| 11 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/configs/11.txt` |
| 12 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/configs/12.txt` |
| 13 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/configs/13.txt` |
| 14 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/configs/14.txt` |
| 15 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/configs/15.txt` |
| 16 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/configs/16.txt` |
| 17 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/configs/17.txt` |
| 18 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/configs/18.txt` |
| 19 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/configs/19.txt` |
| 20 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/configs/20.txt` |
| 21 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/configs/21.txt` |
| 22 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/configs/22.txt` |
| 23 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/configs/23.txt` |
| 24 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/configs/24.txt` |
| 25 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/configs/25.txt` |
| 26 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/configs/26.txt` |

---

## 📱 Гайды по установке

### 📲 Android

1. Установите приложение **v2rayNG** (или аналог: NekoRay, Hiddify).
2. Скопируйте выбранную ссылку на подписку из таблицы выше.
3. В приложении нажмите «+» в правом верхнем углу и выберите «Импорт из буфера обмена» или «Добавить подписку».
4. Выполните обновление подписки (иконка обновления в разделе «Группы»). При необходимости запустите «Проверка профилей группы» и «Сортировка по результатам теста».
5. Выберите сервер и нажмите кнопку подключения.

При отсутствии соединения обновите подписку и выберите другой узел.

### 🖥 Windows / Linux

1. Установите клиент **Throne**, **NekoRay** или **v2rayN**.
2. Скопируйте ссылку на подписку и в меню «Профили» выберите «Добавить профиль из буфера обмена» или «Добавить из URL».
3. При необходимости выполните тест задержки (пинга) и отсортируйте профили по задержке.
4. Включите режим TUN при необходимости, выберите сервер с наименьшей задержкой и запустите подключение.

### 📱 iOS / iPadOS

1. Установите приложение **V2Box (V2ray Client)**.
2. Скопируйте ссылку на подписку. В приложении откройте вкладку «Config», нажмите «+» и выберите «Добавить подписку».
3. Укажите произвольное название и вставьте ссылку в поле «URL».
4. После загрузки списка выберите сервер и нажмите «Подключиться».

### 💻 macOS

1. Установите **Hiddify** или другой поддерживаемый клиент.
2. Нажмите «Новый профиль» или «Добавить из буфера обмена» и вставьте ссылку на подписку.
3. В настройках при необходимости измените вариант маршрутизации. Включите VPN-сервис и выберите сервер для подключения.

При проблемах с подключением рекомендуется обновить подписку и выбрать другой сервер из списка; часть узлов может быть временно недоступна.

---

## 🔗 Полные списки (оригинал)

При необходимости использовать **полный** список серверов (без сокращения) ссылки можно взять из репозитория **[AvenCores/goida-vpn-configs](https://github.com/AvenCores/goida-vpn-configs)**. Следует учитывать, что большой объём конфигов может приводить к замедлению работы клиента.

<details>
<summary>Развернуть таблицу ссылок на полные списки (1–26)</summary>

| № | Описание | Ссылка |
|---|----------|--------|
| 1 | OpenRay | [1.txt](https://github.com/AvenCores/goida-vpn-configs/raw/refs/heads/main/githubmirror/1.txt) |
| 2 | 5ubscrpt10n | [2.txt](https://github.com/AvenCores/goida-vpn-configs/raw/refs/heads/main/githubmirror/2.txt) |
| 3 | proxy-minging | [3.txt](https://github.com/AvenCores/goida-vpn-configs/raw/refs/heads/main/githubmirror/3.txt) |
| 4 | AutoVPN | [4.txt](https://github.com/AvenCores/goida-vpn-configs/raw/refs/heads/main/githubmirror/4.txt) |
| 5 | V2RayCFGDumper | [5.txt](https://github.com/AvenCores/goida-vpn-configs/raw/refs/heads/main/githubmirror/5.txt) |
| 6 | openproxylist | [6.txt](https://github.com/AvenCores/goida-vpn-configs/raw/refs/heads/main/githubmirror/6.txt) |
| 7 | v2ray-configs | [7.txt](https://github.com/AvenCores/goida-vpn-configs/raw/refs/heads/main/githubmirror/7.txt) |
| 8 | cid-vpn-config | [8.txt](https://github.com/AvenCores/goida-vpn-configs/raw/refs/heads/main/githubmirror/8.txt) |
| 9 | telegram-v2ray-configs | [9.txt](https://github.com/AvenCores/goida-vpn-configs/raw/refs/heads/main/githubmirror/9.txt) |
| 10 | .proxy | [10.txt](https://github.com/AvenCores/goida-vpn-configs/raw/refs/heads/main/githubmirror/10.txt) |
| 11 | V2rayCollector | [11.txt](https://github.com/AvenCores/goida-vpn-configs/raw/refs/heads/main/githubmirror/11.txt) |
| 12 | .proxy | [12.txt](https://github.com/AvenCores/goida-vpn-configs/raw/refs/heads/main/githubmirror/12.txt) |
| 13 | config | [13.txt](https://github.com/AvenCores/goida-vpn-configs/raw/refs/heads/main/githubmirror/13.txt) |
| 14 | Mineral | [14.txt](https://github.com/AvenCores/goida-vpn-configs/raw/refs/heads/main/githubmirror/14.txt) |
| 15 | Config-Collector | [15.txt](https://github.com/AvenCores/goida-vpn-configs/raw/refs/heads/main/githubmirror/15.txt) |
| 16 | Free-servers | [16.txt](https://github.com/AvenCores/goida-vpn-configs/raw/refs/heads/main/githubmirror/16.txt) |
| 17 | V2rayCollector_Py | [17.txt](https://github.com/AvenCores/goida-vpn-configs/raw/refs/heads/main/githubmirror/17.txt) |
| 18 | v2ray | [18.txt](https://github.com/AvenCores/goida-vpn-configs/raw/refs/heads/main/githubmirror/18.txt) |
| 19 | V2rayCollector | [19.txt](https://github.com/AvenCores/goida-vpn-configs/raw/refs/heads/main/githubmirror/19.txt) |
| 20 | Proxy-List | [20.txt](https://github.com/AvenCores/goida-vpn-configs/raw/refs/heads/main/githubmirror/20.txt) |
| 21 | kamaji | [21.txt](https://github.com/AvenCores/goida-vpn-configs/raw/refs/heads/main/githubmirror/21.txt) |
| 22 | xray-config-toolkit | [22.txt](https://github.com/AvenCores/goida-vpn-configs/raw/refs/heads/main/githubmirror/22.txt) |
| 23 | Xray | [23.txt](https://github.com/AvenCores/goida-vpn-configs/raw/refs/heads/main/githubmirror/23.txt) |
| 24 | STRUGOV | [24.txt](https://github.com/AvenCores/goida-vpn-configs/raw/refs/heads/main/githubmirror/24.txt) |
| 25 | V2RayConfig | [25.txt](https://github.com/AvenCores/goida-vpn-configs/raw/refs/heads/main/githubmirror/25.txt) |
| 26 | Обход SNI/CIDR | [26.txt](https://github.com/AvenCores/goida-vpn-configs/raw/refs/heads/main/githubmirror/26.txt) |

В репозитории AvenCores/goida-vpn-configs рекомендуются списки 1, 6, 22, 23, 24, 25. Список 26 предназначен для обхода блокировок по SNI/CIDR (белые списки).

</details>

---

## ⚙️ Обновление

Обновление укороченных списков выполняется **автоматически**. Workflow GitHub Actions обращается к репозиторию AvenCores/goida-vpn-configs **раз в минуту**; как только там обновляются исходные конфиги, в течение минуты изменения попадают и в файлы данного репозитория. Таким образом, локальные списки в папке `configs/` актуализируются сразу после обновления исходного источника.

Технически: для каждого из 26 списков загружается соответствующий файл, из него отбираются строки с конфигурациями протоколов vless, trojan, vmess, ss, hy2; если конфигов меньше 300 — все; иначе каждая 4‑я строка (но не более 300); результат записывается в `configs/1.txt` … `configs/26.txt`. Собственный сервер не требуется, обработка выполняется на инфраструктуре GitHub.
