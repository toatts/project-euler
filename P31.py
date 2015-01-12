# ==============================================================================
print ("=============================")
print ("Project Euler - Problem 31")
print ("=============================")
# ==============================================================================
# Description:
# In England the currency is made up of pound, f, and pence, p, and there are
# eight coins in general circulation:
# 1p, 2p, 5p, 10p, 20p, 50p, f1(100p), and f2(200p)
# It is possible to make f2 in the following way:
# 1*f1 + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p
# How many different ways can f2 be made using any number of coins?
# ==============================================================================
import time
import math

result = 0
start_time = time.time()
# ***** BEGIN CODE FOR P31.py *****

total = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]

coeff = [1]
for i in range(1,(total+1)):
    coeff.append(0)

for coin in coins:
    for i in range(0, (total+1-coin)):
        coeff[i+coin] += coeff[i]

result = coeff[total]

# ***** END CODE FOR P31.py *****
run_time = time.time() - start_time
print ("Result is: ", result)
print ("Run time:   %.5f seconds" % run_time)
# END P31.py
