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
    print(blackHand)
    print(whiteHand)
    if blackHand["hand"].value == whiteHand["hand"].value:
        return tieBreaker(blackHand["hand"], blackHand["face"], whiteHand["face"])
    elif blackHand["hand"].value > whiteHand["hand"].value:
        winningHand = specifyWinningHand(blackHand["hand"])
        return ("Black wins. - with " + winningHand)
    else:
        winningHand = specifyWinningHand(whiteHand["hand"])
        return ("White wins. - with " + winningHand)


#                      1.7. rankOfHand
#          2. 6. parseHand               -  8. tieBreaker
#  3.5. numberOfPairs  - handofAKind
#  4. countOfFaces

def specifyWinningHand(winningHandEnum):
    winningHand = str(winningHandEnum)
    hand = winningHand.split(".")
    nameOfHand = hand[1]
    return nameOfHand


def tieBreaker(handType, blackHandCard, whiteHandCard):

    print(handType)
    print(blackHandCard)
    print(whiteHandCard)
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
    if threeOrFourOfAKind["hand"] == Hand.THREE_OF_A_KIND \
       and numOfPairs["numberOfPairs"] == 1:
        return {"hand": Hand.FULL_HOUSE, "face": None}
    if isFlush == True:
        return {"hand": Hand.FLUSH, "face": None}
    if isStraight == True:
        return {"hand": Hand.STRAIGHT, "highCard": isStraight["highCard"]}
    if threeOrFourOfAKind['hand'] != 0:
        return threeOrFourOfAKind
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
    handInformation = {"hand": 0, "face": 0}
    for face in faceCounts:
        if faceCounts[face] == 3:
            return {"hand": Hand.THREE_OF_A_KIND, "face": face}
        elif faceCounts[face] == 4:
            return {"hand": Hand.FOUR_OF_A_KIND, "face": face}

    return handInformation


def isAStraight(parsedCards):
    faceCounts = countOfFaces(parsedCards)
    straightHandInformation = {"hand": 0, "highCard": 0}
    faces = list(faceCounts.keys())
    faces.sort()
    confirmStraight = min(
        faces) + 1 == faces[1] and max(faces) - min(faces) == 4
    if confirmStraight == True:
        for face in faces:
            return {"hand": Hand.STRAIGHT, "highCard": max(faces)}

    return straightHandInformation

    # if max(faces) - min(faces) == 4:
    # return True


def isAFlush(parsedCards):
    firstSuit = parsedCards[0][1]
    faceCounts = countOfFaces(parsedCards)
    flushHandInformation = {"hand": 0, "highCard": 0}
    faces = list(faceCounts.keys())
    faces.sort()
    for parsedCard in parsedCards:
        suit = parsedCard[1]
        if firstSuit != suit:
            return False
    for face in faces:
        return {"hand": Hand.FLUSH, "highCard": max(faces)}
    return flushHandInformation
