from datetime import datetime

class Transaction():

    def __init__(self, trans_data_dict):
        self.id = trans_data_dict["id"]
        self.state = trans_data_dict["state"]
        self.date = self.change_date(trans_data_dict["date"])
        self.operationAmount = trans_data_dict["operationAmount"]
        self.description = trans_data_dict["description"]
        self.tr_from = trans_data_dict["from"]
        self.to = trans_data_dict["to"]

    def __repr__(self):
        pass

    def change_date(self, date):
        pass


    def hide_card(self, date):
        pass

    def hide_number(self, date):
        pass



#     "id": 441945886,
#     "state": "EXECUTED",
               #14.10.2018
#     "date": "2019-08-26T10:50:58.294041",
#     "operationAmount": {
#       "amount": "31957.58",
#       "currency": {
#         "name": "руб.",
#         "code": "RUB"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "Maestro 1596837868705199",
#     "to": "Счет 64686473678894779589"