# commands using numpy to manipulate arrays (matrices)

import numpy as np

# array/matrix with single row
data1 = [2,3,4]
array1 = np.array(data1)
print "list1: %s" % data1
print "array1: %s " % array1
print "value of index two: %s \n" % array1[1]

# array/matrix with multiple rows
data2 = [ [1,2,3],[6,7,8],[10,11,12] ]
print "list2: %s" % data2
array2 = np.array(data2)
print "array2: \n %s" % array2
print "row2, column1 of array2: %s" % array2[1,0]
print "row2 of array2: %s" % array2[1,:]
print "column3 of array2: %s" % array2[:,2]
print "first 2rows and columns 2,3rd of array2: \n %s" % array2[:2,1:]
print "first 2rows and columns 1,2 of array2: \n %s" % array2[0:2,:2]
print "dim of array2: %s" % (array2.shape,)
print "no.of rows of array2: %s \n" % array2.ndim

# use shape than ndim to get number of rows or columns
print np.array([1,2,3,4,5]).ndim
print np.array([[1,2,3],[6,7,8]]).ndim
print np.array([ [1,2,3],[6,7,8],[10,11,12],[10,11,12] ]).ndim
# number of rows
print np.array([ [1,2,3],[6,7,8],[10,11,12],[10,11,12] ]).shape[0]

# multidimensional arrays
array3 = np.array([ [[1,2,3],[4,5,6]] , [[7,8,9],[10,11,12]], [[13,14,15],[16,17,18]] ])
print "\n array3: \n %s" % array3
print "dimension of array3: \n %s" % (array3.shape,)
print "2nd matrix of array3: \n %s" % array3[1]
print "2nd row, column 2,3 of matrix1 of array3: \n %s \n" % array3[0,1,1:]

# boolean indexing
names = np.array(["c","a","b","c"])
print names
data4 = np.random.randn(4,3)
print "%s \n" % data4
print(names == "c")
print "rows with name c: \n %s \n" % (data4[names == "c"])
print "rows with name c and last two columns: \n %s \n" % (data4[names == "c",1:])
print "rows with name b or c: \n %s \n" % (data4[(names == "c")| (names == "b")])

print "rows where c==False: \n %s \n" % (data4[names != "c"])
print "rows where c==False: \n %s \n" % (data4[-(names == "c")])

# transpose
data5 = np.arange(12).reshape(3,4)
print "array5: \n %s \n" % data5
# transpose of 2-dimensional array
print "transpose of array5: \n %s \n" % data5.T
data6 = np.arange(36).reshape(3,3,4)
print "array6: \n %s \n" % data6
# transpose of multi-dimensional array. take transpose of each matrix
print "transpose of array6: \n %s \n" % data6.swapaxes(1,2)
# transpose of multi-dimensional array. swap the rows between matrices
print "transpose of array6: \n %s \n" % data6.transpose(1,0,2)

# statistical functions
print "array1: %s " % array1
print "mean array1: %s " % array1.mean()
print "mean array1: %s \n" % np.mean(array1)

print "mean array2: \n %s" % array2
print "mean array2: %s " % array2.mean()
print "mean array2 along rows: %s " % array2.mean(axis=1)
print "mean array2 along columns: %s " % array2.mean(axis=0)
# cumulative sum of elements row-wise. add all previous rows values to next row
print "cumulative sum of elements row-wise: \n %s" % array2.cumsum(0)
# cumulative sum of elements column-wise. add all previous column to next column
print "cumulative sum of elements column-wise: \n %s" % array2.cumsum(1)
# cumulative product of elements column-wise
print "cumulative product of elements row-wise: \n %s \n" % array2.cumprod(1)

# multiply each element of x by 5
x = [1, 2, 3, 4]
print x
# wrong way
print x * 5

# using for loop
y = [None] * len(x)
for i in range(len(x)):
    y[i] = x[i] * 5
print y

# list comprehension
z = [i * 5 for i in x]
print z

# using numpy
x = np.array([1, 2, 3, 4])
w = x * 5
print w