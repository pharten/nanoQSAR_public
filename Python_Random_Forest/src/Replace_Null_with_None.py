'''
This module contains a function that replaces NULL entries with Python's None.

Created on Dec 21, 2020

@author: Wmelende
'''



def replace_null_with_none(df):
    '''
    Name
    ----
    replace_null_with_none
    
    Description
    -----------
    This function replaces NULL entries with Python's None object.
    
    Input Parameters
    ----------------
    df : DataFrame
        DataFrame containing the in vitro rows.
    
    Output Parameters
    -----------------
    Modified DataFrame df.
    
    '''
    # Replace all NULL entries with Python's object.
    df.replace({'NULL': None}, inplace = True)
    
    # Replace empty string with None.
    df.replace({"": None}, inplace = True) 
    