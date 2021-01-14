class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        return Cell(self.cell - other.cell if (self.cell - other.cell) > 0 else "Число клеток не может быть "
                                                                                "отрицательным")

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell(self.cell // other.cell)

    def __str__(self):
        return f'Число клеток: {self.cell}'

    def make_order(self, row):
        num_row = ''
        for i in range(int (self.cell / row)):
            num_row += '*' * row + '\n'
        num_row += '*' * (self.cell % row) + '\n'
        return num_row


one = Cell(13)
two = Cell(5)
three = Cell(1)
print(one)
print(one + two)
print(one + two - three)
print(one / two / three)
print(one * two)
print(one.make_order(5))
print(three.make_order(2))
