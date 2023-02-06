#Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет
# и наличие лекционных, практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы
# занятий.
#Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести его на экран.

import re

data_file = open("file_predmet.txt", "r", encoding="utf8")

predmety = {}

for line in data_file.readlines():
    predmet = line.split()[0]
    zaniatija = 0

    for x in re.findall('\d+', line):
        zaniatija += int(x)
    predmety.update({predmet: zaniatija})

print(predmety)

data_file.close()