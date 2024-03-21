import unittest
import math
from Q2 import ShapeCalculator


class TestShapeCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = ShapeCalculator()

    def test_is_triangle(self):
        self.assertTrue(self.calculator.is_triangle(3, 4, 5))
        self.assertFalse(self.calculator.is_triangle(3, 4, 11))

    def test_circle_area(self):
        self.assertEqual(self.calculator.circle_area(5), 25 * math.pi)
        self.assertEqual(self.calculator.circle_area(6), 36 * math.pi)

    def test_triangle_area(self):
        self.assertEqual(self.calculator.triangle_area(3, 4, 5), 6)
        self.assertEqual(self.calculator.triangle_area(1, 2, 12), 'Треугольник с такими сторонами не может существовать')

    def test_is_right_triangle(self):
        self.assertTrue(self.calculator.is_right_triangle(3, 4, 5))
        self.assertTrue(self.calculator.is_right_triangle(6, 6, 6))


if __name__ == '__main__':
    unittest.main()
