'''
Created on Nov 24, 2021

@author: PHARTEN
'''
from Parameters_Fields import split_parameters_fields
from Contaminant_Fields import split_contaminant_fields
from Additive_Fields import split_additive_fields
from Result_Fields import split_result_fields
import re
from UtilRecords import read_from_csv, write_to_csv, replace_null_with_none

def deconcatenationProcess(input_file, assayType):
    '''
    These de-concatenation processes:
    1) separate the AssayType rows
    2) translates the concatenated fields into many non-concatenated fields
    3) eliminates the concatenated fields
    '''
    
    invitro_output = "data\\inVitro_Rows.csv"
    output_file = "data\\assay_all_vw_out_inVitro.csv"
    output_NoConcatenatedFields = "data\\inVitro_No_Concatenated_Fields.csv"
        
    # Read from CSV file.  
    df = read_from_csv(input_file)
    if (len(df.index)==0): return df
    
    # Select in vitro rows
    df = select_AssayType_rows(df, assayType)
    if (len(df.index)==0): return df
        
    # Write inVitro rows to output
    #write_to_csv(df, invitro_output)
        
    # Read from invitro
    #df = read_from_csv(invitro_output)
        
    # Replace NULL with None.
    df = replace_null_with_none(df)
        
    # Proceed to split up the concatenated fields.
    df = split_parameters_fields(df)
    df = split_contaminant_fields(df)
    df = split_additive_fields(df)
    df = split_result_fields(df)
                        
    # Write data frame to a CSV file.
    #write_to_csv(df, output_file)
        
    # Remove concatenated columns
    df = delete_concatenated_columns(df)
    
    # Write DataFrame to a CSV file.
    #write_to_csv(df, output_NoConcatenatedFields)
      
    return df

def select_AssayType_rows(df, sel_assayType):    
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
    assayType: text
        assayType that is wanted
    
    Output Parameters
    -----------------
    Filtered DataFrame df.
    
    '''
    # Select in vitro rows only.
    # Turn strings to lowercase and remove extra white space before selecting the in vitro rows.
    df["assayType"] = df["assayType"].str.lower().str.strip()
    df = df[df.assayType == sel_assayType]
    
    # Reset the rows indices.
    df = df.reset_index(level = 0, drop = True) 
    
    return df

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
    
    return df


    