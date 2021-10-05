import unittest
from pokerKata import Suit, parseCard, parseCards, numberOfPairs, isThreeOfAKind, isAStraight, isAFlush


class TestStringMethods(unittest.TestCase):

    # "2H" -> (2, Suit.HEARTS)
    # def test_parseCard(self):
    #     card = "2H"
    #     (face, suit) = parseCard(card)
    #     self.assertEqual(face, 2)
    #     self.assertEqual(suit, Suit.HEARTS)

    def test_parseCard1(self):
        card = "2H"
        parsedCard = parseCard(card)
        self.assertEqual(parsedCard, (2, Suit.HEARTS))

    def test_parseCard2(self):
        card = "KD"
        parsedCard = parseCard(card)
        self.assertEqual(parsedCard, (13, Suit.DIAMONDS))

    # ("3D", "5S") -> List of tuples [(3, Suit.DIAMONDS),(5, Suit.SPADES)]
    def test_parseCards(self):
        cards = ("2H", "3D", "5S", "9C", "KD")
        parsedCards = parseCards(cards)
        self.assertEqual(parsedCards[0], (2, Suit.HEARTS))
        self.assertEqual(parsedCards[1], (3, Suit.DIAMONDS))
        self.assertEqual(parsedCards[2], (5, Suit.SPADES))
        self.assertEqual(parsedCards[3], (9, Suit.CLUBS))
        self.assertEqual(parsedCards[4], (13, Suit.DIAMONDS))

    # List of tuples -> Integer
    def test_onePair(self):
        parsedCards = [(4, Suit.HEARTS), (3, Suit.DIAMONDS),
                       (3, Suit.SPADES), (9, Suit.CLUBS),
                       (13, Suit.DIAMONDS)]
        detectPair = numberOfPairs(parsedCards)
        self.assertEqual(detectPair, 1)

    def test_twoPair(self):
        parsedCards = [(9, Suit.HEARTS), (3, Suit.DIAMONDS),
                       (3, Suit.SPADES), (9, Suit.CLUBS),
                       (13, Suit.DIAMONDS)]
        detectPair = numberOfPairs(parsedCards)
        self.assertEqual(detectPair, 2)

    def test_noPair(self):
        parsedCards = [(2, Suit.HEARTS), (3, Suit.DIAMONDS),
                       (5, Suit.SPADES), (9, Suit.CLUBS),
                       (13, Suit.DIAMONDS)]
        detectPair = numberOfPairs(parsedCards)
        self.assertEqual(detectPair, 0)

    def test_fourKind(self):
        parsedCards = [(2, Suit.HEARTS), (2, Suit.DIAMONDS),
                       (2, Suit.SPADES), (2, Suit.CLUBS),
                       (13, Suit.DIAMONDS)]
        detectPair = numberOfPairs(parsedCards)
        self.assertEqual(detectPair, 0)

# List of tuples -> Bool
    def test_threeKind(self):
        parsedCards = [(4, Suit.HEARTS), (4, Suit.DIAMONDS),
                       (4, Suit.SPADES), (2, Suit.CLUBS),
                       (13, Suit.DIAMONDS)]
        threeKind = isThreeOfAKind(parsedCards)
        self.assertEqual(threeKind, True)

    def test_isStraight(self):
        parsedCards = [(4, Suit.HEARTS), (5, Suit.DIAMONDS),
                       (6, Suit.SPADES), (7, Suit.CLUBS),
                       (8, Suit.DIAMONDS)]
        isStraight = isAStraight(parsedCards)
        self.assertEqual(isStraight, True)

    def test_isFlush(self):
        parsedCards = [(4, Suit.DIAMONDS), (5, Suit.DIAMONDS),
                       (6, Suit.DIAMONDS), (7, Suit.DIAMONDS),
                       (10, Suit.DIAMONDS)]
        isFlush = isAFlush(parsedCards)
        self.assertEqual(isFlush, True)


if __name__ == '__main__':
    unittest.main()


# Black: 2H 3D 5S 9C KD  White: 2C 3H 4S 8C AH
# Black: 2H 4S 4C 2D 4H  White: 2S 8S AS QS 3S
# Black: 2H 3D 5S 9C KD  White: 2C 3H 4S 8C KH
# Black: 2H 3D 5S 9C KD  White: 2D 3H 5C 9S KH

# Need to decide what goes in and what will come out of the function
# String -> Tuple
