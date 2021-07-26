import unittest
from romanNumerals import arabicToRoman, romanToArabic


class TestStringMethods(unittest.TestCase):
    def test_romanToArabic(self):
        self.assertEqual(1, romanToArabic("I"))
        self.assertEqual(2, romanToArabic("II"))
        self.assertEqual(3, romanToArabic("III"))
        self.assertEqual(4, romanToArabic("IIII"))
        self.assertEqual(5, romanToArabic("V"))
        self.assertEqual(10, romanToArabic("X"))
        self.assertEqual(20, romanToArabic("XX"))

    def test_arabicToRoman(self):
        # 1   - 4   - 5   - 9   - 10
        # 10  - 40  - 50  - 90  - 100
        # 100 - 400 - 500 - 900 - 1000
        self.assertEqual("I", arabicToRoman(1))
        self.assertEqual("II", arabicToRoman(2))
        self.assertEqual("III", arabicToRoman(3))
        self.assertEqual("IV", arabicToRoman(4))
        self.assertEqual("V", arabicToRoman(5))
        self.assertEqual("VI", arabicToRoman(6))
        self.assertEqual("VII", arabicToRoman(7))
        self.assertEqual("VIII", arabicToRoman(8))
        self.assertEqual("IX", arabicToRoman(9))
        self.assertEqual("X", arabicToRoman(10))
        self.assertEqual("XI", arabicToRoman(11))
        self.assertEqual("XIV", arabicToRoman(14))
        self.assertEqual("XIX", arabicToRoman(19))
        self.assertEqual("L", arabicToRoman(50))
        self.assertEqual("C", arabicToRoman(100))
        self.assertEqual("D", arabicToRoman(500))
        self.assertEqual("M", arabicToRoman(1000))


if __name__ == '__main__':
    unittest.main()
