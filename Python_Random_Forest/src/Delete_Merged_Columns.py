'''
This module contains the definition of a function that is used for deleting columns which 
were merged with other columns and thus are no longer needed.

Created on Feb 11, 2021

@author: Wmelende
'''

def delete_merged_columns(df):
    '''
    Name
    ----
    delete_merged_columns
    
    Description
    -----------
    This function deletes columns that had been merged with other columns.
    
    Input Parameters
    ----------------
    df : DataFrame
        DataFrame containing the inVitro data.
    
    Output Parameters
    -----------------
    Modified DataFrame df.
    '''
    # Create list with columns to delete from DataFrame.  
    # These columns were merged with other columns.
    list_merged_columns = ['particle concentration log parameter_value',
                           'particle concentration log parameter_unit',
                           'particle concentration log parameter_nonnum',
                           'penicilin additive_value', 
                           'penicilin additive_unit',
                           'relative fluorescence result_value', 
                           'relative fluorescence result_unit']
                        
    # Delete the merged columns
    df.drop(list_merged_columns, axis = 1, inplace = True)
    
    return df