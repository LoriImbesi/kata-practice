import unittest
from tennisKataDict import makeGameState, printCurrentScore, playerOneScored, playerTwoScored
from unittest import suite


class TestTennisKataDict(unittest.TestCase):

    def test_tennisGame_0_0(self):
        game = makeGameState(0, 0)
        currentScore = printCurrentScore(game)
        self.assertEqual("0 - 0", currentScore)

    def test_tennisGame_1_0(self):
        game = makeGameState(0, 0)
        game1 = playerOneScored(game)
        currentScore = printCurrentScore(game1)
        self.assertEqual("15 - 0", currentScore)

    def test_tennisGame_1_1(self):
        game = makeGameState(0, 0)
        game1 = playerOneScored(game)
        game2 = playerTwoScored(game1)
        currentScore = printCurrentScore(game2)
        self.assertEqual("15 - 15", currentScore)

    def test_tennisGame_2_2(self):
        game = makeGameState(0, 0)
        game = playerOneScored(game)
        game = playerTwoScored(game)
        game = playerOneScored(game)
        game = playerTwoScored(game)
        currentScore = printCurrentScore(game)
        self.assertEqual("30 - 30", currentScore)

    def test_tennisGame_3_3(self):
        game = makeGameState(0, 0)
        game = playerOneScored(game)
        game = playerTwoScored(game)
        game = playerOneScored(game)
        game = playerTwoScored(game)
        game = playerOneScored(game)
        game = playerTwoScored(game)
        currentScore = printCurrentScore(game)
        self.assertEqual("40 - 40", currentScore)


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
