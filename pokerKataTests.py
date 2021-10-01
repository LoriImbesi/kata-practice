import unittest
from pokerKata import Suit, parseCard


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


if __name__ == '__main__':
    unittest.main()


# Black: 2H 3D 5S 9C KD  White: 2C 3H 4S 8C AH
# Black: 2H 4S 4C 2D 4H  White: 2S 8S AS QS 3S
# Black: 2H 3D 5S 9C KD  White: 2C 3H 4S 8C KH
# Black: 2H 3D 5S 9C KD  White: 2D 3H 5C 9S KH

# Need to decide what goes in and what will come out of the function
# String -> Tuple
