import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(10, 5, 2), 17)
        self.assertEqual(self.calc.add(-10, 5, 2), -2)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5, 2), 3)
        self.assertEqual(self.calc.subtract(-10, 5, 2), -17)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(10, 5, 2), 100)
        self.assertEqual(self.calc.multiply(-10, 5, 2), 100)

    def test_divide(self):
        self.assertAlmostEqual(self.calc.divide(10, 5, 2), 1)
        self.assertAlmostEqual(self.calc.divide(100, 10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0, 2)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 5), 0)
        self.assertEqual(self.calc.modulo(10, 3), 1)

if __name__ == '__main__':
    unittest.main()
