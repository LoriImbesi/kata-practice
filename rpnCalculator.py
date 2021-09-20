

def rpnCalculate(input):
    stringValues = input.split(' ')

    pointerIndex = 0
    currentNumber = int(stringValues[0])
    while (pointerIndex + 1) < len(stringValues):
        nextNumber = stringValues[pointerIndex + 1]
        nextOperator = stringValues[pointerIndex + 2]

        if nextOperator == "/":
            currentNumber = currentNumber / int(nextNumber)
        elif nextOperator == "*":
            currentNumber = currentNumber * int(nextNumber)
        elif nextOperator == "+":
            currentNumber = currentNumber + int(nextNumber)
        elif nextOperator == "-":
            currentNumber = currentNumber - int(nextNumber)
        pointerIndex = pointerIndex + 2

    return int(currentNumber)
