class Smartphone:

    def __init__(self, mark, model, number):
        self.mark = mark
        self.model = model
        self.number = number

    def get_mark(self):
        return self.mark

    def get_model(self):
        return self.model

    def get_number(self):
        return self.number

    def get_Smartphone_info(self):
        return f"Модель: {self.mark}, Марка: {self.model}, Номер телефона: {self.number}"
