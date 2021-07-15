#! python3


class TennisGame:
    def __init__(self, player1Score, player2Score):
        self.player1Score = player1Score
        self.player2Score = player2Score

    def printCurrentScore(self):
        scores = {0: "0", 1: "15"}
        player1Score = scores[self.player1Score]
        player2Score = scores[self.player2Score]
        return (player1Score) + " - " + (player2Score)

    def playerOneScored(self):
        self.player1Score += 1

    def playerTwoScored(self):
        self.player2Score += 1
