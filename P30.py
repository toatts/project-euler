# ==============================================================================
print ("=============================")
print ("Project Euler - Problem 30")
print ("=============================")
# ==============================================================================
# Description:
# Surprisingly there are only three numbers that can be written as the sum of
# fourth powers of their digits:
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# Find the sum of all the numbers that can be written as the sum of fifth powers
# of their digits.
# ==============================================================================
import time
import math

result = 0
start_time = time.time()
# ***** BEGIN CODE FOR P30.py *****

def boundChecker(power):
    bound_inc = 9**power
    bounds = bound_inc
    value  = 9
    while (value <= bounds):
        value = (value*10) + 9
        bounds += bound_inc

    return bounds

POWER  = 5
BOUNDS = boundChecker(POWER)

number = 10
answer_list = []

while (number < BOUNDS):
    digits = number
    digit_sum = 0
    loop_cnt = 1
    leading_zero = True

    while (digits):
        digit = digits % 10
        digit_sum += (digit ** POWER)
        if (digit_sum > number):
            break
        digits //= 10
        if ((digit == 0) and leading_zero):
            loop_cnt += 1
        else:
            leading_zero = False
            loop_cnt = 1

    if (digit_sum == number):
        answer_list.append(number)

    if (digit_sum > number):
        number = number - (number % (10**loop_cnt)) + (10**loop_cnt)
    else:
        number += 1

result = sum(answer_list)

# ***** END CODE FOR P30.py *****
run_time = time.time() - start_time
print ("Result is: ", result)
print ("Run time:   %.5f seconds" % run_time)
# END P30.py
