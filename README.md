## bewise_task

### Описание
Реализовано REST API, принимающее на вход POST запросы с содержимым вида {"questions_num": integer}.
После получения запроса сервис запрашивает с публичного API https://jservice.io/api/random?count=questions_num" 
указанное в полученном запросе количество вопросов. Полученные ответы сохраняются в базе данных.
В случае, если в БД имеется такой же вопрос, то к публичному API с викторинами должны выполняться дополнительные запросы
до тех пор, пока не будет получен уникальный вопрос для викторины. Ответом на запрос должен быть предыдущей сохранённый вопрос для викторины.
В случае его отсутствия - пустой объект.

### Технологии 
  
 - Python  
 - Django
 - Django rest_framework
 - PostgreSQL
 - Celery
 - Redis
 - Docker
   
### Запуск проекта в контейнерах локально на Windows

* Установить WSL и Docker Desktop. Запустить Doker Desktop.
* Скачать проект:
  ```git clone git@github.com:ddr533/bewise_task.git```
* Перейти в папку с проектом.
* Создать файл .env и указать в нём свои данные для переменных окружения.
  Или использовть данные из файла example.env
* Запустить сборку контейнеров: 
  ```
   docker-compose up -d
  ```
* После сборки контейнеров убедиться, что контейнер с БД работает, выполнить миграции и запуск приложения: 
  ```
  docker compose exec -it app python manage.py makemigrations
  docker compose exec -it app python manage.py migrate

  ```
* Перейти в браузере по адресу 127.0.0.1:8000
  Или использовать другой способ для тестирования API, например, Postman.

### Пример запроса к API:
  - POST
  - 127.0.0.1:8000
```
{"questions_num": 1000}
```
![post запрос](https://i.ibb.co/mbBXXFc/image.jpg)
