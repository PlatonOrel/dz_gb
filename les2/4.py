#4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

text_input = input("Вводите строку из нескольких слов: ")
concatenation_text = text_input.split()
for num_str, one_word in enumerate (concatenation_text, start=1) :
    if len(one_word) > 11 :
        y = y[:10]
        print(num_str, one_word)
    else :
        print (num_str,one_word)