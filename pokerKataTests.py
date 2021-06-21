import unittest
from unittest import suite
from pokerKata import Suit, parseCard, parseCards, Hand, parseHand


class TestStringMethods(unittest.TestCase):

    def test_parseHand(self):
        hand = parseHand(["3H", "5D", "4D", "3D", "8S"])
        self.assertEqual(Hand.PAIR, hand)
        self.assertEqual(Hand.THREE_OF_A_KIND, hand)

    def test_parseCards(self):
        cards = parseCards(["3H", "4D", "5D"])
        self.assertEqual(Suit.HEARTS, cards[0].suit)
        self.assertEqual(3, cards[0].face)
        self.assertEqual(Suit.DIAMONDS, cards[2].suit)
        self.assertEqual(5, cards[2].face)

    def test_parseCard(self):
        card = parseCard("3H")
        self.assertEqual(Suit.HEARTS, card.suit)
        self.assertEqual(3, card.face)

        card = parseCard("5S")
        self.assertEqual(Suit.SPADES, card.suit)
        self.assertEqual(5, card.face)


if __name__ == '__main__':
    unittest.main()
