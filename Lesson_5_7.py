import json
with open("task_7.txt", "r", encoding="utf-8") as my_file:
    my_list = [i.split() for i in my_file]
my_dict = {}
avg = 0
num = 0
for i in my_list:
    my_dict.setdefault(i[0])
    my_dict[i[0]] = int(i[2]) - int(i[3])
    if int(my_dict[i[0]]) > 0:
        num += 1
        avg = (avg + my_dict[i[0]])
avg = avg / num
my_dict.setdefault('average_profit', round(avg, 2))
json_my = json.dumps([my_dict])
print(json_my)
