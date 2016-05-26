# import required packages
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import svm
from sklearn.naive_bayes import BernoulliNB
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, accuracy_score
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import KFold
from sklearn import cross_validation

# load features data
features = pd.read_csv("/Users/shruti/Desktop/WorkMiscellaneous/MachineLearning/SanFranciscoCrime/dataset_dummy_variables.csv")
print(features.shape)
print(features.head(3))
print(features.iloc[0:4,0:4])

# load classes to be predicted
outcomes = pd.read_csv("/Users/shruti/Desktop/WorkMiscellaneous/MachineLearning/SanFranciscoCrime/outcomes.csv",header=None,squeeze=True)
outcomes.shape
outcomes_frequency = outcomes.value_counts(ascending=True)
outcomes_frequency.head()

# divide data in to training and intermediate set
features_train, features_intermediate, outcomes_train, outcomes_intermediate = train_test_split(features,outcomes,test_size=0.4,random_state=0)

# divide intermediate set into test and validation set. validation set will be only used once to evalaute final model's performance
features_test, features_validation, outcomes_test, outcomes_validation = train_test_split(features_intermediate,outcomes_intermediate,test_size=0.5,random_state=0)
print(features_train.shape)
print(features_test.shape)
print(features_validation.shape)

# build the model
model = LogisticRegression(n_jobs=-1,random_state=0)
#model = RandomForestClassifier(n_estimators=200,max_depth=15,n_jobs=-1,random_state=0)
#model = BernoulliNB()
#model = SVC() # donot try, takes very very long
#model= GradientBoostingClassifier(random_state=0) # takes very long
model.fit(features_train, outcomes_train)

# make predictions
expected = outcomes_test
predicted = model.predict(features_test)

# summarize the fit of the model
print(classification_report(expected, predicted))
print(confusion_matrix(expected, predicted))
print(roc_auc_score(expected, predicted)) # predicted outputs have to be binarized
print(accuracy_score(expected, predicted))

###################### Grid Search with Cross Validation ######################
# to run k-fold cross validation, remove classes which are less than "k" samples.
# cv< minimum no.of samples in each class. So either remove such samples or use KFold
outcomes_frequency.head()
outcomes_frequency[outcomes_frequency < 10 ]
matchings_indices = [ i for i, value in enumerate(outcomes) if value == "TREA" ]
# for i, value in enumerate(outcomes):
#             if value == "TREA":
#                 print i
outcomes[matchings_indices]
# remove these samples from features and outcomes data
outcomes2 = outcomes.drop(matchings_indices)
features2 = features.drop(matchings_indices)

# divide data in to training and intermediate set
features_train, features_intermediate, outcomes_train, outcomes_intermediate = train_test_split(features2,outcomes2,test_size=0.4,random_state=0)

# divide data in to intermediate set into test and validation set. validation set will be only used once to evalaute final model's performance
features_test, features_validation, outcomes_test, outcomes_validation = train_test_split(features_intermediate,outcomes_intermediate,test_size=0.5,random_state=0)
print(features_train.shape)
print(features_test.shape)
print(features_validation.shape)

# select the machine learning algorithm you want to apply
algo = LogisticRegression(random_state=0,n_jobs=-1)
# algo = RandomForestClassifier(random_state=0,n_jobs=-1)
# algo = BernoulliNB()
# algo = GradientBoostingClassifier()

# param_grid is dictionary where key is parameter name and value is the numeric values you want to try for that parameter
# parameter grid for Logistic Regression
param_grid = {'C': [0.01, 0.1, 1, 10, 100]}
# # parameter grid for Random Forest
# param_grid = {'n_estimators': [10, 100, 200], 'max_depth': [None,15,30], 'max_features': ['sqrt','log2']}
# # parameter grid for Naive Bayes
# param_grid = {'alpha': [0.01, 0.1, 1, 10, 100]}
# # parameter grid for Gradient Boosting Classifier
# param_grid = {'learning_rate': [0.1,1,10], 'max_depth': [3,10,15], 'n_estimators': [100, 500, 1000], 'max_features': ['sqrt','log2']}

model = GridSearchCV(algo, param_grid, cv=10, scoring='accuracy')
# TODO: model = GridSearchCV(algo, param_grid, cv=10, scoring='f1_samples',n_jobs=-1) ; gives error
# scoring: f1_samples (for multilabel sample); f1 (for for binary targets); accuracy (for model accuracy)
model.fit(features_train, outcomes_train)

# model scores for each parameter used in grid
model.grid_scores_
# examine the best model
print model.best_score_
print model.best_params_
print model.best_estimator_

# now create model with the best parameters
model = LogisticRegression(solver='lbfgs',multi_class='multinomial',n_jobs=-1,random_state=0,C=1)
# model = RandomForestClassifier(n_estimators=200,max_depth=15,n_jobs=-1,random_state=0)
# model = BernoulliNB(alpha=300)
# TODO: model = GradientBoostingClassifier(random_state=0)

# make predictions. GridSearchCV automatically refits the best model
predicted = model.predict(features_test)

# summarize the fit of the model
print(classification_report(expected, predicted))
print(confusion_matrix(expected, predicted))

# use RandomizedSearchCV searches a subset of the parameters to reduce computational expense