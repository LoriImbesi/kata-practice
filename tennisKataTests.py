import unittest
from tennisKata import TennisGame
from unittest import suite


class TestTennisKata(unittest.TestCase):

    def test_tennisGame(self):
        game = TennisGame(0, 0)
        currentScore = game.printCurrentScore()
        self.assertEqual("0 - 0", currentScore)

    def test_tennisGamePlayerOneScores(self):
        game = TennisGame(0, 0)
        game.playerOneScored()
        currentScore = game.printCurrentScore()
        self.assertEqual("15 - 0", currentScore)

    def test_tennisGamePlayerTwoScores(self):
        game = TennisGame(0, 0)
        game.playerTwoScored()
        currentScore = game.printCurrentScore()
        self.assertEqual("0 - 15", currentScore)

    def test_tennisGameBothScore(self):
        game = TennisGame(0, 0)
        game.playerOneScored()
        game.playerTwoScored()
        currentScore = game.printCurrentScore()
        self.assertEqual("15 - 15", currentScore)

    def test_tennisGameBothScore1(self):
        game = TennisGame(0, 0)
        game.playerOneScored()
        game.playerTwoScored()
        game.playerTwoScored()
        currentScore = game.printCurrentScore()
        self.assertEqual("15 - 30", currentScore)

    def test_tennisGameBothScore3(self):
        game = TennisGame(3, 3)
        currentScore = game.printCurrentScore()
        self.assertEqual("deuce", currentScore)

    def test_tennisGameBothScore3(self):
        game1 = TennisGame(0, 0)
        game2 = TennisGame(0, 0)

        game1.playerOneScored()
        game2.playerTwoScored()

        currentScoreGame1 = game1.printCurrentScore()
        currentScoreGame2 = game2.printCurrentScore()
        self.assertEqual("15 - 0", currentScoreGame1)
        self.assertEqual("0 - 15", currentScoreGame2)

    def test_tennisGameBothScore2(self):
        game = TennisGame(0, 0)
        game.playerOneScored()
        game.playerTwoScored()
        game.playerOneScored()
        game.playerTwoScored()
        game.playerOneScored()
        game.playerTwoScored()
        currentScore = game.printCurrentScore()
        self.assertEqual("deuce", currentScore)

    def test_tennisGameBothScore4(self):
        game = TennisGame(4, 3)
        currentScore = game.printCurrentScore()
        self.assertEqual("advantage: player1", currentScore)

    def test_tennisGameBothScore5(self):
        game = TennisGame(4, 5)
        currentScore = game.printCurrentScore()
        self.assertEqual("advantage: player2", currentScore)

    # def test_score(self):
        # self.assertEqual("0 - 0", currentScore(0, 0))
        # self.assertEqual("15 - 0", currentScore(1, 0))
        # self.assertEqual("0 - 15", currentScore(0, 1))
        # self.assertEqual("15 - 15", currentScore(1, 1))
        # self.assertEqual("30 - 0", currentScore(2, 0))
        # self.assertEqual("0 - 30", currentScore(0, 2))
        # self.assertEqual("15 - 15", currentScore(1, 1))
        # self.assertEqual("30 - 30", currentScore(2, 2))
        # self.assertEqual("40 - 0", currentScore(3, 0))
        # self.assertEqual("0 - 40", currentScore(0, 3))
        # self.assertEqual("40 - 30", currentScore(3, 2))
        # self.assertEqual("deuce", currentScore(3, 3))
        # self.assertEqual("deuce", currentScore(4, 4))
        # self.assertEqual("deuce", currentScore(5, 5))
        # self.assertEqual("advantage: player1", currentScore(4, 3))
        # self.assertEqual("advantage: player1", currentScore(5, 4))
        # self.assertEqual("advantage: player2", currentScore(3, 4))
        # self.assertEqual("advantage: player2", currentScore(4, 5))
        # self.assertEqual("winner: player1", currentScore(5, 3))
        # self.assertEqual("winner: player1", currentScore(6, 4))
        # self.assertEqual("winner: player1", currentScore(7, 5))
        # self.assertEqual("winner: player2", currentScore(3, 5))
        # self.assertEqual("winner: player2", currentScore(4, 6))
        # self.assertEqual("winner: player2", currentScore(5, 7))


if __name__ == '__main__':
    unittest.main()

# score(0, 0) => "0 - 0"
# score(1, 1) => "15 - 15"
# score(1, 0) => "15 - 0"
# score(2, 0) => "30 - 0"
# score(3, 0) => "40 - 0"
# score(3, 2) => "40 - 30"
# score(3, 3) => "deuce"
# score(4, 0) => "player one wins"
# score(4, 4) => "deuce"
