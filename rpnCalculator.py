
def isOperator(input):
    return input == "/" or input == "*" or input == "+" or input == "-"


# space: O(1)
# result = [1, 2, 3]
# result = [6, 2, 3]
# result = [6, 7, 3]
# result = [6, 7, 8]
def mapAdd5Loop(list):
    for index, number in enumerate(list):
        list[index] = number+5
    return list

# space: O(N)
# mapAdd5([1,2,3])
# =>
# [6] + mapAdd5([2,3])
# [6] + [7] + mapAdd5([3])
# [6] + [7] + [8] + mapAdd5([])
# [6] + ([7] + ([8] + []))
# [6] + ([7] + [8])
# [6] + [7, 8]
# [6, 7, 8]

# mapAdd5([1,2,3])


def mapAdd5(list):
    if (len(list) > 0):
        firstPlus5 = list[0] + 5
        rest = list[1:]
        return [firstPlus5] + mapAdd5(rest)
    return []


def rpnCalculateList(stringValues):
    for index, string in enumerate(stringValues):
        isOp = isOperator(string)
        if isOp == True:
            e2 = stringValues[index-1]
            e1 = stringValues[index-2]
            result = calculate(e1, e2, string)
            if len(stringValues) > 3:
                # ["4",  "2", "+", "3", "-"]
                # ["6", "3", "-"]
                # ["3", "-"]

                # ["3", "5", "8", "*", "7", "+", "*"]
                # 3, 40, 7, +, *
                # 3, 47, *
                # 141

                uncalculatedValues = stringValues[3:]
                print(uncalculatedValues)
                uncalculatedValues.insert(0, str(result))  # ["6", "3", "-"]
                print(uncalculatedValues)
                return rpnCalculateList(uncalculatedValues)
            else:
                return result


def rpnCalculate(input):
    stringValues = input.split(' ')
    return rpnCalculateList(stringValues)


def calculate(e1, e2, operator):
    if operator == "/":
        return int(e1) / int(e2)
    elif operator == "*":
        return int(e1) * int(e2)
    elif operator == "+":
        return int(e1) + int(e2)
    elif operator == "-":
        return int(e1) - int(e2)
