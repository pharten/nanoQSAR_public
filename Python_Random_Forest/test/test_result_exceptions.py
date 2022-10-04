'''
Created on Dec 31, 2020

@author: Wmelende
'''
import pytest
import pandas as pd
from Result_Fields import split_result_fields

def test_result_noName_exception():
    # Create DataFrame
    data = {'result01_num_type_dtl_val_approx_unit_uncert_low_hi':['190481:front scatter::1::ratio to control:::'],
            'result02_num_type_dtl_val_approx_unit_uncert_low_hi':['190493:::1::ratio to control:::']}
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Extract column names.
    col_names = list(df.columns)
    
    # Determine number of rows in data frame.
    nrow = len(df.index)
    
    with pytest.raises(Exception):
        assert split_result_fields(df, nrow, col_names)
        
def test_result_noInt_exception():
    # Create DataFrame
    data = {'result01_num_type_dtl_val_approx_unit_uncert_low_hi':['abc:front scatter::1::ratio to control:::'],
            'result02_num_type_dtl_val_approx_unit_uncert_low_hi':['190493:side scatter::1::ratio to control:::']}
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Extract column names.
    col_names = list(df.columns)
    
    # Determine number of rows in data frame.
    nrow = len(df.index)
    
    with pytest.raises(Exception):
        assert split_result_fields(df, nrow, col_names)
        

def test_result_noFloat_exception():
    # Create DataFrame
    data = {'result01_num_type_dtl_val_approx_unit_uncert_low_hi':['190481:front scatter::A::ratio to control:::'],
            'result02_num_type_dtl_val_approx_unit_uncert_low_hi':['190493:side scatter::1::ratio to control:::']}
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Extract column names.
    col_names = list(df.columns)
    
    # Determine number of rows in data frame.
    nrow = len(df.index)
    
    with pytest.raises(Exception):
        assert split_result_fields(df, nrow, col_names)    