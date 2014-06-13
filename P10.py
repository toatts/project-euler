# ==============================================================================
print ("Project Euler - Problem 10\n\n")
# ==============================================================================
# Description:
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
# ==============================================================================
import time
import math

start_time = time.time()
result = 0
# ***** BEGIN CODE FOR P10.py *****

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

MAX_PRIME = 2000000

i = 3
prime_sum = 2

while (i <= MAX_PRIME):
	if (isPrime(i) == True):
		prime_sum += i
	i += 1

result = prime_sum

# ***** END CODE FOR P10.py *****
print ("Result is: ", result)
print ("Run time: " + str((time.time() - start_time)) + " seconds")
# END P10.py