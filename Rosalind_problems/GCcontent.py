import math
import re
import numpy as np
from Sequence import SequenceUtils

#filename = "/Users/shruti/Documents/Python/DNAfile.txt"
filename = "/Users/shruti/git/Python/Rosalind_problems/datasets/DNAfile.txt"
file_object = open(filename, 'r')
file_content = file_object.read()
# remove white space from starting and end of the file
file_content = file_content.strip()
# split the data by newline character
content = file_content.split("\n")
print "Solution -1"

sequence_array = np.empty((len(content)/2, 3), dtype=object)

for i in range(0, (len(content)/2)):
    # extract rosalind id
    identifier = content[2*i].strip()
    if(identifier.startswith(">Rosalind")):
        sequence_array[i][0] = identifier
        # extract the sequence
        sequence = content[2*i+1].strip()
        sequence_array[i][1] = sequence
        # calculate GC content in sequence
        #sequence_array[i][2] = sequence.count("G") + sequence.count("C")
        GCcontent = float(len(re.findall("G|C",sequence)))/float(len(sequence))*100
        sequence_array[i][2] = round(GCcontent,4)
    else:
        print "Invalid Input"

print "marix: %s \n" % sequence_array
print sequence_array[:,2].max()
print "maximum GC content: %s" % sequence_array[2,(0,2)]



print "\nSolution-2"
sequences = SequenceUtils.get_sequences_from_content(content)
maxSequence = SequenceUtils.find_max_sequence(sequences)
maxSequence.print_sequence()

