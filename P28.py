# ==============================================================================
print ("=============================")
print ("Project Euler - Problem 28")
print ("=============================")
# ==============================================================================
# Description:
# Starting with the number 1 and moving to the right in a clockwise direction a
# 5 by 5 spiral is formed as follows:
# 21 22 23 24 25
# 20 7  8  9  10
# 19 6  1  2  11
# 18 5  4  3  12
# 17 16 15 14 13
# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
# formed in the same way?
# ==============================================================================
import time
import math

result = 0
start_time = time.time()
# ***** BEGIN CODE FOR P28.py *****

# Algorithm = 1 + summation_3->n_only_odds(n^2 + (n^2 - n + 1) + (n^2 - 2n + 2) + (n^2 - 3n + 3))
# Simplifies to 1 + summation_3->n_only_odds(4n^2-6n+6)
# Program runs this algorithm for n = 1001

def spiral_diagonals(n):
    if (n == 1):
        return 1
    elif (n % 2):
        return ((4*(n**2))-(6*n)+6) + spiral_diagonals(n-2)
    else:
        print ("Error: Only works for odd numbers")
        return 0

result = spiral_diagonals(1001)

# ***** END CODE FOR P28.py *****
run_time = time.time() - start_time
print ("Result is: ", result)
print ("Run time:   %.5f seconds" % run_time)
# END P28.py
