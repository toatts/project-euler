# ==============================================================================
print ("=============================")
print ("Project Euler - Problem 35")
print ("=============================")
# ==============================================================================
# Description:
# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
# 73, 79, and 97.
# How many circular primes are there below one million?
# ==============================================================================
import time
from pe_library import *

result = 0
start_time = time.time()
# ***** BEGIN CODE FOR P35.py *****

digits = []

MAX_RANGE = 1000000

for i in range(1, MAX_RANGE+1):
    circular = True
    if (isPrime(i)):
        digits = digitizer(i, True)
        if (len(digits) > 1):
            for digit in digits:
                if not(digit % 2):
                    circular = False
                    #print ("NO1")
                    break
        if circular:
            for j in range(1, len(digits)):
                #digits, rotated_num = rotateList(digits)
                rotated_num = numerizer(digits)
                digits = rotateList(digits, 1)

                #print (digits, rotated_num)
                if (not isPrime(rotated_num)):
                    #print ("NO2")
                    circular = False
                    break
    else:
        circular = False

    if circular:
        result += 1

# ***** END CODE FOR P35.py *****
run_time = time.time() - start_time
print ("Result is: ", result)
print ("Run time:   %.5f seconds" % run_time)
# END P35.py
