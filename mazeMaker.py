import random

# 1. every cell must "connect" to another cell, above, below, or side to side
# 2. a cell direction must be random
# 3. the path can go in all 4 directions
# 4. cells cannot "cross" each other
# 5. cells cannot leave the board


def makeEmptyBoard(size):
    board = []
    for _ in range(size):
        board.append(list(range(size)))
    return board

# x x x x x
# x x - - x
# x - - - x
# x x x x x


def cellFilled(board, row, column):
    maxSize = len(board)
    if (row < 0):
        return True
    if (column < 0):
        return True
    if (row > maxSize-1):
        return True
    if (column > maxSize-1):
        return True
    if (board[row][column] == "x"):
        return True


def generateMaze(pathLength, boardSize):
    board = makeEmptyBoard(boardSize)
    maxIndex = boardSize - 1
    column = 1
    row = 1
    board[1][1] = "x"
    for i in range(pathLength):
        validMoves = []

        # Look ahead!
        if row > 0 \
                and (not cellFilled(board, row - 1, column)) \
                and (not cellFilled(board, row - 2, column)) \
                and (not cellFilled(board, row - 1, column - 1)) \
                and (not cellFilled(board, row - 1, column + 1)):
            validMoves.append("up")
        if row < maxIndex \
                and (not cellFilled(board, row + 1, column)) \
                and (not cellFilled(board, row + 2, column)) \
                and (not cellFilled(board, row + 1, column - 1)) \
                and (not cellFilled(board, row + 1, column + 1)):
            validMoves.append("down")
        if column > 0 \
                and (not cellFilled(board, row, column - 1)) \
                and (not cellFilled(board, row, column - 2)) \
                and (not cellFilled(board, row - 1, column - 1)) \
                and (not cellFilled(board, row + 1, column - 1)):
            validMoves.append("left")
        if column < maxIndex \
                and (not cellFilled(board, row, column + 1)) \
                and (not cellFilled(board, row, column + 2)) \
                and (not cellFilled(board, row - 1, column + 1)) \
                and (not cellFilled(board, row + 1, column + 1)):
            validMoves.append("right")

        if len(validMoves) == 0:
            validMoves.append("endOfMaze")

        move = random.choice(validMoves)

        if move == "up":
            row -= 1
        if move == "down":
            row += 1
        if move == "left":
            column -= 1
        if move == "right":
            column += 1

        # print("row: " + str(row) + " col: " + str(column))
        board[row][column] = "x"

    return board


def printMaze(pathLength, boardSize):
    populatedMaze = generateMaze(pathLength, boardSize)
    maxIndex = boardSize - 1

    for row, rowList in enumerate(populatedMaze):
        for column, cell in enumerate(rowList):
            if (cell == "x"):
                # end prevents a newline (which is the default)
                print(" x ", end="")
            elif row == 0 and column == 0:
                print(" + ", end="")
            elif row == 0 and column == maxIndex:
                print(" + ", end="")
            elif row == maxIndex and column == maxIndex:
                print(" + ", end="")
            elif row == maxIndex and column == 0:
                print(" + ", end="")
            elif row == 0 or row == maxIndex:
                print(" - ", end="")

            elif column == 0 or column == maxIndex:
                print(" | ", end="")
            else:
                print("   ", end="")

        print("")


printMaze(60, 20)
