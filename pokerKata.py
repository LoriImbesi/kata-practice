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


def parseHand(cardStrings):
    cards = parseCards(cardStrings)
    countOfFaces = {}
    print("starting loop")
    for card in cards:
        if card.face in countOfFaces:
            countOfFaces[card.face] += 1
        else:
            countOfFaces[card.face] = 1

        print(countOfFaces)
    # do something to check to see if it is a pair

    for countOfFace in countOfFaces.values():
        print(countOfFace)
        if countOfFace == 2:
            return Hand.PAIR
