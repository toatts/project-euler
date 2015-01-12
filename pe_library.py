# ==============================================================================
# Project Euler Library
# ==============================================================================
import random

# isPrime: Primality checker
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Miller-Rabin algorithm
# http://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Primality_Testing
# n = integer to be tested for primality
# k = parameter that determines the accuracy of the guess (highest error probability = 4^-k)
# a = random integer in range [2, n-2]
# s = factor of 2 in 2^s * d
# d = n - 1

def isPrime(n, k = 7):
    # Eliminate negatives
    if (n < 0):
        return False
    # Eliminate small numbers
    elif (n < 6):
        return [False, False, True, True, False, True][n]
    # Even numbers (faster than n % 2)
    elif (n & 1 == 0):
        return False
    # Odd numbers
    else:
        s = 0
        d = n - 1
        while (d & 1 == 0):
            s = s + 1
            d = d >> 1
        # Witness Loop: Grab k random integers in range [2, n-2]
        for a in random.sample(range(2, n-2), min(n-4, k)):
            x = pow(a, d, n) # a^d mod n
            if (x != 1) and (x != n - 1):
                for r in range(1, s):
                    x = pow(x, 2, n)
                    if (x == 1):
                        # Definitely composite
                        return False
                    elif (x == n - 1):
                        a = 0 # so we know loop didn't continue to end
                        break # could be a strong liar, try another a
                if a:
                    # Composite if we reached the end of the loop
                    return False
        # Probably true if it passed everything else
        return True

# digitizer: Create list of digits in number
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# n = integer to have digits counted (i.e. n = 312, digits = 3)
# base = decimal (10) by default, any other base valid by input
def digitizer(n, base = 10):
    digits = []
    while (n):
        digits.append(n % base)
        n //= base
    return digits

# listDuplicates: Return true if list contains one or more duplicates
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# item_list = list of items to be checked for duplicates
def listDuplicates(item_list):
    return (len(item_list)!=len(set(item_list)))
