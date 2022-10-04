'''
Created on Apr 12, 2021

@author: Wmelende
'''

import pytest
import pandas as pd
import math
from Process_Results_Units import process_results_units


def test_result_units():
    # Create data
    data = {'front scatter result_value':[1.01, 0.9, 0.78],
            'front scatter result_unit':['ratio to control', 'ratio to control', 'ratio'],
            'fluorescence result_value':[1.35, 717.557, 2011330],
            'fluorescence result_unit':['ratio to control', 'relative fluorescence units', 'Fluorescence Intensity']}
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Process units
    process_results_units(df)
    
    # Process units
    assert df['front scatter result_value'][0] == 1.01
    assert df['front scatter result_value'][1] == 0.9
    assert df['front scatter result_value'][2] == 0.78
    
    assert df['front scatter result_unit'][0] == 'ratio to control'
    assert df['front scatter result_unit'][1] == 'ratio to control'
    assert df['front scatter result_unit'][2] == 'ratio to control'
    
    assert (math.isnan(df['fluorescence result_value'][0])) 
    assert df['fluorescence result_value'][1] == 717.557
    assert (math.isnan(df['fluorescence result_value'][2])) 
    
    assert df['fluorescence result_unit'][0] == None
    assert df['fluorescence result_unit'][1] == 'relative fluorescence units'
    assert df['fluorescence result_unit'][2] == None
    