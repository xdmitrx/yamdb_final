![<-yamdb workflow](https://github.com/xdmitrx/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

# API_YAMDB
REST API проект для сервиса YaMDb — сбор отзывов о фильмах, книгах или музыке.

## Описание

Проект YaMDb собирает отзывы пользователей на произведения.
Произведения делятся на категории: «Книги», «Фильмы», «Музыка».
Список категорий  может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).
### Как запустить проект:

Все описанное ниже относится к ОС Linux.
Клонируем репозиторий и переходим в него:
```bash
git clone https://github.com/xdmitrx/yamdb_final
cd yamdb_final

Переходим в папку с файлом docker-compose.yaml:
```bash
cd infra
```

Поднимаем контейнеры (infra_db_1, infra_web_1, infra_nginx_1):
```bash
docker-compose up -d --build
```

Выполняем миграции:
```bash
docker-compose exec web python manage.py migrate
```

Создаем суперпользователя:
```bash
docker-compose exec web python manage.py createsuperuser
```

Србираем статику:
```bash
docker-compose exec web python manage.py collectstatic --no-input
```

Создаем дамп базы данных (нет в текущем репозитории):
```bash
docker-compose exec web python manage.py dumpdata > dumpPostrgeSQL.json
```

Останавливаем контейнеры:
```bash
docker-compose down -v
```

### Шаблон наполнения .env (не включен в текущий репозиторий) расположенный по пути infra/.env
```
SECRET_KEY=default-key
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

### Документация API YaMDb
Документация доступна по эндпойнту: http://localhost/redoc/

Автор: Беликов Дмитрий https://github.com/xdmitrx

Проект: https://github.com/xdmitrx/yamdb_final.git

Проект доступен по адресу: (http://51.250.69.189/) (if you got lucky).
