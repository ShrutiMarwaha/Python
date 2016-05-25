# import required packages
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import svm
from sklearn.naive_bayes import BernoulliNB
from sklearn.grid_search import GridSearchCV

from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import KFold
from sklearn import cross_validation
from sklearn import metrics

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
#model = SVC() # donot try, takes very long
#model= GradientBoostingClassifier(random_state=0)
model.fit(features_train, outcomes_train)

# make predictions
expected = outcomes_test
predicted = model.predict(features_test)

# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))


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
outcomes2 = outcomes.drop(matchings_indices)

# divide data in to training and intermediate set
features_train, features_intermediate, outcomes_train, outcomes_intermediate = train_test_split(features,outcomes2,test_size=0.4,random_state=0)
# divide data in to intermediate set into test and validation set. validation set will be only used once to evalaute final model's performance
features_test, features_validation, outcomes_test, outcomes_validation = train_test_split(features_intermediate,outcomes_intermediate,test_size=0.5,random_state=0)

# select the malchine learning algorithm you want to apply
algo = LogisticRegression()

# param_grid is dictionary where key is parameter name and value is the numeric values you want to try for that parameter
param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000] }
model = GridSearchCV(algo, param_grid, cv=10, scoring='accuracy',n_jobs=-1,random_state=0)
model.fit(features_train, outcomes_train)

# examine the best model
print model.best_score_
print model.best_params_
print model.best_estimator_

# make predictions. GridSearchCV automatically refits the best model
predicted = model.predict(features_test)

# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))