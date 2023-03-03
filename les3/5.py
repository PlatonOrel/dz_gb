#5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.

def my_sum(my_list):
    items_sum = 0
    for item in my_list:
        try:
            items_sum += float(item)
        except ValueError:
            continue
    return items_sum


def sum_my_string(s):
    s = s.replace('@', '')
    s = s.replace(',', '.')
    numbers = s.split(' ')
    return my_sum(numbers)


numbers_sum = 0

while True:
    numbers_sting = input("Введите строку чисел, разделенных пробелом. Спецсимвол для завершения '@'\n")
    numbers_sum += sum_my_string(numbers_sting)
    if numbers_sum != 0:
        print(f"Сумма значений элементов {numbers_sum}")
    if numbers_sting.count('@') > 0:
        break