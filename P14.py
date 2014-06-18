# ==============================================================================
print ("Project Euler - Problem 14\n\n")
# ==============================================================================
# Description:
# The following iterative sequence is defined for the set of positive integers:
#
# n -> n/2    if n is even
# n -> 3n+1   if n is odd
#
# Using the rule above and starting with 13, we generate the following
# sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#
# This sequence (starting at 13 and finishing at 1) contains 10 terms. Although
# it has not been proved yet (Collatz Problem), it is thought that all starting
# numbers finish at 1. Which starting number, under one million, produces the
# longest chain? Note: Once the chain starts the terms are allowed to go above
# one million.
# ==============================================================================
import time
import math

start_time = time.time()
result = 0
# ***** BEGIN CODE FOR P14.py *****

MAX_LENGTH = 1000000

def collatz(n, computed_values):
    count = 0
    while True:
        # Beyond cached list
        if (n >= len(computed_values)):
            count += 1
            # Even n = n/2
            if ((n % 2) == 0):
                n /= 2
            # Odd n = 3n+1
            else:
                n = 3*n + 1
        # No match in table
        elif (computed_values[int(n)] == 0):
            count += 1
            # Even n = n/2
            if ((n % 2) == 0):
                n /= 2
            # Odd n = 3n+1
            else:
                n = 3*n + 1
        # Found match in list
        else:
            return (computed_values[int(n)] + count)

cur_chain = 0
max_chain = 0
computed_values = [0] * MAX_LENGTH
computed_values[0] = 1
computed_values[1] = 1

for i in range(MAX_LENGTH):
    cur_chain = collatz(i, computed_values)
    computed_values[i] = cur_chain
    if (cur_chain > max_chain):
        result = i
        max_chain = cur_chain

# ***** END CODE FOR P14.py *****
print ("Result is: ", result)
print ("Run time:   " + str((time.time() - start_time)) + " seconds")
# END P14.py

