'''
Created on Apr 8, 2021

@author: Wmelende
'''

import pytest
import pandas as pd
from Process_Parameters_Units import process_parameters_units

def test_parameter_units():
    # Create data
    data = {'particle concentration parameter_value':[10, 0.5, 988.6],
            'particle concentration parameter_unit':['micrograms/milliliter', 'parts per million', 'micrograms/cubed meter'],
            'irradiance power parameter_value':[3710, 3.500, 3.800],
            'irradiance power parameter_unit':['microwatts/square centimeter', 'milliwatts/square centimeter', 'milliwatts/square centimeter']}
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Process units
    process_parameters_units(df)
    
    assert df['particle concentration parameter_value'][0] == 10
    assert df['particle concentration parameter_value'][1] == 0.5
    assert df['particle concentration parameter_value'][2] == 0.0009886
    
    assert df['irradiance power parameter_value'][0] == 3710
    assert df['irradiance power parameter_value'][1] == 3500
    assert df['irradiance power parameter_value'][2] == 3800
    
    assert df['particle concentration parameter_unit'][0] == 'micrograms/milliliter'
    assert df['particle concentration parameter_unit'][1] == 'micrograms/milliliter'
    assert df['particle concentration parameter_unit'][2] == 'micrograms/milliliter'
    
    assert df['irradiance power parameter_unit'][0] == 'microwatts/square centimeter'
    assert df['irradiance power parameter_unit'][1] == 'microwatts/square centimeter'
    assert df['irradiance power parameter_unit'][2] == 'microwatts/square centimeter'
     
     
     