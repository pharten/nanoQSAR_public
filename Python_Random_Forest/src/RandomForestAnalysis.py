'''
Created on Mar 9, 2021

@author: Wmelende
'''
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
from numpy.core.numeric import indices
#from numpy.array_api._dtypes import float64

class RandomForestAnalysis():
    
    def __init__(self, train_features):
        self.train_features = train_features
            
    def train(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train
        #self.regressor = RandomForestRegressor(n_estimators = 300, n_jobs=4, random_state = 0, min_samples_split=4, max_features=0.25)
        self.regressor = RandomForestRegressor(n_estimators=100, n_jobs=6, random_state=37, min_samples_split=4, max_samples=0.8)
        self.regressor.fit(self.X_train, self.y_train)
        return self.regressor
    
    def predict(self, X_test):
        return self.regressor.predict(X_test)
    
    def Rsq(self, X, y):
        # r2 value = 1 - u/v where u = (((y_train(i)-y_pred(i))**2).sum(i))/n_train
        # and v = (((y_train(i)-y_train(i).avg())**2).sum(i))/n_train
        # this the same self.regressor.score(X,y)
        y_pred = self.regressor.predict(X)
        y_avg = y.mean()
        u = ((y-y_pred)**2).sum() / y.size
        v = ((y-y_avg)**2).sum() / y.size
        return 1.0-u/v
    
    def Qsq(self, X, y):
        # q2 value = 1 - u/v where u = (((y(i)-y_pred(i))**2).sum(i))/y.count()
        # and v = (((y_train(i)-y_train(i).avg()).sum(i))/n_train
        # notice v is based upon self.y_train information, different from what has been used before
        y_pred = self.regressor.predict(X)
        y_avg = self.y_train.mean()
        u = ((y-y_pred)**2).sum() / y.size
        v = ((self.y_train-y_avg)**2).sum() / self.y_train.size
        return 1.0-u/v
    
    # Evaluate the algorithm
    def evaluate(self, X_test, y_test):
        y_pred = self.predict(X_test)
        mean_abs_error = metrics.mean_absolute_error(y_test, y_pred)
        mean_sqr_error = metrics.mean_squared_error(y_test, y_pred)
        root_mean_sqr_error = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
    
        print('Rsq for Training set = ',self.Rsq(self.X_train, self.y_train))
        print('Score for Training set = ',self.regressor.score(self.X_train, self.y_train))
        print('Rsq for Testing set: ',self.Rsq(X_test, y_test))
        print('Score for Testing set: ',self.regressor.score(X_test, y_test))
        print('Qsq for Testing set: ',self.Qsq(X_test, y_test))
        print('Mean absolute error: ', mean_abs_error)
        print('Mean square error: ', mean_sqr_error)
        print('Root mean square error: ', root_mean_sqr_error)
    
        importances = self.regressor.feature_importances_
        indices = np.argsort(importances)[::-1]

    # Print the feature ranking
        print("\nFeature ranking:\n")

        for f in range(len(indices)):
            thisimp = importances[indices[f]]
            if thisimp > 1.0e-3:
                print("%d) %s \t= %f" % (f,self.train_features[indices[f]],importances[indices[f]]))


    