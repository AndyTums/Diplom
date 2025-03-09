# Трекер задач сотрудников

Это серверное приложение для работы с базой данных, представляющее собой трекер задач сотрудников. Приложение
обеспечивает CRUD (Create, Read, Update, Delete) операции для сотрудников и задач, а также предоставляет специальные
эндпоинты для получения информации о загруженности сотрудников и важных задачах.

## Оглавление

- [Описание](#описание)
- [Требования](#требования)
- [Функциональность](#функциональность)
- [Технические требования](#технические-требования)
- [Установка и запуск](#установка-и-запуск)
- [Документация API](#документация-api)
- [Тестирование](#тестирование)
- [Лицензия](#лицензия)

## Описание

Трекер задач позволяет компании эффективно управлять заданиями, назначенными сотрудникам, и обеспечивает прозрачность
процессов выполнения задач. Это помогает в равномерном распределении нагрузки между сотрудниками и своевременном
выполнении ключевых задач.

## Требования

### База данных

- Реляционная база данных: PostgreSQL

### Структура базы данных

- **Таблица сотрудников**:
    - ФИО
    - Должность
    - Список задач, который связан форматом ManytoMany в модели Tracker и доступен по запросу "trackers"

- **Таблица задач**:
    - Наименование
    - Ссылка на родительскую задачу (если есть зависимость)
    - Исполнители
    - Срок
    - Статус

## Функциональность

- **CRUD для сотрудников и задач**: Реализованы стандартные операции для создания, чтения, обновления и удаления записей
  для таблиц сотрудников и задач.
- **Специальные эндпоинты**:
    - **Занятые сотрудники**: Возвращает список сотрудников и их задачи, отсортированный по количеству активных задач.
    - **Важные задачи**:
        1. Получает задачи, которые не взяты в работу, но от которых зависят другие задачи, взятые в работу.
        2. Поиск сотрудников, которые могут взять такие задачи (наименее загруженный сотрудник или сотрудник,
           выполняющий родительскую задачу, если ему назначено максимум на 2 задачи больше, чем у наименее загруженного
           сотрудника).
        3. Возвращает список объектов в формате: `{Важная задача, Срок, [ФИО сотрудника]}`.

## Технологии

1. **Язык программирования**: Python 3.12
2. **Фреймворк**: Django с использованием Django REST Framework (DRF)
3. **База данных**: PostgreSQL
4. **ORM**: Django ORM
5. **Контейнеризация**: Docker, Docker-Compose
6. **Валидация данных**: Реализована валидация данных входящих запросов.
7. **Документация**: README.md с описанием структуры проекта, инструкциями по установке и запуску, а также описанием
   API.
8. **Качество кода**: Соблюдение стандартов PEP8. Весь код хранится в удаленном Git репозитории.
9. **Тестирование**: Тесты для всех основных функций платформы, покрытие минимум 75%.
10. **Автодокументация**: Автогенерируемая документация API с использованием Swagger или ReDoc.

## Установка и запуск

1. Клонируйте репозиторий:

```bash
git clone https://github.com/AndyTums/MyDRFCourse.git
````

3. Установите зависимости:

```bash
poetry update
````

4. Настройте базу данных `PostgreSQL` и заполните переменные окружения:

```bash
SECRET_KEY=

DEBUG=

NAME=Diplom
HOST=
USER=
PASSWORD=
PORT=

````

5. Запустите миграции:

```bash
python manage.py makemigrations
python manage.py migrate
````

6. Запустите сервер:
```bash
python manage.py runserver
````

7. По необходимости добавить проект в контейнер:
```bash
docker-compose up --build
````

#### После запуска приложение будет доступно по адресу: http://localhost:8000

## Документация API

Автоматическая документация API будет доступна по адресу: [http://localhost:8000/api/docs](http://localhost:8000/api/docs)

## Тестирование

Для запуска тестов используйте следующую команду:
```bash
python manage.py test
````

## Лицензия

Этот проект лицензирован на условиях MIT License. Смотрите файл [LICENSE](LICENSE) для подробностей.



[//]: # (# Приложение для управления привычками)

[//]: # ()
[//]: # (Это приложение позволяет пользователям создавать, отслеживать и управлять своими привычками. Оно построено на основе Django REST Framework &#40;DRF&#41; и включает следующие функции:)

[//]: # ()
[//]: # (- **Авторизация пользователей**: Регистрация, вход и управление профилем.)

[//]: # (- **Управление привычками**: Создание, редактирование, удаление и отслеживание привычек.)

[//]: # (- **Периодические задачи**: Использование Celery и Celery Beat для напоминаний и уведомлений.)

[//]: # (- **Docker**: Простая установка и запуск с помощью Docker.)

[//]: # (- **Deploy**: Отправка проекта на удаленный сервер.)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (## Основные функции)

[//]: # ()
[//]: # (- **Регистрация и авторизация**:)

[//]: # (  - Регистрация нового пользователя.)

[//]: # (  - Вход в систему с использованием JWT-токенов.)

[//]: # (  - Обновление и удаление профиля.)

[//]: # ()
[//]: # (- **Управление привычками**:)

[//]: # (  - Создание привычек с указанием названия, описания, периодичности и времени выполнения.)

[//]: # (  - Отслеживание прогресса выполнения привычек.)

[//]: # (  - Получение списка привычек с фильтрацией и сортировкой.)

[//]: # ()
[//]: # (- **Напоминания и уведомления**:)

[//]: # (  - Использование Celery для отправки уведомлений &#40;например, в Телеграм&#41; о необходимости выполнения привычек.)

[//]: # (  - Использование Celery Beat для периодических задач &#40;например, ежедневных напоминаний&#41;.)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (## Технологии)

[//]: # ()
[//]: # (- **Backend**:)

[//]: # (  - Django)

[//]: # (  - Django REST Framework &#40;DRF&#41;)

[//]: # (  - Celery)

[//]: # (  - Celery Beat)

[//]: # (  - PostgreSQL)

[//]: # (  - Docker)

[//]: # (  - Nginx)

[//]: # (  - Git Actions)

[//]: # ()
[//]: # (- **Авторизация**:)

[//]: # (  - JWT &#40;JSON Web Tokens&#41;)

[//]: # ()
[//]: # (- **Очереди задач**:)

[//]: # (  - Redis)

[//]: # ()
[//]: # (- **Контейнеризация**:)

[//]: # (  - Docker)

[//]: # (  - Docker Compose)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (## Установка и запуск)

[//]: # ()
[//]: # (### 1. Клонируйте репозиторий)

[//]: # ()
[//]: # (```bash)

[//]: # (git clone https://github.com/AndyTums/MyDRFCourse.git)

[//]: # (````)

[//]: # ()
[//]: # (### 2. Настройте переменные окружения)

[//]: # (```bash)

[//]: # (Создайте файл `.env` в корневой директории и добавьте в него следующие переменные:)

[//]: # ()
[//]: # (SECRET_KEY=)

[//]: # ()
[//]: # (DEBUG=)

[//]: # ()
[//]: # (# Данные для подключения к БД)

[//]: # (NAME=)

[//]: # (USER=)

[//]: # (PASSWORD=)

[//]: # (HOST=)

[//]: # (PORT=)

[//]: # ()
[//]: # (# DOCKER)

[//]: # (POSTGRES_PASSWORD=PASSWORD)

[//]: # (POSTGRES_USER=USER)

[//]: # (POSTGRES_PORT=PORT)

[//]: # (POSTGRES_DB=NAME)

[//]: # (POSTGRES_HOST=HOST)

[//]: # (CELERY_BROKER_URL = 'redis://redis:6379/0')

[//]: # (CELERY_RESULT_BACKEND = 'redis://redis:6379/0')

[//]: # ()
[//]: # (# Почта для отправки сообщений)

[//]: # (EMAIL_HOST_PASSWORD =)

[//]: # ()
[//]: # (# TELEGRAM)

[//]: # (API_TOKEN_TELEGRAM =)

[//]: # (TG_NAME_CHANEL =)

[//]: # (```)

[//]: # ()
[//]: # (### 3. Запустите приложение с помощью Docker Compose)

[//]: # ()
[//]: # (```bash)

[//]: # (docker-compose up --build)

[//]: # (```)

[//]: # ()
[//]: # (После запуска приложение будет доступно по адресу: http://localhost:8000.)

[//]: # ()
[//]: # (### API Endpoints)

[//]: # ()
[//]: # (**Авторизация**:)

[//]: # ()
[//]: # (  - POST http://localhost:8000/login/ - вход в ЛК)

[//]: # (  - POST http://localhost:8000/logout/ - выход с ЛК)

[//]: # ()
[//]: # (  - POST http://localhost:8000/token/refresh/ - обновление токена)

[//]: # ()
[//]: # (**Привычки**:)

[//]: # ()
[//]: # (  - GET http://localhost:8000/habit/ - список привычек)

[//]: # (  - GET http://localhost:8000/habit/id/ - информация о привычке)

[//]: # (  - POST http://localhost:8000/habit/ - создание привычки)

[//]: # (  - PATCH http://localhost:8000/habit/id/ - редактирование привычки)

[//]: # (  - DELETE http://localhost:8000/habit/id/ - удаление привычки)

[//]: # ()
[//]: # (**Пользователь**:)

[//]: # ()
[//]: # (  - GET http://localhost:8000/user/ - список пользователей)

[//]: # (  - GET http://localhost:8000/user/id/ - информация о пользователе)

[//]: # (  - POST http://localhost:8000/user/ - создание пользователя)

[//]: # (  - PATCH http://localhost:8000/user/id/ - редактирование пользователя)

[//]: # (  - DELETE http://localhost:8000/user/id/ - удаление пользователя)

[//]: # ()
[//]: # ()
[//]: # (### 4. Использование Celery и Celery Beat)

[//]: # ()
[//]: # (- Celery используется для выполнения асинхронных задач, таких как отправка уведомлений.)

[//]: # ()
[//]: # (- Celery Beat используется для выполнения периодических задач, таких как ежедневные напоминания.)

[//]: # ()
[//]: # (#### Пример задачи Celery:)

[//]: # (``` bash)

[//]: # (from celery import shared_task)

[//]: # (from django.core.mail import send_mail)

[//]: # ()
[//]: # (@shared_task)

[//]: # (def send_reminder_email&#40;email, message&#41;:)

[//]: # (    send_mail&#40;)

[//]: # (        'Напоминание о привычке',)

[//]: # (        message,)

[//]: # (        'from@example.com',)

[//]: # (        [email],)

[//]: # (        fail_silently=False,)

[//]: # (    &#41;)

[//]: # (```)

[//]: # ()
[//]: # (#### Пример периодической задачи Celery Beat)

[//]: # (В файле settings.py:)

[//]: # (``` bash)

[//]: # (from celery.schedules import crontab)

[//]: # ()
[//]: # (CELERY_BEAT_SCHEDULE = {)

[//]: # (    'check_is_active': {)

[//]: # (        'task': 'habit.tasks.send_message_to_user',)

[//]: # (        'schedule': timedelta&#40;seconds=20&#41;,)

[//]: # (    },)

[//]: # (})

[//]: # (```)

[//]: # ()
[//]: # (### 5. Структура проекта:)

[//]: # (``` bash)

[//]: # (habit-tracker/)

[//]: # (├── .env)

[//]: # (├── .github/workflows/ci.yml)

[//]: # (├── docker-compose.yml)

[//]: # (├── Dockerfile)

[//]: # (├── manage.py)

[//]: # (├── requirements.txt)

[//]: # (├── habits/)

[//]: # (│   ├── models.py)

[//]: # (│   ├── serializers.py)

[//]: # (│   ├── views.py)

[//]: # (│   ├── tasks.py)

[//]: # (│   └── test.py)

[//]: # (└── myproject/)

[//]: # (    ├── settings.py)

[//]: # (    ├── urls.py)

[//]: # (    └── ...)

[//]: # (```)

[//]: # ()
[//]: # (### 6. Использование Deploy)

[//]: # ()
[//]: # (**Настройка удаленного сервера**:)

[//]: # (- Сервер настроен для развертывания веб-приложения.)

[//]: # (- Установлены необходимые пакеты и зависимости для работы проекта &#40;Python, Django, Gunicorn, Nginx&#41;.)

[//]: # (- Приложение доступно по IP-адресу: 84.201.161.178.)

[//]: # (- Настроены параметры безопасности: используются SSH-ключи для доступа.)

[//]: # ()
[//]: # (**Шаги выполнения запуска workflow**:)

[//]: # ()
[//]: # (- Файл YAML для GitHub Actions находится в репозитории в папке .github/workflows.)

[//]: # (- Workflow запускается при каждом push в репозиторий.)

[//]: # (- Workflow включает шаг для запуска тестов проекта.)

[//]: # (- Тесты успешно выполняются в рамках workflow и завершаются с отчетом.)

[//]: # (- Ошибки тестов останавливают выполнение следующих шагов workflow.)

[//]: # (- Workflow содержит шаг деплоя, который запускается только после успешного завершения тестов.)

[//]: # (- Проект автоматически деплоится на удаленный сервер.)

[//]: # (- Деплой выполняется корректно, без ошибок.)

[//]: # ()
[//]: # (#### Для быстрой загрузки проекта на сервер, используйте Git Actions -->> [.yml]&#40;./.github/workflows/ci.yml&#41;)

[//]: # (Незабудьте внести ваши данные в переменное окружение, а так же запросить secrets. у владельца репозитория!)

[//]: # ()
[//]: # (### 7. Лицензия)

[//]: # ()
[//]: # (#### Этот проект распространяется под лицензией MIT. Подробности см. в файле LICENSE.)
