# API Django Yatube
### ОПИСАНИЕ
API для Yatube — это backend-часть социальной сети, разработанная с использованием Django и Django REST Framework. Проект предоставляет API, которое позволяет управлять контентом и взаимодействием между пользователями. Основная цель проекта — создать удобный инструмент для разработчиков, которые хотят интегрировать функциональность проекта в свои приложения или расширять его возможности.

Проект решает следующие задачи:
1. Пользователи могут создавать, редактировать и удалять посты, а также оставлять комментарии.
2. Реализована возможность подписываться на других пользователей.
3. Используется JWT-аутентификация для защиты данных и управления доступом.
4. API предоставляет удобные инструменты для работы с данными, включая пагинацию, фильтрацию и поиск.

Проект будет полезен для разработчиков, которые хотят создать приложение для Yatube или интегрировать его функциональность в другие платформы.

API предоставляет следующие ключевые функции:
1. Управление постами:
Аутентифицированные пользователи могут публиковать новые посты.
Только автор поста может изменять или удалять его.
Все пользователи могут просматривать посты с поддержкой пагинации.

2. Комментарии
Аутентифицированные пользователи могут оставлять комментарии к постам.
Только автор комментария может изменять или удалять его.
Все пользователи могут просматривать комментарии к конкретному посту.

3. Группы
Все пользователи могут просматривать доступные группы.
Посты могут быть привязаны к группам.

4. Подписки
Аутентифицированные пользователи могут подписываться на других пользователей.
Получение списка подписок: Пользователи могут просматривать свои текущие подписки.
Реализована возможность поиска по имени пользователя, на которого подписан текущий пользователь.

5. Аутентификация и авторизация
Используются JWT-токены для аутентификации пользователей.

6. Права доступа
Неаутентифицированные пользователи могут только читать данные (посты, комментарии, группы).
Аутентифицированные пользователи могут создавать, редактировать и удалять свои посты и комментарии.
Только аутентифицированные пользователи могут управлять подписками.

7. Пагинация и фильтрация
Посты и комментарии возвращаются с поддержкой пагинации.
В подписках реализован поиск по имени пользователя.


### СТЕК
Python 3.9.21,
Django 3.2.16,
djangorestframework 3.12.4,
JWT 2.1.0,
Djoser 2.1.0.


### КАК ЗАПУСТИТЬ ПРОЕКТ

Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone https://github.com/DmitryProtasevich/api_django_yatube.git
```
```bash
cd api_django_yatube
```
Cоздать и активировать виртуальное окружение:
```bash
python3 -m venv env
```
```bash
source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```bash
python3 -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```
Выполнить миграции:
```bash
python3 manage.py migrate
```
Запустить проект:
```bash
python3 manage.py runserver
```
Перейти в браузере по адресу: http://127.0.0.1:8000/.

### ПОЛНАЯ ДОКУМЕНТАЦИЯ API
Доступна по адресу: http://127.0.0.1:8000/redoc/

### ПРИМЕР ИСПОЛЬЗОВАНИЯ

Запрос для получения списка постов:
```bash
GET /v1/posts/
```

Ответ:
```JSON
[
    {
        "id": 3,
        "author": "new_user",
        "text": "Пост зарегистрированного пользователя.",
        "pub_date": "2025-03-14T15:07:00.201654+03:00",
        "image": "http://127.0.0.1:8000/media/posts/t_123.png",
        "group": 1
    },
    {
        "id": 2,
        "author": "new_user",
        "text": "string",
        "pub_date": "2025-03-12T14:23:49.985531+03:00",
        "image": "http://127.0.0.1:8000/media/posts/temp_qyjDTgT.png",
        "group": 1
    }
]
```

### АВТОР
Дмитрий Протасевич  
GitHub: https://github.com/DmitryProtasevich  
Telegram: https://t.me/DmitryProtasevich/  
