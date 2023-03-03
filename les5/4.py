translate_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

input_file = open("original_text.txt", encoding="utf8")
out_file = open("translate_text", "a", encoding="utf8")

for line in input_file.readlines():
    for element in translate_dict:
        if element == line.split()[0]:
            line = line.replace(line.split()[0], translate_dict.get(element))
            out_file.write(f"{line}")
            print(line)

input_file.close()
out_file.close()