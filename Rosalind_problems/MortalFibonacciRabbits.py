# Mortal Fibonacci Rabbits http://rosalind.info/problems/fibd/
# calculate The total number of pairs of rabbits that will remain after the nth month if all rabbits live for m months.
# any given month will contain the rabbits that were alive the previous month, plus any new offspring.
# the number of offspring in any month is equal to the number of rabbits that were alive two months prior.
# all rabbits die out after a fixed number of months.

generations = [1, 1] #Seed the sequence with the 1 pair, then in their reproductive month.

def fib(n, m):
    count = 2
    while count < n:
        if (count < m):
            generations.append((generations[-2]) + generations[-1]) #recurrence relation before rabbits start dying (simply fib seq Fn = Fn-2 + Fn-1)
        elif (count == m or count == m+1):
            print ("in base cases for newborns (1st+2nd gen. deaths)") #Base cases for subtracting rabbit deaths (1 death in first 2 death gens)
            generations.append((generations[-2] + generations[-1]) - 1)#Fn = Fn-2 + Fn-1 - 1
        else:
            generations.append((generations[-2] + generations[-1]) - (generations[-(m+1)])) #Our recurrence relation here is Fn-2 + Fn-1 - Fn-(m+1)
        count += 1
    return (generations, generations[-1])


print (fib(6, 3))
#print ("Here's how the total population looks by generation: \n" + str(generations))