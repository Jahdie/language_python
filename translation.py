from googletrans import Translator

translator = Translator()
new_line = ""
with open("text_4.txt", "r", encoding="utf-8") as f_obj, open("new_text_4.txt", "w", encoding="utf-8") as f_obj_1:
    for line in f_obj:
        trans_line = (translator.translate(line[0:line.index(" ")], src='en', dest='ru'))
        new_line = trans_line.text.title() + line[line.index(" "):]
        f_obj_1.write(new_line)
