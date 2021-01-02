class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


worker_1 = Position('Иван', 'Иванов', 'Продавец', 10000, 10000)
worker_2 = Position('Сергей', 'Измайлов', 'Директор', 15000, 100000)
print(f'Сотрудник {worker_1.get_full_name()}, ЗП {worker_1.get_total_income()} рублей.')
print(f'Сотрудник {worker_2.get_full_name()}, ЗП {worker_2.get_total_income()} рублей.')
