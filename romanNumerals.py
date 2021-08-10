arabicToRomanNums = {1: "I", 5: "V", 10: "X",
                     50: "L", 100: "C", 500: "D", 1000: "M"}
romanNumsToArabic = {"I": 1, "V": 5, "X": 10,
                     "L": 50, "C": 100, "D": 500, "M": 1000}


def romanToArabic():
    return 0


def arabicToRoman(arabicNumber):
    romanNumeral = ""

    while arabicNumber > 0:
        if arabicNumber < 4:
            romanNumeral += arabicToRomanNums[1]
            arabicNumber -= 1
        elif arabicNumber == 4:
            romanNumeral += arabicToRomanNums[1]
            romanNumeral += arabicToRomanNums[5]
            arabicNumber -= 4
        elif arabicNumber < 9:
            romanNumeral = arabicToRomanNums[5]
            arabicNumber -= 5
        elif arabicNumber == 9:
            romanNumeral += arabicToRomanNums[1]
            romanNumeral += arabicToRomanNums[10]
            arabicNumber -= 9
        elif arabicNumber < 50:
            romanNumeral = arabicToRomanNums[10]
            arabicNumber -= 10
        elif arabicNumber < 100:
            romanNumeral = arabicToRomanNums[50]
            arabicNumber -= 50
        elif arabicNumber < 500:
            romanNumeral = arabicToRomanNums[100]
            arabicNumber -= 100
        elif arabicNumber < 1000:
            romanNumeral = arabicToRomanNums[500]
            arabicNumber -= 500
        elif arabicNumber < 3000:
            romanNumeral = arabicToRomanNums[1000]
            arabicNumber -= 1000
    return romanNumeral
