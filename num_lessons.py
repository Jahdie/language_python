my_dict = {}
with open("text_6.txt", "r", encoding="utf-8") as f_obj:
    for line in f_obj:
        new_line = [el for el in line.split() if len(el) > 1]
        new_line = " ".join(new_line)
        try:
            while True:
                new_line = new_line[0:new_line.index("(")] + new_line[new_line.index(")") + 1:]
        except ValueError:
            my_dict.update({new_line[0:new_line.index(":")]: sum([int(el) for el in new_line.split() if el.isdigit()])})

print(my_dict)
