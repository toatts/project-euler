# ==============================================================================
print ("=============================")
print ("Project Euler - Problem 26")
print ("=============================")
# ==============================================================================
# Description:
# A unit fraction contains 1 in the numerator. The decimal representation of the
#  unit fractions with denominators 2 to 10 are given:
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be 
# seen that 1/7 has a 6-digit recurring cycle.
# Find the value of d  1000 for which 1/d contains the longest recurring cycle 
# in its decimal fraction part.
# ==============================================================================
import time
import math

start_time = time.time()
result = 0
# ***** BEGIN CODE FOR P26.py *****



# ***** END CODE FOR P26.py *****
run_time = time.time() - start_time
print ("Result is: ", result)
print ("Run time:   %.5f seconds" % run_time)
# END P26.py