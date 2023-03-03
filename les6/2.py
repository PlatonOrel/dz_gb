#2. Реализовать класс Road (дорога).
#определить атрибуты: length (длина), width (ширина);
#значения атрибутов должны передаваться при создании экземпляра класса;
#атрибуты сделать защищёнными;
#определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
#использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
#проверить работу метода.

class Road:
    WEIGHT1M2 = 25

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self, depth):
        return depth * self.WEIGHT1M2 * self._width * self._length

if __name__ == '__main__':
    road_calculation = Road(5000, 20)
    print(road_calculation.weight(5))
    print(road_calculation._length)
    print(road_calculation._width)