# ==============================================================================
print ("Project Euler - Problem 2\n\n")
# ==============================================================================
# Description:
# Each new term in the Fibonacci sequence is generated by adding the previous 
# two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed 
# four million, find the sum of the even-valued terms.
# ==============================================================================

result = 0
# ***** BEGIN CODE FOR P2.py *****

MAXCOUNT = 4000000

temp = 0
term1 = 1
term2 = 1

while (term1 < MAXCOUNT):
    temp = term2    #Store term2 
    term2 += term1  #Add term1 to term2
    term1 = temp    #Update term1 to previous term2
    
    #If term is even, add to result
    if ((term1 % 2) == 0):
        result += term1

# ***** END CODE FOR P2.py *****
print ("Result is: ", result)

# END P2.py
