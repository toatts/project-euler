# ==============================================================================
print ("=============================")
print ("Project Euler - Problem 33")
print ("=============================")
# ==============================================================================
# Description:
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
# attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
# correct, is obtained by cancelling the 9s.
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# There are exactly four non-trivial examples of this type of fraction, less
# than one in value, and containing two digits in the numerator and denominator.
# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.
# ==============================================================================
import time
import math

result = 0
start_time = time.time()
# ***** BEGIN CODE FOR P33.py *****

from pe_library import *
from fractions import Fraction

MAX_RANGE = 100

den_digits = []
num_digits = []
ans_den = 1
ans_num = 1

for denominator in range(10, MAX_RANGE):
    den_digits = digitizer(denominator)
    if (listContains(den_digits, 0)):
        continue

    for numerator in range(10, MAX_RANGE):
        if ((numerator/denominator) >= 1):
            break

        num_digits = digitizer(numerator)
        if (listContains(num_digits, 0)):
            continue
        elif (len(set(num_digits) & set(den_digits))):
            for n in num_digits:
                if n in den_digits:
                    num_digits.remove(n)
                    den_digits.remove(n)
                    if ((numerator/denominator) == (num_digits[0]/den_digits[0])):
                        ans_num *= num_digits[0]
                        ans_den *= den_digits[0]
                    den_digits.append(n)
                    break
print (ans_num, ans_den)
result = Fraction(ans_num/ans_den).limit_denominator()

# ***** END CODE FOR P33.py *****
run_time = time.time() - start_time
print ("Result is: ", result)
print ("Run time:   %.5f seconds" % run_time)
# END P33.py
