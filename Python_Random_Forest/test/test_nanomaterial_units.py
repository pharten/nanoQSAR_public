'''
Created on Apr 8, 2021

@author: Wmelende
'''

import pytest
import pandas as pd
from Process_Nanomaterial_units import process_nanomaterial_units

def test_nanomaterial_units():
    # Create data
    data = {'OuterDiameterValue':[0.10, 20, 0.50],
            'OuterDiameterUnit':['micrometers', 'nanometers', 'micrometers'],
            'OuterDiameterLow':[0.05, 18, 0.45],
            'OuterDiameterHigh':[0.15, 22, 0.55],
            'Purity':[99, 97, 0.92],
            'PurityUnit':['percent', 'percent', 'fraction']}
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Process units
    process_nanomaterial_units(df)
    
    assert df['OuterDiameterValue'][0] == 100.0
    assert df['OuterDiameterValue'][1] == 20
    assert df['OuterDiameterValue'][2] == 500.0
    
    assert df['OuterDiameterUnit'][0] == 'nanometers'
    assert df['OuterDiameterUnit'][1] == 'nanometers'
    assert df['OuterDiameterUnit'][2] == 'nanometers'