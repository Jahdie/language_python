from itertools import count, cycle
from sys import argv

try:
    for el in count(int(argv[1])):
        if int(argv[2]) < 0:
            print("Второй параметр не может быть отрицательным числом!!!")
            break
        if el > int(argv[2]):
            break
        else:
            print(el)
except ValueError:
    print("Параметры не являются числом!!!")
# *********************************************************************************************************************
print(f"\n{'*'*30} Второй скрипт!!! {'*'*30}")
i = 0
my_list = [1, 2, 3]
try:
    for el in cycle(my_list):
        if int(argv[1]) < 0:
            print("Параметр не может быть отрицательным числом!!!")
            break
        if i >= int(argv[1]):
            break
        print(el)
        i += 1
except ValueError:
    print("Параметр не являются числом!!!")