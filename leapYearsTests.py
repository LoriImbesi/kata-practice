from unittest import result
from leapYears import isItALeapYear
import unittest
from unittest import suite


class TestStringMethods(unittest.TestCase):

    # def test_stringSplit2(self):
    #     self.assertEqual("hello moto".split(), ['hello', 'moto'])

    # def test_stringSplit(self):
    #     # arrange
    #     input = "hello moto"

    #     # act

    #     actual = input.split()

    #     # assert

    #     expected = ['hello', 'moto']
    #     self.assertEqual(actual, expected)

    def test_isItALeapYear_yes(self):
        self.assertTrue(isItALeapYear("2000"))
        self.assertTrue(isItALeapYear("2008"))

    def test_isItALeapYear_no(self):
        self.assertFalse(isItALeapYear("2100"))
        self.assertFalse(isItALeapYear("2019"))


if __name__ == '__main__':
    unittest.main()
