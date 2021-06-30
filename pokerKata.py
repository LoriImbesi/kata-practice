from enum import Enum


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
    FULL_HOUSE = 6
    STRAIGHT = 7


class Card:
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face


faceLookup = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
              '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
suitLookup = {'H': Suit.HEARTS, 'S': Suit.SPADES,
              'D': Suit.DIAMONDS, 'C': Suit.CLUBS}


def parseCard(cardString):
    suitLetter = cardString[1]
    suit = suitLookup[suitLetter]
    faceLetter = cardString[0]
    face = faceLookup[faceLetter]
    return Card(suit, face)


def parseCards(cardStrings):
    cards = []
    for cardString in cardStrings:
        card = parseCard(cardString)
        cards.append(card)
    return cards

# ["3D", "4D"]
# [Card, Card]
# Hand.PAIR


def countFaces(cards):
    countOfFaces = {}
    for card in cards:
        if card.face in countOfFaces:
            countOfFaces[card.face] += 1
        else:
            countOfFaces[card.face] = 1
    return countOfFaces


def countSuits(cards):
    countOfSuits = {}
    for card in cards:
        if card.suit in countOfSuits:
            countOfSuits[card.suit] += 1
        else:
            countOfSuits[card.suit] = 1
    return countOfSuits


def countPairs(countOfFaces):
    countOfPairs = 0
    for countOfFace in countOfFaces.values():
        if countOfFace == 2:
            countOfPairs += 1
    return countOfPairs


def isStraight(cards):
    faceValues = []
    for card in cards:
        faceValues.append(card.face)
    faceValues.sort()
    lowestFace = faceValues[0]
    expectedFaces = list(range(lowestFace, lowestFace+5))
    return faceValues == expectedFaces


def parseHand(cardStrings):
    cards = parseCards(cardStrings)  # parsing

    isAStraight = isStraight(cards)

    countOfFaces = countFaces(cards)  # question asking
    countOfSuits = countSuits(cards)
    countOfPairs = countPairs(countOfFaces)

    # Mapping the answers to the business domain
    for countOfSuit in countOfSuits.values():
        if countOfSuit == 5:
            return Hand.FLUSH

    for countOfFace in countOfFaces.values():

        if countOfFace == 3:
            if countOfPairs == 1:
                return Hand.FULL_HOUSE
            return Hand.THREE_OF_A_KIND
        if countOfFace == 4:
            return Hand.FOUR_OF_A_KIND

    if countOfPairs == 2:
        return Hand.TWO_PAIR
    elif countOfPairs == 1:
        return Hand.PAIR

    if isAStraight:
        return Hand.STRAIGHT
