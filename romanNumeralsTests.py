import unittest

from romanNumerals import romanToArabic


class TestStringMethods(unittest.TestCase):

    def test_romanToArabic(self):
        self.assertEqual("I", romanToArabic(1))


if __name__ == '__main__':
    unittest.main()
