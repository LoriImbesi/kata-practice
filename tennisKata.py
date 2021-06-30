#! python3


def currentScore(player1, player2):
    # tennisScore = {0: '0', 1: '15', 2: '30', 3: '40'}

    if player1 >= 3 and player2 == player1:
        return "deuce"
    if player1 >= 4 and player2 == player1 - 1:
        return "advantage: player1"
    if player2 >= 4 and player1 == player2 - 1:
        return "advantage: player2"
    if player1 >= 5 and player2 == player1 - 2:
        return "winner: player1"
    if player2 >= 5 and player1 == player2 - 2:
        return "winner: player2"

    return convertScore(player1) + ' - ' + convertScore(player2)


def convertScore(player):
    if player == 0:
        return "0"
    if player == 1:
        return "15"
    if player == 2:
        return "30"
    if player == 3:
        return "40"
