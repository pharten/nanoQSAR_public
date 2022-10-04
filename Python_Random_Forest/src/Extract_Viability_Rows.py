'''
Created on Mar 8, 2021

@author: Wmelende
'''

def extract_viability_rows(df):
    column_name = "viability result_value"
    df1 = df.loc[df[column_name].isna() == False]
    
    # Reset the rows indices.
    df1 = df1.reset_index(level = 0, drop = True)
    
    return df1