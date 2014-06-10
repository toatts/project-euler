# ==============================================================================
print ("Project Euler - Problem 9\n\n")
# ==============================================================================
# Description:
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# ==============================================================================
import time
import math

start_time = time.time()
result = 0
# ***** BEGIN CODE FOR P9.py *****

a = 0
b = 0
c = 0

# TODO make this go to 332
for a in range(1,332):
    for b in range(a+1, a+332):
        c = math.sqrt( (math.pow(a,2) + math.pow(b,2)) )
        if (c.is_integer() and (a+b+c == 1000)):
            # print (a, b, c)
            result = a * b * c
            break
 

# ***** END CODE FOR P9.py *****
print ("Result is: ", result)
print ("Run time: " + str((time.time() - start_time)) + " seconds")
# END P9.py
