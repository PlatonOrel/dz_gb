#7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме:
# название, форма собственности, выручка, издержки.
import json


def get_statistics():
    try:
        with open('firm.txt', 'r+', encoding='utf-8') as file:
            statistics_list = []
            profit_dict = {}
            average_profit = {}
            prof = 0
            i = 3
            for line in file:
                name, firm, earning, damage = line.split()
                total = int(earning) - int(damage)
                if total >= 0:
                    prof = prof + total
                else:
                    i -= 1
                profit_dict[name] = total
            statistics_list.append(profit_dict)
            if i != 0:
                (av) = prof / i
                average_profit['average_profit'] = round(av)
                statistics_list.append(average_profit)
            else:
                print('Все компании работают в убыток')
            print(statistics_list)
        with open('file.json', 'a+', encoding='utf-8') as json_file:
            json.dump(statistics_list, json_file)
    except FileNotFoundError:
        return 'Файл не найден.'


get_statistics()
