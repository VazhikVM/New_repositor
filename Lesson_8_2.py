class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


divisible = int(input("Введите делимое число: "))
divisor = int(input("Введите делитель: "))
try:
    if divisor < 1:
        raise MyError("Недопустимое значение делителя, делитель должен быть больше нуля!")
except (ZeroDivisionError, MyError) as er:
    print(er)
else:
    print(divisible / divisor)
