import unittest
from utils.operators import add, subtract, multiply, divide

class TestOperators(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 20), 30)
        self.assertEqual(add(-2, 2), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 0), 5)
        self.assertEqual(subtract(2, 5), -3)
        self.assertEqual(subtract(-3, -1), 2)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
