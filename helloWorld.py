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
    FOUR_OF_A_KIND = 5

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
    cardsStrings = cards.split()  # makes list of strings
    cardDictionaries = []  # assign an empty list to cardDictionaries
    for cardString in cardsStrings:
        card = parseCard(cardString)
        cardDictionaries.append(card)
    return (cardDictionaries)


# outsideState - In this practice, is outsideState the hand you're given from the unittest?
# for loop
#    store in outsideState
# use outsideState

def countFaces(cards):
    faceCounts = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0,
                  9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}
    for card in cards:
        face = card["face"]
        faceCounts[face] += 1

    return faceCounts


def isFlush(cards):
    suitCounts = {Suit.HEARTS: 0, Suit.CLUBS: 0,
                  Suit.SPADES: 0, Suit.DIAMONDS: 0}

    for card in cards:
        suit = card["suit"]
        suitCounts[suit] += 1

    for suit, count in suitCounts.items():
        if (count == 5):
            return True
    return False


def isThreeOfAKind(cards):
    faceCounts = countFaces(cards)

    for face, count in faceCounts.items():
        if (count == 3):
            return True
    return False


def isFourOfAKind(cards):
    faceCounts = countFaces(cards)

    for face, count in faceCounts.items():
        if (count == 4):
            return True
    return False


def detectPair(cards):
    faceCounts = countFaces(cards)

    countOfPairs = 0
    for face, count in faceCounts.items():
        if (count == 2):
            countOfPairs += 1

    if (countOfPairs == 2):
        return Hand.TWO_PAIR
    elif (countOfPairs == 1):
        return Hand.PAIR
    return None


def detectHand(cards):
    # Question - why is "cards" being passed in the ifs? Is it b/c it's the complete function?
    possiblePair = detectPair(cards)
    if (possiblePair):
        return possiblePair

    if (isFlush(cards)):
        return Hand.FLUSH

    if (isThreeOfAKind(cards)):
        return Hand.THREE_OF_A_KIND

    if (isFourOfAKind(cards)):
        return Hand.FOUR_OF_A_KIND


class TestStringMethods(unittest.TestCase):
    def test_detectHand_flush(self):
        cards = parseCards("3D 2D QD AD 4D")
        hand = detectHand(cards)
        self.assertEqual(Hand.FLUSH, hand)

    def test_detectHand_fourOfAKind(self):
        cards = parseCards("3D 3S 3H 3C 4H")
        hand = detectHand(cards)
        self.assertEqual(Hand.FOUR_OF_A_KIND, hand)

    def test_detectHand_threeOfAKind(self):
        cards = parseCards("3D 3S 3H AC 4H")
        hand = detectHand(cards)
        self.assertEqual(Hand.THREE_OF_A_KIND, hand)

    def test_detectHand_pair(self):
        cards = parseCards("3D 3S QH AC 4H")
        hand = detectHand(cards)
        self.assertEqual(Hand.PAIR, hand)

    def test_detectHand_twopair(self):
        cards = parseCards("3D 3S QH 4C 4H")
        hand = detectHand(cards)
        self.assertEqual(Hand.TWO_PAIR, hand)

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
        card = parseCard('TH')
        self.assertEqual(10, card["face"])
        self.assertEqual(Suit.HEARTS, card["suit"])

    def test_parseCard_KS(self):
        card = parseCard("KS")
        self.assertEqual(13, card["face"])
        self.assertEqual(Suit.SPADES, card["suit"])

    def test_parseCards(self):
        cards = parseCards("3S QH AC 4H")
        self.assertEqual(Suit.SPADES, cards[0]["suit"])
        self.assertEqual(3, cards[0]["face"])

        self.assertEqual(Suit.HEARTS, cards[1]["suit"])
        self.assertEqual(12, cards[1]["face"])

        self.assertEqual(Suit.CLUBS, cards[2]["suit"])
        self.assertEqual(14, cards[2]["face"])

        self.assertEqual(Suit.HEARTS, cards[3]["suit"])
        self.assertEqual(4, cards[3]["face"])


if __name__ == '__main__':
    unittest.main()
