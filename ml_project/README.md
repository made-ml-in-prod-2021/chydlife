Installation:

For virtual env create new env and activate requirements using:
pip install -r requirements.txt

Usage:

python ml_project/homework1.py

Test:

pytest ml_project/test.py

Модульный проект, который состоит из нескольких частей:
- папка config содержит необходимую конфигурацию (перечень моделей для классификации и их описание)
- папка data содержит исходные данные и данные для тестирование, скрипт для обработки данных
- папка data_for_tes содержит файл для тестирования
- папка model содержит скрипт для создания и валидации модели
- в папку results пишутся результаты (предсказания) для тестовой выборки
- скрипт homework1 запускает весь pipeline обучения и предсказания
- файл test.py содержит тесты.
- output file.png - пример результирующего лога (пишется в stdout)


