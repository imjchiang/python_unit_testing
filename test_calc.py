import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(100, -1), 99)
        self.assertEqual(calc.add(10, 10), 20)

if __name__ == "__main__":
    unittest.main()