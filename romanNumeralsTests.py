import unittest
from romanNumerals import arabicToRoman


class TestStringMethods(unittest.TestCase):

    def test_arabicToRoman(self):
        self.assertEqual("I", arabicToRoman(1))
        self.assertEqual("II", arabicToRoman(2))
        self.assertEqual("III", arabicToRoman(3))
        self.assertEqual("IIII", arabicToRoman(4))
        self.assertEqual("V", arabicToRoman(5))
        self.assertEqual("VI", arabicToRoman(6))
        self.assertEqual("VII", arabicToRoman(7))
        self.assertEqual("VIII", arabicToRoman(8))
        self.assertEqual("VIIII", arabicToRoman(9))
        self.assertEqual("X", arabicToRoman(10))
        self.assertEqual("XI", arabicToRoman(11))
        self.assertEqual("L", arabicToRoman(50))
        self.assertEqual("C", arabicToRoman(100))
        # self.assertEqual("D", arabicToRoman(500))
        # self.assertEqual("M", arabicToRoman(1000))


if __name__ == '__main__':
    unittest.main()
