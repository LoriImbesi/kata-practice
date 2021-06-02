import unittest
from enum import Enum
from unittest import suite


# Enum OR values together HEARTS or CLUBS or SPADES ...
# Dictionary/Class AND values together {firstName: "steve", lastName: "shogren", email: ""}

class Suit(Enum):
    HEARTS = 1
    CLUBS = 2
    SPADES = 3
    DIAMONDS = 4

 # face = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
    #           '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


def parseCard(cardString):
    faceLookup = {'6': 6, '7': 7}
    suitLookup = {'H': Suit.HEARTS, 'S': Suit.SPADES}

    # faceString = cardString[0]
    # suitString = cardString[1]
    return {"face": faceLookup[cardString[0]],
            "suit": suitLookup[cardString[1]]}


class TestStringMethods(unittest.TestCase):

    def test_parseCard_7S(self):
        actual = parseCard("7S")
        self.assertEqual(7, actual["face"])
        self.assertEqual(Suit.SPADES, actual["suit"])

    def test_parseCard_6H(self):
        actual = parseCard("6H")
        self.assertEqual(6, actual["face"])
        self.assertEqual(Suit.HEARTS, actual["suit"])


if __name__ == '__main__':
    unittest.main()
