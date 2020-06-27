new_my_list, sur_names, my_list = [], [], []

with open("text_3.txt", "r", encoding="utf-8") as f_obj:
    for line in f_obj.readlines():
        my_list = (line.split("\n").pop(0).split())
        my_list[1] = float(my_list[1])
        new_my_list.append(my_list)
result = 0
for el in new_my_list:
    if el[1] < 20000:
        sur_names.append(el[0])
    result = el[1] + result
print(sur_names)

print(f"Фамилии работников имееющих меньше 20000 тыс.: {','.join(sur_names)}"
      f"\nСредний доход на работника: {result / len(my_list)} руб.")
