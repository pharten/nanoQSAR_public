'''
Created on Apr 12, 2021

@author: Wmelende
'''

import pytest
import pandas as pd
import math
from Process_Results_Units import process_results_units
from Refinement import refinement
from UtilRecords import read_from_csv


def test_refinement1():
    # Create data
    
    assayType1 = "nego in vitro"
    assayType2 = "in vitro"
    
    desired_result1 = "not desired"
    desired_result2 = "viability"
    #desired_result = "expression levels"
    
    # Core Compositions, if needed
    coreComp1 = "no core"
    coreComp2 = ""
    #coreComp = "titanium dioxide"
    #coreComp = "silicon dioxide"
    #coreComp = "cerium(iv) oxide"
    #coreComp = "copper(ii) oxide"
    
    yearPub1 = "0000"
    yearPub2 = ""
    #yearPub = 2014
    #yearPub = 2017

    input_file1 = "data\\not_there.csv"
    input_file2 = "data\\assay_all_vw_out_22325rows.csv"
    output_file = "data\\Multivariate_Imputed_Numerical_Columns.csv"
    
    # Test exceptions
    with pytest.raises(FileNotFoundError):
        df = refinement(assayType2, desired_result2, coreComp2, yearPub2, input_file1, output_file)
        assert df
        
    with pytest.raises(ValueError):
        assert refinement(assayType1, desired_result2, coreComp2, yearPub2, input_file2, output_file)

    with pytest.raises(ValueError):
        assert refinement(assayType2, desired_result1, coreComp2, yearPub2, input_file2, output_file)
    
    with pytest.raises(ValueError):
        assert refinement(assayType2, desired_result2, coreComp1, yearPub2, input_file2, output_file)
    
    with pytest.raises(ValueError):
        assert refinement(assayType2, desired_result2, coreComp2, yearPub1, input_file2, output_file)
    
    #assert len(df.index) == 22325
    # Process units
    #assert df['front scatter result_value'][0] == 1.01
    #assert df['front scatter result_value'][1] == 0.9
    #assert df['front scatter result_value'][2] == 0.78
    
def test_refinement2():
    # Create data
    
    assayType2 = "in vitro"
    
    desired_result2 = "viability"
    #desired_result = "expression levels"
    
    # Core Compositions, if needed
    coreComp2 = ""
    #coreComp = "titanium dioxide"
    #coreComp = "silicon dioxide"
    #coreComp = "cerium(iv) oxide"
    #coreComp = "copper(ii) oxide"
    
    yearPub2 = ""
    #yearPub = 2014
    #yearPub = 2017

    input_file2 = "data\\assay_all_vw_out_22325rows.csv"
    output_file = "data\\Multivariate_Imputed_Numerical_Columns.csv"
    
    # Read input_file and assert 22325 records
    df = read_from_csv(input_file2)
    assert(len(df.index) == 22325)
    
    df = refinement(assayType2, desired_result2, coreComp2, yearPub2, input_file2, output_file)
    
    # do full refinement for viability and assert 435 records
    assert(len(df.index) == 435)

        
def tes_refinement3():
    # Create data
    
    assayType1 = "nego in vitro"
    assayType2 = "in vitro"
    
    desired_result1 = "not desired"
    desired_result2 = "viability"
    #desired_result = "expression levels"
    
    # Core Compositions, if needed
    coreComp = ""
    #coreComp = "titanium dioxide"
    #coreComp = "silicon dioxide"
    #coreComp = "cerium(iv) oxide"
    #coreComp = "copper(ii) oxide"
    
    yearPub = ""
    #yearPub = 2014
    #yearPub = 2017

    input_file1 = "data\\not_there.csv"
    input_file2 = "data\\assay_all_vw_out_22325rows.csv"
    output_file = "data\\Multivariate_Imputed_Numerical_Columns.csv"
    
    # Create DataFrame
    #refinement(assayType, desired_result, coreComp, yearPub, input_file1, output_file)
    
    with pytest.raises(KeyError):
        assert refinement(assayType1, desired_result2, coreComp, yearPub, input_file2, output_file)

    with pytest.raises(KeyError):
        assert refinement(assayType2, desired_result1, coreComp, yearPub, input_file2, output_file)
    #assert df == Null
    
    df = refinement(assayType1, desired_result2, coreComp, yearPub, input_file2, output_file)

    # Process units
    #assert df['front scatter result_value'][0] == 1.01
    #assert df['front scatter result_value'][1] == 0.9
    #assert df['front scatter result_value'][2] == 0.78
    

    with pytest.raises(KeyError):
        assert refinement(assayType2, desired_result1, coreComp, yearPub, input_file2, output_file)
    #assert df == Null
    
    # Process units
    #assert df['front scatter result_value'][0] == 1.01
    #assert df['front scatter result_value'][1] == 0.9
    #assert df['front scatter result_value'][2] == 0.78
    
def tes_refinement4():
    # Create data
    
    assayType2 = "in vitro"
    
    desired_result2 = "viability"
    #desired_result = "expression levels"
    
    # Core Compositions, if needed
    coreComp2 = ""
    #coreComp = "titanium dioxide"
    #coreComp = "silicon dioxide"
    #coreComp = "cerium(iv) oxide"
    #coreComp = "copper(ii) oxide"
    
    yearPub2 = ""
    #yearPub = 2014
    #yearPub = 2017

    input_file2 = "data\\assay_all_vw_out_22325rows.csv"
    output_file = "data\\Multivariate_Imputed_Numerical_Columns.csv"
    
    # Create DataFrame
    #refinement(assayType, desired_result, coreComp, yearPub, input_file1, output_file)
    
    with pytest.raises(KeyError):
        assert refinement(assayType2, desired_result2, coreComp2, yearPub2, input_file2, output_file)

    # Process units
    #assert df['front scatter result_value'][0] == 1.01
    #assert df['front scatter result_value'][1] == 0.9
    #assert df['front scatter result_value'][2] == 0.78
    
    