import unittest
from unittest import suite
from rpnCalculator import rpnCalculate


class TestStringMethods(unittest.TestCase):

    # "20 5 /" => 4
    # "20 5 *" => 120
    # "20 5 +" => 25
    # "20 5 -" => 15
    def test_simpleDivisionExpression(self):
        input = "20 5 /"
        actual = rpnCalculate(input)
        self.assertEqual(actual, 4)

    def test_simpleMultExpression(self):
        input = "20 5 *"
        actual = rpnCalculate(input)
        self.assertEqual(actual, 100)

    def test_simpleAddExpression(self):
        input = "20 5 +"
        actual = rpnCalculate(input)
        self.assertEqual(actual, 25)

    def test_simpleSubtrExpression(self):
        input = "20 5 -"
        actual = rpnCalculate(input)
        self.assertEqual(actual, 15)

    def test_additionSubtraction(self):
        input = "4 2 + 3 -"
        actual = rpnCalculate(input)
        self.assertEqual(actual, 3)


if __name__ == '__main__':
    unittest.main()
