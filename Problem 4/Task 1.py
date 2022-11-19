# in this program we  Find All Occurrences of a Pattern in a String mean i give a string and pattren then find the
# pattren occurrence in a string

import re

Pattern = "GATATATGCATATACTT"
# initializing substring
string = "ATAT"

# I use for this task python built in library name is Regular expression operations
# I use finditer function , Return an iterator yielding MatchObject instances over all non-overlapping matches for the
# RE pattern in string. The string is scanned left-to-right, and matches are returned to the order found. Empty matches
# are included in the result.
# find All occurrences of substring in string
res = [i.start() for i in re.finditer(string, Pattern)]

# printing result
print("Occurrences : " + str(res))
