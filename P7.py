# ==============================================================================
print ("Project Euler - Problem 7\n\n")
# ==============================================================================
# Description:
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
# that the 6th prime is 13.
# What is the 10 001st prime number?
# ==============================================================================
import time
import math

start_time = time.time()
result = 0
# ***** BEGIN CODE FOR P7.py *****

def isPrime(number):
	root = math.sqrt(number)
	prime = True
	divisor = 3
    
	# If 1, then not prime
	if (number == 1):
		prime = False
	# If 2, then prime
	elif (number == 2):
		prime = True
	# If even, not prime
	elif ((number % 2) == 0):
		prime = False
	else:
		# Check odd divisors that are less than or equal to the square root of
		# the test value
		while (divisor <= root):
			# Check if any remainder to divider
			if ((number % divisor) == 0):
				prime = False
				break
			#Add two for next odd number
			divisor += 2
	return (prime)
  	
# Main Function

MAX_COUNT = 10001

i = 1
prime_count = 0


while (prime_count < MAX_COUNT):
	if (isPrime(i) == True):
		prime_count += 1
	i += 1

result = (i - 1)

# ***** END CODE FOR P7.py *****
print ("Result is: ", result)
print ("Run time: " + str((time.time() - start_time)) + " seconds")
# END P7.py
