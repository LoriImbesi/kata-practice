import unittest

from romanNumerals import *


class TestStringMethods(unittest.TestCase):

    def test_returnString0(self):
        self.assertEqual("ey", returnString("Hey"))

    def test_returnString1(self):
        self.assertEqual("hicken", returnString("chicken"))

    def test_addArrayOfNumbers(self):
        self.assertEqual(10, addArrayOfNumbers([5, 5]))   
     

    # def test_romanToArabic(self):
    #     self.assertEqual("I", romanToArabic(1))


if __name__ == '__main__':
    unittest.main()
