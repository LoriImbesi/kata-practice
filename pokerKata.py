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
    blackHand = parseHand(handStrings["black"])
    whiteHand = parseHand(handStrings["white"])
    if blackHand["hand"].value == whiteHand["hand"].value:
        return tieBreaker(blackHand["hand"], blackHand["face"], whiteHand["face"])
    elif blackHand["hand"].value > whiteHand["hand"].value:
        winningHand = specifyWinningHand(blackHand["hand"])
        return ("Black wins. - with " + winningHand)
    else:
        winningHand = specifyWinningHand(whiteHand["hand"])
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
    numOfPairs = numberOfPairs(parsedCards)

    threeOrFourOfAKind = handOfAKind(parsedCards)
    isStraight = isAStraight(parsedCards)
    isFlush = isAFlush(parsedCards)

    if isFlush == True and isStraight == True:
        return {"hand": Hand.STRAIGHT_FLUSH, "face": None}
    if threeOrFourOfAKind == Hand.THREE_OF_A_KIND and numOfPairs["numberOfPairs"] == 1:
        return {"hand": Hand.FULL_HOUSE, "face": None}
    if isFlush == True:
        return {"hand": Hand.FLUSH, "face": None}
    if isStraight == True:
        return {"hand": Hand.STRAIGHT, "face": None}
    if threeOrFourOfAKind:
        return {"hand": threeOrFourOfAKind, "face": None}
    if numOfPairs["numberOfPairs"] == 1:
        return {"hand": Hand.PAIR, "face": numOfPairs["relevantFace"]}
    if numOfPairs["numberOfPairs"] == 2:
        return {"hand": Hand.TWO_PAIR, "face": None}
    return {"hand": Hand.HIGH_CARD, "face": None}


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
    pairInformation = {"numberOfPairs": 0, "relevantFace": 0}
    if uniqueFaces == 5:
        return pairInformation
    for face in faceCounts:
        if faceCounts[face] == 2:
            if uniqueFaces == 4 or uniqueFaces == 2:
                pairInformation["numberOfPairs"] = 1
                pairInformation["relevantFace"] = face
                return pairInformation
            elif uniqueFaces == 3:
                pairInformation["numberOfPairs"] = 2
                # pairInformation["relevantFace"] = face
                return pairInformation

    return pairInformation


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
