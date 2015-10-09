__author__ = 'shruti'
# to print all numbers which appear more than once in a list

x = [1,2,3,4,3,5,6,4,7,8,4,1,1,1]

#for i in range(len(x)):
#    print x[i]

NumberDictionary = {}
for i in range(len(x)):
    if x[i] in NumberDictionary:
        NumberDictionary[x[i]] += 1
    else:
        NumberDictionary[x[i]] = 1

print("dictionary: %s \n" % NumberDictionary)

for key, value in dict.items(NumberDictionary):
    if value>1:
        print ("number: %i frequency: %i" % (key, value))