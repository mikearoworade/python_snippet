# Months with their respective days
month_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isleap(year):
    """Return true if it is a leap year, otherwise, false."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """get days in month"""
    if not 1 <= month <= 12:
        return 'invalid month'

    if isleap(year) and month == 2:
        return 29

    return month_day[month]


print(days_in_month(2022, 2))
