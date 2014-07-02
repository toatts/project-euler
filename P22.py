# ==============================================================================
print ("Project Euler - Problem 22\n\n")
# ==============================================================================
# Description:
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
# containing over five-thousand first names, begin by sorting it into
# alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name
# score.
# For example, when the list is sorted into alphabetical order, COLIN, which is
# worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
# would obtain a score of 938 x  53 = 49714.
# What is the total of all the name scores in the file?
# ==============================================================================
import time
import math

start_time = time.time()
result = 0
# ***** BEGIN CODE FOR P22.py *****

import csv

letter_offset = ord('A')-1
name_result = 0

with open("names.txt", "r") as f:
    reader = csv.reader(f)
    for name_list in reader:
        name_list.sort()
        for names in name_list:
            name_result = 0
            for letter in names:
                name_result += ord(letter) - letter_offset
            name_result *= (name_list.index(names) + 1)
            result += name_result


# ***** END CODE FOR P22.py *****
print ("Result is: ", result)
print ("Run time:   %.5f seconds" % (time.time() - start_time))
# END P22.py
