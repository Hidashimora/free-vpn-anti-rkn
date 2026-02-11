# 🔒 VPN подписки без лагов — обход блокировок

> 26 укороченных списков вместо тонны нод. Скопировал ссылку — вставил в клиент — полетело.

---

## 📑 Содержание

- [Что здесь лежит](#-что-здесь-лежит)
- [🗂 Структура репозитория](#-структура-репозитория)
- [🚀 Быстрый старт](#-быстрый-старт)
- [📋 Ссылки на подписки (1–26)](#-ссылки-на-подписки-1-26)
- [📱 Гайды по установке](#-гайды-по-установке)
- [🔗 Полные списки (оригинал)](#-полные-списки-оригинал)
- [⚙️ Обновление](#️-обновление)

---

## 💡 Что здесь лежит

Серверы из подписок помогают **обходить блокировки** — открывать то, до чего провайдер сам не пускает. Беда в том, что в популярных списках по **тысяче с лишним нод**: клиент грузит, парсит, тормозит, иногда вылетает.

Здесь для каждого из 26 списков [goida-vpn-configs](https://github.com/AvenCores/goida-vpn-configs) лежит **свой укороченный файл** — примерно четверть серверов (каждая 4‑я строка). Меньше конфигов — нормальная работа без лагов. Обновление **автоматическое**: каждую минуту и при пуше в репозиторий.

---

## 🗂 Структура репозитория

```
.github/workflows/
├── update-vpn-config.yml    # запуск каждую минуту + при пуше

configs/
├── 1.txt … 26.txt          # укороченные подписки (~1/4 серверов)

index.html                  # страница со ссылками на все конфиги
README.md
```

---

## 🚀 Быстрый старт

1. Открой [главную страницу](https://hidashimora.github.io) или скопируй любую ссылку из таблицы ниже.
2. В VPN-клиенте добавь подписку по URL (подписка / subscription / импорт по ссылке).
3. Обнови список, при желании проверь пинг.
4. Выбери сервер и подключайся.

---

## 📋 Ссылки на подписки (1–26)

В каждом файле — примерно четверть конфигов из соответствующего списка (vless, trojan, vmess, ss, hy2). Нужен обход SNI/CIDR — бери **26**. Остальные номера — разные источники, смотри [оригинальный репо](https://github.com/AvenCores/goida-vpn-configs).

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

**Android** — v2rayNG, NekoRay, Hiddify: добавить подписку → вставить ссылку → обновить список → проверить пинг (по желанию) → выбрать сервер и подключиться.

**Windows / Linux** — Throne, NekoRay, v2rayN: профили → добавить из URL/буфера → вставить ссылку → тест задержки → включить VPN.

**iOS / iPadOS** — V2Box: Config → добавить подписку → URL → выбрать сервер → подключиться.

**macOS** — Hiddify и др.: новый профиль / из буфера → ссылка → выбор сервера → включить VPN.

Не подключается — обнови подписку и попробуй другой узел.

---

## 🔗 Полные списки (оригинал)

Нужны **все** серверы разом — бери ссылки из [AvenCores/goida-vpn-configs](https://github.com/AvenCores/goida-vpn-configs). Учти: с тысячами нод клиент может тормозить.

| № | Оригинал |
|---|----------|
| 1–25 | [1](https://github.com/AvenCores/goida-vpn-configs/raw/refs/heads/main/githubmirror/1.txt) … [25](https://github.com/AvenCores/goida-vpn-configs/raw/refs/heads/main/githubmirror/25.txt) |
| 26 (SNI/CIDR) | [26.txt](https://github.com/AvenCores/goida-vpn-configs/raw/refs/heads/main/githubmirror/26.txt) |

Рекомендуемые в оригинале: 1, 6, 22, 23, 24, 25.

---

## ⚙️ Обновление

**GitHub Actions**: при пуше в `main` и **каждую минуту** по cron workflow качает все 26 списков из goida-vpn-configs, оставляет строки с конфигами (vless, trojan, vmess, ss, hy2), берёт каждую 4‑ю и пишет в `configs/1.txt` … `configs/26.txt`. Без своего сервера, всё на GitHub.
