#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input('Введите число: ')
nn = int(n+n)
nnn = int(n+n+n)
n = int(n)
sum_numbers = n+nn+nnn
print(sum_numbers)