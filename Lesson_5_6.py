my_file = open("task_6.txt", "r", encoding="utf-8")
my_list = [i.split() for i in my_file]
my_dist = {}
my_sum = 0
for i in my_list:
    my_dist.setdefault(i[0])
    for el in i:
        if el[:el.find('(')].isdigit():
            my_sum = int(el[:el.find('(')]) + my_sum
    my_dist[i[0]] = my_sum
    my_sum = 0

my_file.close()
print(my_dist)
