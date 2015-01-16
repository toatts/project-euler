# ==============================================================================
print ("=============================")
print ("Project Euler - Problem 34")
print ("=============================")
# ==============================================================================
# Description:
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of
# their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
# ==============================================================================
import time
import math

result = 0
start_time = time.time()
# ***** BEGIN CODE FOR P34.py *****

from pe_library import *

MAX_RANGE = boundChecker()
FACTORIALS = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

digits = []

for i in range(10, MAX_RANGE):
    digits = digitizer(i)
    fact_sum = 0

    for digit in digits:
        fact_sum += FACTORIALS[digit]
        if (fact_sum > i):
            break
    if (fact_sum == i):
        result += fact_sum

# ***** END CODE FOR P34.py *****
run_time = time.time() - start_time
print ("Result is: ", result)
print ("Run time:   %.5f seconds" % run_time)
# END P34.py
