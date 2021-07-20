#! python3


class TennisGame:
    def __init__(self, player1Score, player2Score):
        self.player1Score = player1Score
        self.player2Score = player2Score

    def printCurrentScore(self):
        scores = {0: "0", 1: "15", 2: "30", 3: "40"}

        if self.player1Score >= 3 and self.player2Score == self.player1Score:
            return "deuce"
        player1ScoreString = scores[self.player1Score]
        player2ScoreString = scores[self.player2Score]

        return (player1ScoreString) + " - " + (player2ScoreString)

    def playerOneScored(self):
        self.player1Score += 1

    def playerTwoScored(self):
        self.player2Score += 1
