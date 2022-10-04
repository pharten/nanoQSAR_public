#!/usr/bin/env python
# coding: utf-8

import os

import numpy as np

# Pandas is used for data manipulation
import pandas as pd

# Time is used for timing
import time

# Import the model we are using
from sklearn.ensemble import RandomForestRegressor

# Import sklearn metri
from sklearn.metrics import mean_squared_error

# Import math function square roo
from math import sqrt
# In[2]:

from pathlib import Path

import RandomForest

rf_train = RandomForest

# Read in data and display first 5 rowsj
train_features = RandomForest.readcsv(rf_train, "../data/LD50_training_set-2d.csv")
train_features.head()

# In[3]:


print('The shape of our training features is:', train_features.shape)


# In[4]:


# Descriptive statistics for each column
train_features.describe()


# In[5]:


# Read in data and display first 5 rows
rf_test = RandomForest
test_features = RandomForest.readcsv(rf_test, '../data/LD50_prediction_set-2d.csv')
test_features.head(5)


# In[6]:


print('The shape of our test features is:', test_features.shape)


# In[7]:


# Descriptive statistics for each column
test_features.describe()


# In[9]:


# One-hot encode the data using pandas get_dummies
# train_features = pd.get_dummies(train_features)
# Display the first 5 rows of the last 12 columns
train_features.iloc[:,:].head(5)


# In[10]:


# One-hot encode the data using pandas get_dummies
# test_features = pd.get_dummies(test_features)
# Display the first 5 rows of the last 12 columns
test_features.iloc[:,:].head(5)


# In[11]:


# Labels are the values we want to predict
train_labels = np.array(train_features['Tox'])
# Remove the labels from the features
# axis 1 refers to the columns
train_features = train_features.drop('CAS', axis = 1)
train_features = train_features.drop('Tox', axis = 1)
# Saving feature names for later use
train_features_list = list(train_features.columns)


# In[12]:


# Convert to numpy array
train_features = np.array(train_features)
print('Training Features Shape:', train_features.shape)
print('Training Labels Shape:', train_labels.shape)


# In[13]:


# Labels are the values we want to predict
test_labels = np.array(test_features['Tox'])
# Remove the labels from the features
# axis 1 refers to the columns
test_features = test_features.drop('CAS', axis = 1)
test_features = test_features.drop('Tox', axis = 1)
# Saving feature names for later use
test_features_list = list(test_features.columns)


# In[14]:


# Convert to numpy array
test_features = np.array(test_features)
print('Testing Features Shape:', test_features.shape)
print('Testing Labels Shape:', test_labels.shape)


# In[27]:

t1 = time.time()

# Instantiate model with 1000 decision trees
rf = RandomForestRegressor(n_estimators = 400, random_state = 42, n_jobs = 36)
# Train the model on training data
rf.fit(train_features, train_labels);
t2 = time.time()
print('Time lapse = ',t2-t1)


# In[28]:
print('params = ',rf.get_params(True))


print('Rsq for Training Data = ',rf.score(train_features, train_labels))
# Use the forest's predict method on the train data
train_predictions = rf.predict(train_features)
meanSquaredError=mean_squared_error(train_labels, train_predictions)
rootMeanSquaredError = sqrt(meanSquaredError)
print("RMSE:", rootMeanSquaredError)

# In[29]:


#fimp = rf.feature_importances_
#fnam = rf.features
#print(rf.feature_importances_)


# In[30]:


# Use the forest's predict method on the test data
predictions = rf.predict(test_features)
# Calculate the absolute errors
errors = abs(predictions - test_labels)
# Print out the mean absolute error (mae)
print('Mean Absolute Error:', round(np.mean(errors), 2), 'toxicity.')


# In[31]:


# Calculate mean absolute percentage error (MAPE)
mape = 100 * (errors / test_labels)
# Calculate and display accuracy
accuracy = 100 - np.mean(mape)
print('Accuracy:', round(accuracy, 2), '%.')


# In[32]:


print('Rsq for Test Data = ',rf.score(test_features, test_labels))
# Use the forest's predict method on the train data
meanSquaredError=mean_squared_error(test_labels, predictions)
rootMeanSquaredError = sqrt(meanSquaredError)
print("RMSE:", rootMeanSquaredError)

# In[43]:


importances = rf.feature_importances_
indices = np.argsort(importances)[::-1]

# Print the feature ranking
print("Feature ranking:\n")

for f in range(len(train_features_list)):
    thisimp = importances[indices[f]]
    if thisimp > 1.0e-2:
        print("%d) %s \t= %f" % (f,train_features_list[indices[f]],importances[indices[f]]))

