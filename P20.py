# ==============================================================================
print ("Project Euler - Problem 20\n\n")
# ==============================================================================
# Description:
# n! means n * (n - 1) * ... * 3 * 2 * 1
# For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800 and the sum of the
# digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!
# ==============================================================================
import time
import math

start_time = time.time()
result = 0
# ***** BEGIN CODE FOR P20.py *****

def factorial(n):
    if (n == 1):
        return 1
    else:
        return (n * factorial(n-1))

str_ans = str(factorial(100))
for i in range(len(str_ans)):
    result += int(str_ans[i])

# ***** END CODE FOR P20.py *****
print ("Result is: ", result)
print ("Run time:   %.5f seconds" % (time.time() - start_time))
# END P20.py
