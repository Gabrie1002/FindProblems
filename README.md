# Инструкция по запуску проекта

## Требования
- Установленный Docker
- Установленный Docker Compose

## Запуск проекта

Создайте файл .env в корне проекта (если нужно изменить настройки):

FLASK_HOST=1.1.1.1
FLASK_PORT=8000
FLASK_DEBUG=true

MONGO_URI=mongodb://mongo:27017/problems
MONGO_DB_NAME=name
MONGO_COLLECTION_NAME=col_name

Для запуска используйте:
docker-compose up -d --build
