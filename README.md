# Python: домашние задания и проекты

Учебный репозиторий для домашних заданий, небольших программ и более крупных проектов на Python.

## Структура

```text
homework/             # задания по урокам и темам
  lesson_01/
projects/             # отдельные учебные проекты
tests/                # автоматические тесты
```

Для нового урока создайте папку `homework/lesson_02`, для нового проекта — папку внутри `projects`.

## Быстрый старт

Нужен Python 3.11 или новее. В PowerShell выполните:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

Проверка кода:

```powershell
python -m ruff check .
python -m pytest
```

## Как отправить работу на GitHub

```powershell
git status
git add .
git commit -m "Добавлено домашнее задание 1"
git push
```

Перед коммитом полезно запускать `python -m ruff check .` и `python -m pytest`.

## Полезные команды Git

- `git status` — показать изменённые файлы.
- `git diff` — показать изменения до добавления в коммит.
- `git log --oneline` — показать краткую историю коммитов.
- `git pull --rebase` — забрать свежие изменения с GitHub.
- `git push` — отправить свои коммиты на GitHub.

