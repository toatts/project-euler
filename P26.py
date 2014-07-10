# ==============================================================================
print ("=============================")
print ("Project Euler - Problem 26")
print ("=============================")
# ==============================================================================
# Description:
# A unit fraction contains 1 in the numerator. The decimal representation of the
# unit fractions with denominators 2 to 10 are given:
# 1/2  = 0.5
# 1/3  = 0.(3)
# 1/4  = 0.25
# 1/5  = 0.2
# 1/6  = 0.1(6)
# 1/7  = 0.(142857)
# 1/8  = 0.125
# 1/9  = 0.(1)
# 1/10 = 0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
# seen that 1/7 has a 6-digit recurring cycle.
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle
# in its decimal fraction part.
# ==============================================================================
import time
import math

start_time = time.time()
result = 0
# ***** BEGIN CODE FOR P26.py *****

def recurringDecimal(numerator, denominator):
    rem = numerator % denominator
    pat_match = []
    dec_count = 0
    numerator *= 10
    # Remainder exists
    while (rem):
        div = int(numerator / denominator)
        # print (numerator, "/", denominator, "Div: ", div, "Rem: ", rem, "Patterns: ", pat_match)

        dec_count += 1
        for i in range(len(pat_match)):
            if pat_match[i] == numerator:
                # print ("Pattern match: DC=", dec_count, "i=", i)
                return (dec_count - i - 1)

        pat_match.append(numerator)
        numerator = (numerator % denominator) * 10
        if (numerator == 0):
            return 0

        rem = numerator % denominator

    return 0

MAX_NUM = 1000
max_length = 0
cur_length = 0

for i in range(1, MAX_NUM):
    cur_length = recurringDecimal(1, i)
    if (cur_length > max_length):
        max_length = cur_length
        result = i

# ***** END CODE FOR P26.py *****
run_time = time.time() - start_time
print ("Result is: ", result)
print ("Run time:   %.5f seconds" % run_time)
# END P26.py
