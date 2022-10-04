'''
This module contains the definition of a function that 
extracts the X and Y matrices.

Created on Mar 3, 2021

@author: Wmelende
'''

def extract_X_Y_matrices(desired_result, df):
    '''
    Name
    ----
    extract_X_Y_matrices
    
    Description
    -----------
    This function extracts the X and Y matrices from a DataFrame.
    
    Input Parameters
    ----------------
    df : DataFrame
        DataFrame containing the inVitro data.
    
    Output Parameters
    -----------------
    X and Y matrices.
    
    Raises
    ------
    ValueError
        If units are unknown or incompatible.
    '''   
    # Extract column names
    col_names = list(df.columns)
    
    # Extract results columns 
    subs_value = "result_value"
    subs_low = "result_low"
    subs_high = "result_high"   
    list_result_value =  [icol for icol in col_names if subs_value in icol]
    list_result_low = [icol for icol in col_names if subs_low in icol]
    list_result_high = [icol for icol in col_names if subs_high in icol]
    
    list_results = list_result_value + list_result_low + list_result_high
    
    # Extract viability result column only (Y matrix)
    desired_column = desired_result+" result_value"
    #desired_column = desired_result
    dfY = df[desired_column]
    
    # Extract the X matrix
    dfX = df.drop(list_results, inplace = False, axis = 1)
    
    return dfX, dfY