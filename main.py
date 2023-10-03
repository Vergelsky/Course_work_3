from src import transaction as tr
import json


# Извлекаем список транзакций в переменную
with open("transaction.json", "r") as trans_file:
    operations = json.load(trans_file)

#Создаём список объектов выполненных транзакций
transactions = [tr.Transaction(trans) for trans in operations if trans.status == "EXECUTED"]

#Нам нужны последние, поэтому сортируем
transactions.sort(key=getattr("datetime"))

for trans in transactions[:4]:
    pass