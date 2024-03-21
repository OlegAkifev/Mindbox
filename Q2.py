# Напишите на Python библиотеку для поставки внешним клиентам,
# которая умеет вычислять площадь круга по радиусу и треугольника по трем сторонам.
# Дополнительно к работоспособности оценим:
#
# Юнит-тесты
# Легкость добавления других фигур
# Вычисление площади фигуры без знания типа фигуры в compile-time
# Проверку на то, является ли треугольник прямоугольным

import math


class ShapeCalculator:
    # Проверка на существование треугольника
    @classmethod
    def is_triangle(cls, side1, side2, side3):
        if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
            return True
        else:
            return False

    @staticmethod
    def circle_area(radius):
        return math.pi * radius ** 2

    @staticmethod
    def triangle_area(side1, side2, side3):
        if ShapeCalculator.is_triangle(side1, side2, side3):
            # Полупериметр треугольника
            s = (side1 + side2 + side3) / 2
            # Вычисление площади треугольника по формуле Герона
            area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
            return area
        return f'Треугольник с такими сторонами не может существовать'

    @staticmethod
    def is_right_triangle(side1, side2, side3):
        if ShapeCalculator.is_triangle(side1, side2, side3):
            sides = [side1, side2, side3]
            sides.sort()
            if sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2:
                return f'Данный треугольник ЯВЛЯЕТСЯ прямоугольным'
            else:
                return f'Данный треугольник НЕ ЯВЛЯЕТСЯ прямоугольным'
        return f'Треугольник с такими сторонами не может существовать'

    @staticmethod
    def calculate_area(*args):
        # Площадь круга
        if len(args) == 1:
            radius = args[0]
            return math.pi * radius ** 2

        # Площадь треугольника по формуле Герона
        elif len(args) == 3:
            return ShapeCalculator.triangle_area(*args)
        else:
            return len(args)


print(ShapeCalculator.circle_area(5))
print(ShapeCalculator.triangle_area(3, 4, 5))
print(ShapeCalculator.is_right_triangle(3, 4, 5))
print(ShapeCalculator.calculate_area(3, 4, 5))

