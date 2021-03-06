#! python3
from enum import Enum

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


class PossibleWinner(Enum):
    PlayerXWins = 1
    PlayerOWins = 2
    Neither = 3


class TicTacToeWinner:

    def __init__(self, board):
        self.board = board

    def whoIsPossibleWinner(self, playerIcon):
        if playerIcon == "X":
            return PossibleWinner.PlayerXWins
        if playerIcon == "O":
            return PossibleWinner.PlayerOWins

    def gameWinHoriz(self):
        players = ["X", "O"]
        for row in range(3):
            for playerIcon in players:
                if self.board[row][0] == playerIcon and self.board[row][1] == playerIcon and self.board[row][2] == playerIcon:
                    return self.whoIsPossibleWinner(playerIcon)

        return PossibleWinner.Neither

    def gameWinVert(self):
        players = ["X", "O"]
        for col in range(3):
            for playerIcon in players:
                if self.board[0][col] == playerIcon and self.board[1][col] == playerIcon and self.board[2][col] == playerIcon:
                    return self.whoIsPossibleWinner(playerIcon)

        return PossibleWinner.Neither

    def gameOverForPlayer(self):
        players = ["X", "O"]
        for playerIcon in players:
            if self.board[0][0] == playerIcon and self.board[1][1] == playerIcon and \
                    self.board[2][2] == playerIcon:
                return self.whoIsPossibleWinner(playerIcon)

            if self.board[0][2] == playerIcon and self.board[1][1] == playerIcon and \
                    self.board[2][0] == playerIcon:
                return self.whoIsPossibleWinner(playerIcon)

        gameHorizWon = self.gameWinHoriz()
        if gameHorizWon != PossibleWinner.Neither:
            return gameHorizWon
        gameVertWon = self.gameWinVert()
        if gameVertWon != PossibleWinner.Neither:
            return gameVertWon

        return PossibleWinner.Neither

    # how many possible outputs does this have?
    # what does it have now?
    # what could it be simplified as?

    def tieNoWinner(self):
        isTie = True

        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "":
                    isTie = False
        return isTie


def detectGameOver(board):
    playerWins = TicTacToeWinner(board).gameOverForPlayer()
    tieNoWinner = TicTacToeWinner(board).tieNoWinner()

    if playerWins == PossibleWinner.PlayerXWins:
        return "Yes - Player X wins"
    elif playerWins == PossibleWinner.PlayerOWins:
        return "Yes - Player O wins"
    elif tieNoWinner == True:
        return "Tie - no winner"
    else:
        return "No"
