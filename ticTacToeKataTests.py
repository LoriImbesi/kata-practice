from ticTacToeKata import makeEmptyBoard, playerXMove, playerOMove, detectGameOver
import unittest

import ticTacToeKata


class TestTicTacToeKata(unittest.TestCase):

    def test_ticTacToe_gameOver_tieNoWinner(self):
        board = [["X", "O", "O"],
                 ["O", "X", "X"],
                 ["X", "O", "O"]]
        isGameOver = detectGameOver(board)

        self.assertEqual("Tie - no winner", isGameOver)

    def test_ticTacToe_gameOver_PlayerXWinsRow3(self):
        board = [["", "", "X"],
                 ["", "", "X"],
                 ["", "", "X"]]
        isGameOver = detectGameOver(board)

        self.assertEqual("Yes - Player X wins", isGameOver)

    def test_ticTacToe_gameOver_PlayerXWinsRow2(self):
        board = [["", "X", ""],
                 ["", "X", ""],
                 ["", "X", ""]]
        isGameOver = detectGameOver(board)

        self.assertEqual("Yes - Player X wins", isGameOver)

    def test_ticTacToe_gameOver_PlayerXWinsRow1(self):
        board = [["X", "", ""],
                 ["X", "", ""],
                 ["X", "", ""]]
        isGameOver = detectGameOver(board)

        self.assertEqual("Yes - Player X wins", isGameOver)

    def test_ticTacToe_gameOver_PlayerXWinsCol1(self):
        board = [["X", "X", "X"],
                 ["", "", ""],
                 ["", "", ""]]
        isGameOver = detectGameOver(board)

        self.assertEqual("Yes - Player X wins", isGameOver)

    def test_ticTacToe_gameOver_PlayerXWinsCol2(self):
        board = [["", "", ""],
                 ["X", "X", "X"],
                 ["", "", ""]]
        isGameOver = detectGameOver(board)

        self.assertEqual("Yes - Player X wins", isGameOver)

    def test_ticTacToe_gameOver_PlayerXWinsCol3(self):
        board = [["", "", ""],
                 ["", "", ""],
                 ["X", "X", "X"]]
        isGameOver = detectGameOver(board)

        self.assertEqual("Yes - Player X wins", isGameOver)

    def test_ticTacToe_gameOver_PlayerXWinsTopLeftDiag(self):
        board = [["X", "", ""],
                 ["", "X", ""],
                 ["", "", "X"]]
        isGameOver = detectGameOver(board)

        self.assertEqual("Yes - Player X wins", isGameOver)

    def test_ticTacToe_gameOver_PlayerXWinsTopRightDiag(self):
        board = [["", "", "X"],
                 ["", "X", ""],
                 ["X", "", ""]]
        isGameOver = detectGameOver(board)

        self.assertEqual("Yes - Player X wins", isGameOver)

    def test_ticTacToe_gameOver_PlayerXWins(self):
        board = makeEmptyBoard()

        updatedBoard = playerXMove(board, 0, 0)
        updatedBoard = playerXMove(board, 1, 0)
        updatedBoard = playerXMove(board, 2, 0)

        isGameOver = detectGameOver(updatedBoard)

        self.assertEqual("Yes - Player X wins", isGameOver)

    def test_ticTacToe_gameOver_PlayerOWinsRow3(self):
        board = [["", "", "O"],
                 ["", "", "O"],
                 ["", "", "O"]]
        isGameOver = detectGameOver(board)

        self.assertEqual("Yes - Player O wins", isGameOver)

    def test_ticTacToe_gameOver_PlayerOWinsRow2(self):
        board = [["", "O", ""],
                 ["", "O", ""],
                 ["", "O", ""]]
        isGameOver = detectGameOver(board)

        self.assertEqual("Yes - Player O wins", isGameOver)

    def test_ticTacToe_gameOver_PlayerOWinsRow1(self):
        board = [["O", "", ""],
                 ["O", "", ""],
                 ["O", "", ""]]
        isGameOver = detectGameOver(board)

        self.assertEqual("Yes - Player O wins", isGameOver)

    def test_ticTacToe_gameOver_PlayerOWinsCol1(self):
        board = [["O", "O", "O"],
                 ["", "", ""],
                 ["", "", ""]]
        isGameOver = detectGameOver(board)

        self.assertEqual("Yes - Player O wins", isGameOver)

    def test_ticTacToe_gameOver_PlayerOWinsCol2(self):
        board = [["", "", ""],
                 ["O", "O", "O"],
                 ["", "", ""]]
        isGameOver = detectGameOver(board)

        self.assertEqual("Yes - Player O wins", isGameOver)

    def test_ticTacToe_gameOver_PlayerOWinsCol3(self):
        board = [["", "", ""],
                 ["", "", ""],
                 ["O", "O", "O"]]
        isGameOver = detectGameOver(board)

        self.assertEqual("Yes - Player O wins", isGameOver)

    def test_ticTacToe_gameOver_PlayerOWinsTopLeftDiag(self):
        board = [["O", "", ""],
                 ["", "O", ""],
                 ["", "", "O"]]
        isGameOver = detectGameOver(board)

        self.assertEqual("Yes - Player O wins", isGameOver)

    def test_ticTacToe_gameOver_PlayerOWinsTopRightDiag(self):
        board = [["", "", "O"],
                 ["", "O", ""],
                 ["O", "", ""]]
        isGameOver = detectGameOver(board)

        self.assertEqual("Yes - Player O wins", isGameOver)

    # def test_ticTacToe_gameOver_PlayerOWins(self):
    #     board = makeEmptyBoard()

    #     updatedBoard = playerOMove(board, 0, 0)
    #     updatedBoard = playerOMove(board, 1, 0)
    #     updatedBoard = playerOMove(board, 2, 0)

    #     isGameOver = detectGameOver(updatedBoard)

    #     self.assertEqual("Yes - Player O wins", isGameOver)

    def test_ticTacToe_gameOver_no(self):
        board = makeEmptyBoard()

        updatedBoard = playerXMove(board, 1, 0)
        updatedBoard = playerOMove(updatedBoard, 1, 1)

        isGameOver = detectGameOver(updatedBoard)

        self.assertEqual("No", isGameOver)

    def test_ticTacToe_playerOne_firstMove(self):
        board = makeEmptyBoard()

        updatedBoard = playerXMove(board, 1, 0)
        updatedBoard = playerOMove(updatedBoard, 1, 1)

        self.assertEqual("X", updatedBoard[1][0])
        self.assertEqual("O", updatedBoard[1][1])

    def test_ticTacToe_emptyboard(self):
        board = makeEmptyBoard()

        self.assertEqual("", board[2][2])
        self.assertEqual("", board[0][0])


if __name__ == '__main__':
    unittest.main()
