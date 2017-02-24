#generate sequence of chromosomes and write to a file
chr_comma_sep = open("chr_comma_sep.txt", "w")

chr_list = []
for i in range(1,23) + ['M', 'X', 'Y', 'MT']:
    chr_name = 'chr' + str(i)
    chr_list.append(chr_name)

chr_comma_sep.write(chr_list)
chr_comma_sep.close()


# chr_file = open("chromosome_notation_rtg.txt", "w" )
#
# for i in range(1,23) + ['M', 'X', 'Y']:
#     line = str(i) + ' ' + 'chr' + str(i) + "\n"
#     chr_file.write(line)
#     print(line)
#
# chr_file.close()
