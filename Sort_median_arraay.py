from __future__ import division
import numpy as np

np.random.seed(0)
y = np.random.randint(10, size=5)
print "y: %s" % y

np.random.seed(0)
z = np.random.randint(10, size=6)
print "z: %s \n" % z

############ Mean ###############
def Mean(x):
    l = len(x)
    s = 0
    for i in range(l):
        s += x[i]
    return(s/l)

print ("mean of y: %s" % Mean(y))
print ("mean of z: %s \n" % Mean(z))
####################################

############ Sort / Min / Max ############

def Sort(x):
    for i in range(len(x)-1):
        for j in range(len(x)-1):
            if x[j] > x[(j+1)]:
                temp = x[j]
                x[j] = x[(j+1)]
                x[(j+1)] = temp
    return(x)

sorted_array_y = Sort(y)
print("minimum of y: %s" % sorted_array_y[0])
print("maximum of y: %s \n" % sorted_array_y[len(sorted_array_y)-1])

sorted_array_z = Sort(z)
print("minimum of z: %s" % sorted_array_z[0])
print("maximum of z: %s \n" % sorted_array_z[len(sorted_array_z)-1])
####################################

############ Median ###############

def Median(x):
    l = len(x)
    sorted_array = Sort(x)

    if l%2!=0:
        # In Python 3.0, 5 / 2 will return 2.5 and 5 // 2 will return 2 . The former is floating point division, and the latter is floor division
        median_index =  l//2
        median = sorted_array[median_index]
    else:
        median_index = l/2
        median = (sorted_array[median_index-1] + sorted_array[median_index])/2
    return(median)

print("Median of y: %s" % Median(y))
print("Median of z: %s" % Median(z))
####################################