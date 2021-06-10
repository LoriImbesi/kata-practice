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


class Hand(Enum):
    PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    FLUSH = 4

# parseCard : string -> dict


def parseCard(cardString):
    faceLookup = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                  '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    suitLookup = {'H': Suit.HEARTS, 'S': Suit.SPADES,
                  'D': Suit.DIAMONDS, 'C': Suit.CLUBS}

    return {"face": faceLookup[cardString[0]],
            "suit": suitLookup[cardString[1]]}

# split : string -> string[]

# parseCards : string -> dict[]


def parseCards(cards):
    # splits a string into a list; default separator is any whitespace
    cardsStrings = cards.split()
    # need a list of dicts b/c key value pairs - face: face value & suit: suit name
    cardDictionaries = []
    for cardString in cardsStrings:
        card = parseCard(cardString)
        cardDictionaries.append(card)
        print(card)
    return (cardDictionaries)


# outsideState
# for loop
#    store in outsideState
# use outsideState

def detectHand(cards):
    faceCounts = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0,
                  9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}
    for card in cards:
        faceCounts[card["face"]] += 1

    for faceCount, count in faceCounts.items():
        if count == 2:
            print("You have a pair.")
            return (Hand.PAIR)

    suitCounts = {Suit.HEARTS: 0, Suit.CLUBS: 0,
                  Suit.SPADES: 0, Suit.DIAMONDS: 0}

    for card in cards:
        suitCounts[card["suit"]] += 1

    for suitCount, count in suitCounts.items():
        if count == 5:
            return (Hand.FLUSH)
    return None


class TestStringMethods(unittest.TestCase):
    def test_detectHand_flush(self):
        cards = parseCards("3D 2D QD AD 4D")
        hand = detectHand(cards)
        self.assertEqual(Hand.FLUSH, hand)

    def test_detectHand_pair(self):
        cards = parseCards("3D 3S QH AC 4H")
        hand = detectHand(cards)
        self.assertEqual(Hand.PAIR, hand)

    def test_parseCard_7D(self):
        card = parseCard("7D")
        self.assertEqual(Suit.DIAMONDS, card["suit"])

    def test_parseCard_7C(self):
        card = parseCard("7C")
        self.assertEqual(Suit.CLUBS, card["suit"])

    def test_parseCard_7S(self):
        card = parseCard("7S")
        self.assertEqual(7, card["face"])
        self.assertEqual(Suit.SPADES, card["suit"])

    def test_parseCard_6H(self):
        card = parseCard("6H")
        self.assertEqual(6, card["face"])
        self.assertEqual(Suit.HEARTS, card["suit"])

    def test_parseCard_TH(self):
        card = parseCard("TH")
        self.assertEqual(10, card["face"])
        self.assertEqual(Suit.HEARTS, card["suit"])

    def test_parseCard_KS(self):
        card = parseCard("KS")
        self.assertEqual(13, card["face"])
        self.assertEqual(Suit.SPADES, card["suit"])

    def test_parseCards(self):
        cards = parseCards("3S QH AC 4H")
        self.assertEqual(3, cards[0]["face"])
        self.assertEqual(Suit.SPADES, cards[0]["suit"])

        self.assertEqual(12, cards[1]["face"])
        self.assertEqual(Suit.HEARTS, cards[1]["suit"])

        self.assertEqual(14, cards[2]["face"])
        self.assertEqual(Suit.CLUBS, cards[2]["suit"])

        self.assertEqual(4, cards[3]["face"])
        self.assertEqual(Suit.HEARTS, cards[3]["suit"])


if __name__ == '__main__':
    unittest.main()
