'''
Created on Mar 9, 2021

@author: Wmelende
'''

import random

from sklearn.model_selection import train_test_split
import pandas as pd

def split_X_y_training_testing(dfX, dfy):
    # Split the data into training and testing sets.
    X_train, X_test, y_train, y_test = train_test_split(dfX, dfy, test_size = 0.2, random_state = 0)
    return X_train, X_test, y_train, y_test
    
    # Combine dfX and dfY into a single DataFrame
    dfXy = pd.concat([dfX, dfy], axis = 1)
    
    # Extract column names
    column_names = list(dfXy.columns)
    
    # Determine number of rows
    nrows = len(dfXy.index)
    
    # Calculate 20% of rows
    nrows_testing = int(0.20 * nrows)
    
    # Create list of core compositions
    subs_value = "CoreComposition"
    core_comp_columns  = [icol for icol in column_names if subs_value in icol]
    
    # Cast core composition columns as integers.
    dfXy[core_comp_columns] = dfXy[core_comp_columns].round(0).astype(int)
    
    # Remove Titanium Dioxide from list
    #core_comp_columns.remove('CoreComposition_titanium dioxide')
    core_comp_columns.remove('CoreComposition_no material')
    
    # Create list that will contain the test rows.
    list_test_rows = []
    
    # Initialize test DataFrame 
    dfXy_test = None
    
    # Initialize sum of test rows to zero.
    sum_rows = 0
    
    while (sum_rows <= nrows_testing):
        # Randomly select core composition from list
        core_composition = random.choice(core_comp_columns)
        
        # Determine number of times this core composition occurs (equal to 1).
        df1 = dfXy[core_composition].value_counts()
        num1 = df1.values[df1.index == 1][0]
        
        sum_rows = sum_rows + num1
        # Remove chosen core composition from list
        core_comp_columns.remove(core_composition)  
                     
        # Add core composition to test list
        # core_comp_test.append(core_composition)                
        dfTemp1 = dfXy[dfXy[core_composition] == 1]
        list_test_rows = list_test_rows + list(dfTemp1.index)
        if (dfXy_test is not None):
            dfXy_test = pd.concat([dfXy_test, dfTemp1], axis = 0)
        else:
            dfXy_test = dfTemp1
                            
    # Remove rows that correspond to the testing set.
    dfXy_train = dfXy.drop(list_test_rows, inplace = False, axis = 0)
        
    # Extract viability result column only (Y matrix)
    viability_column = "viability result_value"
    dfy_test = dfXy_test[[viability_column]]
    dfy_train = dfXy_train[[viability_column]]
    dfX_test = dfXy_test.drop(viability_column, inplace = False, axis = 1)
    dfX_train = dfXy_train.drop(viability_column, inplace = False, axis = 1)
    
    return dfX_train, dfX_test, dfy_train, dfy_test