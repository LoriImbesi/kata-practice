# input is a year - need to change from string to int
# divide by 400


def isItALeapYear(year):
    year = int(year)
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    return False
