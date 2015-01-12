# ==============================================================================
print ("=============================")
print ("Project Euler - Problem 32")
print ("=============================")
# ==============================================================================
# Description:
# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
# through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing
# multiplicand, multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only
# include it once in your sum.
# ==============================================================================
import time
import math

result = 0
start_time = time.time()
# ***** BEGIN CODE FOR P32.py *****

from pe_library import digitizer, listDuplicates

def zeros(digits):
    for digit in digits:
        if (digit):
            continue
        else:
            return True
    return False

MAX_RANGE = 5000

multiplicand_digits = []
multiplier_digits   = []
product_digits      = []
all_digits          = []
num_digits          = 0
results             = []

for multiplicand in range(1, MAX_RANGE+1):
    multiplicand_digits = digitizer(multiplicand)
    if (listDuplicates(multiplicand_digits) or zeros(multiplicand_digits)):
        continue
    for multiplier in range(1, MAX_RANGE+1):
        multiplier_digits = digitizer(multiplier)
        if (listDuplicates(multiplier_digits) or zeros(multiplier_digits)):
            continue
        num_digits = len(multiplicand_digits) + len(multiplier_digits)
        if (num_digits < 6):
            product = multiplicand * multiplier
            product_digits = digitizer(product)
            num_digits += len(product_digits)
            if (num_digits == 9):
                all_digits = multiplicand_digits + multiplier_digits + product_digits
                if (listDuplicates(all_digits) or zeros(all_digits)):
                    continue
                else:
                    results.append(product)
#                    print ("Solution:", multiplicand, multiplier, product)
            elif (num_digits > 9):
                break

result = sum(set(results))

# ***** END CODE FOR P32.py *****
run_time = time.time() - start_time
print ("Result is: ", result)
print ("Run time:   %.5f seconds" % run_time)
# END P32.py
