# http://rosalind.info/problems/grph/
# For a collection of strings and a positive integer k, the overlap graph for the strings is a directed graph O-k
# in which each string is represented by a node, and string s is connected to string t with a directed edge
# when there is a length k suffix of s that matches a length k prefix of t, as long as s!=t; we demand s!=t to
# prevent directed loops in the overlap graph (although directed cycles may be present).

# Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
# Return: The adjacency list corresponding to O3O3. You may return edges in any order.

import re

file = "/Users/shruti/Downloads/rosalind_grph.txt"

print file

def get_prefix(seq, k):
    return seq[:k]

def get_suffix(seq, k):
    l = len(seq)
    return seq[(l-k):l]

def OverlapGraph(filename,k):

    try:
        sequence_file = open(filename,"r")
    except IOError:
        print("the file does not exist")

    sequence_identifier = []
    sequences_list = []
    sequence_string = ""

    for line in sequence_file:
        # discard any newline character at the end
        line = line.rstrip()
        # if the line does not start with ">", add it to sequence_string
        if re.search("^[^>]",line):
            sequence_string += line
        else:
            # add the sequence identifier
            sequence_identifier.append(line[1:])
            # if sequence_string is not empty, add it to the string_list and then empty the sequence_string to add next sequence
            if len(sequence_string) != 0:
                sequences_list.append(sequence_string)
                sequence_string = ""

    # the last sequence will not be followed by a >, the dna_string that
    # contains the last sequence will not be appended to dna_list.
    if len(sequence_string)!=0:
                sequences_list.append(sequence_string)

    print "sequence identifiers: %s" % sequence_identifier
    print "sequences: %s \n" % sequences_list

    overlapping_seq = []
    for i in range(len(sequences_list)):
        for j in range(i+1,len(sequences_list)):
            seq_a = sequences_list[i]
            seq_a_id = sequence_identifier[i]

            seq_b = sequences_list[j]
            seq_b_id = sequence_identifier[j]

            # if sequences are equal. don't process
            if seq_a != seq_b:
                if get_suffix(seq_b, k) == get_prefix(seq_a,k):
                    overlapping_seq.append([seq_b_id, seq_a_id])

                if get_suffix(seq_a, k) == get_prefix(seq_b,k):
                    overlapping_seq.append([seq_a_id, seq_b_id])

    for seq in overlapping_seq:
        print "%s %s" % (seq[0],seq[1])

    return ("\nadjacency list: %s" % overlapping_seq)

print OverlapGraph(file,3)


