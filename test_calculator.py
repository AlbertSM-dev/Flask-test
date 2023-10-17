#!/usr/bin/env python3
'''
Import unittest framework and the Calculator class
we defined.
'''
import unittest
from calculator import Calculator


'''
Test cases are created by subclassing unittest.TestCase
'''
class TestCalculator(unittest.TestCase):
    '''
    setUp function is used to instantiate the object we are testing.
    '''
    def setUp(self):
        self.calculator = Calculator()

    '''
    Test the add function.
    '''
    def test_add(self):
        add_result = self.calculator.add(1, 2)
        self.assertEqual(add_result, 3)

    '''
    Test the subtract function.
    '''
    def test_subtract(self):
        subtract_result = self.calculator.subtract(1, 1)
        self.assertEqual(subtract_result, 0)


if __name__ == '__main__':
    unittest.main()