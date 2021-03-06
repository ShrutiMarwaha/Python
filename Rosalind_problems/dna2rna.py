__author__ = 'shruti'
#dna_string = "GATGGAACTTGACTACGTAAATT"
dna_string = "TCGAGAGGTTGCACGATAAGTACCTCGTCAGATAAGCCCCCGACAGTTTTACGACTGCTAGTATATCTGAGTGCACTGAGAGGCGGGCAAGCAGCGAGTGAGCAGTGATGCTCCGCCAATTAACTATTTGTAGTCGACAGGGTTCCATTCATGGATCTTATCGATGCAGCCTATAAGTTGGTTCTACGAGTGATAATTGGGCAAAGCCTGCAGCTCAAAGAACTTGCTTCATACTTGCTGTCTATACGCGAATCTTGAGTGGGACAGTACGACCAGTGACACTTAACGGGTTGATACCATTCATCATACGGCCGCATCATCCGGGTAGGAATTTGTTTATCCCATTCTACTGCTTGGAGGCAGAGTCGTGGCAGCTTGCTTAGGTACGTGCTTAGAAGCCTTATGTCAAAATATTATTCCTGTGCACAAGTCGCTCGACCCAACCACGCGTCTAGACGTGCGTCGAGCTCCACCAACTGAATCCGGGCGGTATACATAAATAGTGTGAATCACTCTGGGTGGTTTCACTAATGAGTGTTCGTGCTCGATACGGCCCCGATTACCGAGGTCTGTTTACTGCAGGGCTGTAGGTGCAACTATCCTTTTTAAATCGGCCCGTGACCTGTAACATGCTCTATTCAATGTAACTGCTTGTGGCTCTCGCTTCCTAGACCATAAACAGGCTTAATGACCCTCACGGCCGCACCGAGCGAATAAATAGGCGAGAATGTATCGGCGCAAGGTATCTCGGTTCGTAAGCCGTTCGTGTTACAATCCCCAAGAGGTTTGTTCGGACACTACTCTCGCTAACAACGTCTGTAAAAAGTAGACGATCTTGATTCCACCGCCACGGAGGGTCCTCCTCAGATCAGACCATGTATATCGATAATGCTCTCAGATTTTTCTTCCGAGACTTCCCCATAGATCAATGTTGGGCTAAAGCGCTCAGCCGTGAGCATTGCACACTGTTGCGCA"
dna_string = dna_string.upper()
dna_length = len(dna_string)
# strings are immutable in python, so you can't change rna_sting in the loop later, so fist convert into an array
# use "list" to convert string to an array
rna_array = list(dna_string)
print "DNA: %s \n" %(dna_string)

for i in range(0,dna_length):
    if dna_string[i]=="T":
        rna_array[i]="U"

# use "join" to convert array to string
print "Solution1: using for loop"
print "mRNA: " + "".join(rna_array) + "\n"

print "Solution2 using string replace:"
rna_string2 = dna_string.replace("T","U")
print "mRNA: " + rna_string2 + "\n"

# solve using regular expression
print "Solution3 using regular expression"
import re
rna_string3 = re.sub("T","U",dna_string)
print "mRNA: " + rna_string3 + "\n"