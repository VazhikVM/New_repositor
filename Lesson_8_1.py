class MyDate:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def get_num(cls, num):
        d, m, y = num
        return cls(d, m, y)

    @staticmethod
    def get_date(date):
        month_dict = {1: "Января", 2: "Фераля", 3: "Марта", 4: "Апреля", 5: "Мая", 6: "Июня", 7: "Июля", 8: "Августа",
                      9: "Сентября", 10: "Октября", 11: "Ноября", 12: "Декабря"}
        return f'{int(date.day) if 32 > int(date.day) > 0 else print("День введен некорректно (1-31)")}' \
               f' {month_dict[int(date.month)] if 13 > int(date.month) > 0 else print("Месяц введен некорректно (1-12)")}' \
               f' {int(date.year)if 2100 > int(date.year) > 1949 else print("Год введен некорректно 1950 - 2099")} года'


data_list = input('Введите дату формата "01-01-2000": ').split('-')
result = MyDate.get_num(data_list)
print(MyDate.get_date(result))
