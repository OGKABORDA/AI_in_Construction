# TODO импортировать необходимые молули

import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, mode="r", newline='', encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)  # DictReader автоматически использует первую строку как заголовок
        data = [row for row in reader]  # Преобразуем в список словарей
    with open(OUTPUT_FILENAME, mode="w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)  # indent=4 делает JSON удобным для чтения
if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
