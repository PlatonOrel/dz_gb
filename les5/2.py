#2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.
def count_info():
    try:
        with open('file_2.txt', 'r', encoding="utf-8") as file:
            text_list = file.readlines()
            for i in range(len(text_list)):
                new_line = text_list[i].split()
                print(f'Количество строк в файле {len(text_list)}. В {i + 1}-ой строке {len(new_line)} слов(а)')
    except FileNotFoundError:
        return 'Файл не найден.'


count_info()