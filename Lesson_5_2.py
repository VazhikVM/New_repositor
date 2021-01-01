with open("task_2.txt", "r", encoding="utf-8") as my_file:
    string = 0
    words = []
    for i in my_file:
        words = len(i.split())
        string += 1
        print(f'This strings number {string} contain {words} words.')
