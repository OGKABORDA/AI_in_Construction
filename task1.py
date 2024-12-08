# TODO решите задачу


import json

def task() -> float:
    with open("input.json", "r") as file:
        data = json.load(file)
    summ = sum(i["score"] * i["weight"] for i in data)
    return round(summ, 3)
print(task())
