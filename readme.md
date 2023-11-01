# Тестовое задание AcePlace
## Подход к решению поставленной задачи
Для создания REST API я использовал веб-фреймворк FastAPI. Все операции с базой данных mongoDB осуществлял через mongoexpress(Document-Object Mapper). В качестве ASGI веб-сервера для запуска RESTAPI использовал Uvicorn. Для smtp сервера для отправки email использовал встроенную в python библиотеку smtplib.

## Installation

Проект требует наличия [Docker](https://nodejs.org/) для запуска.

Корректно заполните .env файл. Он будет в проекте с примером заполнения.

Собираем образ в папке с проектом и запускаем его:

```sh
docker-compose up
```

После окончания сборки и запуска проекта, в консоли(либо в "api" контейнере) должно появится следующее сообщение:

```sh
api                           | INFO:app.db:User_id is 6542cf19580622257a1746b5
api                           | INFO:     Started server process [1]
api                           | INFO:     Waiting for application startup.
api                           | INFO:     Application startup complete.
api                           | INFO:     Uvicorn running on http://0.0.0.0:8002 (Press CTRL+C to quit)
```

Так как тестовое задание не подразумевает создания документов пользователя, будет создан тестовый документ пользователя согласно инструкциям в задании. Id документа будет выведен в консоль. Id понадобится для обращения к документу в API.
## Доступ к API и Mongoexpress

Внимание: порт к api, согласно заданию, регулируется через переменные окружения .env.
В примере .env установлен порт "8002".

| Plugin | README |
| ------ | ------ |
| FastAPI Docs | http://localhost:8002/docs |
| Mongoexpress | http://localhost:8081/ |

Данные для доступа к mongoexpress.

| Поле | Значение |
| ------ | ------ |
| Логин | admin |
| Пароль | pass |

