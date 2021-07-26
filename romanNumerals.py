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
