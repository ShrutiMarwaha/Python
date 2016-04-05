# http://rosalind.info/problems/grph/
# For a collection of strings and a positive integer k, the overlap graph for the strings is a directed graph O-k
# in which each string is represented by a node, and string s is connected to string t with a directed edge
# when there is a length k suffix of s that matches a length k prefix of t, as long as s!=t; we demand s!=t to
# prevent directed loops in the overlap graph (although directed cycles may be present).

# Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
# Return: The adjacency list corresponding to O3O3. You may return edges in any order.

import re

file = "/Users/shruti/PycharmProjects/firstProject/Fasta_overlap_graphs.txt"
#file = "/Users/shruti/Downloads/rosalind_grph.txt"
#file = "/Users/shruti/Downloads/test.txt"

# define a class called Sequence which will contain sequence identifier and the sequence
class Sequence:

    def __init__(self, id, seq):
        self.id = id
        self.seq = seq

# function to extract first "k" characters from a sequence
def get_prefix(seq, k):
    return seq[:k]

# function to extract last "k" characters from a sequence
def get_suffix(seq, k):
    l = len(seq)
    return seq[(l-k):l]

def overlap_graph(filename, k):
    # load the file
    try:
        sequence_file = open(filename,"r")
    except IOError:
        print("the file does not exist")

    sequence_list = []
    sequence = None
    for line in sequence_file:
        line = line.rstrip()

        if re.search("^>",line):
            seq_id = line[1:]
            sequence = Sequence(seq_id, "")
            sequence_list.append(sequence)
        else:
            sequence.seq = sequence.seq + line

    overlapping_seq = []
    for i in range(len(sequence_list)):
        for j in range(i+1,len(sequence_list)):
            seq_a = sequence_list[i]
            seq_b = sequence_list[j]

            # if sequences are equal. don't process
            if seq_a.seq != seq_b.seq:
                if get_suffix(seq_b.seq, k) == get_prefix(seq_a.seq,k):
                    overlapping_seq.append([seq_b.id, seq_a.id])

                if get_suffix(seq_a.seq, k) == get_prefix(seq_b.seq,k):
                    overlapping_seq.append([seq_a.id, seq_b.id])

    for seq in overlapping_seq:
        print "%s %s" % (seq[0],seq[1])

    return ("\nadjacency list: %s" % overlapping_seq)

print overlap_graph(file,3)


