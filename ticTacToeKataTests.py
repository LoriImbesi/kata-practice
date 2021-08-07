from ticTacToeKata import gameBoardStatus
import unittest

import ticTacToeKata


class TestTicTacToeKata(unittest.TestCase):

    def test_ticTacToe_playerOne_firstMove(self):
        self.assertEqual("x", currentMove("3"))


if __name__ == '__main__':
    unittest.main()
