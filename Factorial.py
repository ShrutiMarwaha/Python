# find a factorial of a number
def Factorial(n):
    fact = 1
    if n==0:
        return fact
    elif n<0:
        return None
    else:
        for i in range(1,n+1):
            fact *= i
        return fact

def FactorialRecursion(n):
    if n==0:
        return 1
    elif n<0:
        return None
    else:
        return n * FactorialRecursion(n-1)

def FactorialRecursionOneLine(n):
    return (None if n<0 else (1 if n==0 else n * FactorialRecursionOneLine(n-1)))

print(Factorial(5))
print(FactorialRecursion(5))
