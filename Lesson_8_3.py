class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
number = 0
while number != 'stop':
    number = input("Введите число: ")
    try:
        if number == 'stop':
            raise MyError ("Спасибо за игру")
    except (ValueError, MyError) as er:
        print(er)
        print(my_list)
        break
    if number.isdigit():
        my_list.append(number)
    else:
        print("Ввод текста не допустим, для выхода из программы введите 'stop'")
