import unittest
from romanNumerals import arabicToRoman


class TestStringMethods(unittest.TestCase):

    def test_arabicToRoman(self):
        self.assertEqual("I", arabicToRoman(1))
        self.assertEqual("V", arabicToRoman(5))
        self.assertEqual("X", arabicToRoman(10))
        self.assertEqual("L", arabicToRoman(50))
        self.assertEqual("C", arabicToRoman(100))
        self.assertEqual("D", arabicToRoman(500))
        self.assertEqual("M", arabicToRoman(1000))
        self.assertEqual("VII", arabicToRoman(7))


if __name__ == '__main__':
    unittest.main()
