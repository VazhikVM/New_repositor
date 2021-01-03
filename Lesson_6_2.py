class Road:
    mass = 25
    height = 5

    def __init__(self, length, width):
        self._l = length
        self._w = width

    def asphalt(self):
        sum_asphalt = (self._l * self._w * self.mass * self.height)/1000
        return sum_asphalt


street_1 = Road(float(input("Введите длину дороги в метрах: ")), float(input("Введите ширину дороги в метрах: ")))
print(f'Для покрытия дороги необходимо {round(street_1.asphalt(), 2)} тонн асфальта')
