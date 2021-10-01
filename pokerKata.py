from enum import Enum


class Suit(Enum):
    HEARTS = 1
    SPADES = 2
    CLUBS = 3
    DIAMONDS = 4


def parseCard(card):
    parsedCard = []
    face = int(card[0])
    suit = card[1]
    parsedCard.append(face)
    parsedCard.append(suit)
    parsedCard = tuple(parsedCard)
    return parsedCard
