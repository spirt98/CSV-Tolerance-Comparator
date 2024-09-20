# CSV Tolerance Comparator

Этот проект представляет собой скрипт на Python для сравнения двух CSV файлов с учетом заданных допусков.

## Установка

1. Клонируйте репозиторий:
    ```sh
    git clone https://github.com/yourusername/csv-tolerance-comparator.git
    cd csv-tolerance-comparator
    ```

2. Убедитесь, что у вас установлен Python 3.6 или выше.

## Использование

1. Поместите ваши CSV файлы в корневую директорию проекта и назовите их `1.csv` и `2.csv`.

2. Запустите скрипт:
    ```sh
    python csv_tolerance_comparator.py
    ```

3. Результат будет записан в файл `output.csv`.

## Конфигурация

Вы можете изменить заголовки и допуски для сравнения, отредактировав следующие строки в `csv_tolerance_comparator.py`:

```python
# Заголовки которые надо сравнить
headers = ['scanId', 'distance', 'bearing', 'radialVelocity']
# Погрешности
tolerance = [0, 200, 2, 0.4]
