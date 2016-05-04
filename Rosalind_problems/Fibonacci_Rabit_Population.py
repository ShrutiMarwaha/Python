# http://rosalind.info/problems/fib/
# calculate total number of rabbit pairs that will be present after "n" months
# if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces
# a litter of "k" rabbit pairs (instead of only 1 pair).

# any given month will contain the rabbits that were alive the previous month, plus any new offspring.
# the number of offspring in any month is equal to the number of rabbits that were alive two months prior.

def rabbit_fib(n,k=1,m):
    # Fn-2
    first_gen = 1
    # Fn-1
    second_gen = 1
    RabbitFibSeries = []
    for i in range(n):
        RabbitFibSeries.append(first_gen)
        FinalPopulation = first_gen

        # Fn
        new_gen = (second_gen + first_gen*k)
        # so in this "i" month, the current Fn-1 is Fn and Fn-2 is the old Fn-1
        first_gen = second_gen
        #print first_gen
        second_gen = new_gen

    return "number of rabbits in each generation: %s and after %sth generation: %s" % (RabbitFibSeries, n, FinalPopulation)

print rabbit_fib(6,1,3)
#print rabbit_fib(29,2)



