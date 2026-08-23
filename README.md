## Support The Author
BNB Smart Chain (BEP20): `0x78187a5efaefa1a790be883492c4f0952a167c4a`  
Tron (TRC20): `TBynQEXksZzCcx5KC52i7VyjRKvmv6DrjV`  
Ethereum (ERC20): `0x78187a5efaefa1a790be883492c4f0952a167c4a` 

# 🔒 VPN подписки без лагов — обход блокировок

<p align="center">
  <a href="https://hidashimora.github.io/free-vpn-anti-rkn/">
    <img src="https://img.shields.io/badge/Перейти_на_сайт—подписки_без_лагов-06b6d4?style=for-the-badge&labelColor=0c4a6e" alt="Перейти на сайт" height="120" />
  </a>
</p>

> Укороченные списки VPN-серверов для обхода блокировок. 34 укороченных списка вместо тонны нод. Скопировал ссылку — вставил в клиент — и всё работает без тормозов и вылетов.
>
> Автоматически обновляемая коллекция публичных VPN-конфигов (V2Ray / VLESS / Hysteria / Trojan / VMess / Reality / Shadowsocks) для быстрого обхода блокировок. Каждый конфиг — это TXT-подписка, которую можно импортировать практически в любой современный клиент (v2rayNG, NekoRay, Throne, v2rayN, V2Box, v2RayTun, Hiddify и др.). Списки обновляются раз в минуту с помощью GitHub Actions, поэтому ссылки из раздела «📋 Ссылки на подписки (1–34)» всегда актуальны.

---

## 📑 Содержание

