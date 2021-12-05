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
    blackHand = findHandType(handStrings["black"])
    whiteHand = findHandType(handStrings["white"])
    # print(blackHand)
    # print(whiteHand)
    if blackHand["hand"].value == whiteHand["hand"].value:
        return tieBreaker(blackHand["hand"], blackHand["face"], whiteHand["face"])
    elif blackHand["hand"].value > whiteHand["hand"].value:
        winningHand = specifyWinningHand(blackHand["hand"])
        return ("Black wins. - with " + winningHand)
    else:
        winningHand = specifyWinningHand(whiteHand["hand"])
        return ("White wins. - with " + winningHand)


#                      1.7. rankOfHand
#          2. 6. findHandType()               -  8. tieBreaker
#  3.5. numberOfPairs  - handofAKind
#  4. countOfFaces

# if isWhateverHand is tie, detectHighCard
# does this logic then get repeated in every hand?
# Is there a more efficient way to insert this?
# What are the baseline conditions for each hand

def specifyWinningHand(winningHandEnum):
    winningHand = str(winningHandEnum)
    hand = winningHand.split(".")
    nameOfHand = hand[1]
    return nameOfHand


def tieBreaker(handType, blackHandCard, whiteHandCard):

    # print(handType)
    # print(blackHandCard)
    # print(whiteHandCard)
    handRank = specifyWinningHand(handType)
    if blackHandCard > whiteHandCard:
        return ("Black wins. - with " + handRank + ": " + str(blackHandCard) + " over " + str(whiteHandCard))
    else:
        return ("White wins. - with " + handRank + ": " + str(whiteHandCard) + " over " + str(blackHandCard))


def findHandType(cardStrings):
    parsedCards = parseHand(cardStrings)
    numOfPairs = numberOfPairs(parsedCards)
    threeOrFourOfAKind = handOfAKind(parsedCards)
    # [(2, Suit.HEARTS), (2, Suit.CLUBS)]
    # if isAFlush(parsedCards) == True and isAStraight(parsedCards) == True:
        # return {"hand": Hand.STRAIGHT_FLUSH, "highCard": isAStraight(parsedCards)["highCard"]}
    if threeOrFourOfAKind["hand"] == Hand.THREE_OF_A_KIND \
       and numOfPairs["numberOfPairs"] == 1:
        return {"hand": Hand.FULL_HOUSE, "face": None}
    if isAFlush(parsedCards):
        return {"hand": Hand.FLUSH, "highCard": isAFlush(parsedCards)["highCard"]}
    if isAStraight(parsedCards):
        return {"hand": Hand.STRAIGHT, "highCard": isAStraight(parsedCards)["highCard"]}
    if threeOrFourOfAKind['hand'] != 0:
        return threeOrFourOfAKind
    if numOfPairs["numberOfPairs"] == 1:
        return {"hand": Hand.PAIR, "face": numOfPairs["relevantFace"]}
    if numOfPairs["numberOfPairs"] == 2:
        return {"hand": Hand.TWO_PAIR, "face": None}
    return {"hand": Hand.HIGH_CARD, "face": None}


def parseCard(card):
    faceString = card[0:-1]
    face = faceLookup[faceString]
    suitString = card[-1]
    suit = suitLookup[suitString]
    return (face, suit)


def parseHand(cardStrings):
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
    faces = list(faceCounts.keys())
    faces.sort()
    print(faces)
    confirmStraight = min(
        faces) + 1 == faces[1] and max(faces) - min(faces) == 4
    if confirmStraight == True:
        return {"hand": Hand.STRAIGHT, "highCard": max(faces)}


def isAFlush(parsedCards):
    firstSuit = parsedCards[0][1]
    for parsedCard in parsedCards:
        suit = parsedCard[1]
        if firstSuit != suit:
            return False
   
    return {"hand": Hand.FLUSH, "highCard": detectHighCard(parsedCards)}


def detectHighCard(parsedCards):
    faceCounts = countOfFaces(parsedCards)
    faces = list(faceCounts.keys())
    faces.sort()
    return (max(faces))


    # Suit.HEARTS == <Suit.HEARTS : 1>

    # Not sure what detectHighCard should return
    # should it be a dict with "hand" as none?
    # Then it gets updated in other functions?
    # How can isAHighCard be used easily?
    # what's needed where?
    # findHandType() needs simple, flexible structures

    # truthiness diagram:
    # True, data, {key: 0, value: 1}, [1, 5, "stuff"], "ham", 5 === truthy
    # False, none {}, [], 0 === falsey

    # Test isAFlush1 failing, line 200 isn't hitting, all of the tuples are comparing
    # identically, but we do not know why. Something going wrong with datatype? Enum?

    # Tesing a single test: TestPokerKata.test_findHandType_isPair