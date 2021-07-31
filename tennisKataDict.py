#! python3


def makeGameState(player1Score, player2Score):
    return {"player1Score": player1Score,
            "player2Score": player2Score}


def printCurrentScore(gameState):
    currentToGameScore = {0: "0", 1: "15", 2: "30", 3: "40", 4: "game"}

    player1IntegerScore = gameState["player1Score"]
    player2IntegerScore = gameState["player2Score"]

    if player1IntegerScore >= 3 and player1IntegerScore == player2IntegerScore:
        return "deuce"
    if player1IntegerScore >= 3 and player1IntegerScore == player2IntegerScore + 1:
        return "Player1 advantage"

    player1 = currentToGameScore[player1IntegerScore]
    player2 = currentToGameScore[player2IntegerScore]

    # for score in currentToGameScore.values():
    #    player1 = currentToGameScore[gameState.player1Score]
    #    player2 = currentToGameScore[gameState.player2Score]

    return player1 + " - " + player2

    # player1 = str(gameState['player1Score'])
    # player2 = str(gameState['player2Score'])

    # return player1 + " - " + player2


def playerOneScored(gameState):
    gameState['player1Score'] += 1
    return gameState


def playerTwoScored(gameState):
    gameState['player2Score'] += 1
    return gameState
