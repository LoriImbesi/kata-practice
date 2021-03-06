import unittest
from unittest import suite
from pokerKata2 import parseCard, Card, Suit, parseCards, faceCounts, suitCounts, parseHand, Hand


class TestStringMethods(unittest.TestCase):

    def test_parseHand(self):
        self.assertEqual(Hand.PAIR, parseHand(["3H", "5D", "4D", "3D", "8S"]))
        self.assertEqual(Hand.THREE_OF_A_KIND, parseHand(
            ["3H", "3S", "4D", "3D", "8S"]))
        self.assertEqual(Hand.FOUR_OF_A_KIND, parseHand(
            ["3H", "3S", "3C", "3D", "8S"]))
        self.assertEqual(Hand.FLUSH, parseHand(
            ["7S", "5S", "JS", "3S", "8S"]))
        self.assertEqual(Hand.TWO_PAIR, parseHand(
            ["7S", "3H", "7D", "3S", "8S"]))
        self.assertEqual(Hand.FULL_HOUSE, parseHand(
            ["7S", "7H", "7D", "8D", "8S"]))
        self.assertEqual(Hand.STRAIGHT, parseHand(
            ["3S", "2H", "5D", "4D", "6S"]))
        self.assertEqual(Hand.STRAIGHT_FLUSH, parseHand(
            ["9H", "6H", "7H", "8H", "5H"]))
        self.assertEqual(Hand.ROYAL_FLUSH, parseHand(
            ["AD", "KD", "TD", "JD", "QD"]))

    def test_faceCounts(self):
        cards = [Card(Suit.HEARTS, 3),
                 Card(Suit.SPADES, 3),
                 Card(Suit.DIAMONDS, 3),
                 Card(Suit.HEARTS, 8),
                 Card(Suit.HEARTS, 4)]
        actual = faceCounts(cards)
        expected = {3: 3, 4: 1, 8: 1}
        self.assertEqual(expected, actual)

    def test_suitCounts(self):
        cards = [Card(Suit.HEARTS, 3),
                 Card(Suit.SPADES, 3),
                 Card(Suit.DIAMONDS, 3),
                 Card(Suit.HEARTS, 8),
                 Card(Suit.HEARTS, 4)]
        actual = suitCounts(cards)
        expected = 3
        self.assertEqual(expected, actual)

    def test_split(self):
        input = "hi my name is"
        output = input.split()
        expected = ["hi", "my", "name", "is"]
        self.assertEqual(expected, output)

    def test_parseCards(self):
        cards = parseCards(["3H", "4D", "5D"])
        self.assertEqual(Suit.HEARTS, cards[0].suit)
        self.assertEqual(3, cards[0].face)
        self.assertEqual(Suit.DIAMONDS, cards[1].suit)
        self.assertEqual(4, cards[1].face)
        self.assertEqual(Suit.DIAMONDS, cards[2].suit)
        self.assertEqual(5, cards[2].face)

    def test_parseCard(self):
        card = parseCard("3H")
        self.assertEqual(Suit.HEARTS, card.suit)
        self.assertEqual(3, card.face)

        card = parseCard("5S")
        self.assertEqual(Suit.SPADES, card.suit)
        self.assertEqual(5, card.face)

        card = parseCard("TS")
        self.assertEqual(Suit.SPADES, card.suit)
        self.assertEqual(10, card.face)


if __name__ == '__main__':
    unittest.main()
