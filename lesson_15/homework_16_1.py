# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


"""Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та
периметру. Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через
конструктор.
Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної."""
import math
from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Figure):
    def __init__(self, side_a):
        self._side_a = side_a

    def area(self):
        return self._side_a **2

    def perimeter(self):
        return self._side_a * 4

class Circle(Figure):
    def __init__(self, radius):
        self._radius = radius

    def area(self):
        return math.pi *(self._radius **2)

    def perimeter(self):
        return 2* math.pi * self._radius


class Rectangle(Figure):
    def __init__(self, side_b, side_c):
        self._side_b = side_b
        self._side_c = side_c


    def area(self):
        return self._side_c * self._side_b

    def perimeter(self):
        return 2 * (self._side_b + self._side_c)


figure1 = Square(3)
figure2 = Rectangle(6, 5)
figure3 = Circle(3)

print(figure1.perimeter(), figure1.area())
print(figure2.perimeter(), figure2.area())
print(figure3.perimeter(), figure3.area())












