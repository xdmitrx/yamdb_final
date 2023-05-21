# Проект YaMDb

## Описание проекта
Проект YaMDb собирает **отзывы** пользователей на **произведения**. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

Произведения делятся на **категории**, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).

Произведению может быть присвоен **жанр** из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»).

Добавлять произведения, категории и жанры может только администратор.

Благодарные или возмущённые пользователи оставляют к произведениям текстовые **отзывы** и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — **рейтинг** (целое число). На одно произведение пользователь может оставить только один отзыв.

Пользователи могут оставлять **комментарии** к отзывам.

Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.


## Инструкция по запуску

Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone git@github.com:gweicox/api_yamdb.git
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:
```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполнить миграции:
```bash
cd api_yamdb
python3 manage.py makemigrations
python3 manage.py migrate
```

 В директории */api_yamdb/static/data*, подготовлены несколько файлов в формате csv с контентом для ресурсов **Users**, **Titles**, **Categories**, **Genres**, **Reviews** и **Comments**.
Ими можно наполнить базу данных с помощью команды:
```bash
python3 manage.py load_data
```

Запустить проект:
```bash
python3 manage.py runserver
```


## Примеры запросов к API
Когда вы запустите проект, по адресу `http://127.0.0.1:8000/redoc/` будет доступна документация для API. Документация представлена в формате **Redoc**.

#### Получить код подтверждения на e-mail
Пример запроса: <br>
POST http://127.0.0.1:8000/api/v1/auth/signup/ <br>
Content-Type: application/json <br>

```JSON
{
    "email":    "testuser@testuser.com",
    "username": "test_user"
}
```

#### Получить JWT-токен
Пример запроса: <br>
POST http://127.0.0.1:8000/api/v1/auth/token/ <br>
Content-Type: application/json <br>

```JSON
{
    "confirmation_code": "646960",
    "username": "test_user"
}
```

Пример ответа: <br>
```JSON
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY5NzE2OTgwLCJqdGkiOiI1MzJkMjcyYjY2NjE0MDA3YjJmMjdmYmIzZjU5MTc5MiIsInVzZXJfaWQiOjEwNn0.SMUhL1hHQDEQxW-jBhM0UqB1XhtfdPHXMxw76TMe_H0"
}
```

#### Получение данных своей учетной записи
Пример запроса: <br>
GET http://127.0.0.1:8000/api/v1/users/me/ <br>
Content-Type: application/json <br>
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc... <br>

Пример ответа: <br>
```JSON
{
  "username": "test_user",
  "email": "testuser@testuser.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```

#### Добавление новой категории
Пример запроса: <br>
POST http://127.0.0.1:8000/api/v1/categories/ <br>
Content-Type: application/json <br>

```JSON
{
  "name": "Фильм",
  "slug": "movie"
}
```

Пример ответа: <br>
```JSON
{
  "name": "Фильм",
  "slug": "movie"
}
```

#### Получение списка всех произведений
Пример запроса: <br>
GET http://127.0.0.1:8000/api/v1/titles/ <br>
Content-Type: application/json <br>

Пример ответа: <br>
```JSON
{
  "count": 32,
  "next": "http://127.0.0.1:8000/api/v1/titles/?page=2",
  "previous": null,
  "results": [
    {
      "id": 3,
      "name": "Deep Purple — Smoke on the Water",
      "year": 1971,
      "rating": 10,
      "description": null,
      "genre": [
        {
          "name": "Рок",
          "slug": "rock"
        }
      ],
      "category": {
        "name": "Музыка",
        "slug": "music"
      }
    },
    {
      "id": 4,
      "name": "Elvis Presley - Blue Suede Shoes",
      "year": 1955,
      "rating": 10,
      "description": null,
      "genre": [
        {
          "name": "Rock-n-roll",
          "slug": "rock-n-roll"
        }
      ],
      "category": {
        "name": "Музыка",
        "slug": "music"
      }
    }
  ]
}
```

#### Удаление жанра
Пример запроса: <br>
DELETE http://127.0.0.1:8000/api/v1/genres/rock-n-roll/ <br>
Content-Type: application/json <br>
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc... <br>

Пример ответа: <br>
HTTP/1.1 204 No Content <br>

#### Получение списка всех отзывов на произведение
Пример запроса: <br>
GET http://127.0.0.1:8000/api/v1/titles/1/reviews/ <br>
Content-Type: application/json <br>

Пример ответа: <br>
```JSON
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Побег из Шоушенка",
      "author": "bingobongo",
      "score": 10,
      "text": "Ставлю десять звёзд!\n...Эти голоса были чище и светлее тех, о которых мечтали в этом сером, убогом месте. Как будто две птички влетели и своими голосами развеяли стены наших клеток, и на короткий миг каждый человек в Шоушенке почувствовал себя свободным.",
      "pub_date": "2022-11-22T08:05:10.149044Z"
    },
    {
      "id": 2,
      "title": "Побег из Шоушенка",
      "author": "capt_obvious",
      "score": 10,
      "text": "Не привыкай\n«Эти стены имеют одно свойство: сначала ты их ненавидишь, потом привыкаешь, а потом не можешь без них жить»",
      "pub_date": "2022-11-22T08:05:10.157207Z"
    }
  ]
}
```

#### Добавление комментария к отзыву
Пример запроса: <br>
POST http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/ <br>
Content-Type: application/json <br>

```JSON
{
  "text": "Кстати, а что такое 'четверть фунта'? В граммах это сколько?"
}
```

Пример ответа: <br>
```JSON
{
  "id": 4,
  "author": "test_user",
  "pub_date": "2022-11-22T10:46:17.493268Z",
  "text": "Кстати, а что такое 'четверть фунта'? В граммах это сколько?"
}
```


## Использованные технологии
##### Python 3.7, Django REST Framework 3.12, DRF Simple JWT 4.7


## Об авторах
##### Студенты Яндекс.Практикума: Александр, Виталий, Дмитрий
##### Факультет Бэкенд, специальность Python-разработчик, Когорта №45
