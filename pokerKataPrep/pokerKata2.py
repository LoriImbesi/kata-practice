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
    STRAIGHT_FLUSH = 8
    ROYAL_FLUSH = 9

# structure to hold the card - class
# object-oriented example


class Card:
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face

    def toString(self):
        return 'suit: ' + self.suit + '  face: ' + self.face


faceLookup = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
              '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
suitLookup = {'H': Suit.HEARTS, 'S': Suit.SPADES,
              'D': Suit.DIAMONDS, 'C': Suit.CLUBS}


def parseCard(cardString):  # cardString, comprised of face and suit - coming from test
    cardFace = cardString[0]  # location of cardFace in cardString
    face = faceLookup[cardFace]  # location of face in faceLookup dict
    cardSuit = cardString[1]  # location of cardSuit in cardString
    suit = suitLookup[cardSuit]  # location of suit in suitLookup dict
    return Card(suit, face)


def parseCards(cardStrings):
    cardsToReturn = []  # empty state list
    for cardString in cardStrings:  # build up state
        # set card to the function parseCard and pass cardString
        card = parseCard(cardString)
        cardsToReturn.append(card)  # append card to cardsToReturn list

    return cardsToReturn


def faceCounts(cards):
    countOfFaces = {}  # countOfFaces needs a dict to hold the count
    for card in cards:
        countOfFaces[card.face] = 0  # count the face of each card
    for card in cards:
        countOfFaces[card.face] += 1
    return countOfFaces


def suitCounts(cards):
    countOfSuits = {}  # countOfSuits needs a dict to hold the count
    for card in cards:
        countOfSuits[card.suit] = 0
    for card in cards:
        countOfSuits[card.suit] += 1
    return countOfSuits


def isPairOrKind(countOfFaces):  # passing in the returned dict from faceCounts
    isAPair = 0
    isAThreeOfAKind = 0
    isAFourOfAKind = 0
    for count in countOfFaces:
        faceCount = countOfFaces[count]
        if faceCount == 2:
            isAPair += 1
        if faceCount == 3:
            isAThreeOfAKind += 1
        if faceCount == 4:
            isAFourOfAKind = 1
    return{'pairs': isAPair, 'triplets': isAThreeOfAKind, 'quads': isAFourOfAKind}


def parseHand(cardStrings):

    cards = parseCards(cardStrings)
    countTheFaces = faceCounts(cards)
    isAFlush = isFlush(cards)
    isAStraight = isStraight(cards)
    isARoyalFlush = isRoyalFlush(cards)

    pairOrKindCount = isPairOrKind(countTheFaces)
    isAPair = pairOrKindCount['pairs']
    isAThreeOfAKind = pairOrKindCount['triplets']
    isAFourOfAKind = pairOrKindCount['quads']

    if isAStraight and isARoyalFlush == True:
        return Hand.ROYAL_FLUSH
    elif isAStraight and isAFlush:
        return Hand.STRAIGHT_FLUSH
    elif isAThreeOfAKind == 1 and isAPair == 1:
        return Hand.FULL_HOUSE
    elif isAPair == 0 and isAThreeOfAKind == 1:
        return Hand.THREE_OF_A_KIND
    elif isAFourOfAKind == 1:
        return Hand.FOUR_OF_A_KIND
    elif isAPair == 2:
        return Hand.TWO_PAIR
    elif isAFlush == True:
        return Hand.FLUSH
    elif isAStraight == True:
        return Hand.STRAIGHT
    elif isAPair == 1:
        return Hand.PAIR

    return None


def isFlush(cards):
    isAFlush = False
    countOfSuits = suitCounts(cards)
    for count in countOfSuits:
        suitCount = countOfSuits[count]
        if suitCount == 5:
            isAFlush = True
    return isAFlush


def isStraight(cards):
    isAStraight = False
    faceList = []
    for card in cards:
        faceList.append(card.face)
    faceList.sort()
    if faceList[-1] - faceList[0] == 4:
        isAStraight = True
    return isAStraight


def isRoyalFlush(cards):
    isARoyalFlush = False
    faceList = []
    for card in cards:
        faceList.append(card.face)
    faceList.sort()
    if faceList[-1] - faceList[0] == 4 and faceList[0] == 10:
        isARoyalFlush = True
    return isARoyalFlush
