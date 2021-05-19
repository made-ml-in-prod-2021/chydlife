### Все запуски происходят из папки online_inference. Перед запуском активируется виртуальное окружение 
pip install -r requirements.txt

## Запуск сервиса и запуск скрипта
```bash
python app.py
python make_request.py
```


## Построение и запуск докера
```bash
docker build -t chydlife/online_inference:v2 .
docker run -p 8000:8000 -t online_inference/chydlife/online_inference:v2
```


## Запуск скрипта происходит аналогичным образом
```bash
python make_request.py
```

Остановка сервиса происходит с помощью команды control+C

## Push докера
```bash
docker push chydlife/online_inference:v2
```


## Pull докера
```bash
docker pull chydlife/online_inference:v2
```

Затем докер можно запустить с помощью команды 
```bash
docker run -p 8000:8000 -t online_inference/chydlife/online_inference:v2
```


## Запуск теста
```bash
pytest app_test.py
```
