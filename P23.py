# ==============================================================================
print ("Project Euler - Problem 23\n\n")
# ==============================================================================
# Description:
# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number. For example, the sum of the proper divisors of 28
# would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than
# n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
# number that can be written as the sum of two abundant numbers is 24. By
# mathematical analysis, it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers. However, this upper limit
# cannot be reduced any further by analysis even though it is known that the
# greatest number that cannot be expressed as the sum of two abundant numbers is
# less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum
# of two abundant numbers.
# ==============================================================================
import time
import math

start_time = time.time()
result = 0
# ***** BEGIN CODE FOR P23.py *****

MAX_NUM = 28124

def isAbundant(n):

    if (n < 1):
        return False

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

    return (int(d_n) > n)

# Main
i = 1
test_list = []

result_list = list(range(MAX_NUM))

while (i < MAX_NUM):
    if (isAbundant(i)):
        test_list.append(i)

    i += 1

for i in range(len(test_list)):
    abundant_sum = test_list[i] * 2
    j = i
    while (abundant_sum < MAX_NUM):
        # print(abundant_sum)
        result_list[abundant_sum] = 0
        j += 1
        abundant_sum = test_list[i] + test_list[j]

result = sum(result_list)

# ***** END CODE FOR P23.py *****
print ("Result is: ", result)
print ("Run time:   %.5f seconds" % (time.time() - start_time))
# END P23.py
