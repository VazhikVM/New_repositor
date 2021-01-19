class ComplexNumber:
    def __init__(self, z):
        self.z = z

    def __add__(self, other):
        return f'Сумма комплексных чисел: {(self.z + other.z)}'

    def __mul__(self, other):
        return f'Произведение комплексных чисел: {self.z * other.z}'

    def __str__(self):
        return f'z = {self.z}'


complex_number_1 = ComplexNumber(3 + 1j)
complex_number_2 = ComplexNumber(2 - 3j)
print(complex_number_1)
print(complex_number_2)
print(complex_number_1 + complex_number_2)
print(complex_number_1 * complex_number_2)
