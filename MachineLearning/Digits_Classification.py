from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn import svm
from sklearn.metrics import confusion_matrix
import random

digits = datasets.load_digits()

# model features
digits_features = digits.data
print "type of iris features %s" % type(digits_features)
print "dimension of iris features %s" % (digits_features.shape,)
# features that can be used to classify the digits samples
print "first three rows of features: \n %s \n" % digits_features[:3,]

# response variables / classes you want to predict
print "classes you want to predict %s" % digits.target_names
digits_classes = digits.target

# each original sample is an image of shape (8, 8) and can be accessed:
print "each original sample is an image of shape (8, 8) \n %s \n" % digits.images[0]

# Data Splitting
random.seed(1)
training_features, test_features, training_classes, test_classes = train_test_split(digits_features, digits_classes, train_size=0.60)
print "dimension of training set: %s" % (training_features.shape,)
print "dimension of test set: %s \n" % (test_features.shape,)


# create Support Vector Classification model
clf = svm.SVC(gamma=0.001, C=100.)
# fit the model on training set
clf.fit(training_features, training_classes)
# apply the classifier on test set
predicted_classes = clf.predict(test_features)
print "confusion Matrix: \n %s" % confusion_matrix(test_classes,predicted_classes)