# ==============================================================================
print ("Project Euler - Problem 15\n\n")
# ==============================================================================
# Description:
# Starting in the top left corner of a 2 x 2 grid and moving only down and
# right, there are 6 route to the bottom right corner.
#     __ __   1 __ __ 2 __    3 __    4        5       6
#    |__|__|         |    |__     |     |__ __  |__     |
#    |__|__|         |       |    |__         |    |__  |__ __
#
# How many routes are there through a 20 x 20 grid?
# ==============================================================================
import time
import math

start_time = time.time()
result = 0
# ***** BEGIN CODE FOR P15.py *****

CUBE_SIZE = 20

paths = [[0 for i in range(CUBE_SIZE)] for i in range(CUBE_SIZE)]

for i in range(CUBE_SIZE):
    for j in range(CUBE_SIZE):
        if (i == 0):
            paths[i][j] = j + 2
        elif (j == 0):
            paths[i][j] = i + 2
        else:
            paths[i][j] = paths[i-1][j] + paths[i][j-1]

result = paths[CUBE_SIZE-1][CUBE_SIZE-1]

# FIXME: Recursion is way too inefficient for this
#SIZE = [20,20]
#
## TODO: should always be an even number due to symmetry?
#def pathExplore(location, size):
#    # print (location)
#    # Reached final location
#    if (location == size):
#        # print ("Found path")
#        return 1
#    # Height max
#    elif (location[0] == size[0]):
#        return pathExplore([location[0], location[1]+1], size)
#    # Width max
#    elif (location[1] == size[1]):
#        return pathExplore([location[0]+1, location[1]], size)
#    else:
#        # Explore right and down
#        return pathExplore([location[0],location[1]+1], size) + pathExplore([location[0]+1, location[1]], size)
#
#
#location = [0,0]
#
#result = pathExplore(location, SIZE)

# ***** END CODE FOR P15.py *****
print ("Result is: ", result)
print ("Run time:   %.5f seconds" % (time.time() - start_time))
# END P15.py

