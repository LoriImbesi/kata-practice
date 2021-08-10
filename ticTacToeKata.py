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


def detectGameOver(board):
    if board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        return "Yes - Player X wins"
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        return "Yes - Player X wins"
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        return "Yes - Player X wins"
    elif board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
        return "Yes - Player X wins"
    elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
        return "Yes - Player X wins"
    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
        return "Yes - Player X wins"
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        return "Yes - Player X wins"
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        return "Yes - Player X wins"
    else:
        return "No"
