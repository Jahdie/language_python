from sys import argv
wage = argv[1:]
try:
    print(f"Размер заработной платы составляет: {(float(wage[0])*int(wage[1]))+int(wage[2])} руб.")
except ValueError:
    print("Параметры не являются числами!!!")