# Блогикум

Учебный Django-проект с публикациями, категориями и местоположениями.
Публикации хранятся в SQLite. На главной отображаются пять последних
опубликованных записей. Будущие публикации и записи скрытых категорий
недоступны посетителям. Модели можно редактировать через админку.

## Запуск в Windows PowerShell

Из папки `projects/blogicum` выполните:

```powershell
python -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
.\venv\Scripts\python.exe blogicum/manage.py migrate
.\venv\Scripts\python.exe blogicum/manage.py loaddata db.json
.\venv\Scripts\python.exe blogicum/manage.py runserver
```

Откройте http://127.0.0.1:8000/.

Для доступа к админке создайте своего суперпользователя:

```powershell
.\venv\Scripts\python.exe blogicum/manage.py createsuperuser
```

Админка находится по адресу http://127.0.0.1:8000/admin/.

## Проверка

Из той же папки:

```powershell
.\venv\Scripts\python.exe -m pytest
```

В проект включены 82 теста Практикума, миграции, шаблоны,
статические файлы и учебные фикстуры `db.json`.
