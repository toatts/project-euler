# ==============================================================================
print ("Project Euler - Problem 15\n\n")
# ==============================================================================
# Description:
# Starting in the top left corner of a 2 x 2 grid and moving only down and
# right, there are 6 route to the bottom right corner.
#     __ __   1 __ __ 2 __    3 __    4        5       6
#    |__|__|         |    |__     |     |__ __  |__     |
#    |__|__|         |       |    |__         |    |__  |__ __
#
# How many routes are there through a 20 x 20 grid?
# ==============================================================================
import time
import math

start_time = time.time()
result = 0
# ***** BEGIN CODE FOR P15.py *****

# TODO: should always be an even number due to symmetry?

# ***** END CODE FOR P15.py *****
print ("Result is: ", result)
print ("Run time:   " + str((time.time() - start_time)) + " seconds")
# END P15.py

