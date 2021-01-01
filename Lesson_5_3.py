from functools import reduce


def avg(x, y):
    return x + y


with open("task_3.txt", "r", encoding="utf-8") as my_file:
    my_list = [i.split() for i in my_file]
    workers = [i[0] for i in my_list if int(my_list[my_list.index(i)][1]) < 20000]
    salary = [i[1] for i in my_list]
    print('Сотрудники с окладом меньше 20 000 рублей:')
    for a, i in enumerate(workers, 1):
        print(f'{a}. {i}')
print(f'Средняя заработная плата {round(reduce(avg, list(map(int, salary)))/len(salary), 2)} рублей.')
