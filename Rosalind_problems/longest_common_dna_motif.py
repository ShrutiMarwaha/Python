# Problem: Finding a Shared Motif  http://rosalind.info/problems/lcsm/
#
# A common substring of a collection of strings is a substring of every member of the collection.
# We say that a common substring is a longest common substring if there does not exist a longer common substring.
# For example, "CG" is a common substring of "ACGTACGT" and "AACCGGTATA", but it is not as long as possible;
# in this case, "GTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

# Given: A collection of k DNA strings of length at most 1 kbp each in FASTA format.
# Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
#
# Sample Dataset
# >Rosalind_1
# GATTACA
# >Rosalind_2
# TAGACCA
# >Rosalind_3
# ATACA

# Sample Output
# AC


import re

# function to extract dna sequences from fasta files
def sequences_from_fasta_file(f):

    try:
        sequence_file = open(f,"r")
    except IOError:
        print("the file does not exist")

    seq_list = []
    seq_string = ""
    for line in sequence_file:
        line = line.rstrip()

        if re.search("^[^>/w]",line):
            seq_string += line
        else:
            if len(seq_string)>0:
                seq_list.append(seq_string)
                seq_string = ""

    if len(seq_string)>0:
        seq_list.append(seq_string)

    return(seq_list)

#########################################################################################

# function to find longest pattern common among all sequences
def longest_common_motif(f):
    # call sequences_from_fasta_file function to extract dna sequences from fasta files
    dna_sequences = sequences_from_fasta_file(f)
    print "input sequences: %s" % dna_sequences

    # sort the dna_sequences list by length of each sequence
    sorted_seq_list = sorted(dna_sequences, key=len) # using length as key is very important, else it will sort alphabetically

    shortest_sequence = sorted_seq_list[0]
    other_sequences = sorted_seq_list[1:]
    print "shortest sequence in the list: %s" % shortest_sequence
    # print "sequences across which the motif should be searched %s" % other_sequences

    len_shortest_sequence = len(shortest_sequence)
    shared_motif = ""

    for i in range(0,len_shortest_sequence):
        for j in range(len_shortest_sequence, i+len(shared_motif), -1):
            pattern = shortest_sequence[i:j]

            matched_all = True
            for seq in other_sequences:
                if pattern not in seq:
                    matched_all = False
                    break

            if matched_all:
                shared_motif = pattern
                print "shared motif found: %s" % shared_motif
                break

    return(shared_motif)


small_dataset = "/Users/shruti/Downloads/dna_motif.txt"
big_dataset = "/Users/shruti/Downloads/rosalind_lcsm.txt"

print "\nlongest common motif: %s" % longest_common_motif(small_dataset)