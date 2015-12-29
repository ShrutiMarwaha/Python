# The Social Security administration has this neat data by year of what names are most popular for babies born that year in the USA (see social security baby names).
# The files baby1990.html baby1992.html ... contain raw html, similar to what you get visiting the above social security site.
# Write function which takes the filename of a baby1990.html file and returns the data from the file as a single list -- the year string at the start of the list followed by the name-rank strings in alphabetical order.
# eg ['2006', 'Aaliyah 91', 'Abagail 895', 'Aaron 57', ...].


def popular_babynames(filename):
    import re # for regular expression

    try:
        file_object = open(filename,"r")
    except IOError:
        print ("file doesnt exist")
    file_content = file_object.read()
    file_object.close()

    output_list = []

    # find the year
    matched_year = re.search("Popularity in (\d{4})",file_content)
    if matched_year is not None:
        output_list.append(matched_year.group(1))
    else:
        print("file doesn't contain year information")

    # find ranks and boy and girl name and store it as list of tupules
    name_rank_list = re.findall("<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>",file_content)
    # store names associated with each rank as key value pair in a dictionary
    name_rank_dict = {}
    for name in name_rank_list:
        # if the boyname is not already in dictionary, add it as key and rank as value
        if name[1] not in name_rank_dict:
            name_rank_dict[name[1]] = name[0]
        # if the girlname is not already in dictionary, add it as key and rank as value
        if name[2] not in name_rank_dict:
            name_rank_dict[name[2]] = name[0]

    # list containing names in sorted in alphabetical order
    sorted_names = (sorted(name_rank_dict.keys()))
    # append the names (key) and values (rank) from dictionary to output list in the order of sorted_names list
    for i in sorted_names:
        output_list.append(i + " " + name_rank_dict[i])

    return(output_list)


#print(popular_babynames("baby1992.html"))


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


def main():
    test(popular_babynames("baby1992.html")[0],"1992")
    test(popular_babynames("baby2006.html")[1],"Aaliyah 91")
    test( (popular_babynames("baby2000.html")[3],popular_babynames("baby2000.html")[8]), ('Abagail 953', 'Abdullah 870') )

if __name__ == '__main__':
  main()

