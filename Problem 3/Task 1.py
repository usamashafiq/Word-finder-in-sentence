# in this program we Find the Reverse Complement of a String mean every alphabet have own complement word which is
# defined in dict when retrieve the string then find complement the string

# given string
DNA_string = 'AAAACCCGGT'


# this function use to complement the string
def reverseComplement(Pattern):
    # in this dict same the key and values which is complement of alphabets
    dict = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
    Reverse = ''
    # this loop to treverse the all string and complement the string and return the list
    for i in Pattern:
        Reverse += dict[i]
    return Reverse[::-1]


# function calling
print('Complementing a Strand of DNA')
print(reverseComplement(DNA_string))
