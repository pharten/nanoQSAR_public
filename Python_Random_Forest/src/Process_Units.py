'''
This module contains the definition of a function that calls 
other functions that will process the data units. 

Created on Jan 10, 2021

Functions
---------
process_data_units(df)
    Calls processing units functions.
    
@author: Wmelende
'''

from Process_Nanomaterial_units import process_nanomaterial_units
from Process_Parameters_Units import process_parameters_units
from Process_Additives_Units import process_additive_units
from Process_Contaminants_Units import process_contaminants_units
from Process_Results_Units import process_results_units


def process_data_units(df):
    '''
    Name
    ----
    process_data_units
    
    Description
    -----------
    This function calls other functions that will process the units for nanomaterials, parameters,
    additives, contaminants, and results.
    
    Input Parameters
    ----------------
    df : DataFrame
        DataFrame containing the inVitro data.
    
    Output Parameters
    -----------------
    Modified DataFrame df.
    
    Function calls
    --------------
    process_nanomaterial_units
    process_parameters_units
    process_additive_units
    process_contaminants_units
    process_results_units
    
    '''
    # Process nanomaterial units
    df = process_nanomaterial_units(df)
    
    # Process parameters' units
    df = process_parameters_units(df)
    
    # Process additives' units
    df = process_additive_units(df)
    
    # Process contaminants' units
    df = process_contaminants_units(df)
    
    # Process results units
    df = process_results_units(df)
    
    return df