my_file = open("task_1.txt", "w", encoding="utf-8")
my_file.close()
enter = input("Введите текс и нажмите Enter: ")
my_file = open("task_1.txt", "a", encoding="utf-8")
while True:
    if enter.lower() == 'q':
        break
    else:
        print(enter, file=my_file)
        enter = input("Для продолжения введите текс и нажмите Enter (для выхода введите 'q'): ")

my_file.close()
