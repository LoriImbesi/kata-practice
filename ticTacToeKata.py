#! python3

# row 0 - 0,1,2
# 1 - 0,1,2
# 2 - 0,1,2
# 0,1,2 - col 0
# 0,1,2 - 1
# 0,1,2 - 2
# 0,0 1,1 2,2
# 0,2 1,1 2,0


# def gameBoardStatus(player1, player2):
#     gameState = [["", "", ""],
#                  ["", "", ""],
#                  ["", "", ""]]
#
#     return None


def makeEmptyBoard():
    return [["", "", ""],
            ["", "", ""],
            ["", "", ""]]


def playerXMove(board, row, col):
    board[row][col] = "X"
    return board


def playerOMove(board, row, col):
    board[row][col] = "O"
    return board


class TicTacToeWinner:

    def __init__(self, board, playerIcon):
        self.board = board
        self.playerIcon = playerIcon

    def gameWinHoriz(row):
        return (board[row][0] == playerIcon and board[row][1] == playerIcon and board[row][2] == playerIcon)

    def gameWinVert(col):
        return (board[0][col] == playerIcon and board[1][col] == playerIcon and board[2][col] == playerIcon)

    def gameOverForPlayer():
        gameWinDiagLeft = board[0][0] == playerIcon and board[1][1] == playerIcon and board[2][2] == playerIcon
        gameWinDiagRight = board[0][2] == playerIcon and board[1][1] == playerIcon and board[2][0] == playerIcon

        if gameWinHoriz(row=0) \
                or gameWinHoriz(row=1) \
                or gameWinHoriz(row=2) \
                or gameWinVert(col=0) \
                or gameWinVert(col=1) \
                or gameWinVert(col=2) \
                or gameWinDiagLeft \
                or gameWinDiagRight:
            return "Yes - Player " + playerIcon + " wins"

        else:
            return None


def gameOverForPlayer(board, playerIcon):
    def gameWinHoriz(row):
        return (board[row][0] == playerIcon and board[row][1] == playerIcon and board[row][2] == playerIcon)

    def gameWinVert(col):
        print(board)
        return (board[0][col] == playerIcon and board[1][col] == playerIcon and board[2][col] == playerIcon)

    gameWinDiagLeft = board[0][0] == playerIcon and board[1][1] == playerIcon and board[2][2] == playerIcon
    gameWinDiagRight = board[0][2] == playerIcon and board[1][1] == playerIcon and board[2][0] == playerIcon

    if gameWinHoriz(row=0) \
            or gameWinHoriz(row=1) \
            or gameWinHoriz(row=2) \
            or gameWinVert(col=0) \
            or gameWinVert(col=1) \
            or gameWinVert(col=2) \
            or gameWinDiagLeft \
            or gameWinDiagRight:
        return "Yes - Player " + playerIcon + " wins"

    else:
        return None


def detectGameOver(board):

    playerXWins = TicTacToeWinner(board, "X").gameOverForPlayer()
    #playerXWins = gameOverForPlayer(board, "X")
    #playerOWins = gameOverForPlayer(board, "O")

    if playerXWins:
        return playerXWins
    elif playerOWins:
        return playerOWins
    else:
        return "No"
