'''
This module contains the definition of a function that selects the
in vitro rows from the original data. 

Created on Dec 21, 2020

@author: Wilson Melendez
'''

def select_in_vitro_rows(df):    
    '''
    Name
    ----
    select_in_vitro_rows
    
    Description
    -----------
    This function selects only the rows that have in vitro as entries under the assayType column.
    
    Input Parameters
    ----------------
    df : DataFrame
        DataFrame containing the original data.
    
    Output Parameters
    -----------------
    Filtered DataFrame df.
    
    '''
    # Select in vitro rows only.
    # Turn strings to lowercase and remove extra white space before selecting the in vitro rows.
    df["assayType"] = df["assayType"].str.lower().str.strip()
    df = df[df.assayType == 'in vitro']
    
    # Reset the rows indices.
    df = df.reset_index(level = 0, drop = True) 
    
    return df
