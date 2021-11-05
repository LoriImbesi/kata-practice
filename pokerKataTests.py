import unittest
from pokerKata import Suit, Hand, countOfFaces, handOfAKind, parseCard, parseCards, numberOfPairs, handOfAKind, isAStraight, isAFlush, parseHand, rankOfHand, splitPlayerHandInput, specifyWinningHand, tieBreaker, detectHighCard


class TestPokerKata(unittest.TestCase):

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

    def test_parseCard3(self):
        card = "10D"
        parsedCard = parseCard(card)
        self.assertEqual(parsedCard, (10, Suit.DIAMONDS))

    def test_countOfFaces(self):
        cards = ("2H", "3D")
        parsedCards = parseCards(cards)
        countedFaces = countOfFaces(parsedCards)
        self.assertEqual(countedFaces, {2: 1, 3: 1})

    def test_countOfFaces2(self):
        cards = ("10H", "10D", "5D")
        parsedCards = parseCards(cards)
        countedFaces = countOfFaces(parsedCards)
        self.assertEqual(countedFaces, {5: 1, 10: 2})

    # ("3D", "5S") -> List of tuples [(3, Suit.DIAMONDS),(5, Suit.SPADES)]

    def test_parseCards(self):
        cards = ("2H", "3D", "5S", "9C", "KD")
        parsedCards = parseCards(cards)
        self.assertEqual(parsedCards[0], (2, Suit.HEARTS))
        self.assertEqual(parsedCards[1], (3, Suit.DIAMONDS))
        self.assertEqual(parsedCards[2], (5, Suit.SPADES))
        self.assertEqual(parsedCards[3], (9, Suit.CLUBS))
        self.assertEqual(parsedCards[4], (13, Suit.DIAMONDS))

    # hand strings -> Dict with Hand enum & face value

    def test_parseHand_isPair(self):
        cardStrings = ("3H", "3D", "5S", "9C", "KD")
        parsedHand = parseHand(cardStrings)
        self.assertEqual(parsedHand, {"hand": Hand.PAIR, "face": 3})

    def test_parseHand_isTwoPair(self):
        cardStrings = ("3H", "3D", "9S", "9C", "KD")
        parsedHand = parseHand(cardStrings)
        self.assertEqual(parsedHand, {"hand": Hand.TWO_PAIR, "face": None})

    def test_parseHand_isHighCard(self):
        cardStrings = ("2H", "3D", "9S", "8C", "QD")
        parsedHand = parseHand(cardStrings)
        self.assertEqual(parsedHand, {"hand": Hand.HIGH_CARD, "face": None})

    def test_parseHand_isThreeOfAKind(self):
        cardStrings = ("3H", "3D", "3S", "8C", "QD")
        parsedHand = parseHand(cardStrings)
        self.assertEqual(
            parsedHand, {"hand": Hand.THREE_OF_A_KIND, "face": 3})

    def test_parseHand_isFourOfAKind(self):
        cardStrings = ("4H", "4D", "3S", "4C", "4S")
        parsedHand = parseHand(cardStrings)
        self.assertEqual(
            parsedHand, {"hand": Hand.FOUR_OF_A_KIND, "face": 4})

    def test_parseHand_isAStraight(self):
        cardStrings = ("3H", "4D", "5S", "6C", "7D")
        parsedHand = parseHand(cardStrings)
        self.assertEqual(parsedHand, {"hand": Hand.STRAIGHT, "highCard": 7})

    def test_parseHand_isAFlush(self):
        cardStrings = ("3H", "4H", "9H", "6H", "7H")
        parsedHand = parseHand(cardStrings)
        self.assertEqual(parsedHand, {"hand": Hand.FLUSH, "highCard": 9})

    def test_parseHand_isAStraightFlush(self):
        cardStrings = ("3H", "4H", "5H", "6H", "7H")
        parsedHand = parseHand(cardStrings)
        self.assertEqual(
            parsedHand, {"hand": Hand.STRAIGHT_FLUSH, "highCard": 7})

    def test_parseHand_isAFullHouse(self):
        cardStrings = ("3H", "3S", "3C", "JD", "JS")
        parsedHand = parseHand(cardStrings)
        self.assertEqual(parsedHand, {"hand": Hand.FULL_HOUSE, "face": None})

    # List of tuples -> Integer

    def test_numberOfPairs_onePair(self):
        parsedCards = [(4, Suit.HEARTS), (3, Suit.DIAMONDS),
                       (3, Suit.SPADES), (9, Suit.CLUBS),
                       (13, Suit.DIAMONDS)]
        detectPair = numberOfPairs(parsedCards)
        self.assertEqual(detectPair, {"numberOfPairs": 1, "relevantFace": 3})

    def test_numberOfPairs_onePairWithThreeOfAKind(self):
        parsedCards = [(3, Suit.HEARTS), (3, Suit.CLUBS),
                       (3, Suit.SPADES), (11, Suit.DIAMONDS),
                       (11, Suit.SPADES)]
        detectPair = numberOfPairs(parsedCards)
        self.assertEqual(detectPair, {"numberOfPairs": 1, "relevantFace": 11})

    def test_numberOfPairs_twoPair(self):
        parsedCards = [(9, Suit.HEARTS), (3, Suit.DIAMONDS),
                       (3, Suit.SPADES), (9, Suit.CLUBS),
                       (13, Suit.DIAMONDS)]
        detectPair = numberOfPairs(parsedCards)
        self.assertEqual(detectPair, {"numberOfPairs": 2, "relevantFace": 0})

    def test_numberOfPairs_highCardFindsNoPairs(self):
        parsedCards = [(2, Suit.HEARTS), (3, Suit.DIAMONDS),
                       (5, Suit.SPADES), (9, Suit.CLUBS),
                       (13, Suit.DIAMONDS)]
        detectPair = numberOfPairs(parsedCards)
        self.assertEqual(detectPair, {"numberOfPairs": 0, "relevantFace": 0})

    def test_numberOfPairs_fourOfAKindDoesntCountAsAPair(self):
        parsedCards = [(2, Suit.HEARTS), (2, Suit.DIAMONDS),
                       (2, Suit.SPADES), (2, Suit.CLUBS),
                       (13, Suit.DIAMONDS)]
        detectPair = numberOfPairs(parsedCards)
        self.assertEqual(detectPair, {"numberOfPairs": 0, "relevantFace": 0})

