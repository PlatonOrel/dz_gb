#5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

rate_list = [7, 5, 3, 3, 2]
print(f"Рейтинг {rate_list}")
rate_input = int(input("Введите число, сколько значений необходимо добавить в рейтинг: "))
for j in range(rate_input):
    add_new = int(input("Введите значение которое необходимо добавить в рейтинг: "))
    if add_new in rate_list:
        i = rate_list.index(add_new)
        while (i + 1) <= (len(rate_list) - 1) and (rate_list[i] == rate_list[i + 1]):
            i += 1
        rate_list.insert(i, add_new)
        print(f"Обновлённый рейтинг {rate_list}")
    else:
        if add_new <= rate_list[-1]:
            rate_list.append(add_new)
            print(f"Обновлённый рейтинг {rate_list}")
        else:
            rate_list.insert(0, add_new)
            print(f"Обновлённый рейтинг {rate_list}")