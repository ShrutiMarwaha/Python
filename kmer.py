# Given a file of reads, find reads which have complete match of sequences for k bases.

def kmer(seq_list,id_list,k):
    # dictionary containing different "k" bases from each sequence
    kseq = {}
    # dictionary containing k bases which are common across sequences
    matched_seq = {}

    for i in range(len(seq_list)):
        for j in range(len(seq_list[i])-(k-1)):
            if seq_list[i][j:j+k] not in kseq:
                # if the k-bases are not present in the dictionary, add the k-bases as key and the sequence id as value.
                # since the values should be unique, store the values as set and not as lists
                kseq[ seq_list[i][j:j+k] ] = {id_list[i]}
            else:
                kseq[seq_list[i][j:j+k]].add(id_list[i])

    for key, value in kseq.iteritems():
        if len(value) >1:
            matched_seq[key] = value

    return(matched_seq)


sequence_list = ["ATGCTAGC", "TTGCATA", "CTGCTGAT"]
identifier_list = ["seq1","seq2","seq3"]

print kmer(sequence_list,identifier_list,3)



