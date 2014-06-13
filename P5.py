# ==============================================================================
print ("Project Euler - Problem 5\n\n")
# ==============================================================================
# Description:
# 2520 is the smallest number that can be divided by each of the numbers from 1 
# to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the 
# numbers from 1 to 20?
# ==============================================================================
import time

start_time = time.time()
result = 0
# ***** BEGIN CODE FOR P5.py *****

result = 20
i = 19
solved = True

# Loop until minimum answer found
while True:
    # Decrement from 19 to 11 checking each value for no remainder 
    # Note: 19 through 11 is all that is required to check with even multiples
    while (i > 10):
    #for i in req_dividends:
        # If remainder found, break out and try new result
        if ((result % i) > 0):
            solved = False
            break
        # Decrement i each cycle
        i -= 1
    # If all numbers are evenly divisible, break out and supply result
    if (solved == True):
        break
    
    # Increment result by 20 for next round since it must be at least an 
    # increment of 20. Also reset i to 19 and solved to True
    result += 20
    i = 19
    solved = True    

# ***** END CODE FOR P5.py *****
print ("Result is: ", result)
print ("Run time: " + str((time.time() - start_time)) + " seconds")
# END P5.py
