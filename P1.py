# ==============================================================================
print ("Project Euler - Problem 1\n\n")
# ==============================================================================
# Description:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we 
# get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# ==============================================================================
import time
import math

start_time = time.time()
result = 0
# ***** BEGIN CODE FOR P1.py *****

for i in range(0, 1000):
    if (((i%3)==0) or ((i%5)==0)):
        result += i

# ***** END CODE FOR P1.py *****
print ("Result is: ", result)
print ("Run time: " + str((time.time() - start_time)) + " seconds\n")
# END P1.py
