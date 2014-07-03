# ==============================================================================
print ("Project Euler - Problem 24\n\n")
# ==============================================================================
# Description:
# A permutation is an ordered arrangement of objects. For example, 3124 is one
# possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
# are listed numerically or alphabetically, we call it lexicographic order. The
# lexicographic permutations of 0, 1 and 2 are:
# 012 021 102 120 201 210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4,
# 5, 6, 7, 8 and 9?
# ==============================================================================
import time
import math

start_time = time.time()
result = 0
# ***** BEGIN CODE FOR P24.py *****

import itertools

DIGITS = [0,1,2,3,4,5,6,7,8,9]

result_list = list(itertools.permutations(DIGITS))

result = result_list[999999]

# ***** END CODE FOR P24.py *****
print ("Result is: ", result)
print ("Run time:   %.5f seconds" % (time.time() - start_time))
# END P24.py
