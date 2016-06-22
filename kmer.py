# Given a file of reads, find reads which have complete match of sequences for k bases.
def kmer(seq_list,id_list,k):
    match = []
    matched_bases = {}

    # compare sequences to all the following sequences in the list
    for i in range(len(seq_list)-1):
        # loop through each index in ith sequence to select k elements. there is no need to look last k-1 indices
        for j in range(len(seq_list[i])-(k-1)):
            # search for the above k elements in each of following sequences in the list
            for m in range(i+1,len(seq_list)):
                if seq_list[i][j:j+k] in seq_list[m]:
                    # print seq_list[i][j:j+k]
                    # print seq_list[m]
                    # print "\n"
                    match.append([seq_list[i][j:j+k], id_list[i], id_list[m]])

                    if seq_list[i][j:j+k] not in matched_bases:
                        matched_bases[seq_list[i][j:j+k]] = [ id_list[i], id_list[m] ]
                    else:
                        matched_bases[seq_list[i][j:j+k]].append([id_list[i], id_list[m]])

    #print match
    return matched_bases

sequence_list = ["ATGCTAGC", "TTGCATA", "CTGCTAT"]
identifier_list = ["seq1","seq2","seq3"]

print kmer(sequence_list,identifier_list,3)