<div id="header" align="center">
  <img src="https://media.giphy.com/media/M9gbBd9nbDrOTu1Mqx/giphy.gif" width="100"/>
</div>
<div id="badges" align="center">
  <img src="https://img.shields.io/badge/Python-blue?style=for-the-badge&logo=python&logoColor=yellow" alt="Python"/>
  <img src="https://img.shields.io/badge/Django-dark_green?style=for-the-badge&logo=django&logoColor=white" alt="Django"/>
  <img src="https://img.shields.io/badge/API-blue?style=for-the-badge&logo=API&logoColor=white" alt="API"/>

<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=25&pause=500&color=F70000&center=true&vCenter=true&width=435&lines=Backend+Yatube" alt="Backend Yatube" /></a>
</div>


## Описание:
Backend социальной сети, которая предназначен для создания и публикации личных дневников. Можно делиться своими публикациями и подписаться на любимых авторов.

## Технологии используемые в проекте:
- python==3.9.13
- Django==3.2.16
- pytest==6.2.4
- pytest-pythonpath==0.7.3
- pytest-django==4.4.0
- djangorestframework==3.12.4
- djangorestframework-simplejwt==4.7.2
- Pillow==9.3.0
- PyJWT==2.1.0
- requests==2.26.0
- djoser==2.1.0

## Инструкция по запуску

1) Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/QualityRU/api_final_yatube.git
```

```
cd api_final_yatube
```

2) Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source env/bin/activate
```

3) Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

4) Выполнить миграции:

```
python manage.py migrate
```

5) Запустить проект:

```
python manage.py runserver
```

## Примеры работы с API:

- Получение публикаций:
```
GET http://127.0.0.1:8000/api/v1/posts/
```
- Создание публикации:
```
POST http://127.0.0.1:8000/api/v1/posts/
```
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
- Получение публикации:
```
GET http://127.0.0.1:8000/api/v1/posts/{id}/
```
- Обновление публикации:
```
PUT http://127.0.0.1:8000/api/v1/posts/{id}/
```
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
- Частичное обновление публикации:
```
PATCH http://127.0.0.1:8000/api/v1/posts/{id}/
```
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
- Удаление публикации:
```
DELETE http://127.0.0.1:8000/api/v1/posts/{id}/
```

Доступ к остальной документации:
```
http://127.0.0.1:8000/redoc/
```

### Автор:
###### Первоначальное авторское право © 2020 Яндекс.Практикум <https://github.com/yandex-praktikum>
###### Раздвоенное авторское право © 2023 Quality <mr.quality@ya.ru>