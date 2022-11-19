# this code is to find a pattern in given string mean we enter a string and find a number of pattern present
# in this given string and at the end give a number of match pattern in this file we calculate the time how much
# required a time to calculate the pattern matching

# Putting characters together one at a time is an easy fix. And we raise the count whenever we find a perfect match.
# Here is a straightforward answer based on naive pattern searching. This function find occurrences of Pattern in text.
def PattrenCount(Pattren, Text):
    M = len(Pattren)
    N = len(Text)
    res = 0

    # A loop to slide Pattren one by one
    for i in range(N - M + 1):

        # For current index i, check
        # for pattern match
        j = 0
        while j < M:
            if Text[i + j] != Pattren[j]:
                break
            j += 1

        if j == M:
            res += 1
            j = 0
    return res


Text = "GCGCG"
Pattren = "GCG"
# function calling
print(PattrenCount(Pattren, Text))