- [Описание проекта](#-описание-проекта)
- [🗂 Структура репозитория](#-структура-репозитория)
- [🚀 Быстрый старт](#-быстрый-старт)
- [📋 Ссылки на подписки (1–34)](#ссылки-на-подписки-1-34)
- [📱 Гайды по установке](#-гайды-по-установке)
- [🔗 Полные списки (не рекомендовано)](#-полные-списки-не-рекомендовано)
- [⚙️ Обновление](#️-обновление)
- [⚠️ Дисклеймер](#️-дисклеймер)

---

## 💡 Описание проекта

VPN-серверы из подписок позволяют **обходить блокировки** доступа к сайтам, мессенджерам и сервисам, ограниченным провайдером. Подписочные конфиги представляют собой списки таких серверов в форматах vless, trojan, vmess, shadowsocks, hysteria и других.

В популярных открытых списках нередко содержится **более тысячи узлов**. При загрузке и обработке такого объёма данных клиентское приложение испытывает повышенную нагрузку: замедляется интерфейс, долго подгружается список, возможны сбои и завершение работы приложения.

В данном репозитории для каждого из 26 списков проекта **[AvenCores/goida-vpn-configs](https://github.com/AvenCores/goida-vpn-configs)** и для 8 списков **[igareck/vpn-configs-for-russia](https://github.com/igareck/vpn-configs-for-russia)** подготовлен **отдельный укороченный файл**: если в исходном списке меньше 300 конфигов — сохраняются все; иначе в файл входит примерно четверть серверов (каждая 4‑я строка), но не более 300. Уменьшение числа конфигов снижает нагрузку на клиент и обеспечивает стабильную работу без задержек. Обновление списков выполняется **автоматически** — проверка исходных данных выполняется раз в минуту, поэтому изменения появляются вскоре после обновления исходных репозиториев.

---

## 🗂 Структура репозитория

```
.github/workflows/
├── update-vpn-config.yml    # запуск по расписанию (раз в минуту)

configs/
├── 1.1.txt … 26.1.txt       # короткие подписки по источникам 1–26 (макс. 300)
├── 1.2.txt … 26.2.txt       # полные подписки по источникам 1–26 (не рекомендовано)
├── 27.txt, 29.txt, 30.txt, 31.txt, 34.txt   # короткие подписки igareck (без полного варианта)
├── 28.1.txt, 28.2.txt, 32.1.txt, 32.2.txt, 33.1.txt, 33.2.txt   # короткий + полный (BLACK_VLESS_RUS, WHITE-CIDR-RU-all, WHITE-CIDR-RU-checked)
├── counts.json               # число серверов в каждом файле и totalUnique (без повторов)

index.html                   # страница со ссылками на все конфиги
README.md
```

---

## 🚀 Быстрый старт

1. Откройте [главную страницу](https://hidashimora.github.io/free-vpn-anti-rkn/) или скопируйте нужную ссылку из таблицы в разделе «Ссылки на подписки».
2. В VPN-клиенте добавьте подписку по URL (меню «Подписка» / «Subscription» / «Импорт по ссылке»).
3. Выполните обновление списка; при необходимости запустите проверку задержки (пинга).
4. Выберите сервер и установите подключение.

---

<a id="ссылки-на-подписки-1-34"></a>
## 📋 Ссылки на подписки (1–34)

В каждом **коротком** файле — не более 300 конфигов из соответствующего источника. **Полные** списки (№1.2–№26.2 и №28.2, №32.2, №33.2) — все серверы источника (не рекомендовано: могут тормозить устройство). Учитываются только строки с протоколами **vless**, **trojan**, **vmess**, **ss**, **hy2**. Списки 1–26 — [AvenCores/goida-vpn-configs](https://github.com/AvenCores/goida-vpn-configs); 27–34 — [igareck/vpn-configs-for-russia](https://github.com/igareck/vpn-configs-for-russia). Для источников 28, 32, 33 (BLACK_VLESS_RUS, WHITE-CIDR-RU-all, WHITE-CIDR-RU-checked) — короткий №N.1 и полный №N.2.

Базовый URL: `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/`

| № | Raw-ссылка |
|---|------------|
| 1.1 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/1.1.txt` |
| 1.2 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/1.2.txt` |
| 2.1 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/2.1.txt` |
| 2.2 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/2.2.txt` |
| 3.1 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/3.1.txt` |
| 3.2 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/3.2.txt` |
| 4.1 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/4.1.txt` |
| 4.2 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/4.2.txt` |
| 5.1 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/5.1.txt` |
| 5.2 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/5.2.txt` |
| 6.1 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/6.1.txt` |
| 6.2 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/6.2.txt` |
| 7.1 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/7.1.txt` |
| 7.2 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/7.2.txt` |
| 8.1 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/8.1.txt` |
| 8.2 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/8.2.txt` |
| 9.1 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/9.1.txt` |
| 9.2 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/9.2.txt` |
| 10.1 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/10.1.txt` |
| 10.2 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/10.2.txt` |
| 11.1 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/11.1.txt` |
| 11.2 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/11.2.txt` |
| 12.1 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/12.1.txt` |
| 12.2 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/12.2.txt` |
| 13.1 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/13.1.txt` |
| 13.2 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/13.2.txt` |
| 14.1 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/14.1.txt` |
| 14.2 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/14.2.txt` |
| 15.1 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/15.1.txt` |
| 15.2 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/15.2.txt` |
| 16.1 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/16.1.txt` |
| 16.2 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/16.2.txt` |
| 17.1 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/17.1.txt` |
| 17.2 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/17.2.txt` |
| 18.1 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/18.1.txt` |
| 18.2 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/18.2.txt` |
| 19.1 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/19.1.txt` |
| 19.2 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/19.2.txt` |
| 20.1 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/20.1.txt` |
| 20.2 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/20.2.txt` |
| 21.1 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/21.1.txt` |
| 21.2 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/21.2.txt` |
| 22.1 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/22.1.txt` |
| 22.2 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/22.2.txt` |
| 23.1 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/23.1.txt` |
| 23.2 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/23.2.txt` |
| 24.1 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/24.1.txt` |
| 24.2 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/24.2.txt` |
| 25.1 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/25.1.txt` |
| 25.2 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/25.2.txt` |
| 26.1 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/26.1.txt` |
| 26.2 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/26.2.txt` |
| 27 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/27.txt` |
| 28.1 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/28.1.txt` |
| 28.2 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/28.2.txt` |
| 29 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/29.txt` |
| 30 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/30.txt` |
| 31 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/31.txt` |
| 32.1 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/32.1.txt` |
| 32.2 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/32.2.txt` |
| 33.1 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/33.1.txt` |
| 33.2 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/33.2.txt` |
| 34 | `https://raw.githubusercontent.com/Hidashimora/free-vpn-anti-rkn/main/configs/34.txt` |

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

## 🔗 Полные списки (не рекомендовано)

> **⚠️ Не рекомендовано.** Полные списки содержат тысячи серверов и **могут приводить к тормозам устройства, долгой загрузке и сбоям клиента.** Используйте только если нужен полный набор; для обычного использования — укороченные подписки выше.

Полные подписки: **№1.2–№26.2** (источники 1–26) и **№28.2, №32.2, №33.2** (igareck: BLACK_VLESS_RUS, WHITE-CIDR-RU-all, WHITE-CIDR-RU-checked) — в таблице в разделе [Ссылки на подписки](#ссылки-на-подписки-1-34). Оригиналы: [AvenCores/goida-vpn-configs](https://github.com/AvenCores/goida-vpn-configs) (1–26), [igareck/vpn-configs-for-russia](https://github.com/igareck/vpn-configs-for-russia) (27–34).

---

## ⚙️ Обновление

Обновление укороченных списков выполняется **автоматически**. Workflow GitHub Actions обращается к репозиториям AvenCores/goida-vpn-configs и igareck/vpn-configs-for-russia **раз в минуту**; как только там обновляются исходные конфиги, в течение минуты изменения попадают и в файлы данного репозитория. Таким образом, локальные списки в папке `configs/` актуализируются сразу после обновления исходных источников.

Технически: для источников 1–26 загружаются файлы из AvenCores/goida-vpn-configs; для 27–34 — из igareck/vpn-configs-for-russia. Короткие списки: `configs/1.1.txt` … `configs/26.1.txt`, `configs/27.txt`, `configs/28.1.txt`, `configs/29.txt` … `configs/34.txt` (для 28, 32, 33 — также полные `configs/28.2.txt`, `configs/32.2.txt`, `configs/33.2.txt`). Полные для 1–26: `configs/1.2.txt` … `configs/26.2.txt`. Собственный сервер не требуется, обработка выполняется на инфраструктуре GitHub.

---

## ⚠️ Дисклеймер

**Данный проект ни в коем случае не является рекламой VPN.** Автор не является владельцем, разработчиком или поставщиком перечисленных VPN-конфигураций. Это независимый информационный обзор и агрегация публичных подписок. Весь материал предназначен исключительно в информационных целях и только для граждан тех стран, где эта информация легальна (как минимум — в научных целях). Если вам такое читать нельзя — закройте эту страницу немедленно.

Автор не побуждает, не поощряет и не оправдывает использование VPN ни при каких обстоятельствах. Ответственность за любое применение данных конфигураций лежит на пользователе. Автор не несёт ответственности за точность, полноту и достоверность опубликованных данных. Вся информация предоставлена «как есть». Используйте в соответствии с местным законодательством и только в законных целях (в частности — для обеспечения безопасности в сети и защищённого удалённого доступа).

## Support The Author
BNB Smart Chain (BEP20): `0x78187a5efaefa1a790be883492c4f0952a167c4a`  
Tron (TRC20): `TBynQEXksZzCcx5KC52i7VyjRKvmv6DrjV`  
Ethereum (ERC20): `0x78187a5efaefa1a790be883492c4f0952a167c4a` 
