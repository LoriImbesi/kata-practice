from enum import Enum


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
    parsedCardsList = []
    for card in cards:
        parsedCard = parseCard(card)
        parsedCardsList.append(parsedCard)
    return (parsedCardsList)
