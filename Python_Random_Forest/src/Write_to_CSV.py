'''
This module contains a function that writes a DataFrame to a CSV file.

Created on Dec 21, 2020

@author: Wmelende
'''

from pathlib import Path

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
    
    '''
    if not Path(file_output).exists():
        file_output = "..\\" + file_output
        
    # Write DataFrame to output.
    # Note that we must specify the right type of encoding to write out all characters correctly.
    # Some of the data contain Greek letters which need to be accounted for when writing to a CSV file.
    df.to_csv(file_output, encoding = 'utf-8-sig', index = False)
    
    # Print message to console indicating that writing to CSV has completed.
    print("Writing of " + file_output + " to a CSV file has completed.")