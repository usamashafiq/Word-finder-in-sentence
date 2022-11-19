# this program is use to find the word on given length in the given string in this code i use the naive base
# algorithm to find the given length word like k_mer
from collections import defaultdict

# Data input
Pattern = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
# this is the k_mer number
frequent = 4

# Finding k-mers this is the default dict which i use to store the most freqent word in it and show the output
k_mers = defaultdict(int)


# this is the function which is find most frequent word
def FindKmer(Pattern, frequent):
    # this is the use to upper case the all word before solve the problem then solve the pattren
    Pattern = Pattern.upper()

    for i in range(0, len(Pattern) - (frequent - 1)):
        k_mers[Pattern[i:i + frequent]] += 1
    return [key for key, val in k_mers.items()
            if val == max(k_mers.values())]


# function calling

print(FindKmer(Pattern, frequent))
