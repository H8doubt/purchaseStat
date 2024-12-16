# purchaseStat

## Запустите контейнеры с помощью команды:
docker-compose --project-name="ps-pg-16" up -d

## Установка зависимостей
python -m pip install -r requirements.txt

## Запуск приложения
fastapi run 

##▎Эндпоинты API

▎Создание пользователя

POST /users/

Создает нового пользователя.

Тело запроса:
{
  "name": "Имя пользователя"
}


Ответ:
{
  "id": 1
}


▎Создание продукта

POST /products/

Создает новый продукт.

Тело запроса:
{
  "name": "Название продукта"
}


Ответ:
{
  "id": 1
}


▎Создание покупки

POST /purchases/

Создает запись о покупке.

Тело запроса:
{
  "user_id": 1,
  "product_id": 1
}


Ответ:
{
  "message": "Purchase created"
}


▎Получение рекомендаций

GET /recommendations/{user_id}

Получает рекомендации по продуктам для указанного пользователя.

Ответ:
{
  "product_id": 1
}

