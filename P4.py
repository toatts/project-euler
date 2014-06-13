# ==============================================================================
print ("Project Euler - Problem 4\n\n")
# ==============================================================================
# Description:
# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
# ==============================================================================
import time
import math

start_time = time.time()
result = 0
# ***** BEGIN CODE FOR P4.py *****

# Palindrome Test Function
def isPalindrome(test_str):
    isPal = True
    i = 0
    
    # Iterate through first half of value while still considered palindrome
    while ((i <= int(len(test_str)/2)) and (isPal == True)):
        # Test the ith value with the ith value from the end
        if (test_str[i] != test_str[-(i+1)]):
            isPal = False
            break
        i += 1
    return (isPal)
    
# Main Function
product = 0

for i in range(101,1000):
    for j in range(101,1000):
        product = i*j
        if ((isPalindrome(str(product))) and (product > result)):
            result = product


# ***** END CODE FOR P4.py *****
print ("Result is: ", result)
print ("Run time: " + str((time.time() - start_time)) + " seconds\n")
# END P4.py
