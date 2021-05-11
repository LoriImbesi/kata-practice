import unittest
from enum import Enum
class Suit(Enum):
     HEARTS = 1
     CLUBS = 2
     SPADES = 3
     DIAMONDS = 4

def makeSentence(string1, string2) :
    return string1+ " " +string2

def parseCard(cardString) :
    suitString = cardString[1]
    faceValue = int(cardString[0])
    suit = None
    if suitString == "H" :
        suit = Suit.HEARTS
    elif suitString == "D" :
        suit = Suit.DIAMONDS
    elif suitString == "C" :
        suit = Suit.CLUBS
    return (faceValue, suit)

class TestStringMethods(unittest.TestCase):

    def test_parseCard1(self):
        expect = (3, Suit.DIAMONDS)
        actual = parseCard("3D")
        self.assertEqual(expect, actual)

    def test_parseCard(self):
        expect = (2, Suit.HEARTS)
        actual = parseCard("2H")
        self.assertEqual(expect, actual)

    def test_parseCard2(self):
        expect = (9, Suit.CLUBS)
        actual = parseCard("9C")
        self.assertEqual(expect, actual)


    def test_makeSentence(self):
        expect = "hello world"
        actual = makeSentence("hello", "world")
        self.assertEqual(expect, actual)

if __name__ == '__main__':
    unittest.main()