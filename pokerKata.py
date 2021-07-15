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


# parse data (cardString) then match values in dicts and return

def parseCard(cardString):
    cardFace = cardString[0]
    face = faceLookup[cardFace]
    cardSuit = cardString[1]
    suit = suitLookup[cardSuit]
    return Card(suit, face)

# string[](N) -> Card[](N)


def parseCards(cardStrings):
    # empty "state" list
    cardsToReturn = []

    # populate "state" list
    for cardString in cardStrings:
        card = parseCard(cardString)
        cardsToReturn.append(card)

    # return "state" list
    return cardsToReturn


def countFaces(cards):
    faceCounts = {}
    for card in cards:
        faceCounts[card.face] = 0
    for card in cards:
        faceCounts[card.face] += 1
    return faceCounts


def countSuits(cards):
    suitCount = {}
    for card in cards:
        suitCount[card.suit] = 0
    for card in cards:
        suitCount[card.suit] += 1
    return suitCount


def isFlush(cards):
    isAFlush = False
    countOfSuits = countSuits(cards)
    for suit in countOfSuits:
        suitCount = countOfSuits[suit]
        if suitCount == 5:
            isAFlush = True
    return isAFlush


def isStraight(cards):
    isAStraight = False
    countOfFaces = countFaces(cards)
    listOfFaces = []
    listOfFaces = list(countOfFaces.keys())
    if len(listOfFaces) == 5:
        listOfFaces.sort()
        sortedFaces = listOfFaces
        if sortedFaces[-1] - sortedFaces[0] == 4:
            isAStraight = True
    return isAStraight


def isStraightFlush(cards):
    isAStraightFlush = False
    aFlush = isFlush(cards)
    aStraight = isStraight(cards)
    if aFlush and aStraight == True:
        isAStraightFlush = True
    return isAStraightFlush


def isRoyalFlush(cards):
    isARoyalFlush = False
    aStraightFlush = isStraightFlush(cards)
    countOfFaces = countFaces(cards)
    if aStraightFlush == True:
        listOfFaces = []
        listOfFaces = list(countOfFaces.keys())
        if len(listOfFaces) == 5:
            listOfFaces.sort()
            sortedFaces = listOfFaces
            if sortedFaces[0] == 10 and sortedFaces[-1] == 14:
                isARoyalFlush = True
    return isARoyalFlush


def countSets(countOfFaces):
    numberOfQuads = 0
    numberOfPairs = 0
    numberOfTriplets = 0
    for face in countOfFaces:
        faceCount = countOfFaces[face]
        if faceCount == 2:
            numberOfPairs += 1
        if faceCount == 3:
            numberOfTriplets += 1
        if faceCount == 4:
            numberOfQuads = 1
    return {'pairs': numberOfPairs, 'triplets': numberOfTriplets, 'quads': numberOfQuads}


def parseHand(cardStrings):
    # parsing
    # populate "state" list
    cards = parseCards(cardStrings)
    countOfFaces = countFaces(cards)
    confirmFlush = isFlush(cards)
    confirmStraight = isStraight(cards)
    confirmStraightFlush = isStraightFlush(cards)
    confirmRoyalFlush = isRoyalFlush(cards)
    # analyze face pairings

    setCounts = countSets(countOfFaces)
    numberOfPairs = setCounts['pairs']
    numberOfTriplets = setCounts['triplets']
    numberOfQuads = setCounts['quads']

    # determine what to do with analysis
    if numberOfPairs == 2:
        return Hand.TWO_PAIR
    elif numberOfPairs == 1 and numberOfTriplets == 1:
        return Hand.FULL_HOUSE
    elif numberOfPairs == 1:
        return Hand.PAIR
    elif numberOfPairs == 0 and numberOfTriplets == 1:
        return Hand.THREE_OF_A_KIND
    elif numberOfQuads == 1:
        return Hand.FOUR_OF_A_KIND
    elif confirmRoyalFlush == True:
        return Hand.ROYAL_FLUSH
    elif confirmStraightFlush == True:
        return Hand.STRAIGHT_FLUSH
    elif confirmFlush == True:
        return Hand.FLUSH
    elif confirmStraight == True:
        return Hand.STRAIGHT

    # return "state" list
    return None

    #     # question asking

    #     # Mapping the answers to the business domain
