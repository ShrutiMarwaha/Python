import pandas as pd
import numpy as np
from numpy import genfromtxt
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import KFold
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

features = pd.read_csv("/Users/shruti/Desktop/WorkMiscellaneous/MachineLearning/SanFranciscoCrime/dataset_dummy_variables.csv")
print(features.shape)
print(features.head(3))
print(features.iloc[0:4,0:4])

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

model = LogisticRegression()
model.fit(features_train, outcomes_train)

# make predictions
expected = outcomes_test
predicted = model.predict(features_test)

# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
model.coef_

############### run Cross Validation on training data
kf = KFold(n=len(features_train), n_folds=10, random_state=0)

for cv_train_index, cv_test_index in kf:
    X_train, X_test = features_train.iloc[cv_train_index,], outcomes_train[cv_train_index,]
    y_train, y_test = features_train.iloc[cv_test_index,], outcomes_train[cv_test_index,]

scores = []
for cv_train_index, cv_test_index in kf:
    model_fit = model.fit(features_train.iloc[cv_train_index,], outcomes_train[cv_train_index,])
    #print(model_fit.score(features_train.iloc[cv_test_index,],outcomes_train.iloc[cv_test_index,]))
    scores.append(model_fit).score(features_train.iloc[cv_test_index,],outcomes_train[cv_test_index,])

scores
np.mean(scores)