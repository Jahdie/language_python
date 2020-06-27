my_string = " "
with open("text_1.txt", "w", encoding="utf-8") as f_obj:
    while my_string != "":
        my_string = input("Введите текст: ")
        f_obj.write(f"{my_string}\n")
