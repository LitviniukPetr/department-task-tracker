# Завдання з питань охорони праці
## філії "УЗ Вагон-сервіс"

Веб-застосунок для управління завданнями з охорони праці across 18 підрозділів філії.

## Функціонал

- 🔐 Авторизація користувачів
- 👁 Перегляд завдань свого підрозділу
- ✅ Статуси завдань: Активне / Виконане
- 👤 Три ролі: Співробітник / Менеджер / Supervisor
- 🛠 Адмін-панель для керування даними

## Ролі користувачів

| Роль | Перегляд | Створення/редагування |
|------|----------|-----------------------|
| Співробітник | Тільки свій підрозділ | ❌ |
| Менеджер | Тільки свій підрозділ | ✅ |
| Supervisor | Всі 18 підрозділів | ✅ |

## Технології

- Python 3.14
- Django 6.0
- Bootstrap 5
- SQLite

## Запуск локально

```bash
git clone https://github.com/LitviniukPetr/department-task-tracker.git
cd department-task-tracker
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```