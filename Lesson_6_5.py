class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Draw a picture with a pen on the canvas")


class Pencil(Stationery):
    def draw(self):
        print("Draw a picture with a pencil on the canvas")


class Handle(Stationery):
    def draw(self):
        print("Draw a picture with a marker on the canvas")


pen_1 = Pen("Гелевая ручка")
pencil_1 = Pencil("Простой карандаш")
hand_1 = Handle("Нестераемый маркер")

print(pen_1.draw())
print(pencil_1.draw())
print(hand_1.draw())
