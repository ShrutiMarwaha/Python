# check if two strings are isomorphic.
def Isomorph(s1,s2):
    '''
    Two strings are isomorphic if the characters in s can be replaced to get t.
    All occurrences of a character must be replaced with another character while preserving the order of characters.
    No two characters may map to the same character but a character may map to itself.

    :param s1: string s
    :param s2: string t
    :return: true if the two strings are isomorphic ; false if the two strings are not isomorphic
    '''
    if s1==None or s2==None:
        return "please enter valid strings"

    # Condition1: they should be of same length
    elif len(s1) != len(s2):
        return False
    else:
        # create a dictionary which maps elements from first string to that in second string.
        alphabet_mapping = {}
        for i in range(len(s1)):
            # if the ith element from string1 is not present as a key in dictionary, add it and its value as the corresponding element in string2
            if s1[i] not in alphabet_mapping:
                alphabet_mapping[s1[i]] = s2[i]
            # if the key in dictionary (ith element from string1) contains a value that is different from ith element from string2
            elif alphabet_mapping[s1[i]] != s2[i]:
                return False

    return True

s1 = "abbac"
s2 = "xyyxz"

print Isomorph(s1,s2)




