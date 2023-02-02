#Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.

source_list = [element for element in range(100, 1001) if element % 2 == 0]
print(source_list)
from functools import reduce
def calc_func(el_p, element):
    return el_p * element
print(reduce(calc_func, source_list))

