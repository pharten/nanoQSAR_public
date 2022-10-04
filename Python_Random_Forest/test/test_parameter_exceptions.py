'''
Created on Dec 10, 2020

@author: Wmelende
'''

import pytest
import pandas as pd
from Parameters_Fields import split_parameters_fields

def test_parameter_noName_exception():
    # Create DataFrame
    data = {'parameters01_num_name_numval_unit_nonnum':['1182512::0:days:'],
            'parameters02_num_name_numval_unit_nonnum':['1182513:Particle concentration:0:micrograms/milliliter:']}
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Extract column names.
    col_names = list(df.columns)
    
    # Determine number of rows in data frame.
    nrow = len(df.index)
    
    with pytest.raises(Exception):
        assert split_parameters_fields(df, nrow, col_names)
        
def test_parameter_noInt_exception():
    # Create DataFrame
    data = {'parameters01_num_name_numval_unit_nonnum':['1182512:Duration Aging:0:days:'],
            'parameters02_num_name_numval_unit_nonnum':[':Particle concentration:0:micrograms/milliliter:']}
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Extract column names.
    col_names = list(df.columns)
    
    # Determine number of rows in data frame.
    nrow = len(df.index)
    
    with pytest.raises(Exception):
        assert split_parameters_fields(df, nrow, col_names)
        

def test_parameter_noFloat_exception():
    # Create DataFrame
    data = {'parameters01_num_name_numval_unit_nonnum':['1182512:Duration Aging:0:days:'],
            'parameters02_num_name_numval_unit_nonnum':['1182513:Particle concentration::micrograms/milliliter:']}
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Extract column names.
    col_names = list(df.columns)
    
    # Determine number of rows in data frame.
    nrow = len(df.index)
    
    with pytest.raises(Exception):
        assert split_parameters_fields(df, nrow, col_names)      