with open("text_1.txt", "r", encoding="utf-8") as f_obj:
    my_list = f_obj.readlines()
for i in range(len(my_list)):
    num_words = len(my_list[i].split())
    print(f"В {i + 1}-й строке - {num_words} слов. ")
