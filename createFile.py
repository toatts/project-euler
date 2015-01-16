# createFile.py
# Creates a header file for a new Project Euler problem. Input the problem
# number at the command line to create a new file:
# $ python createFile.py <n>
# If file exists, the program asks for confirmation to overwrite, otherwise
# the file is automatically created.

import urllib.request
import sys
import os
import re

from html.parser import HTMLParser

# HTML Parser to pull in the data in <p> tags
class MyHTMLParser(HTMLParser):
    def __init__(self, *args, **kwargs):
        HTMLParser.__init__(self)
        self.startPrint = False
        self.textData = ''
    def handle_starttag(self, tag, attrs):
        if (tag == "p"):
            self.startPrint = True
    def handle_data(self, data):
        if (self.startPrint):
            self.textData += data
    def handle_endtag(self, tag):
        if (tag == "p"):
            self.startPrint = False
            self.textData += '\n'

# Pull in problem number from first argument of command line and append to file
probnum = str(sys.argv[1])
filename = "P" + probnum + ".py"

# Check if file exists. If yes, asks for confirmation to overwrite or exits. If
# no, the file is automatically created
if (os.path.exists(filename)):
    ret = input("File " + filename + " exists. Would you like to overwrite? [Y/n]: ")
    if (ret == "Y"):
        print ("Overwriting",filename)
        f = open(filename, "w")
    else:
        print ("Exiting without overwriting",filename)
        sys.exit()
else:
    print ("No file named", filename, "detected in directory, creating new file.")
    f = open(filename, "w")

#Print header to new file
f.write('# ==============================================================================\n')
f.write('print ("=============================")\n')
f.write('print ("Project Euler - Problem ')
f.write(probnum)
f.write('")\n')
f.write('print ("=============================")\n')
f.write('# ==============================================================================\n')
f.write('# Description:\n')

# Create the URL address and open it with urllib.request. Save the source as a
# string to be parsed.
addr = "http://projecteuler.net/problem=" + probnum
url = urllib.request.urlopen(addr)
source = str(url.readlines())

# Create instance of HTML Parser and feed the source file to be parsed
parser = MyHTMLParser()
parser.feed(source)

# Take raw string and split on newlines and spaces. () around delimiter to
# retain delimiter. Filter list for empty strings "None".
wordList = re.split('( )|(\n)', parser.textData)
wordList = filter(None, wordList)

# Initialize character count to wrap lines at 80 characters
charCount = 0

# Loop through words for description section. If character count + length of
# next word exceeds 78 (each line starts with two characters "# ") then insert
# newline and reset count. If newline detected, write it and reset count. If
# count is zero, add the comment and space to beginning of line. Always write
# the word and add the length of it to the count.
for i in wordList:
    if ((charCount + len(i)) > 78):
        f.write('\n')
        charCount = 0
    if (i == '\n'):
        charCount = 0
        f.write(i)
        continue
    if (charCount == 0):
        f.write('# ')
    f.write(i)
    charCount += len(i)

# Close out the header and add the result and print section
f.write('# ==============================================================================\n')
f.write('import time\n')
f.write('from pe_library import *\n')
f.write('\n')
f.write('result = 0\n')
f.write('start_time = time.time()\n')
f.write('# ***** BEGIN CODE FOR ' + filename + ' *****\n')
f.write('\n')
f.write('\n')
f.write('\n')
f.write('# ***** END CODE FOR ' + filename + ' *****\n')
f.write('run_time = time.time() - start_time\n')
f.write('print ("Result is: ", result)\n')
f.write('print ("Run time:   %.5f seconds" % run_time)\n')
f.write('# END ' + filename)

# Close the URL and file
url.close()
f.close()

# Indicate success
print (filename + " template file created!")
