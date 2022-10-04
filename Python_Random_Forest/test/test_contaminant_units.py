'''
Created on Apr 8, 2021

@author: Wmelende
'''

import pytest
import pandas as pd
from Process_Contaminants_Units import process_contaminants_units

def test_contaminant_units():
    # Create data
    data = {'vanadium contaminant_value':[300, 251, 325],
            'vanadium contaminant_unit':['parts per million', 'parts per billion', 'parts per billion'],
            'silicon dioxide contaminant_value':[1500, 5.0, 0.31],
            'silicon dioxide contaminant_unit':['parts per million', 'parts per billion', 'parts per billion']}
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Process units
    process_contaminants_units(df)
    
    assert df['vanadium contaminant_value'][0] == 300
    assert df['vanadium contaminant_value'][1] == 0.251
    assert df['vanadium contaminant_value'][2] == 0.325
    
    assert df['vanadium contaminant_unit'][0] == 'parts per million'
    assert df['vanadium contaminant_unit'][1] == 'parts per million'
    assert df['vanadium contaminant_unit'][2] == 'parts per million'
    
    
    assert df['silicon dioxide contaminant_value'][0] == 1500
    assert df['silicon dioxide contaminant_value'][1] == 0.005
    assert df['silicon dioxide contaminant_value'][2] == 0.00031
    
    assert df['silicon dioxide contaminant_unit'][0] == 'parts per million'
    assert df['silicon dioxide contaminant_unit'][1] == 'parts per million'
    assert df['silicon dioxide contaminant_unit'][2] == 'parts per million'
    
    