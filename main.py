from code import transaction as tr
from code import func

transactions_history_file = "operations.json"



# Извлекаем словарь с транзакциями в переменную
operations = func.load_transactions_list()

#Создаём список объектов выполненных транзакций
transactions = func.make_list_of_executed()

#Нам нужны самые свежие, поэтому сортируем по дате
transactions.sort(key=getattr("date"))

#Выводим в консоль первые 5 транзакций из отсортированного списка
for trans in transactions[:4]:
    print(trans)
    print()