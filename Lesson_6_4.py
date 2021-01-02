from random import randint


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def show_speed(self):
        print(f'Скорость {self.speed} км/ч')

    def start(self):
        print('Go!')

    def ston(self):
        print('Stop!')

    def direction(self):
        i = ['right', 'left']
        print(f'Поворот на {i[randint(0, 1)]}, \nМашина полицейская - {self.is_police}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Привышение скрости! Необъодимо снизить скорость до 60 км/ч')
        else:
            print(f'Скорость {self.speed} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Привышение скрости! Необъодимо снизить скорость до 40 км/ч')
        else:
            print(f'Скорость {self.speed} км/ч')


class PoliceCar(Car):
    pass


car_1 = WorkCar(60, 'green', 'Lada', 0)
car_2 = TownCar(70, 'black', 'BMV', 0)
car_3 = SportCar(120, 'black', 'audi', 0)
car_4 = PoliceCar(120, 'black', 'audi', 1)
print(car_1.show_speed(), car_1.start(), car_1.ston(),car_1.direction())
print(car_2.show_speed(), car_2.start(), car_2.ston(),car_2.direction())
print(car_3.show_speed(), car_3.start(), car_3.ston(),car_3.direction())
print(car_4.show_speed(), car_4.start(), car_4.ston(),car_4.direction())