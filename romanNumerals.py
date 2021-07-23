arabicToRomanNums = {1: "I", 5: "V", 10: "X",
                     50: "L", 100: "C", 500: "D", 1000: "M"}


def arabicToRoman(arabicNumber):
    romanNumeral = ""

    while arabicNumber > 0:
        if arabicNumber < 5:
            romanNumeral += arabicToRomanNums[1]
            arabicNumber -= 1
        elif arabicNumber < 10:
            romanNumeral = arabicToRomanNums[5]
            arabicNumber -= 5
        elif arabicNumber < 50:
            romanNumeral = arabicToRomanNums[10]
            arabicNumber -= 10
        elif arabicNumber < 100:
            romanNumeral = arabicToRomanNums[50]
            arabicNumber -= 50
        elif arabicNumber < 500:
            romanNumeral = arabicToRomanNums[100]
            arabicNumber -= 100
    print(romanNumeral)
    return romanNumeral


def arabicPlaceValues(arabicNumber):

    numPlaceVal = []

    # break arabic number into place values and pull and
    # concat values from dict

    # if arabicNum 1 - 3 concat "I"
    # if arabicNum 4 - 8 concat "IV"
    # if arabicNum 9,11 - 13 concat "IX"
    # if arabicNum 14 - 18 concat "IVX"
    # if arabicNum 19 - 23 concat "IX"
    # if arabicNum 24 - 28 concat "IVX"

    # 40 introduces "L" 40 = "XL"
    # 90 introduces "C" 90 = "XC"
    # 400 introduces "D" 400 = CD
    # 900 introduces "M"  900 = "CM"
    # 1001 = "MI"
    # upper limit: 3000
