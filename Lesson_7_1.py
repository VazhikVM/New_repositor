class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        return Matrix([[sum(x) for x in zip(*y)] for y in zip(self.matrix, other.matrix)])

    def __str__(self):
        return '\n'.join(['\t'.join([str(el) for el in i]) for i in self.matrix])


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])
matrix_3 = Matrix([[13, 14], [15, 16], [17, 18]])
print(matrix_1)
print(matrix_1 + matrix_2)
print(matrix_1 + matrix_2 + matrix_3)
