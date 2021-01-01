import random
import functools


def my_sum(x, y):
    return x + y


with open("task_5.txt", "w", encoding="utf-8") as my_file:
    for i in range(random.randint(0, 6), random.randint(10, 50)):
        print(i, file=my_file, end=' ')
    my_file.write(f'\n')
with open("task_5.txt", "r", encoding="utf-8") as my_file:
    my_list = [i.split() for i in my_file]
print(f'Сумма всех чисел в файле: {functools.reduce(my_sum, list(map(int, functools.reduce(my_sum, my_list))))}')
