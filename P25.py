# ==============================================================================
print ("Project Euler - Problem 25\n\n")
# ==============================================================================
# Description:
# The Fibonacci sequence is defined by the recurrence relation:
# Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1
# Hence the first 12 terms will be:
# F1  = 1
# F2  = 1
# F3  = 2
# F4  = 3
# F5  = 5
# F6  = 8
# F7  = 13
# F8  = 21
# F9  = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
# What is the first term in the Fibonacci sequence to contain 1000 digits?
# ==============================================================================
import time
import math

start_time = time.time()
result = 0
# ***** BEGIN CODE FOR P25.py *****

def digitCounter(n):
    i = 0
    for digits in str(n):
        i += 1

    return i

prev = 1
fib  = 1
tmp  = 0
result = 2

while (digitCounter(fib) < 1000):
    tmp  = fib
    fib += prev
    prev = tmp
    result += 1


# ***** END CODE FOR P25.py *****
print ("Result is: ", result)
print ("Run time:   %.5f seconds" % (time.time() - start_time))
# END P25.py
