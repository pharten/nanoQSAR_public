'''
This module contains the definition of a function that 
processes the units for the contaminants. 

Created on Feb 15, 2021

@author: Wmelende, Pharten
'''
import math
 
def process_contaminants_units(df):
    '''
    Name
    ----
    process_contaminants_units
    
    Description
    -----------
    This function processes the contaminants' units.
    
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
        If units are unknown or incompatible.
    '''   
    # Determine number of rows in data frame.
    nrow = len(df.index)
    column_names = list(df.columns)
    subs_value = "contaminant_value"
    contam_columns  = [icol for icol in column_names if subs_value in icol]
    ''' Double Check this works, use similar conversions for additives '''
    # ########################################################################################################
    # Process contaminant units
    # ########################################################################################################
    for col_value in list(contam_columns):
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        col_units = col_value.replace("_value","_unit")
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'parts per million' or 
                        str_units == 'parts per billion'):
                        if (str_units == 'parts per billion'):
                            # convert contaminants to 'parts per million'
                            df.loc[irow, col_units] = 'parts per million' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E-03
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)

    return df