'''
Created on Feb 10, 2021

@author: Wmelende
'''


def remove_rows_with_no_results(df):
    # Extract the column headers
    col_names = list(df.columns)
    
    # Extract the columns headers associated with the values of the results
    subs_value = "result_value"
    list_result_value = [icol for icol in col_names if subs_value in icol]
    
    # Determine number of rows in data frame.
    nrow = len(df.index)
    
    for irow in range(0, nrow):
        # Check whether all result values are empty for this row.
        if (df.loc[irow, list_result_value].isna().values.all()):
            # Delete DataFrame row
            df.drop(index = irow, inplace = True)
            
    # Reset the rows indices. 
    df.reset_index(level = 0, drop = True, inplace = True)
    #print("rows =",nrow,", no results =",nrow-len(df.index))
    