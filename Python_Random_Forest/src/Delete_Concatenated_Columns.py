'''
This module contains the definition of a function used to delete columns with 
concatenated fields containing parameters, contaminants, additives, and results. 

Created on Dec 27, 2020

@author: Wmelende
'''
import re 

def delete_concatenated_columns(df):
    '''
    Name
    ----
    delete_concatenated_columns
    
    Description
    -----------
    This function deletes all the columns containing concatenated fields of parameters, contaminants,
    additives, and results.
    
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
    '''
    # Extract column names
    column_names = list(df.columns)
    
    # Extract the columns with concatenated parameter fields
    parameter_regex = re.compile(r'parameters\d\d_num_name_numval_unit_nonnum')
    parameter_concatenated_columns = list(filter(parameter_regex.match, column_names))
    
    # Delete the parameters concatenated columns
    df.drop(parameter_concatenated_columns, axis = 1, inplace = True)
    
    # Extract the columns with concatenated contaminant fields
    contaminant_regex = re.compile(r'contam\d\d_num_name_amt_unit_meth')
    contaminant_concatenated_columns = list(filter(contaminant_regex.match, column_names))
    
    # Delete the contaminant concatenated columns
    df.drop(contaminant_concatenated_columns, axis = 1, inplace = True)
    
    # Extract the columns with concatenated additive fields
    additive_regex = re.compile(r'additive\d\d_num_name_amt_unit')
    additive_concatenated_columns = list(filter(additive_regex.match, column_names))
    
    # Delete the additive concatenated columns
    df.drop(additive_concatenated_columns, axis = 1, inplace = True)
    
    # Extract the columns with concatenated result fields
    result_regex = re.compile(r'result\d\d_num_type_dtl_val_approx_unit_uncert_low_hi')
    result_concatenated_columns = list(filter(result_regex.match, column_names))
    
    # Delete the result concatenated columns
    df.drop(result_concatenated_columns, inplace = True, axis = 1)
    
    