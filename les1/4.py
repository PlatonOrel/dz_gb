#4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

n = int(input('Введите положительное число: '))

max_numbers = n % 10
while True:
    n = n // 10
    if n % 10 > max_numbers:
        max_numbers = n % 10
    elif n > 9:
        continue
    else:
        print(f'Максимальное число: {max_numbers}')
        break