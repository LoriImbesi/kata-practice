import unittest
from pokerKata import Suit, parseCard, parseCards


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


if __name__ == '__main__':
    unittest.main()


# Black: 2H 3D 5S 9C KD  White: 2C 3H 4S 8C AH
# Black: 2H 4S 4C 2D 4H  White: 2S 8S AS QS 3S
# Black: 2H 3D 5S 9C KD  White: 2C 3H 4S 8C KH
# Black: 2H 3D 5S 9C KD  White: 2D 3H 5C 9S KH

# Need to decide what goes in and what will come out of the function
# String -> Tuple
