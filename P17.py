# ==============================================================================
print ("Project Euler - Problem 17\n\n")
# ==============================================================================
# Description:
# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3+3+5+4+4=19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
# words, how many letters would be used?
#
# Note: Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
# letters. The use of "and" when writing out numbers is in compliance with
# British usage.
# ==============================================================================
import time
import math

start_time = time.time()
result = 0
# ***** BEGIN CODE FOR P17.py *****

COUNT = 1000

# 0-19, null zero
SINGLES = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
# 20-99
TEENS   = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]
# 100-999
HUNDRED = 7
AND = 3
# 1000-9999
THOUSAND = 8

def numberLetters(n):
    letters = 0
    # Thousands
    # print (SINGLES[int(n/1000)])
    letters += SINGLES[int(n/1000)]
    if (n > 999):
        # print (THOUSAND)
        letters += THOUSAND
        n %= 1000
    # Hundreds
    # print (SINGLES[int(n/100)])
    letters += SINGLES[int(n/100)]
    if (n > 99):
        # print (HUNDRED)
        letters += HUNDRED
        n %= 100
        if (n):
            # print (AND)
            letters += AND
    if (n < 20):
        # print (SINGLES[n])
        letters += SINGLES[n]
    else:
        # print (TEENS[int(n/10)])
        letters += TEENS[int(n/10)]
        # print (SINGLES[n%10])
        letters += SINGLES[n%10]

    return letters

for i in range(1, COUNT+1):
    result += numberLetters(i)

# ***** END CODE FOR P17.py *****
print ("Result is: ", result)
print ("Run time:   %.5f seconds" % (time.time() - start_time))
# END P17.py
