# Calculate expected number of offspring displaying the dominant phenotype http://rosalind.info/problems/iev/

from __future__ import division

# function to generate probability of dominant offspring (F1) from parent's genotypes
def dominant_F1_probability(parents_genotype):
    # 4 possible offspings
    F1 = parents_genotype[0]+parents_genotype[3], parents_genotype[0]+parents_genotype[4], parents_genotype[1]+parents_genotype[3], parents_genotype[1]+parents_genotype[4]
    # percentage of offsprings with dominant genotype
    dominant_count = 0
    for i in range(len(F1)):
        if F1[i]=="AA" or F1[i]=="Aa" or F1[i]=="aA":
            dominant_count += 1

    return(dominant_count/4)

genotypes = ["AA-AA","AA-Aa","AA-aa","Aa-Aa","Aa-aa","aa-aa"]
genotypes_dominant_probability = []

for i in range(len(genotypes)):
    genotypes_dominant_probability.append( dominant_F1_probability(genotypes[i]) )

# function to calculate expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly same number of offsprings
def dominant_F1_population(couples_per_genotype,number_of_offsprings):
    # couples_per_genotype: number of couples in a population possessing each genotype pairing for a given factor
    expected_value = 0
    for i in range(len(couples_per_genotype)):
        expected_value += couples_per_genotype[i] * genotypes_dominant_probability[i]

    return(expected_value*number_of_offsprings)

print dominant_F1_population( [1,0,0,1,0,1], 2)
print dominant_F1_population( [17636, 19549, 19895, 18623, 16520, 19352], 2)
print dominant_F1_population( [19853, 19327, 16954, 17994, 18595, 19163], 2)



