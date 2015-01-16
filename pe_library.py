# ==============================================================================
# Project Euler Library
# ==============================================================================
import random
import math
import collections

# {{{ isPrime: Primality checker
# ==============================================================================
# Miller-Rabin algorithm
# http://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Primality_Testing
# n = integer to be tested for primality
# k = parameter that determines the accuracy of the guess (highest error probability = 4^-k)
# a = random integer in range [2, n-2]
# s = factor of 2 in 2^s * d
# d = n - 1
# Example: isPrime(13) = True, isPrime(20) = False
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
# }}}

# {{{ digitizer: Create list of digits in number
# ==============================================================================
# n = integer to have digits counted (i.e. n = 312, digits = 3)
# base = decimal (10) by default, any other base valid by input
# Example: digitizer(20345) = [5,4,3,0,2], digitizer(20345, True) = [2,0,3,4,5]
def digitizer(n, ordered = False, base = 10):
    digits = []
    while (n):
        digits.append(n % base)
        n //= base
    if (ordered):
        digits = list(reversed(digits))
    return digits
# }}}

# {{{ listDuplicates: Checks list for at least one set of duplicates
# ==============================================================================
# item_list = list of items to be checked for duplicates
# Example: listDuplicates([1,2,3,4,5]) = False, listDuplicates([1,2,3,4,1]) = True
def listDuplicates(item_list):
    return (len(item_list)!=len(set(item_list)))
# }}}

# {{{ listContains: Checks list for existence of input value
# ==============================================================================
# item_list = list of items to be checked for value
# value = check for existence of value in item_list
# Example: listContains([1,2,3], 5) = False, listContains([1,2,3], 2) = True
def listContains(item_list, value):
    for item in item_list:
        if (value == item):
            return True
    return False
# }}}

# {{{ zeros: Checks list of digits for any zeros
# ==============================================================================
# digits = list of digits to be checked for a zero
# Example: zeros([1,2,3,4]) = False, zeros([1,0,0,2,3]) = True
def zeros(digits):
    for digit in digits:
        if (digit):
            continue
        else:
            return True
    return False
# }}}

# {{{ boundChecker: Checks for the condition when some number is higher than some
# manipulation of its digit components. Valid for exponent and factorial expansion
# ==============================================================================
# exp = if testing bounds using digit to some exponent, input exp
def boundChecker(exp=0):
    if (exp):
        bound_inc = 9**exp
    else:
        bound_inc = math.factorial(9)
    bounds = bound_inc
    value  = 9
    while (value <= bounds):
        value = (value*10) + 9
        bounds += bound_inc

    return bounds
# }}}

# {{{ rotateList: Takes in list of items, barrel rotates and returns new list
# ==============================================================================
# item_list = list of items to be rotated and returned
# n = number of locations to barrel rotate to the right
def rotateList(item_list, number):
   collection_list = collections.deque(item_list)
   collection_list.rotate(number)
   return list(collection_list)
# }}}

# {{{ numerizer: Takes in list of digits, combines them and returns the single
# number
# ==============================================================================
# num_list = list of digits to be combined into a single number
# Example: numerizer([1,2,3,4]) = 1234
def numerizer(num_list):
    return int(''.join(map(str, num_list)))
# }}}

# {{{ isPalindrome: Takes in list and checks if the items create a palindrome
# ==============================================================================
# item_list = list of items to be tested for a palindrome
# Example: isPalindrome([1,2,3,2,1]) = True, isPalindrome([1,2,3,4,5]) = False
def isPalindrome(item_list):
    isPal = True
    i = 0
    while ((i <= int(len(item_list)/2))):
        if (item_list[i] != item_list[-(i+1)]):
            isPal = False
            break
        i += 1
    return (isPal)
# }}}

# {{{ numDivisors: Checks input number for the amount of divisors it has
# ==============================================================================
# number: Input number to check for divisors
# Example: numDivisors(10) = 4
def numDivisors(number):
    if (number == 1):
        return 1
    elif (number < 1):
        return 0

    divisors = 1
    prime_factors = 1
    i = 2
    while (number > 1):
        if not(number % i):
            number /= i
            prime_factors += 1
            continue
        if (i > 2):
            i += 2
        else:
            i += 1
        divisors *= prime_factors
        prime_factors = 1
    if (divisors == 1):
        return 2
    else:
        return (divisors*prime_factors)
# }}}

# {{{ collatz: Computes the length of the Collatz Chain for the number n
# ==============================================================================
# http://en.wikipedia.org/wiki/Collatz_conjecture
# n: Input number to determine length of Collatz Chain
# computed_values: List of values of previously computed Collatz Chain lengths (useful if running iteratively)
# Example: collatz(13) = 10
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
# }}}

# {{{ numberLetters: Computes the number of letters used to spell out a number n
# ==============================================================================
# n = input number to be converted to letter length
# Example: numberLetters(342) = 23 (three hundred and forty two)
N_0_19   = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
N_20_99  = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]
HUNDRED  = 7 # 100-999
THOUSAND = 8 # 1000-9999
AND      = 3 # included past 100
def numberLetters(n):
    # Thousand
    letters = N_0_19[int(n/1000)]
    if (n > 999):
        letters += THOUSAND
        n %= 1000
    # Hundred
    letters += N_0_19[int(n/100)]
    if (n > 99):
        letters += HUNDRED
        n %= 100
        if (n):
            letters += AND
    # 20-99
    if (n > 19):
        letters += TEENS[int(n/10)]
        letters += SINGLES[n%10]
    # 0-19
    else:
        letters += SINGLES[n]

    return letters
# }}}

# {{{ sumOfProperDivisors: Computes the sum of the proper divisors of number n
# ==============================================================================
# n = input number to determine proper divisors
# Example: sumOfProperDivisors(220) = 284
def sumOfProperDivisors(n):
    if (n < 1):
        return 0

    # d(n) = sum of proper divisors of n, at least 1
    d_n = 1
    i   = 2
    termination = math.sqrt(n)

    while (i <= termination):
        if ((n % i) == 0):
            if (i == termination):
                d_n += i
            else:
                d_n += (i + (n / i))

        i += 1

    return int(d_n)
# }}}

# {{{ recurringDecimal: Computes the length of the recurring decimal in a fraction
# ==============================================================================
# numerator   = top portion of the input decimal
# denominator = bottom portion of the input decimal
# Example: recurringDecimal(1,7) = 6 (0.(142857))
def recurringDecimal(numerator, denominator):
    rem = numerator % denominator
    pat_match = []
    dec_count = 0
    numerator *= 10

    while (rem):
        div = int(numerator / denominator)
        dec_count += 1
        for i in range(len(pat_match)):
            if pat_match[i] == numerator:
                return (dec_count - i - 1)

        pat_match.append(numerator)
        numerator = (numerator % denominator) * 10
        if (numerator == 0):
            return 0

        rem = numerator % denominator

    return 0
# }}}


# {{{ spiralDiagonalSum: Computes sum of spiral diagonals in an n x n spiral
# ==============================================================================
# Algorithm = 1 + summation_3->n_only_odds(n^2 + (n^2 - n + 1) + (n^2 - 2n + 2) + (n^2 - 3n + 3))
# Simplifies to 1 + summation_3->n_only_odds(4n^2-6n+6)
# n = Input length of dimensions for the generated cube (must be odd)
# Example: spiralDiagonalSum(5) = 101
def spiralDiagonalSum(n):
    if (n == 1):
        return 1
    elif (n % 2):
        return ((4*(n**2))-(6*n)+6) + spiralDiagonalSum(n-2)
    else:
        print ("Error: Only works for odd numbers")
        return 0


