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

    def test_moreThanTwoOperations(self):
        # "3 5 8 * 7 + *"
        # "3 40 7 + *"
        # "3 47 *"

        # E E O
        # (E ((E E O) E O) O)
        input = "3 5 8 * 7 + *"
        actual = rpnCalculate(input)
        self.assertEqual(actual, 141)


if __name__ == '__main__':
    unittest.main()
