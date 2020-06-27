my_list = [el for (el) in range(1, 11)]
for i in range(len(my_list)):
    my_list[i] = str(my_list[i])
with open("text_5.txt", "w+", encoding="utf-8") as f_obj:
    f_obj.write(" ".join(my_list))
with open("text_5.txt", "r", encoding="utf-8") as f_obj:
    new_my_list = f_obj.read().split()
for i in range(len(new_my_list)):
    new_my_list[i] = int(new_my_list[i])
print(sum(new_my_list))
