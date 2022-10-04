'''
Created on Dec 10, 2020

@author: Wmelende
'''
import pytest
import pandas as pd
from Additive_Fields import split_additive_fields

def test_additive_noName_exception():
    # Create DataFrame
    data = {'additive01_num_name_amt_unit':['2348::10:percent'],
            'additive02_num_name_amt_unit':['2050:potassium bisulfate:1:normality']}
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Extract column names.
    col_names = list(df.columns)
    
    # Determine number of rows in data frame.
    nrow = len(df.index)
    
    with pytest.raises(Exception):
        assert split_additive_fields(df, nrow, col_names)
        
def test_additive_noInt_exception():
    # Create DataFrame
    data = {'additive01_num_name_amt_unit':['2348:Fetal Bovine Serum:10:percent'],
            'additive02_num_name_amt_unit':['abc:potassium bisulfate:1:normality']}
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Extract column names.
    col_names = list(df.columns)
    
    # Determine number of rows in data frame.
    nrow = len(df.index)
    
    with pytest.raises(Exception):
        assert split_additive_fields(df, nrow, col_names)
        

def test_additive_noFloat_exception():
    # Create DataFrame
    data = {'additive01_num_name_amt_unit':['2348:Fetal Bovine Serum:abc:percent'],
            'additive02_num_name_amt_unit':['2050:potassium bisulfate:1:normality']}
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Extract column names.
    col_names = list(df.columns)
    
    # Determine number of rows in data frame.
    nrow = len(df.index)
    
    with pytest.raises(Exception):
        assert split_additive_fields(df, nrow, col_names)      