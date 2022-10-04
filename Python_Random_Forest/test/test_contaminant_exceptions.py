'''
Created on Dec 9, 2020

@author: Wmelende
'''

import pytest
import pandas as pd
from Contaminant_Fields import split_contaminant_fields

def test_contaminant_noName_exception():
    # Create DataFrame
    data = {'contam01_num_name_amt_unit_meth':['158::971:parts per million:inductively coupled plasma mass spectrometry'],
            'contam02_num_name_amt_unit_meth':['159:Potassium:350:parts per million:inductively coupled plasma mass spectrometry']}
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Extract column names.
    col_names = list(df.columns)
    
    # Determine number of rows in data frame.
    nrow = len(df.index)
    
    with pytest.raises(Exception):
        assert split_contaminant_fields(df, nrow, col_names)
        
def test_contaminant_noInt_exception():
    # Create DataFrame
    data = {'contam01_num_name_amt_unit_meth':['158:Cobalt:971:parts per million:inductively coupled plasma mass spectrometry'],
            'contam02_num_name_amt_unit_meth':['abc:Potassium:350:parts per million:inductively coupled plasma mass spectrometry']}
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Extract column names.
    col_names = list(df.columns)
    
    # Determine number of rows in data frame.
    nrow = len(df.index)
    
    with pytest.raises(Exception):
        assert split_contaminant_fields(df, nrow, col_names)
        

def test_contaminant_noFloat_exception():
    # Create DataFrame
    data = {'contam01_num_name_amt_unit_meth':['158:Cobalt:971:parts per million:inductively coupled plasma mass spectrometry'],
            'contam02_num_name_amt_unit_meth':['159:Potassium:abc:parts per million:inductively coupled plasma mass spectrometry']}
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Extract column names.
    col_names = list(df.columns)
    
    # Determine number of rows in data frame.
    nrow = len(df.index)
    
    with pytest.raises(Exception):
        assert split_contaminant_fields(df, nrow, col_names)       
        


