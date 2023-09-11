'''
Created on Nov 29, 2021

@author: PHARTEN
'''

import pandas as pd
from pathlib import Path
import os
from numpy import NaN
from pandas.tests.extension.test_external_block import df

def read_from_csv(input_file):
    '''
    Name
    ----
    read_from_csv
    
    Description
    -----------
    This function reads a DataFrame from a CSV file.
    
    Input Parameters
    ----------------
    # input_file, a csv file. 
    # Note that we must specify the right type of encoding in order to read in all characters
    # correctly.  Some of the data contain Greek letters which me must account for.
    '''
    if not Path(input_file).exists():
        if input_file.startswith("..\\"):
            input_file = input_file[3:]
    
    if not Path(input_file).exists():
        AssertionError("input_file not found")
    
    df = pd.read_csv(input_file, skip_blank_lines = False, 
                     na_filter = True, low_memory = False,
                     encoding = 'utf-8-sig')
    
    return df

def write_to_csv(df, file_output):
    '''
    Name
    ----
    write_to_csv
    
    Description
    -----------
    This function writes a DataFrame to a CSV file.
    
    Input Parameters
    ----------------
    df : DataFrame
        DataFrame containing the in vitro rows.
    file_output: text
        output file name
    '''
    #if file_output.startswith("data"):
        #file_output = "..\\" + file_output
    if not Path(file_output).parent.is_dir():
        if file_output.startswith("..\\"):
            file_output = file_output[3:]
            
    if not Path(file_output).parent.is_dir():
        if file_output.startswith("data"):
            file_output = "..\\" + file_output
        
    # Write DataFrame to output.
    # Note that we must specify the right type of encoding to write out all characters correctly.
    # Some of the data contain Greek letters which need to be accounted for when writing to a CSV file.
    df.to_csv(file_output, encoding = 'utf-8-sig', index = False)
    #df.replace({None,'Null'}).to_csv(file_output, encoding = 'utf-8-sig', index = False)
    
        # Print message to console indicating that writing to CSV has completed.
    #print("Writing of " + file_output + " to a CSV file has completed.")
    
def remove(filename):
    '''
    Name
    ----
    remove
    
    Description
    -----------
    This function removes a file with alternate possible pathways
    
    '''
    # remove file
    if Path(filename).exists(): os.remove(filename)
    else:
        if filename.startswith("data"):
            filename = "..\\" + filename
            if Path(filename).exists(): os.remove(filename)
    

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
    
    # Replace empty string with None.
    df.replace({NaN: None}, inplace = True)
    
    return df

def delete_columns_with_all_equal_values(df, keepUnits = True):
    '''
    Name
    ----
    delete_columns_with_all_equal_values
    
    Description
    -----------
    This function deletes columns in DataFrame that have the same value repeated in all their rows,
    except for units and other columns which might be needed for future use.
    
    Input Parameters
    ----------------
    df : DataFrame
        DataFrame containing the inVitro data.
    keepUnits: boolean
        default value of True
        
    Output Parameters
    -----------------
    Modified DataFrame df.
    '''

    unit_needed = False
    low_needed = False
    high_needed = False
    for column in df:
        if (keepUnits and "_value" in column):
            unit_needed = True
        elif (keepUnits and "Value" in column):
            unit_needed = True
            low_needed = True
            high_needed = True
        elif (keepUnits and "ChargeAvg" in column):
            unit_needed = True
            low_needed = True
            high_needed = True
            
        if (unit_needed and "_unit" in column):
            unit_needed = False
        elif (unit_needed and "Unit" in column):
            unit_needed = False
        elif (low_needed and "Low" in column):
            low_needed = False
        elif (high_needed and "High" in column):
            high_needed = False
        elif (df[column].eq(df[column].iloc[0]).all() == True):
            if ("_value" in column):
                unit_needed = False
            elif ("Value" in column):
                unit_needed = False
                low_needed = False
                high_needed = False
            elif ("ChargeAvg" in column):
                unit_needed = False
                low_needed = False
                high_needed = False
            df.drop(column, axis = 1, inplace = True)
        elif (df[column].isna().values.all() == True):
            if ("_value" in column):
                unit_needed = False
            elif ("Value" in column):
                unit_needed = False
                low_needed = False
                high_needed = False
            elif ("ChargeAvg" in column):
                unit_needed = False
                low_needed = False
                high_needed = False
            df.drop(column, axis = 1, inplace = True)

    return df
