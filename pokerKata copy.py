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

card1 = (Suit.HEARTS, 5)
card1[0] # tuple: fully completed, no name, no autocomplete, infinite values

card3 = [Suit.HEARTS, 8]
card3[0] # list: partially completed, no name, no autocomplete, infinite values

card2 = {'suit': Suit.HEARTS, 'face': 8}
card2['suit'] # dict: partially created, no autocomplete, infinite keys, can use variables for key

card4 = Card(Suit.HEARTS, 8)
card4.suit # class: fully created, autocomplete, finite keys, cannot use variables for key

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
