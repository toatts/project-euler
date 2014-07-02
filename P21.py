# ==============================================================================
print ("Project Euler - Problem 21\n\n")
# ==============================================================================
# Description:
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
# which divide evenly into n).
# If d(a) = b and d(b) = a, where a not equal to b, then a and b are an
# amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
# and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71
# and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.
# ==============================================================================
import time
import math

start_time = time.time()
result = 0
# ***** BEGIN CODE FOR P21.py *****

MAX_LENGTH = 10000

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

# Main
i = 1
computed_values = [0] * MAX_LENGTH

while (i < MAX_LENGTH):
    d_n = sumOfProperDivisors(i)
    computed_values[i] = d_n
    if (d_n < MAX_LENGTH):
        if (i != d_n) and (computed_values[d_n] == i):
            # print("amicable: ", i, d_n)
            result += d_n + i

    i += 1


# ***** END CODE FOR P21.py *****
print ("Result is: ", result)
print ("Run time:   %.5f seconds" % (time.time() - start_time))
# END P21.py
