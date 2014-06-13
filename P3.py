# ==============================================================================
print ("Project Euler - Problem 3\n\n")
# ==============================================================================
# Description:
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# ==============================================================================
import time

start_time = time.time()
result = 0
# ***** BEGIN CODE FOR P3.py *****

NUMBER = 600851475143

i = 2

# If number greater than 1, there is still a prime factor
while (NUMBER > 1):
    # Loop through infinitely to find an evenly divisible number, starting at 2
    while True:
        if ((NUMBER % i) == 0):
            NUMBER /= i     #Prime found, divide by it and iterate over new number
            break           #Break out of infinite loop
        # If prime not found, increment 1
        i += 1
    
# Save last prime as the answer, largest prime factor
result = i

# ***** END CODE FOR P3.py *****
print ("Result is: ", result)
print ("Run time: " + str((time.time() - start_time)) + " seconds\n")
# END P3.py
