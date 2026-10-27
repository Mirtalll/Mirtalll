# Настройка GitHub-профиля Mirtalll

Готовые файлы лежат в `~/github-profile`:

| Файл | Что это |
|:--|:--|
| `banner.png` | Баннер для README (1280×420) |
| `avatar-lightning.png` | Чистый аватар с молнией (500×500) — рекомендую |
| `avatar-500.png` | Аватар из исходной молнии `~/.face` (500×500, мягкий) |
| `avatar.png` | Круглая версия для README |
| `README.md` | README профиля |

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

## 3. Репозиторий профиля

README показывается на главной странице профиля, только если существует **публичный** репозиторий с именем, совпадающим с ником: `Mirtalll/Mirtalll`.

1. Откройте https://github.com/new
2. **Repository name:** `Mirtalll`
3. **Description:** `GitHub profile`
4. Выберите **Public**
5. **Не добавляйте** README, .gitignore и лицензию — репозиторий должен быть пустым
6. Нажмите **Create repository**

После этого отправьте файлы (или скажите мне — я запушу):

```bash
cd ~/github-profile
git init -b main
git add .
git commit -m "Add GitHub profile README"
git remote add origin git@github.com:Mirtalll/Mirtalll.git
git push -u origin main
```

---

## 4. Что ещё можно улучшить

- **Закрепить репозитории:** Profile → **Customize your pins** — выбрать 4–6 лучших проектов.
- **Приватные контрибуции:** Profile → **Contribution settings** → включить **Private contributions**, чтобы активность была видна.
- **Публичное портфолио:** сейчас на GitHub нет публичных репозиториев, поэтому карточки статистики в README не добавлены. Когда опубликуете 2–3 проекта (QA-фреймворк, API-тесты, pet-проект), можно добавить GitHub Stats и Top Languages.
- **Status / Currently working on:** можно указать в профиле через настройки статуса.

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
