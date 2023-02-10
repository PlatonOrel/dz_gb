#1. Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.
write_file = open('text_write.txt', 'w')
line = input('Введите текст \n')
while line:
    write_file.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

write_file.close()
write_file = open('text_write.txt', 'r')
content = write_file.readlines()
print(content)
write_file.close()