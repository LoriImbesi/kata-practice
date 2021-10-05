from enum import Enum, unique

from pokerKataPrep.pokerKata2 import faceCounts


class Suit(Enum):
    HEARTS = 1
    SPADES = 2
    CLUBS = 3
    DIAMONDS = 4


suitLookup = {"H": Suit.HEARTS, "S": Suit.SPADES,
              "C": Suit.CLUBS, "D": Suit.DIAMONDS}

faceLookup = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
              "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12,
              "K": 13, "A": 14}


def parseCard(card):
    faceString = card[0]
    face = faceLookup[faceString]
    suitString = card[1]
    suit = suitLookup[suitString]
    return (face, suit)


def parseCards(cards):
    parsedCardList = []
    for card in cards:
        parsedCards = parseCard(card)
        parsedCardList.append(parsedCards)
    return parsedCardList


def countOfFaces(parsedCards):
    faceCounts = {}
    for parsedCard in parsedCards:
        face = parsedCard[0]
        if face in faceCounts:
            faceCounts[face] += 1
        else:
            faceCounts[face] = 1
    return faceCounts

# def countOfSuits(parsedCards):
#     suitCounts = {}
#     for parsedCard in parsedCards:
#         suit = parsedCard[1]
#         for suit in suitCounts:


def numberOfPairs(parsedCards):
    faceCounts = countOfFaces(parsedCards)
    uniqueFaces = len(faceCounts)
    if uniqueFaces == 5:
        return 0
    for face in faceCounts:
        if faceCounts[face] == 2:
            if uniqueFaces == 4:
                return 1
            elif uniqueFaces == 3:
                return 2

    return 0


def isThreeOfAKind(parsedCards):
    faceCounts = countOfFaces(parsedCards)

    for face in faceCounts:
        if faceCounts[face] == 3:
            return True


def isAStraight(parsedCards):
    faceCounts = countOfFaces(parsedCards)
    faces = faceCounts.keys()
    if max(faces) - min(faces) == 4:
        return True


def isAFlush(parsedCards):
    firstSuit = parsedCards[0][1]

    for parsedCard in parsedCards:
        suit = parsedCard[1]
        if firstSuit != suit:
            return False

    return True
