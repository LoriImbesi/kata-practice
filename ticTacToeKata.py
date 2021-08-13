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

    def __init__(self, board):
        self.board = board

    def gameWinHoriz(self):
        players = ["X", "O"]
        for row in range(3):
            for player in players:
                if self.board[row][0] == player and self.board[row][1] == player and self.board[row][2] == player:
                    return "Player " + player + " wins"

    def gameWinVert(self, col):
        return (self.board[0][col] == self.playerIcon and self.board[1][col] == self.playerIcon and self.board[2][col] == self.playerIcon)

    def gameOverForPlayer(self):

        gameWinDiagLeft = self.board[0][0] == self.playerIcon and self.board[
            1][1] == self.playerIcon and self.board[2][2] == self.playerIcon
        gameWinDiagRight = self.board[0][2] == self.playerIcon and self.board[
            1][1] == self.playerIcon and self.board[2][0] == self.playerIcon

        if self.gameWinHoriz() \
                or self.gameWinVert(col=0) \
                or self.gameWinVert(col=1) \
                or self.gameWinVert(col=2) \
                or gameWinDiagLeft \
                or gameWinDiagRight:
            return "Yes - Player " + self.playerIcon + " wins"

        else:
            return None

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


def detectGameOver(board):
    playerWins = TicTacToeWinner(board).gameOverForPlayer()
    tieNoWinner = TicTacToeWinner(board).tieNoWinner()

    if playerWins:
        return playerWins
    elif tieNoWinner:
        return tieNoWinner
    else:
        return "No"
