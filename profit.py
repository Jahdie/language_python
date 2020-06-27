from functools import reduce
import json

my_dict = {}


def solution(prev_el, el):
    return prev_el - el


with open("text_7.txt", "r", encoding="utf-8")as f_obj:
    for line in f_obj:
        my_dict.update({line[0: line.index(" ")]: reduce(solution, [int(el) for el in line.split() if el.isdigit()])})
# profit = sum([val for val in my_dict.values() if val > 0])
profit = [val for val in my_dict.values() if val > 0]
profit = sum(profit)/len(profit)
my_dict.update({"average_profit": profit})
my_list_json = [my_dict]
print(my_list_json)

with open("my_file.json", "w", encoding="utf-8") as write_f:
    json.dump(my_list_json, write_f, ensure_ascii=False)
