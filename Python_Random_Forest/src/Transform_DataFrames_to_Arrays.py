'''
Created on Mar 4, 2021

@author: Wmelende
'''

def transform_dataframes_to_arrays(dfX_train, dfX_test, dfy_train, dfy_test):
    # Transform X DataFrames to arrays.
    X_train = dfX_train.iloc[:,:].values
    X_test = dfX_test.iloc[:,:].values

    # Transform y DataFrames to arrays.
    y_train = dfy_train['viability result_value'].values
    y_test = dfy_test['viability result_value'].values
    
    return X_train, y_train, X_test, y_test