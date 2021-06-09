# Запуск сервиса и запуск скрипта
Для этого нужно перейти в папку images\airflow-ml-base\
Запустить команду
```bash
docker build . -t airflow-ml-base:latest
```
Затем перейти обратно в основную папку, и запустить оттуда команду: 
```bash
docker-compose up --build
```
Заход в airflow 