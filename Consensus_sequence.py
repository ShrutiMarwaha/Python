# Input: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
# Output: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

import re
import numpy as np
from pandas import DataFrame

# read the input file
#filename = "/Users/shruti/PycharmProjects/firstProject/Fasta.txt"
filename = "/Users/shruti/GIT/Python/rosalind_cons.txt"

try:
    sequence_file = open(filename)
except IOError:
    print("the file does not exist","r")

# extract sequences and store as a list
dna_list = []
dna_string = ""

for line in sequence_file:
    # discard any newline character at the end
    line = line.rstrip()

    # distinguish header from sequence. if the line does not start with ">", it is a seqeunce
    if re.search('^[^>]\w',line):
        dna_string = dna_string + line
    else:
        if len(dna_string) != 0:
            dna_list.append(dna_string)
            dna_string = ""

print "DNA sequences: %s \n" % dna_list

rows = len(dna_list)
cols = len(dna_list[0])

dna_matrix = np.chararray(shape=(rows,cols))

for i in range(rows):
    dna_matrix[i] = list(dna_list[i])

print "DNA Strings: \n %s \n" % dna_matrix

# construct profile matrix which counts the number of nucleotide occurence at each position among different sequences.
profile_matrix = np.zeros(shape=(4,cols))

for j in range(cols):
    for i in range(rows):
        if dna_matrix[i,j]=="A":
            profile_matrix[0,j] += 1
        if dna_matrix[i,j]=="C":
            profile_matrix[1,j] += 1
        if dna_matrix[i,j]=="G":
            profile_matrix[2,j] += 1
        if dna_matrix[i,j]=="T":
            profile_matrix[3,j] += 1

# convert matrix to data frame
profile_matrix2 = DataFrame(profile_matrix,index=["A","C","G","T"])
print "Profile: \n %s \n" % profile_matrix2

# find the nucleotide which is most common at a given position in the sequence
consensus = []

for j in range(cols):
    most_frequent_nucleotide = np.argmax(profile_matrix2[j])
    consensus.append(most_frequent_nucleotide)

consensus = "".join(consensus)

print("consensus sequence: %s \n" % consensus)