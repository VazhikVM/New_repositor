with open("task_4.txt", "r", encoding="utf-8") as my_file:
    my_list = [i.split() for i in my_file]
a = 0
for i in my_list:
    i.pop([a][0])
my_list[0].insert(0, 'Один')
my_list[1].insert(0, 'Два')
my_list[2].insert(0, 'Три')
my_list[3].insert(0, 'Четыре')
with open("task_4_1.txt", "w", encoding="utf-8") as my_file:
    for i in my_list:
        for _ in i:
            print(_, file=my_file, end=' ')
        my_file.write(f'\n')
