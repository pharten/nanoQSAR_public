'''
Created on Mar 11, 2021

@author: Wmelende
'''

import pytest
import pandas as pd
from Process_Additives_Units import process_additive_units

def test_additive_units():
    # Create data
    data = {'fetal bovine serum additive_value':[10, 10, 20],
            'fetal bovine serum additive_unit':['5', 'percent', 'percent'],
            'bovine serum albumin additive_value':[0.1, 5.0, 0.31],
            'bovine serum albumin additive_unit':['fraction', 'percent', 'fraction']}
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Process units
    process_additive_units(df)
    
    assert df['fetal bovine serum additive_unit'][0] == 'percent'
    assert df['fetal bovine serum additive_unit'][1] == 'percent'
    assert df['fetal bovine serum additive_unit'][2] == 'percent'
    
    assert df['fetal bovine serum additive_value'][0] == 10
    assert df['fetal bovine serum additive_value'][1] == 10
    assert df['fetal bovine serum additive_value'][2] == 20
       
    assert df['bovine serum albumin additive_value'][0] == 10.0
    assert df['bovine serum albumin additive_value'][1] == 5.0
    assert df['bovine serum albumin additive_value'][2] == 31.0
    
    assert df['bovine serum albumin additive_unit'][0] == 'percent'
    assert df['bovine serum albumin additive_unit'][1] == 'percent'
    assert df['bovine serum albumin additive_unit'][2] == 'percent'