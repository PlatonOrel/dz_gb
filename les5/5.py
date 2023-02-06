#5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
def summary():
    try:
        with open('dz5.txt', 'w+') as file_obj:
            user_numbers = input('Введите числа через пробел \n')
            file_obj.writelines(user_numbers)
            my_numb = user_numbers.split()

            print(sum(map( int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summary()