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
    faceCount = 0
    face
    for card in cards:
        faceCount += 1
    return faceCount


def countSuits(cards):
    suitCount = 0
    for suit in suitCount:
        suitCount += 1
    return suitCount


def countPairs(countOfFaces):
    pairCount = 0
    for pair in pairCount:
        pair += 1
    if pairCount == 2:
        return Hand.TWO_PAIR
    elif pairCount == 1:
        return Hand.PAIR

    # def isStraight(cards):


def parseHand(cardStrings):
    # parsing
    cards = []
    # populate "state" list
    for cardString in cardStrings:
        card = parseCard(cardString)
        cards.append(card)

    # return "state" list
    return cards

    #     # question asking
    if countFaces == 3:
        return Hand.THREE_OF_A_KIND
    #     # Mapping the answers to the business domain