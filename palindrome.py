#### reverse a number
import math
def ReverseNumber(x):
    reverse = 0
    while(x>0):
        # find the remainder of number on dividing by 10
        remainder = x % 10
        reverse = (reverse*10) + remainder
        # find the quotient and assign it as new number
        x = x/10
    return(reverse)
#print(ReverseNumber(123))

def Palindrome(x):
    # if input is integer
    if type(x) is int:
        if ReverseNumber(x)==x:
            #print "%s is palindrome \n" % x
            return True
        else:
            return False
    # if input is string
    elif type(x) is str:
        length = len(x)
        for i in range(0,(int(length/2))):
            if x[i] != x[(length-1)-i]:
                return False
        return True


print(Palindrome(1234321))
print(Palindrome(12345321))
print(Palindrome("MADAM"))
print(Palindrome("MADAME"))


