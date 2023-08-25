'''
Created on Jul 26, 2022

@author: PHARTEN
'''

import pandas as pd
import numpy
import random

from sklearn.model_selection import train_test_split, KFold

from Extract_X_and_Y_Matrices import extract_X_Y_matrices
from Transform_DataFrames_to_Arrays import transform_dataframes_to_arrays

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score, cross_val_predict, cross_validate
from sklearn.metrics import r2_score
from tokenize import Double
from _operator import index

def main():
    desired_result = "viability"
    #desired_result = "expression levels"

    # input_Imputed_Values = "..\\data\\Imputed_Numerical_Columns.csv"
    input_Imputed_Values = "..\\data\\Multivariate_Imputed_Numerical_Columns.csv" 
    
    # Read X and Y matrices from CSV files.
    df = pd.read_csv(input_Imputed_Values, na_values = "NULL", skip_blank_lines = False, 
                     keep_default_na = True, na_filter = False, low_memory = False,
                     encoding = 'utf-8-sig')
    
    # Extract X and Y matrices
    dfX, dfY = extract_X_Y_matrices(desired_result, df)
    
    # Keep features from dfX
    #train_features = list(dfX.columns)
    
    # Transform X and y DataFrames to arrays.
    XFull = dfX.to_numpy()
    yFull = dfY.to_numpy()
    
    # sklearn RandomForestRegressor
    rfa = RandomForestRegressor(n_estimators=200, n_jobs=10, random_state=37, min_samples_split=4, max_samples=0.8)
    
    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 37)
    # scramble arrays X and y

    random.seed(0)
    n = len(yFull)
    for i in range(n):
        ranint = random.randint(0,n-1)
        row = XFull[i].copy()
        XFull[i] = XFull[ranint]
        XFull[ranint] = row
        elem = yFull[i].copy()
        yFull[i] = yFull[ranint]
        yFull[ranint] = elem

    """
    ns = 6
    n = len(yFull)
    nsplit = int(n*((ns-1)/ns))
    
    # divide up XFull, yFull between X, y and XSave, ySave
    X = XFull[0:nsplit]
    y = yFull[0:nsplit]
    XSave = XFull[nsplit:n]
    ySave = yFull[nsplit:n]
    """
    X = XFull
    y = yFull
    
    index = 0
    ns = 5
    r2_train = numpy.zeros(ns)
    r2_test = numpy.zeros(ns)
    kf = KFold(n_splits=ns, shuffle=False)
    for train, test in kf.split(X):
        X_train, X_test, y_train, y_test = X[train], X[test], y[train], y[test]
        rfa.fit(X_train, y_train)
        r2_train[index] = rfa.score(X_train,y_train)
        r2_test[index] = rfa.score(X_test, y_test)
        print(" r2_train = %f, r2_test = %f" % (r2_train[index], r2_test[index] ))
        index += 1

    print(" r2_train = %f +/- %f, r2_test = %f +/- %f" % (r2_train.mean(), r2_train.std(), r2_test.mean(), r2_test.std()))
    
    print ("\n",cross_val_score(rfa, X, y, cv=ns))

    """
    rfa.fit(X, y)
    r2_trains = rfa.score(X, y)
    r2_save = rfa.score(XSave, ySave)
    print("\n r2_trains = %f, r2_save = %f" % (r2_trains, r2_save ))
    """
    
if __name__ == "__main__":
    main()
