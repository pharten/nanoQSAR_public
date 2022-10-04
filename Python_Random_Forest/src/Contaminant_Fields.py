'''
This module contains the definition of a function used to split up 
concatenated fields containing contaminants. 

Created on Nov 30, 2020

Functions
---------
split_contaminant_fields(df, nrow, col_names)
    Splits up the concatenated contaminant fields.

@author: Wilson Melendez
'''
import re
import pandas as pd 

def split_contaminant_fields(df):
    '''
    Name
    ----
    split_contaminant_fields
    
    Description
    -----------
    This function splits up the concatenated fields containing the contaminants.
    
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
    
    # Generate a list containing the column headers associated with contaminants. 
    contaminant_regex = re.compile(r'contam\d\d_num_name_amt_unit_meth')
    list_contaminants = list(filter(contaminant_regex.match, column_names))
    
    # Determine the number of contaminant column headers.
    num_contaminants = len(list_contaminants)
    
    # Declare empty set that will contain the contaminant names.
    # contaminants_set = set()
    try:
        for icol in range(0, num_contaminants):
            if (df[list_contaminants[icol]].isna().values.all() == True):
                continue
            for irow in range(0, nrow):       
                if (df[list_contaminants[icol]].iloc[irow] == None):            
                    continue       
                else:  
                    # Split up concatenated string and store items in a list.        
                    list_str = df[list_contaminants[icol]].iloc[irow].split(":") 
                    
                    # If contaminant name was not present, throw an exception.
                    if (list_str[1] == ''):
                        error_message = "Name is missing for contaminant " + list_contaminants[icol] + " at row " + irow
                        raise ValueError(error_message)  
                    
                    # list_str[0] = number associated with contaminant
                    # list_str[1] = name of contaminant
                    # list_str[2] = amount of contaminant (numeric value)
                    # list_str[3] = unit of numeric value
                    # list_str[4] = method used  
                    
                    # contaminants_set.add(list_str[1].strip().lower())
                    strvalue = list_str[1].strip().lower() + ' contaminant_value'
                    strunits = list_str[1].strip().lower() + ' contaminant_unit'
                    # strnum = list_str[1].strip().lower() + ' contaminant_number'
                    strnonnum = list_str[1].strip().lower() + ' contaminant_method'
                    
                    if strvalue not in list(df.columns):
                        new_columns = pd.DataFrame(columns=[strvalue, strunits, strnonnum])
                        df = pd.concat([df,new_columns], axis=1)
                    
                    # New columns are added to the DataFrame by specifying a new name and 
                    # assigning a value to it.  If the location of a new column is important, we 
                    # can use the 'insert' method to specify its location within the DataFrame.  
                    # In this function new columns are appended to the DataFrame so no attempt  
                    # at specifying a specific location is made.   
                    
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
        error_message = msg + ", contaminant = " + list_contaminants[icol] + ", row = " + irow
        print(error_message)
        
    # Print message to console indicating completion of this function's task.
    print("Splitting of concatenated contaminant fields has completed.")
    
    return df