# List of tuples -> Bool
    def test_isAStraight(self):
        parsedCards = [(4, Suit.HEARTS), (5, Suit.DIAMONDS),
                       (6, Suit.SPADES), (7, Suit.CLUBS),
                       (8, Suit.DIAMONDS)]
        isStraight = isAStraight(parsedCards)
        self.assertEqual(isStraight, {"hand": Hand.STRAIGHT, "highCard": 8})

    def test_isAStraight_WithFourOfAKind(self):
        parsedCards = [(9, Suit.HEARTS), (9, Suit.DIAMONDS),
                       (9, Suit.SPADES), (9, Suit.CLUBS),
                       (13, Suit.DIAMONDS)]
        isStraight = isAStraight(parsedCards)
        self.assertEqual(isStraight, None)

    def test_isAFlush(self):
        parsedCards = [(4, Suit.DIAMONDS), (5, Suit.DIAMONDS),
                       (6, Suit.DIAMONDS), (7, Suit.DIAMONDS),
                       (10, Suit.DIAMONDS)]
        isFlush = isAFlush(parsedCards)
        self.assertEqual(isFlush, {"hand": Hand.FLUSH, "highCard": 10})

    def test_handOfAKind_isThreeKind(self):
        parsedCards = [(3, Suit.HEARTS), (3, Suit.DIAMONDS),
                       (3, Suit.SPADES), (2, Suit.CLUBS),
                       (13, Suit.DIAMONDS)]
        threeKind = handOfAKind(parsedCards)
        self.assertEqual(threeKind, {"hand": Hand.THREE_OF_A_KIND, "face": 3})

    def test_handOfAKind_isFourOfAKind(self):
        parsedCards = [(4, Suit.HEARTS), (4, Suit.DIAMONDS),
                       (4, Suit.SPADES), (4, Suit.CLUBS),
                       (13, Suit.DIAMONDS)]
        fourKind = handOfAKind(parsedCards)
        self.assertEqual(fourKind, {"hand": Hand.FOUR_OF_A_KIND, "face": 4})

    def test_handOfAKind_isFourOfAKind_EvenWhen4IsTheHigherNumber(self):
        parsedCards = [(2, Suit.DIAMONDS),
                       (4, Suit.HEARTS), (4, Suit.DIAMONDS),
                       (4, Suit.SPADES), (4, Suit.CLUBS)]
        fourKind = handOfAKind(parsedCards)
        self.assertEqual(fourKind, {"hand": Hand.FOUR_OF_A_KIND, "face": 4})

    def test_detectHighCard(self):
        parsedCards = [(4, Suit.SPADES), (8, Suit.HEARTS),
                       (6, Suit.DIAMONDS), (7, Suit.DIAMONDS),
                       (10, Suit.CLUBS)]
        isHighCard = detectHighCard(parsedCards)
        self.assertEqual(isHighCard, {"hand": Hand.HIGH_CARD, "highCard": 10})

    def test_rankOfHand(self):
        playerHands = "Black: 2H 3D 5S 9C KD  White: 2C 2H 4S 8C AH"
        handRank = rankOfHand(playerHands)
        self.assertEqual(handRank, "White wins. - with PAIR")

    def test_rankOfHand_tie(self):
        playerHands = "Black: 9H 3D 5S 9C KD  White: 2C 2H 4S 8C AH"
        handRank = rankOfHand(playerHands)
        self.assertEqual(handRank, "Black wins. - with PAIR: 9 over 2")

    def test_rankOfHand_fourOfAKind(self):
        playerHands = "Black: 9H 9D 9S 9C KD  White: 2C 2H 2S 2D AH"
        handRank = rankOfHand(playerHands)
        self.assertEqual(
            handRank, "Black wins. - with FOUR_OF_A_KIND: 9 over 2")

    def test_rankOfHand_FULL_HOUSE(self):
        playerHands = "Black: 2H 4S 4C 2D 4H  White: 2S 8S AS QS 3S"
        handRank = rankOfHand(playerHands)
        self.assertEqual(handRank, "Black wins. - with FULL_HOUSE")

    def test_splitPlayerHandInput(self):
        playerHands = "Black: 2H 3D 5S 9C KD  White: 2C 3H 4S 8C AH"
        playerHandStrings = splitPlayerHandInput(playerHands)
        self.assertEqual(playerHandStrings, {"black": [
                         "2H", "3D", "5S", "9C", "KD"], "white": ["2C", "3H", "4S", "8C", "AH"]})

    def test_specifyWinningHand(self):
        winningHandEnum = Hand.PAIR
        winningHand = specifyWinningHand(winningHandEnum)
        self.assertEqual(winningHand, "PAIR")

    def test_tieBreaker(self):
        handType = Hand.PAIR
        blackHandCard = 4
        whiteHandCard = 2
        winnerOfTie = tieBreaker(handType, blackHandCard, whiteHandCard)
        self.assertEqual(winnerOfTie, "Black wins. - with PAIR: 4 over 2")

    def test_tieBreaker_blackWinsDifferentFaceValues(self):
        handType = Hand.PAIR
        blackHandCard = 8
        whiteHandCard = 7
        winnerOfTie = tieBreaker(handType, blackHandCard, whiteHandCard)
        self.assertEqual(winnerOfTie, "Black wins. - with PAIR: 8 over 7")

    def test_tieBreaker2(self):
        handType = Hand.PAIR
        blackHandCard = 4
        whiteHandCard = 9
        winnerOfTie = tieBreaker(handType, blackHandCard, whiteHandCard)
        self.assertEqual(winnerOfTie, "White wins. - with PAIR: 9 over 4")


if __name__ == '__main__':
    unittest.main()

    # c = "Black: 2H 3D 5S 9C KD  White: 2C 3H 4S 8C AH"
# Black: 2H 3D 5S 9C KD  White: 2C 3H 4S 8C AH
# Black: 2H 4S 4C 2D 4H  White: 2S 8S AS QS 3S
# Black: 2H 3D 5S 9C KD  White: 2C 3H 4S 8C KH
# Black: 2H 3D 5S 9C KD  White: 2D 3H 5C 9S KH

# Need to decide what goes in and what will come out of the function
# String -> Tuple
