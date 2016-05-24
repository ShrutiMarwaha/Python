# import required packages
import pandas as pd
import numpy as np
from numpy import genfromtxt
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.naive_bayes import BernoulliNB
from sklearn import cross_validation
from sklearn import metrics

# load features data
features = pd.read_csv("/Users/shruti/Desktop/WorkMiscellaneous/MachineLearning/SanFranciscoCrime/dataset_dummy_variables.csv")
print(features.shape)
print(features.head(3))
print(features.iloc[0:4,0:4])

# load classes to be predicted
outcomes = genfromtxt("/Users/shruti/Desktop/WorkMiscellaneous/MachineLearning/SanFranciscoCrime/outcomes.csv", delimiter=',',dtype=None)
print(outcomes.shape)
print(outcomes[0:4])
print(len(np.unique(outcomes)))

# divide data in to training and intermediate set
features_train, features_intermediate, outcomes_train, outcomes_intermediate = train_test_split(features,outcomes,test_size=0.4,random_state=0)
# divide data in to intermediate set into test and validation set. validation set will be only used once to evalaute final model's performance
features_test, features_validation, outcomes_test, outcomes_validation = train_test_split(features_intermediate,outcomes_intermediate,test_size=0.5,random_state=0)
print(features_train.shape)
print(features_test.shape)
print(features_validation.shape)

model = LogisticRegression(n_jobs=-1,random_state=0)
#model = RandomForestClassifier(n_estimators=200,max_depth=15,n_jobs=-1,random_state=0)
#model = BernoulliNB()
#model = SVC()

model.fit(features_train, outcomes_train)

# make predictions
expected = outcomes_test
predicted = model.predict(features_test)

# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
model.coef_

# Cross Validation
# divide data in to training and test set
features_train, features_test, outcomes_train, outcomes_test = train_test_split(features,outcomes,test_size=0.25,random_state=0)

# Cross Validation on training data
# scores = cross_validation.cross_val_score(model, features_train, outcomes_train, cv=10)
# TODO: 10 fold will not work as one of the class has only 4 samples. cv< minimum no.of samples in each class. So either remove such samples or use KFold
# print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

kf = KFold(n=len(features_train), n_folds=10, random_state=0)
scores = []
for cv_train_index, cv_test_index in kf:
    model_fit = model.fit(features_train.iloc[cv_train_index,], outcomes_train[cv_train_index,])
    #print(model_fit.score(features_train.iloc[cv_test_index,],outcomes_train.iloc[cv_test_index,]))
    scores.append(model_fit.score(features_train.iloc[cv_test_index,],outcomes_train[cv_test_index,]))

scores
np.mean(scores)

# using grid search
from sklearn import grid_search
param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000] }
ml_algo = LogisticRegression()
model = grid_search.GridSearchCV(ml_algo, param_grid)
model.fit(features_train, outcomes_train)