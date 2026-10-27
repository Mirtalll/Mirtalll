# Настройка GitHub-профиля Mirtalll

Репозиторий профиля: https://github.com/Mirtalll/Mirtalll

Готовые файлы лежат в `~/github-profile`:

| Файл | Что это |
|:--|:--|
| `banner.png` | Баннер для README (1280×420) |
| `avatar-lightning.png` | Чистый аватар с молнией (500×500) — рекомендую |
| `avatar-500.png` | Аватар из исходной молнии `~/.face` (500×500, мягкий) |
| `avatar.png` | Круглая версия для README |
| `README.md` | README профиля со всеми виджетами |
| `scripts/make_assets.py` | Генерация аватара и баннера из исходника |
| `.github/workflows/profile-assets.yml` | Автообновление змейки и графика активности |

---

## 1. Аватар

1. Откройте https://github.com/settings/profile
2. **Profile picture → Edit → Upload a photo**
3. Выберите `~/github-profile/avatar-lightning.png` (или `avatar-500.png`, если нужен исходный вариант)
4. Сохраните

GitHub сам обрежет изображение в круг.

---

## 2. Основные данные профиля

На странице https://github.com/settings/profile:

| Поле | Значение |
|:--|:--|
| **Name** | `Даниил Смирнов` |
| **Bio** | `Fullstack QA · Senior Automation QA. Playwright + Python, UI/API/DB, CI/CD. 4000+ автотестов в проде, стабильность 90%. Открыт к предложениям.` |
| **Location** | `Санкт-Петербург, Россия` |
| **Website** | `https://t.me/MirtlPLQA` |
| **Social links** | Telegram: `MirtlPLQA` |

Bio — 149 символов, лимит GitHub — 160.

---

## 3. README и виджеты

В README уже добавлено:

- баннер и анимированный заголовок (Typing SVG)
- контакты и бейджи стека
- блок «Обо мне» и таблица результатов
- GitHub Stats, Top Languages и Streak
- профильные карточки Summary Cards (4 шт.)
- график активности и змейка (генерируются GitHub Actions)
- счётчик просмотров профиля

Проверить работу Actions: https://github.com/Mirtalll/Mirtalll/actions

Первый запуск происходит автоматически при пуше в `main`. Дальше — по расписанию раз в сутки. Результаты складываются в ветку `output`, README ссылается на неё через `raw.githubusercontent.com`.

### Почему не Trophy и не внешний Activity Graph

Сервисы `github-profile-trophy.vercel.app` и `github-readme-activity-graph.vercel.app` из статьи сейчас отдают `402 DEPLOYMENT_DISABLED`. Поэтому график активности генерируется своим GitHub Action, а вместо трофеев используются Summary Cards — они работают стабильно.

Если захотите трофеи, есть self-hosted вариант: [soulteary/github-profile-trophy-action](https://github.com/soulteary/github-profile-trophy-action). Для него нужен отдельный PAT в секрете `PROFILE_STATS_TOKEN`.

---

## 4. Что ещё можно улучшить

- **Закрепить репозитории:** Profile → **Customize your pins** — выбрать 4–6 лучших проектов.
- **Приватные контрибуции:** Profile → **Contribution settings** → включить **Private contributions**, чтобы активность была видна.
- **Публичное портфолио:** сейчас на GitHub один публичный репозиторий — сам профиль. Когда опубликуете 2–3 проекта (QA-фреймворк, API-тесты, pet-проект), карточки статистики и Top Languages станут содержательнее. Можно добавить extra pins через `github-readme-stats`.
- **Metrics:** если нужна более подробная инфографика, можно добавить [lowlighter/metrics](https://github.com/lowlighter/metrics) через GitHub Actions.
- **Blog post workflow:** если появится блог или RSS, можно автоматически выводить последние посты через [gautamkrishnar/blog-post-workflow](https://github.com/gautamkrishnar/blog-post-workflow).

---

## Тексты для копирования

**Bio:**

```
Fullstack QA · Senior Automation QA. Playwright + Python, UI/API/DB, CI/CD. 4000+ автотестов в проде, стабильность 90%. Открыт к предложениям.
```

**Короткое описание репозитория:**

```
GitHub profile
```
