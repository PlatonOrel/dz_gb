#Реализовать базовый класс Worker (работник).
#определить атрибуты: name, surname, position (должность), income (доход);
#последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus};
#создать класс Position (должность) на базе класса Worker;
#в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
# с учётом премии (get_total_income);
#проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров.
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):

    def __init__(self,  name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'ФИО: {self.surname} {self.name}'

    def get_total_income(self):
        return sum(self._income.values())

if __name__ == '__main__':
    test_user = Position('Иванов', 'Иван', 'ИТ специалист', 3500, 1000)
    test_user_two = Position('Ярослав', 'Петрушин', 'Сварщик 5 разряд', 35000, 10000)
    print(test_user.get_full_name())
    print(f'Total income: {test_user.get_total_income()}')
    print(test_user._income)
    print(test_user_two.get_full_name())
    print(f'Total income: {test_user_two.get_total_income()}')
    print(test_user_two.position)