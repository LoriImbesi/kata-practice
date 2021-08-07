#! python3

# game state - open spots on the board
# state needs to remember what has been played to see who wins or
# if there's a tie

# if there's a value in that spot then it's taken otherwise, it's
# an empty string or null?

# winning sets
# 1,2,3
# 4,5,6
# 7,8,9
# 1,4,7
# 2,5,8
# 3,6,9
# 1,5,9
# 3,5,7


def gameBoardStatus(player1, player2):
    gameState = [["", "", ""],
                 ["", "", ""],
                 ["", "", ""]]
    gameState[0][0]
    gameState[0][1]
    gameState[0][2]

    gameBoard = {1: "", 2: "", 3: "",
                 4: "", 5: "", 6: "",
                 7: "", 8: "", 9: ""}

    return gameBoard
