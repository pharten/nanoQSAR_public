'''
This module contains the definition of a function used to delete columns that contain the same
value in all rows.

Created on Dec 29, 2020

@author: Wmelende
'''

def delete_columns_with_all_equal_values(df):
    '''
    Name
    ----
    delete_columns_with_all_equal_values
    
    Description
    -----------
    This function deletes columns in DataFrame that have the same value repeated in all their rows.
    
    Input Parameters
    ----------------
    df : DataFrame
        DataFrame containing the inVitro data.
        
    Output Parameters
    -----------------
    Modified DataFrame df.
    '''
    
    for column in df:
        if (df[column].eq(df[column].iloc[0]).all() == True):
            df.drop(column, axis = 1, inplace = True)
        elif (df[column].isna().values.all() == True):
            df.drop(column, axis = 1, inplace = True)
        
        