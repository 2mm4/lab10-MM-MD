#https://github.com/2mm4/lab10-MM-MD
#Partner 1: Melanie Morgado
#Partner 2: Matthew Doyle

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-10, 5), -5)
        self.assertEqual(add(-5, -5), -10)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(5, 10), -5)
        self.assertEqual(subtract(-5, -2), -3)
    ###########################

    ######## Partner 1
    def test_multiply(self):
        # 3 assertions: standard int mul, 0, negative
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(2, 0), 0)
        self.assertEqual(mul(2, -1), -2)

    def test_divide(self):
        # 3 assertions: standard int div, negative, almostequal.
        self.assertEqual(div(3, 6), 2)
        self.assertEqual(div(-3, 6), -2)
        self.assertAlmostEqual(div(2, 1), 0.5)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
    

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2, 8), 3)
        self.assertEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(4, 2), 0.5)

    def test_log_invalid_base(self): # 1 assertion
    
        with self.assertRaises(ValueError):
            logarithm(1, 10)
    ###########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):
        # 1 assertion. log>0
        with self.assertRaises(ValueError):
            log(0, 5)

    def test_hypotenuse(self):
        # 3 assertions: standard hypot, negative, almostequal
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(-3, 4), 5)
        self.assertAlmostEqual(hypotenuse(3, 3), math.sqrt(18))

    def test_sqrt(self):
        # 3 assertions: standard sqrt, not exact, invalid argument hint
        self.assertEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(2), math.sqrt(2))
        with self.assertRaises(ValueError):
            square_root(-1)


# Do not touch this
if __name__ == "__main__":
    unittest.main()
