# ==============================================================================
print ("Project Euler - Problem 19\n\n")
# ==============================================================================
# Description:
# You are given the following information, but you may prefer to do some
# research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June, and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century
# unless evenly divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century
# (1 Jan 1901 to 31 Dec 2000)?
# ==============================================================================
import time
import math

start_time = time.time()
result = 0
# ***** BEGIN CODE FOR P19.py *****

# First Sunday
day = 6
month = 1
year = 1901

while (year < 2001):
    # Check next Sunday
    day += 7

    if (month == 2):
        if not(year % 4):
            if (day > 29):
                day -= 29
                month += 1
        else:
            if (day > 28):
                day -= 28
                month += 1

    elif (month == 12):
        if (day > 31):
            day -= 31
            month = 1
            year += 1

    elif (month == 4) or (month == 6) or (month == 9) or (month == 11):
        if (day > 30):
            day -= 30
            month += 1

    else:
        if (day > 31):
            day -= 31
            month += 1

    if (day == 1):
        result += 1
#        print ("Found 1st Sunday: ", month, day, year)


# ***** END CODE FOR P19.py *****
print ("Result is: ", result)
print ("Run time:   %.5f seconds" % (time.time() - start_time))
# END P19.py
