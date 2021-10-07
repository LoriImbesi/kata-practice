from enum import Enum


class Suit(Enum):
    HEARTS = 1
    SPADES = 2
    CLUBS = 3
    DIAMONDS = 4


class Hand(Enum):
    HIGH_CARD = 0
    PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8
    ROYAL_FLUSH = 9


suitLookup = {"H": Suit.HEARTS, "S": Suit.SPADES,
              "C": Suit.CLUBS, "D": Suit.DIAMONDS}

faceLookup = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
              "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12,
              "K": 13, "A": 14}


def splitPlayerHandInput(playerHands):
    playerHandInput = playerHands.split()
    playerHandInput.remove("Black:")
    playerHandInput.remove("White:")

    playerHandStrings = {"black": playerHandInput[0:5],
                         "white": playerHandInput[5:]}

    return playerHandStrings


def rankOfHand(playerHands):
    handStrings = splitPlayerHandInput(playerHands)
    (blackHand, blackFaceCards) = parseHand(handStrings["black"])
    (whiteHand, whiteFaceCards) = parseHand(handStrings["white"])
    if blackHand.value == whiteHand.value:
        return tieBreaker(blackHand, blackFaceCards[0], whiteFaceCards[0])
    elif blackHand.value > whiteHand.value:
        winningHand = specifyWinningHand(blackHand)
        return ("Black wins. - with " + winningHand)
    else:
        winningHand = specifyWinningHand(whiteHand)
        return ("White wins. - with " + winningHand)


#            1.7. rankOfHand
#  2. 6. parseHand          -  8. tieBreaker
#  3.5. numberOfPairs
#  4. countOfFaces

def specifyWinningHand(winningHandEnum):
    winningHand = str(winningHandEnum)
    hand = winningHand.split(".")
    nameOfHand = hand[1]
    return nameOfHand


def tieBreaker(handType, blackHandCard, whiteHandCard):
    handRank = specifyWinningHand(handType)
    if blackHandCard > whiteHandCard:
        return ("Black wins. - with " + handRank + ": " + str(blackHandCard) + " over " + str(whiteHandCard))
    else:
        return ("White wins. - with " + handRank + ": " + str(whiteHandCard) + " over " + str(blackHandCard))


def parseHand(cardStrings):
    parsedCards = parseCards(cardStrings)
    (numOfPairs, faceCards) = numberOfPairs(parsedCards)
    threeOrFourOfAKind = handOfAKind(parsedCards)
    isStraight = isAStraight(parsedCards)
    isFlush = isAFlush(parsedCards)

    if isFlush == True and isStraight == True:
        return (Hand.STRAIGHT_FLUSH, [])
    if threeOrFourOfAKind == Hand.THREE_OF_A_KIND and numOfPairs == 1:
        return (Hand.FULL_HOUSE, [])
    if isFlush == True:
        return (Hand.FLUSH, [])
    if isStraight == True:
        return (Hand.STRAIGHT, [])
    if threeOrFourOfAKind:
        return (threeOrFourOfAKind, [])
    if numOfPairs == 1:
        return (Hand.PAIR, faceCards)
    if numOfPairs == 2:
        return (Hand.TWO_PAIR, [])
    return (Hand.HIGH_CARD, [])


def parseCard(card):
    faceString = card[0]
    face = faceLookup[faceString]
    suitString = card[1]
    suit = suitLookup[suitString]
    return (face, suit)


def parseCards(cardStrings):
    parsedCardList = []
    for cardString in cardStrings:
        parsedCards = parseCard(cardString)
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


def numberOfPairs(parsedCards):
    faceCounts = countOfFaces(parsedCards)
    uniqueFaces = len(faceCounts)
    if uniqueFaces == 5:
        return (0, [])
    for face in faceCounts:
        if faceCounts[face] == 2:
            if uniqueFaces == 4 or uniqueFaces == 2:
                return (1, [face])
            elif uniqueFaces == 3:
                return (2, [])  # todo finish two pair

    return (0, [])


def handOfAKind(parsedCards):
    faceCounts = countOfFaces(parsedCards)
    for face in faceCounts:
        if faceCounts[face] == 3:
            return Hand.THREE_OF_A_KIND
        elif faceCounts[face] == 4:
            return Hand.FOUR_OF_A_KIND

    return None


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
