#Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
data_file = open("employee_list.txt", "r", encoding="utf8")
employee_count = 0
employee_sum = 0


for line in data_file.readlines():
    employee_count +=1
    employee_sum += float(line.split()[1])
    if float(line.split()[1]) < 20000:
        print(line.split()[0])

print(f"Средний доход: {employee_sum/employee_count}")

data_file.close()
