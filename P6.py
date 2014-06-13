# ==============================================================================
print ("Project Euler - Problem 6\n\n")
# ==============================================================================
# Description:
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural 
# numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred 
# natural numbers and the square of the sum.
# ==============================================================================
import time
import math

start_time = time.time()
result = 0
# ***** BEGIN CODE FOR P6.py *****

i = 100
sqr_sum = 0
sum_sqr = 0

while (i > 0):
    sum_sqr += math.pow(i,2)
    sqr_sum += i
    i -= 1

sqr_sum = math.pow(sqr_sum,2)

result = int(sqr_sum - sum_sqr)

# ***** END CODE FOR P6.py *****
print ("Result is: ", result)
print ("Run time: " + str((time.time() - start_time)) + " seconds")
# END P6.py
