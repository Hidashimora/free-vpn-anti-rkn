# 🔒 VPN подписки без лагов — обход блокировок

> Укороченные списки VPN-серверов для обхода блокировок. Один раз добавил ссылку в клиент — и всё летает, без тормозов и вылетов.

---

## 📑 Содержание

- [Зачем это нужно](#-зачем-это-нужно)
- [🚀 Быстрый старт](#-быстрый-старт)
- [📋 Наши подписки (1/4 серверов)](#-наши-подписки-14-серверов)
- [📱 Гайды по установке](#-гайды-по-установке)
- [📊 Статистика репозитория](#-статистика-репозитория)
- [🗂 Структура репозитория](#-структура-репозитория)
- [🔗 Полные списки (оригинал)](#-полные-списки-оригинал)
- [⚙️ Как устроено обновление](#️-как-устроено-обновление)

---

## 💡 Зачем это нужно

VPN-серверы помогают **обходить блокировки**: открывать сайты, мессенджеры и сервисы, до которых провайдер не пускает. Конфиги подписок — это как раз списки таких серверов.

Проблема: в популярных списках бывает **больше тысячи нод**. Когда клиент тянет и обрабатывает столько конфигов, начинают тупить все подряд — интерфейс подвисает, список грузится вечность, приложение может вылетать.

Здесь лежат **укороченные подписки**: для каждого из 26 списков [goida-vpn-configs](https://github.com/AvenCores/goida-vpn-configs) свой файл с примерно **четвертью** серверов. Меньше конфигов — меньше нагрузка, всё работает плавно. Списки подтягиваются **автоматически**, как только обновляются исходные конфиги (проверка каждые 10 минут). Вручную ничего настраивать не надо.

---

## 🚀 Быстрый старт

1. **Скопируй** ссылку на подписку (из таблицы ниже или главную — `vpn.txt`).
2. **Открой** свой VPN-клиент (v2rayNG, NekoRay, Throne, Hiddify, V2Box — кто чем пользуется).
3. **Добавь подписку** по URL (меню → подписка / subscription / импорт по ссылке).
4. **Обнови** список, при желании проверь пинг и отсортируй по задержке.
5. **Выбери** сервер и подключайся.

Готово. Дальше — короткие гайды по платформам.

---

## 📋 Наши подписки (1/4 серверов)

В каждом файле — примерно четверть конфигов из соответствующего списка (vless, trojan, vmess, ss, hy2). Удобно и без лагов.

**Главная ссылка** (список №26 — обход SNI/CIDR):

| Куда вставлять | Ссылка |
|-----------------|--------|
| Сайт | `https://hidashimora.github.io/vpn.txt` |
| Raw (для клиентов) | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/vpn.txt` |

**Все 26 укороченных списков** — копируй нужную ссылку:

| № | Raw-ссылка |
|---|------------|
| 1 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/1.txt` |
| 2 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/2.txt` |
| 3 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/3.txt` |
| 4 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/4.txt` |
| 5 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/5.txt` |
| 6 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/6.txt` |
| 7 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/7.txt` |
| 8 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/8.txt` |
| 9 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/9.txt` |
| 10 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/10.txt` |
| 11 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/11.txt` |
| 12 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/12.txt` |
| 13 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/13.txt` |
| 14 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/14.txt` |
| 15 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/15.txt` |
| 16 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/16.txt` |
| 17 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/17.txt` |
| 18 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/18.txt` |
| 19 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/19.txt` |
| 20 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/20.txt` |
| 21 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/21.txt` |
| 22 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/22.txt` |
| 23 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/23.txt` |
| 24 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/24.txt` |
| 25 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/25.txt` |
| 26 | `https://raw.githubusercontent.com/hidashimora/hidashimora.github.io/main/26.txt` |

---

## 📱 Гайды по установке

### 📲 Android

Ставишь **v2rayNG** (или NekoRay, Hiddify). В приложении: плюсик / меню → «Импорт из буфера» или «Добавить подписку» → вставляешь ссылку. Потом обновляешь подписку (кружок со стрелкой в группах), при желании гоняешь проверку пинга и сортируешь по задержке. Выбрал сервер — жми «Подключиться». Не зашло — попробуй другой узел или обнови список ещё раз.

### 🖥 Windows / Linux

Клиент на выбор: **Throne**, **NekoRay**, **v2rayN**. Профили → добавить из URL или из буфера → вставил ссылку. Можно прогнать тест задержки и выбрать сервер с минимальным пингом. Включил VPN — пользуешься.

### 📱 iOS / iPadOS

Ставишь **V2Box** (V2ray Client). Вкладка Config → плюс → «Добавить подписку»: любое название и наша ссылка в поле URL. После загрузки выбираешь сервер и нажимаешь «Подключиться».

### 💻 macOS

**Hiddify** или другой клиент. Новый профиль или «Добавить из буфера» → вставляешь ссылку. Дальше — выбор сервера и включение VPN в настройках.

Если что-то не подключается — проверь, что подписка обновилась, и попробуй другой сервер; часть нодов бывает временно недоступна.

---

## 📊 Статистика репозитория

Показатели просмотров и клонов смотри в **Insights** репозитория на GitHub:

| Показатель | Где смотреть |
|------------|--------------|
| Просмотры | Insights → Traffic |
| Клоны | Insights → Traffic |
| Уникальные посетители | Insights → Traffic |

Статистика обновляется на стороне GitHub.

---

## 🗂 Структура репозитория

```
.github/workflows/   — автообновление подписок (каждые ~10 мин и при пуше)
├── update-vpn-config.yml

1.txt … 26.txt       — укороченные подписки (примерно 1/4 серверов каждая)
vpn.txt              — копия 26.txt (удобная главная ссылка)

index.html           — страница с кнопкой «Скопировать» и ссылкой на подписку
README.md            — этот файл
```

Файлы `1.txt`–`26.txt` и `vpn.txt` создаёт и обновляет workflow; вручную их не трогаем.

---

## 🔗 Полные списки (оригинал)

Если нужен **полный** список серверов (все тысячи), бери ссылки из [AvenCores/goida-vpn-configs](https://github.com/AvenCores/goida-vpn-configs). Учти: с таким объёмом клиент может тормозить — тогда как раз пригодятся наши укороченные подписки выше.

| № | Описание | Ссылка на полный список |
|---|----------|-------------------------|
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

В оригинале рекомендуют списки 1, 6, 22, 23, 24, 25. Список 26 — под обход SNI/CIDR (белые списки).

---

## ⚙️ Как устроено обновление

Всё крутится на **GitHub Actions**. Workflow запускается при каждом пуше в `main` и **каждые 10 минут** по расписанию (исходные списки goida обновляются примерно раз в 9 минут — мы подтягиваем изменения почти сразу). Для каждого номера 1–26 скрипт качает соответствующий список, оставляет только строки с конфигами (vless, trojan, vmess, ss, hy2), берёт каждую 4‑ю строку и сохраняет в свой файл. Файл `vpn.txt` — копия `26.txt`, чтобы главная ссылка не менялась. Свой сервер и PHP не нужны, всё на GitHub.
