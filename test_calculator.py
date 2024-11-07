import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_substract(self):
        self.assertEqual(self.calc.subtract(2,1), 1)
        self.assertEqual(self.calc.subtract(4,5), -1)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4,4), 16)
        self.assertEqual(self.calc.multiply(8,9), 72)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(3,3), 1)
        self.assertEqual(self.calc.divide(12,2), 6)
        self.assertEqual(self.calc.divide(6,2), 3)
        self.assertEqual(self.calc.divide(4,-2), -2)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(3,2), 1)
        self.assertEqual(self.calc.modulo(4,4), 0)
        self.assertEqual(self.calc.modulo(20,4), 0)
        

if __name__ == '__main__':
    unittest.main()