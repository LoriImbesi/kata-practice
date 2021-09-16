from enum import Enum, unique


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
    STRAIGHT_FLUSH = 8
    ROYAL_FLUSH = 9


class Card:
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face

        def toString(self):
            return 'suit: ' + self.suit + '  face: ' + self.face


faceLookup = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
              '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

suitLookup = {'H': Suit.HEARTS, 'C': Suit.CLUBS,
              'S': Suit.SPADES, 'D': Suit.DIAMONDS}


def parseCard(cardString):
    cardFace = cardString[0]
    face = faceLookup[cardFace]
    cardSuit = cardString[1]
    suit = suitLookup[cardSuit]
    return Card(suit, face)


def parseCards(cardStrings):

    cardsToReturn = []

    for cardString in cardStrings:
        card = parseCard(cardString)
        cardsToReturn.append(card)

    return cardsToReturn


def faceCounts(cards):
    countOfFaces = {}

    for card in cards:
        countOfFaces[card.face] = 0
    for card in cards:
        countOfFaces[card.face] += 1
    return countOfFaces


def suitCounts(cards):
    setOfSuits = set()

    for card in cards:
        setOfSuits.add(card.suit)
    return len(setOfSuits)


def countOfPairOrKind(countOfFaces):
    numberOfPairs = 0
    numberOfThreeOfAKind = 0
    numberOfFourOfAKind = 0

    for countOfFace in countOfFaces:
        faceCount = countOfFaces[countOfFace]
        if faceCount == 2:
            numberOfPairs += 1
        elif faceCount == 3:
            numberOfThreeOfAKind += 1
        elif faceCount == 4:
            numberOfFourOfAKind += 1

    return {'pairs': numberOfPairs, 'triplets': numberOfThreeOfAKind,
            'quads': numberOfFourOfAKind}


def isStraight(countOfFaces):
    listOfFaces = list(countOfFaces.keys())
    if len(listOfFaces) == 5:
        listOfFaces.sort()
        sortedFaces = listOfFaces
        highCard = sortedFaces[4]
        if sortedFaces[-1] - sortedFaces[0] == 4:
            return True, highCard
    return False, None


def parseHand(cardStrings):

    cards = parseCards(cardStrings)
    countOfFaces = faceCounts(cards)
    countOfSuits = suitCounts(cards)

    pairOrKindCount = countOfPairOrKind(countOfFaces)
    numberOfPairs = pairOrKindCount['pairs']
    numberOfThreeOfAKind = pairOrKindCount['triplets']
    numberOfFourOfAKind = pairOrKindCount['quads']

    isAFlush = (countOfSuits == 1)
    isAStraight, highCard = isStraight(countOfFaces)

    if isAFlush == True and isAStraight == True and highCard == 14:
        return Hand.ROYAL_FLUSH
    elif numberOfThreeOfAKind == 1 and numberOfPairs == 1:
        return Hand.FULL_HOUSE
    elif numberOfFourOfAKind == 1:
        return Hand.FOUR_OF_A_KIND
    elif numberOfThreeOfAKind == 1:
        return Hand.THREE_OF_A_KIND
    elif numberOfPairs == 2:
        return Hand.TWO_PAIR
    elif numberOfPairs == 1:
        return Hand.PAIR
    elif isAFlush == True and isAStraight == True:
        return Hand.STRAIGHT_FLUSH
    elif isAFlush == True:
        return Hand.FLUSH
    elif isAStraight == True:
        return Hand.STRAIGHT
