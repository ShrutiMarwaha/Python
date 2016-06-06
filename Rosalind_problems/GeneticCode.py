# # convert given rna string into protein using codon table
rna_string = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"

## convert the codon table into a dictionary
codon_table_dict = {}
with open("/Users/shruti/git/Python/datasets/RNA_codon_table.txt") as f:
    for line in f:
        line = line.strip()

        if len(line) > 0:
            codon_map = line.split()
            codon = codon_map[0]
            amino = codon_map[1]
            codon_table_dict[codon] = amino

print ("codon table: %s \n" % codon_table_dict)

# to splice a (rna) sequence into chunks (codons) of given size (eg 3)
def SplitString(sequence,size):
    sequence_chunks = []
    for pos in xrange(0,len(sequence),size):
        #print sequence[pos : (pos+size)]
        splits = sequence[pos : (pos+size)]
        sequence_chunks.append(splits)
    return sequence_chunks

rna_codon = SplitString(rna_string,3)
print ("codons: %s \n" % rna_codon)

## look up the dictionary (codon_table_dict) to find the amino acid corresponding to each codon
protein_sequence = ""
for i in range(len(rna_codon)):
    amino_acid = codon_table_dict[ rna_codon[i] ]
    if amino_acid!="Stop":
        protein_sequence += amino_acid
    else:
        break

print ("protein sequence: %s \n" % protein_sequence)
