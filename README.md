# Sprint_9 — Foodgram

Проект проверяет регистрацию, вход и создание рецепта на учебном стенде Foodgram. Тест регистрации проверяет переход на `/signin` и отображение формы входа. Тест входа проверяет переход на `/recipes` и отображение элемента «Выход». Для тестов входа и создания рецепта фикстура каждый раз регистрирует отдельного пользователя.

На текущем стенде форма входа принимает имя пользователя в поле «Электронная почта». Фикстура по-прежнему задаёт и имя пользователя, и почту при регистрации.

Тест создания рецепта выбирает морковь из подсказок, указывает её количество, загружает `assets/recipe.png` и проверяет, что открылась карточка с введённым названием. Теги оставлены выбранными по умолчанию, как их заполняет форма.

Запуск из папки проекта в PowerShell с установленным Chrome и зависимостями в `venv`:

```powershell
.\venv\Scripts\python.exe -m pytest test -v --alluredir=allure-results --clean-alluredir
```

Если нужно восстановить зависимости, выполни `.\venv\Scripts\python.exe -m pip install -r requirements.txt`.

## Запуск через Docker Compose

Запусти Docker Desktop в режиме Linux containers. Из корня проекта выполни:

```powershell
docker pull selenoid/chrome:128.0
docker compose up --build --exit-code-from tests
docker compose down
```

Compose ждёт готовности Selenoid и передаёт контейнеру тестов его адрес. Selenoid запускает Chrome 128 из `browsers.json`. `LocalFileDetector` передаёт изображение из контейнера тестов в браузер. Итог pytest определяет статус команды `docker compose up`.

Если запуск прервался, логи Selenoid можно посмотреть командой `docker compose logs selenoid` перед `docker compose down`.

## Отчёт и GitHub Actions

После успешного прогона сформируй HTML-отчёт установленным Allure CLI:

```powershell
allure generate allure-results --clean -o allure-report
```

Добавь в репозиторий папку `allure-report/` с готовым отчётом. Сырые результаты `allure-results/` исключены через `.gitignore`.

`.github/workflows/ci.yml` запускает тот же Docker Compose при push, pull request или ручном запуске. Сырые результаты доступны в артефакте `allure-results` на странице запуска. Для сдачи приложи скриншот успешного запуска из вкладки Actions.
