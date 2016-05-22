import sklearn
import pandas as pd

training_set = pd.read_csv("/Users/shruti/Desktop/WorkMiscellaneous/MachineLearning/SanFranciscoCrime/final_training_set.csv", index_col=0)
print (training_set.shape)
print (training_set.head(3))
print (training_set.iloc[0:4,0:4])

training_output = pd.read_csv("/Users/shruti/Desktop/WorkMiscellaneous/MachineLearning/SanFranciscoCrime/training_output.csv", index_col=0)
print (training_output.shape)
print (training_output.head(3))
print (training_output.iloc[0:4,])

