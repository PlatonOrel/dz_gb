#2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def div():
    try:
        input_dividend = int(input('Введите делимое: '))
        input_divisor = int(input('Введите делитель: '))
        if input_divisor == 0:
            raise OwnError("Делить на ноль нельзя!")
        else:
            res = input_dividend / input_divisor
            return res
    except ValueError:
        return "Вы ввели не число"
    except OwnError as err:
        return err


print(div())