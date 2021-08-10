#! python3

# game state - open spots on the board
# state needs to remember what has been played to see who wins or
# if there's a tie


# winning sets
# 1,2,3
# 4,5,6
# 7,8,9
# 1,4,7
# 2,5,8
# 3,6,9
# 1,5,9
# 3,5,7

# 0 - 0,1,2
# 1 - 0,1,2
# 2 - 0,1,2
# 0,1,2 - 0
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


def detectGameOver(board):
    if board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        return "Yes - Player X wins"
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        return "Yes - Player X wins"
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        return "Yes - Player X wins"
    else:
        return "No"
