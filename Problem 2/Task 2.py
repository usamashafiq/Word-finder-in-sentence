# this code is same but in this file we calculate the time how much time take the program to find the word

from collections import defaultdict

import timeit

# Data input
Pattern = "CAGGGACAGTTTTCTTCAAACGCTTTACGTCCACAACGTCCACAACTTTCTTCAATTTCTTCAAACGCTTTACGTCCACAACACGCTTTACACGCTTTACGCATGTTGACGCTTTACGTCCACAACGCATGTTGGTCCACAACTTTCTTCAAGTCCACAACGCATGTTGTTTCTTCAAGCATGTTGACGCTTTACCAGGGACAGTGCATGTTGTTTCTTCAAACGCTTTACTTTCTTCAATTTCTTCAAGCATGTTGGCATGTTGGCATGTTGTTTCTTCAAACGCTTTACGCATGTTGCAGGGACAGTACGCTTTACGTCCACAACCAGGGACAGTCAGGGACAGTGCATGTTGACGCTTTACTTTCTTCAAACGCTTTACGCATGTTGACGCTTTACGTCCACAACTTTCTTCAACAGGGACAGTCAGGGACAGTACGCTTTACCAGGGACAGTCAGGGACAGTGCATGTTGTTTCTTCAAACGCTTTACTTTCTTCAAGCATGTTGGTCCACAACACGCTTTACGCATGTTGCAGGGACAGTCAGGGACAGTCAGGGACAGTGTCCACAACCAGGGACAGTTTTCTTCAATTTCTTCAATTTCTTCAACAGGGACAGTTTTCTTCAATTTCTTCAACAGGGACAGTCAGGGACAGTCAGGGACAGTGCATGTTGGCATGTTGACGCTTTACCAGGGACAGTGTCCACAACGCATGTTGGTCCACAACCAGGGACAGTGCATGTTGACGCTTTACACGCTTTACACGCTTTACCAGGGACAGTGTCCACAACCAGGGACAGTTTTCTTCAACAGGGACAGTGTCCACAACGCATGTTGACGCTTTACGCATGTTGGTCCACAACACGCTTTACCAGGGACAGTTTTCTTCAATTTCTTCAAGTCCACAACTTTCTTCAACAGGGACAGTGCATGTTGTTTCTTCAAACGCTTTACACGCTTTACACGCTTTACTTTCTTCAAGTCCACAAC"
# this is the k_mer number
frequent = 12

# Finding k-mers this is the default dict which i use to store the most freqent word in it and show the output
k_mers = defaultdict(int)

# this is the note the start time for program to count the time in which time program calculate the most frequent number
start = timeit.default_timer()


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

# calculated time how much program is running
stop = timeit.default_timer()

print('Time: (sec) ', stop - start)
