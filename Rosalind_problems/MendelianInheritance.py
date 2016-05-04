from __future__ import division

# http://rosalind.info/problems/iprb/
# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

def ProbabilityOfDominantPhenotype(k,m,n):
    t = k+m+n
    Denominator = t * (t-1)

    # probability of dominant phenotype (offspring having at least one dominant allele) among 6 possible pairs
    P_kk = k * (k-1) * (4/4)
    # this probability is multiplied by 2 because of two possible orders i.e, male from k population and female from m OR male from m and female from k
    P_km = k * m * 2 * (4/4)
    P_kn = k * n * 2 * (4/4)
    # in this case, even if two heterozygous individuals mate, there is 3/4 probability of producing dominanat offspring and 1/4th probability of producing recessive offspring
    P_mm = m * (m-1) * (3/4)
    P_mn = m * n * 2 * (2/4)
    P_nn = n * (n-1) * 0

    final_probability = (P_kk + P_km + P_kn + P_mm + P_mn + P_nn) / Denominator

    return final_probability

print ProbabilityOfDominantPhenotype(2,2,2)

print ProbabilityOfDominantPhenotype(21,16,16)

print ProbabilityOfDominantPhenotype(10,30,80)
