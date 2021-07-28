#! python3


def makeGameState(player1Score, player2Score):
    return {"player1Score":  player1Score,
            "player2Score": player2Score}


def printCurrentScore(gameState):
    player1 = str(gameState['player1Score'])
    player2 = str(gameState['player2Score'])
    if gameState['player1Score'] == 1:
        player1 = "15"
    if gameState['player2Score'] == 1:
        player2 = "15"
    if gameState['player1Score'] == 2:
        player1 = "30"
    if gameState['player2Score'] == 2:
        player2 = "30"
    if gameState['player1Score'] == 3:
        player1 = "40"
    if gameState['player2Score'] == 3:
        player2 = "40"
    return player1 + " - " + player2


def playerOneScored(gameState):
    gameState['player1Score'] += 1
    return gameState


def playerTwoScored(gameState):
    gameState['player2Score'] += 1
    return gameState
