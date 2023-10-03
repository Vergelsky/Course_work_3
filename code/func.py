import json
from transaction import Transaction

def load_transactions_list(filename):

    """
    Простое извлечение истории транзакций из json файла в список
    """

    with open(filename, "r", encoding="utf-8") as trans_file:
        operations = json.load(trans_file)

    return operations

def make_list_of_executed(transactions_list):
    return [Transaction(trans) for trans in transactions_list if trans["status"] == "EXECUTED"]