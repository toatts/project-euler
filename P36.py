# ==============================================================================
print ("=============================")
print ("Project Euler - Problem 36")
print ("=============================")
# ==============================================================================
# Description:
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in
# base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include
# leading zeros.)
# ==============================================================================
import time
from pe_library import *

result = 0
start_time = time.time()
# ***** BEGIN CODE FOR P36.py *****
print(numDivisors(1)==1)
print(numDivisors(3)==2)
print(numDivisors(6)==4)
print(numDivisors(10)==4)
print(numDivisors(15)==4)
print(numDivisors(21)==4)
print(numDivisors(28)==6)
print(numDivisors(76576500))

'''
MAX_RANGE = 1000000

for i in range(1, MAX_RANGE+1):
    dec_list = digitizer(i, False, 10)
    if (isPalindrome(dec_list)):
        bin_list = digitizer(i, False, 2)
        if (isPalindrome(bin_list)):
#            print ("Palindrome:", dec_list, bin_list)
            result += i
'''
# ***** END CODE FOR P36.py *****
run_time = time.time() - start_time
print ("Result is: ", result)
print ("Run time:   %.5f seconds" % run_time)
# END P36.py
