# python script for learning to work with arrays and dataframes using pandas.
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
# series is 1-D array like object and associated array of data labels - index. Series is dataframe with one column
obj1 = Series([1,3,5,-6,2])
print "%s \n" % obj1
print "%s \n" % obj1.values
print "%s \n" % obj1.index

obj2 = Series([1,3,5,-6], index=["d","b","a","c"])
print "%s \n" % obj2
print "%s \n" % obj2["b"]
print "%s \n" % obj2["b":"c"]
# sort series by its values
print "%s \n" % obj2.sort_values()
# sort series by index
print "%s \n" % obj2.sort_index()

# create Series from dictionary
sdata = {"ohio":3500, "texas":7100, "oregon":1600, "utah":500}
sdata
obj3 = Series(sdata)
print "%s \n" % sdata
print "%s \n" % obj3

# Dataframe
data={"state":["ohio","ohio","nevada"],
      "year":[2000,2001,2002],
      "pop":[1.5,1.7,3.6]}
print "%s \n" % data
frame=DataFrame(data,columns=["year","state","pop"],index=["one","two","three"])
print "%s \n" % frame
print "%s \n" % frame["state"]
print "%s \n" % frame.year
print "%s \n" % frame.ix["two"]

data2=DataFrame( np.arange(9).reshape(3,3), index=["three","one","four"], columns=["c","a","d"] )
# sort lexicographically by row index
print "sort lexicographically by row index: \n %s \n" % data2.sort_index()
# sort lexicographically by column index
print "sort lexicographically by column index: \n %s \n" % data2.sort_index(axis=1)

