import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(100, -1), 99)
        self.assertEqual(calc.add(10, 10), 20)
    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(100, -1), 101)
        self.assertEqual(calc.subtract(10, 10), 0)
    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(100, -1), -100)
        self.assertEqual(calc.multiply(10, 10), 100)
        self.assertEqual(calc.multiply(10, 0), 0)

if __name__ == "__main__":
    unittest.main()