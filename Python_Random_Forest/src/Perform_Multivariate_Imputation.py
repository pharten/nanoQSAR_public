'''
Created on Apr 1, 2021

@author: Wmelende and pharten
'''

import pandas as pd
import numpy as np
import sympy as sym
from math import isnan

# SKLearn explicitly requires this experimental feature
from sklearn.experimental import enable_iterative_imputer
# Now we can import normally from sklearn.impute
from sklearn.impute import IterativeImputer

from sklearn.linear_model import BayesianRidge
from pandas.tests.test_nanops import skipna
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.ensemble import ExtraTreesRegressor
# from sklearn.neighbors import KNeighborsRegressor
from UtilRecords import read_from_csv, write_to_csv, delete_columns_with_all_equal_values,\
    replace_null_with_none
#from pandas._libs.missing import NA
from pyparsing import And
from numpy import NaN, nan

def iteratively_impute_numerical_columns(desired_type, df):
    
    # Extract column names
    column_names = list(df.columns)
    
    # Use other OuterDiameter values
    if ('OuterDiameterValue' in column_names):
        if ('OuterDiameterLow' in column_names):
            df['OuterDiameterLow'] = df['OuterDiameterLow'].fillna(df['OuterDiameterValue'])
        if ('OuterDiameterHigh' in column_names):    
            df['OuterDiameterHigh'] = df['OuterDiameterHigh'].fillna(df['OuterDiameterValue'])
        if ('OuterDiameterLow' in column_names and 'OuterDiameterHigh' in column_names):
            df['OuterDiameterValue'] = df['OuterDiameterValue'].fillna(0.5*(df['OuterDiameterLow']+df['OuterDiameterHigh']))
    else:
        if ('OuterDiameterLow' in column_names and 'OuterDiameterHigh' in column_names):
            df['OuterDiameterLow'] = df['OuterDiameterLow'].fillna(df['OuterDiameterHigh'])
            df['OuterDiameterHigh'] = df['OuterDiameterHigh'].fillna(df['OuterDiameterLow'])
            
    # set missing temperature values to default 25C.
    if ('temperature parameter_value' in column_names):
        df['temperature parameter_value'] = df['temperature parameter_value'].fillna(value = 25.0) 
        
    # set missing fetal bovine additive_value to default 10.0
    if ("fetal bovine serum additive_value" in column_names):
        df["fetal bovine serum additive_value"] = df["fetal bovine serum additive_value"].fillna(value = 10.0)      
    
    # Define list with possible parameter columns.
    param_names = ['OuterDiameterValue', 'OuterDiameterLow', 'OuterDiameterHigh',
                    'SurfaceAreaValue', 
                    'Purity', 'HydrodynamicDiameterValue', 'ChargeAvg', 
                    'particle concentration parameter_value','duration incubation parameter_value', 
                    'duration exposure parameter_value',
                    'duration aging parameter_value', 'duration irradiation parameter_value',  
                    'temperature parameter_value',
                    'concentration zinc parameter_value', 'concentration copper parameter_value',
                    'irradiance parameter_value', 'irradiation power parameter_value',
                    'number of cells parameter_value', 'concentration carbon dioxide parameter_value'] 
    
    param_columns = []
    for name in param_names:
        if name in column_names:
            param_columns.append(name)
    
    # Store copper and zinc concentrations in a separate list.
    param_conc_names = ['concentration zinc parameter_value', 'concentration copper parameter_value']
    param_conc_columns = []
    for name in param_conc_names:
        if name in param_columns:
            param_columns.remove(name)
            param_conc_columns.append(name)
            
    # Extract columns with additive_value
    subs_value = "additive_value"
    additive_columns  = [icol for icol in column_names if subs_value in icol]
    
    # Extract columns with contaminant_value 
    subs_value = "contaminant_value"
    contaminant_columns  = [icol for icol in column_names if subs_value in icol]
    
    categorical_columns = []
    # Extract encoded categorical data
    cat_patterns = ['CoreComposition', 'ShellComposition', 'CoatingComposition', 'Shape', 'SurfaceChargeType',
                    'particle concentration parameter_nonnum', 'cell type parameter_nonnum',
                    'subject parameter_nonnum', 'light parameter_nonnum',
                    'biochemical name parameter_nonnum', 'subpathway parameter_nonnum']
    
    for pattern in cat_patterns:
        subs_value = pattern
        encoded_columns  = [icol for icol in column_names if subs_value in icol]
        categorical_columns = categorical_columns + encoded_columns
    
    # Add all columns to be used in the iterative imputation algorithm to a single list.
    total_cols = categorical_columns + param_columns + param_conc_columns + additive_columns + contaminant_columns
    
    # Extract results columns and store them in a separate DataFrame
    subs_value = "result_value"
    result_columns  = [icol for icol in column_names if subs_value in icol]
    desired_columns = []
    for icol in result_columns:
        if desired_type in icol:
            result_columns.remove(icol)
            desired_columns.append(icol)
        
    total_cols = total_cols + result_columns
    
    # Make a copy of the DataFrame with the chosen columns.
    df_temp = df[total_cols].copy()
    
    # Place the desired type result value into separate column
    df_desired = df[desired_columns].copy()
    
    # Impute additives and parameter-concentrations missing values with zeros.
    total_cols_zero = param_conc_columns + additive_columns + contaminant_columns
    df_temp[total_cols_zero] = df_temp[total_cols_zero].fillna(value = 0.0)
    
    # Extract minimum and maximum values of features and store them in separate lists.
    minimum_values = list(df_temp.min(axis = 0, skipna = True))
    maximum_values = list(df_temp.max(axis = 0, skipna = True))
    
    # Obtain length of lists
    length = len(maximum_values)
    
    # Loop over each element in lists and determine whether maximum value > minimum value.
    for i in range(length):
        if (maximum_values[i] <= minimum_values[i]):
            maximum_values[i] = 1.1 * maximum_values[i]
    
    # Define iterative imputer
    # Estimators available are:
    # 1) BayesianRidge: regularized linear regression  --> this is the default used by SKLearn
    # 2) DecisionTreeRegressor: non-linear regression
    # 3) ExtraTreesRegressor: similar to missForest in R (missForest is very popular with R users)
    # 4) KNeighborsRegressor: comparable to other KNN imputation approaches
    imputer = IterativeImputer(estimator = BayesianRidge(),
                           #sample_posterior = True,
                           max_iter = 20,
                           n_nearest_features = 10,
                           tol = 1.0e-4,
                           random_state = 0, 
                           missing_values = np.nan, 
                           initial_strategy = 'mean',
                           verbose = 0,
                           imputation_order = 'descending',
                           min_value = minimum_values,
                           max_value = maximum_values)
    
    imputed = imputer.fit_transform(df_temp)
    
    # Create DataFrame with the imputed missing data.
    df_imputed = pd.DataFrame(data=imputed, columns = total_cols)
    
    # Combine imputed DataFrame with desired result as last column
    df_combined = pd.concat([df_imputed, df_desired], axis = 1)
    #df_combined = pd.concat([df_temp, df_desired], axis = 1)
    
    return df_combined

