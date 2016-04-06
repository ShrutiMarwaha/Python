# PRINT fibonacci numbers till "n"
def Fibonacci1(n):
    result1 = []
    a,b = 0,1
    while a <= n:
        result1.append(a)
        a, b = b, a+b
    return result1
print "fibonacci series upto number n: %s" % Fibonacci1(20)

# print fibonacci "n" numbers
def Fibonacci2(n):
    if n==0:
        result = [0]
    elif n==1:
        result = [0,1]
    else:
        result = []
        a,b = 0,1
        for i in range(n):
            result.append(a)
            a, b = b, a+b
    return result
print "fibonacci series for n numbers: %s" % Fibonacci2(5)