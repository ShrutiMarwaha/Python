from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
import random

# input data for scikit is n_samples, n_features array where samples are rows and features are columns.
iris = datasets.load_iris()
print (iris.keys())
#print (iris.values())

# model features
print ("features: %s \n") % iris.feature_names
iris_features = iris.data
print "type of iris features %s" % type(iris_features)
print "dimension of iris features %s" % (iris_features.shape,)

# response variables / classes you want to predict
print "classes you want to predict %s" % iris.target_names
iris_classes = iris.target
print "dimension of iris classes %s \n" % iris_classes.shape

# Data Visualization
x_index = 0
y_index = 1

# this formatter will label the colorbar with the correct target names
formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])

plt.scatter(iris_features[:, x_index], iris_features[:, y_index],
            c=iris_classes, cmap=plt.cm.get_cmap('RdYlBu', 3))
plt.colorbar(ticks=[0, 1, 2], format=formatter)
plt.clim(-0.5, 2.5)
plt.xlabel(iris.feature_names[x_index])
plt.ylabel(iris.feature_names[y_index])

# dimensionality reduction
model_pca = PCA(n_components=2)
model_pca.fit(iris_features)
reduced_iris_features = model_pca.transform(iris_features)
#print "dimension of iris features %s" % (iris_features.shape,)
print "dimension of reduced features %s \n" % (reduced_iris_features.shape,)

random.seed(1)
training_features, test_features, training_classes, test_classes = train_test_split(iris_features, iris_classes, train_size=0.60)
print "dimension of training set: %s" % (training_features.shape,)
print "dimension of test set: %s \n" % (test_features.shape,)

# create Support Vector Classification model
#SVC?
model = SVC()
#print (model)

# fit the model
model.fit(training_features,training_classes)

# What kind of iris has 3cm x 5cm sepal and 4cm x 2cm petal?
# call the "predict" method:
result = model.predict([[3,5,4,2],])
print(iris.target_names[result])

print (model.predict(iris_features[::10])) # [::y] prints every yth element from the list / array
print ((iris_classes[::10]))

predicted_classes = model.predict(test_features)
# numpy.all : Test whether all array elements along a given axis evaluate to True.
print(np.all(test_classes == predicted_classes))

print "confusion Matrix: \n %s" % (confusion_matrix (test_classes,predicted_classes) )