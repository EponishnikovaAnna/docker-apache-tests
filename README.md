# Apache Tests Project

## Описание проекта

Проект содержит два Docker-контейнера:

- **target**: контейнер с Apache2, демонстрирующий статическую страницу `/index.html`
- **agent**: контейнер с Python-тестами (`pytest` + `paramiko`)

## Структура проекта
```apache_tests/
├─ agent/
│   ├─ Dockerfile
│   └─ tests/
│       └─ test_apache.py
├─ target/
│   └─ Dockerfile
├─ html/
│   └─ index.html
├─ .env
├─ docker-compose.yml
├─ build.sh
└─ run.sh
```


**Тесты проверяют:**
- Запущен ли веб-сервер
- Нет ли ошибок в логах Apache за последние N минут
- Корректность отображения `/index.html`
- Обработку ошибок на несуществующие страницы

## Необходимые зависимости
- Docker
- Docker Compose (v2)
- Git
- Bash (для запуска скриптов)

## Настройка переменных окружения
В корне проекта создайте файл `.env` с содержимым:
SSH_USER=testuser
SSH_PASS=testpass
SSH_PORT=22

TARGET_HOST=target
TARGET_PORT=80
LOG_INTERVAL=1

## Сборка проекта

Скрипт для сборки Docker-образов:
./build.sh
Скрипт для запуска контейнеров и выполнения тестов:
./run.sh

## Ожидаемый результат
```agent   | ============================= test session starts ==============================
agent   | platform linux -- Python 3.11.2, pytest-8.4.2, pluggy-1.6.0 -- /opt/venv/bin/python3
agent   | cachedir: .pytest_cache
agent   | rootdir: /home/tester
agent   | collecting ... collected 4 items
agent   | 
agent   | tests/test_apache.py::test_apache_running PASSED                         [ 25%]
agent   | tests/test_apache.py::test_no_errors_in_logs PASSED                      [ 50%]
agent   | tests/test_apache.py::test_index_page_avaliable PASSED                   [ 75%]
agent   | tests/test_apache.py::test_nonexistent_page PASSED                       [100%]





  
