'''
This module contains the definition of a function used to split up 
concatenated fields containing parameters. 

Created on Nov 30, 2020

Functions
---------
split_parameters_fields(df, nrow, col_names)
    Splits up the concatenated parameter fields.
    
@author: Wilson Melendez
'''
import re
import pandas as pd

def split_parameters_fields(df):
    '''
    Name
    ----
    split_parameters_fields
    
    Description
    -----------
    This function splits up the concatenated fields containing the parameters.
    
    Input Parameters
    ----------------
    df : DataFrame
        DataFrame containing the inVitro data.
    
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
    
    # Generate a list containing the column headers associated with parameters.
    parameter_regex = re.compile(r'parameters\d\d_num_name_numval_unit_nonnum')
    list_param = list(filter(parameter_regex.match, column_names))
    
    # Determine number of parameters headers
    num_param = len(list_param)
    
    try:
        for icol in range(0, num_param):
            if (df[list_param[icol]].isna().values.all() == True):
                continue
            for irow in range(0, nrow):            
                if (df[list_param[icol]].iloc[irow] == None):               
                    continue            
                else:
                    parameter = df[list_param[icol]].iloc[irow]
                    list_str = parameter.split(":",6)
                    
                    if (len(list_str) == 6):
                        if (list_str[4] != '' and list_str[5] != ''): # assume : is in nonnum
                            list_str = [list_str[0], list_str[1], list_str[2], list_str[3], list_str[4]+':'+list_str[5]]
                        else:
                            list_str = [list_str[0], list_str[1]+':'+list_str[2], list_str[3], list_str[4], list_str[5]]
                    
                    # If parameter name was not present, throw an exception.
                    if (list_str[1] == ''):
                        error_message = "Name is missing for parameter " + list_param[icol] + " at row " + irow
                        raise ValueError(error_message)   
                    
                    # list_str[0] = number
                    # list_str[1] = name of parameter
                    # list_str[2] = amount of parameter (numeric value)
                    # list_str[3] = unit of numeric value
                    # list_str[4] = non-numeric string
                    
                    # strnum = list_str[1].strip().lower() + ' parameter_number'
                    strvalue = list_str[1].strip().lower() + ' parameter_value'
                    strunits = list_str[1].strip().lower() + ' parameter_unit'                   
                    strnonnum = list_str[1].strip().lower() + ' parameter_nonnum'
                    
                    if strvalue not in list(df.columns):
                        new_columns = pd.DataFrame(columns=[strvalue, strunits, strnonnum])
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
                        df.loc[irow, strvalue] = float(list_str[2])
                    else:
                        df.loc[irow, strvalue] = None
                                            
                    if (list_str[3] != ''):
                        df.loc[irow, strunits] = list_str[3]
                    else:
                        df.loc[irow, strunits] = None
                            
                    if (list_str[4] != ''):
                        df.loc[irow, strnonnum] = list_str[4]
                    else:
                        df.loc[irow, strnonnum] = None
    
    except ValueError as msg:
        error_message = msg + ", parameter = " + list_param[icol] + ", row = " + irow
        print(error_message)
        
    # Print message to console indicating completion of this function's task.
    print("Splitting of concatenated parameter fields has completed.")

    return df
    