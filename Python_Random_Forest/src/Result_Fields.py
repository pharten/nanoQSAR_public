'''
This module contains the definition of a function used to split up 
concatenated fields containing results. 

Created on Nov 30, 2020

Functions
---------
split_result_fields(df, nrow, col_names)
    Splits up the concatenated result fields.
    
@author: Wilson Melendez
'''
import re
import pandas as pd 

def split_result_fields(df):
    '''
    Name
    ----
    split_results_fields
    
    Description
    -----------
    This function splits up the concatenated fields containing the results.
    
    Input Parameters
    ----------------
    df : DataFrame
        DataFrame containing the inVitro data.
    nrow : int
        Number of rows in DataFrame df.
    col_names  : list
        The column headers in DataFrame df.
    
    Output Parameters
    -----------------
    Modified DataFrame df.
    
    Raises
    ------
    ValueError
        If no result type is found in concatenated string or casting to int/float fails.
    '''
    # Extract column names
    column_names = list(df.columns)
    
    # Determine number of rows in data frame.
    nrow = len(df.index)
    
    # Extract the columns with concatenated result fields
    result_regex = re.compile(r'result\d\d_num_type_dtl_val_approx_unit_uncert_low_hi')
    list_results = list(filter(result_regex.match, column_names))            
    
    # Determine number of results headers
    num_results = len(list_results)
    
    try:
        for icol in range(0, num_results):
            if (df[list_results[icol]].isna().values.all() == True):
                continue
            for irow in range(0, nrow):
                if (df[list_results[icol]].iloc[irow] == None):
                    continue
                else:
                    result = df[list_results[icol]].iloc[irow]
                    list_str = result.split(":",10)
                    
                    if (len(list_str)==10): # Assume ':' problem is in detail field
                        list_str = [list_str[0],list_str[1],list_str[2]+':'+list_str[3],list_str[4],
                                    list_str[5],list_str[6],list_str[7],list_str[8],list_str[9]]
                        
                    # If result type was not present, throw an exception.
                    if (list_str[1] == ''):
                        error_message = "Type is missing for result " + list_results[icol] + " at row " + irow
                        raise ValueError(error_message)  
                    
                    # list_str[0] = number
                    # list_str[1] = type of result
                    # list_str[2] = dtl (result detail)
                    # list_str[3] = amount of result (numeric value)
                    # list_str[4] = approximation
                    # list_str[5] = unit of numeric value
                    # list_str[6] = uncertainty
                    # list_str[7] = low value
                    # list_str[8] = high value
                    # strnum = list_str[1].strip().lower() + ' result_number'
                    strdtl = list_str[1].strip().lower() + ' result_detail'
                    strvalue = list_str[1].strip().lower() + ' result_value'
                    strapprox = list_str[1].strip().lower() + ' result_approximation'
                    strunit = list_str[1].strip().lower() + ' result_unit'
                    struncer = list_str[1].strip().lower() + ' result_uncertainty'
                    strlow = list_str[1].strip().lower() + ' result_low'
                    strhigh = list_str[1].strip().lower() + ' result_high'
                    
                    if strvalue not in list(df.columns):
                        new_columns = pd.DataFrame(columns=[strdtl, strvalue, strapprox, strunit, struncer, strlow, strhigh])
                        df = pd.concat([df,new_columns], axis=1)
                    
                    # New columns are added to the DataFrame by specifying a new name and 
                    # assigning a value to it.  If the location of a new column is important, we 
                    # can use the 'insert' method to specify its location within the DataFrame.  
                    # In this function new columns are appended to the DataFrame so no attempt  
                    # at specifying a specific location is made.   
                      
                    # if (list_str[0] != ''):   
                    #     df.loc[irow, strnum] = int(list_str[0])
                    # else:
                    #     df.loc[irow, strnum] = None
                            
                    if (list_str[2] != ''):
                        df.loc[irow, strdtl] = list_str[2]
                    else:
                        df.loc[irow, strdtl] = None
                            
                    if (list_str[3] != ''):
                        df.loc[irow, strvalue] = float(list_str[3])
                    else:
                        df.loc[irow, strvalue] = None
                            
                    if (list_str[4] != ''):
                        df.loc[irow, strapprox] = list_str[4]
                    else:
                        df.loc[irow, strapprox] = None
                            
                    if (list_str[5] != ''):
                        df.loc[irow, strunit] = list_str[5]
                    else:
                        df.loc[irow, strunit] = None
                            
                    if (list_str[6] != ''):
                        df.loc[irow, struncer] = list_str[6]
                    else:
                        df.loc[irow, struncer] = None
                            
                    if (list_str[7] != ''):
                        df.loc[irow, strlow] = float(list_str[7])
                    else:
                        df.loc[irow, strlow] = None
                            
                    if (list_str[8] != ''):
                        df.loc[irow, strhigh] = float(list_str[8])
                    else:
                        df.loc[irow, strhigh] = None             
    
    except ValueError as msg:
        error_message = msg + ", result = " + list_results[icol] + ", row = " + irow
        print(error_message)
        
    # Print message to console indicating completion of this function's task.
    print("Splitting of concatenated result fields has completed.")
    
    return df