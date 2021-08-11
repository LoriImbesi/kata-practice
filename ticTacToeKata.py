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

# example = TicTacToeWinner(board, "X")
# print(example.board)
# print(example.playerIcon)

    # def gameWinHoriz(row):
    #     return (board[row][0] == playerIcon and board[row][1] == playerIcon and board[row][2] == playerIcon)

    def gameWinHoriz(self, row):
        return (self.board[row][0] == self.playerIcon and self.board[row][1] == self.playerIcon and self.board[row][2] == self.playerIcon)

    def gameWinVert(self, col):
        return (self.board[0][col] == self.playerIcon and self.board[1][col] == self.playerIcon and self.board[2][col] == self.playerIcon)

    def gameOverForPlayer(self):
        gameWinDiagLeft = self.board[0][0] == self.playerIcon and self.board[
            1][1] == self.playerIcon and self.board[2][2] == self.playerIcon
        gameWinDiagRight = self.board[0][2] == self.playerIcon and self.board[
            1][1] == self.playerIcon and self.board[2][0] == self.playerIcon

        if self.gameWinHoriz(row=0) \
                or self.gameWinHoriz(row=1) \
                or self.gameWinHoriz(row=2) \
                or self.gameWinVert(col=0) \
                or self.gameWinVert(col=1) \
                or self.gameWinVert(col=2) \
                or gameWinDiagLeft \
                or gameWinDiagRight:
            return "Yes - Player " + self.playerIcon + " wins"

        else:
            return None

    def tieNoWinnerAlt1(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "":
                    return None

        return "Tie - no winner"

    def tieNoWinner(self):
        isTie = True

        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "":
                    isTie = False

        if isTie:
            return "Tie - no winner"
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
    playerOWins = TicTacToeWinner(board, "O").gameOverForPlayer()
    tieNoWinner = TicTacToeWinner(board, "").tieNoWinner()

    #playerXWins = gameOverForPlayer(board, "X")
    #playerOWins = gameOverForPlayer(board, "O")

    if playerXWins:
        return playerXWins
    elif playerOWins:
        return playerOWins
    elif tieNoWinner:
        return tieNoWinner
    else:
        return "No"
