'''
Created on Apr 12, 2021

@author: Wmelende
'''

import pytest
import pandas as pd
import math
from Process_Results_Units import process_results_units
from Refinement import refinement
from UtilRecords import read_from_csv, write_to_csv
from DeconcatenationProcess import deconcatenationProcess
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
from sklearn.impute import SimpleImputer

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

    input_file1 = "..\\data\\not_there.csv"
    input_file2 = "..\\data\\assay_all_vw_out_22325rows.csv"
    output_file = "..\\data\\Multivariate_Imputed_Numerical_Columns.csv"
    
    # Test exceptions
    with pytest.raises(FileNotFoundError):
        assert refinement(assayType2, desired_result2, coreComp2, yearPub2, input_file1, output_file)
        
    with pytest.raises(ValueError):
        assert refinement(assayType1, desired_result2, coreComp2, yearPub2, input_file2, output_file)

    #with pytest.raises(ValueError):
    #    assert refinement(assayType2, desired_result1, coreComp2, yearPub2, input_file2, output_file)
    
    #with pytest.raises(ValueError):
    #    assert refinement(assayType2, desired_result2, coreComp1, yearPub2, input_file2, output_file)
    
    #with pytest.raises(ValueError):
    #    assert refinement(assayType2, desired_result2, coreComp2, yearPub1, input_file2, output_file)
    
    # Read input_file and assert 22325 records
    #df = read_from_csv(input_file2)
    #assert(len(df.index) == 22325)
    #assert len(df.index) == 22325
    # Process units
    #assert df['front scatter result_value'][0] == 1.01
    #assert df['front scatter result_value'][1] == 0.9
    #assert df['front scatter result_value'][2] == 0.78

def test_refinement2():
    
    input_file = "..\\data\\assay_all_vw_out_22325rows.csv"
    
        # Read input_file and assert 22325 records
    df = read_from_csv(input_file)
    print(len(df.index)) 
    assert(len(df.index) == 22325)
    
    # initial processes only, translate concatenated data
    df = deconcatenationProcess(input_file, "in vitro")
    print(len(df.index))
    assert(len(df.index) == 6027)
    
    # initial processes only, translate concatenated data
    df = deconcatenationProcess(input_file, "in vivo")
    print(len(df.index))
    assert(len(df.index) == 2417)
    
    # initial processes only, translate concatenated data
    df = deconcatenationProcess(input_file, "in silico")
    print(len(df.index))
    assert(len(df.index) == 915)
    
    # initial processes only, translate concatenated data
    df = deconcatenationProcess(input_file, "life cycle")
    print(len(df.index))
    assert(len(df.index) == 8882)
    
    # initial processes only, translate concatenated data
    df = deconcatenationProcess(input_file, "chemical characterization")
    print(len(df.index))
    assert(len(df.index) == 509)
    
    # initial processes only, translate concatenated data
    df = deconcatenationProcess(input_file, "physical characterization")
    print(len(df.index))
    assert(len(df.index) == 3530)
    
    return

def test_refinement3():
    
    input_file = "..\\data\\assay_all_vw_out_22325rows.csv"
    #output_file = "data\\assay_all_vw_out_22325rows2.csv"
    
    # Read input_file and assert 22325 records
    df = read_from_csv(input_file)
    assert(len(df.index) == 22325)
    
    #df = correctMisspellings(df)
    #write_to_csv(df, output_file)
    
    columns_multicode = ["assayType"]
    df_multicat = df[columns_multicode]
    
    #print(df_multicat)
    # Create imputation transformer for completing missing values.
    imp_missing = SimpleImputer(missing_values = None, strategy = 'constant', fill_value = 'missing')

    multicat_array = df_multicat.to_numpy()
    imp_array = imp_missing.fit_transform(multicat_array)
    #print (imp_array.shape)

    # Encode the categorical data using the OrdinalEncoder
    #multicoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
    multicoder = LabelEncoder()
    multicoder.fit(imp_array[:,0])
    
    classes = multicoder.classes_
    #categories = multicoder.categories_
    #print (classes)
    #print (len(classes))
    
    countEachLabel(imp_array, classes)
    
    #assert(False)
    
    trans_X_multicat_array = multicoder.transform(imp_array[:,0])
        
    # Create DataFrame with the transformed categorical data.
    df2 = pd.DataFrame(data = trans_X_multicat_array, columns = columns_multicode)
    
    #print(len(df2.index))
    
    assert(len(df2.index) == 22325)
    
    # Combine the Ordinal encoded categorical data with the numerical data.
    df[columns_multicode] = df2[columns_multicode]
    
    return

def test_refinement4():
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

    input_file2 = "..\\data\\assay_all_vw_out_22325rows.csv"
    output_file = "..\\data\\Multivariate_Imputed_Numerical_Columns.csv"
    
    # do full refinement for viability and assert 435 records
    df = refinement(assayType2, desired_result2, coreComp2, yearPub2, input_file2, output_file)
    assert(len(df.index) == 435)

def test_refinement5():
    # Create data
    
    assayType = "in vitro"
    
    desired_result = "expression levels"
    
    # Core Compositions, if needed
    coreComp = ""
    #coreComp = "titanium dioxide"
    #coreComp = "silicon dioxide"
    #coreComp = "cerium(iv) oxide"
    #coreComp = "copper(ii) oxide"
    
    yearPub = ""
    #yearPub = 2014
    #yearPub = 2017

    input_file = "..\\data\\assay_all_vw_out_22325rows.csv"
    output_file = "..\\data\\Multivariate_Imputed_Numerical_Columns.csv"
    
    # do full refinement for viability and assert 435 records
    df = refinement(assayType, desired_result, coreComp, yearPub, input_file, output_file)
    assert(len(df.index) == 2525)

def tes_refinement6():
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

    input_file1 = "..\\data\\not_there.csv"
    input_file2 = "..\\data\\assay_all_vw_out_22325rows.csv"
    output_file = "..\\data\\Multivariate_Imputed_Numerical_Columns.csv"
    
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
    
def tes_refinement7():
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

    input_file2 = "..\\data\\assay_all_vw_out_22325rows.csv"
    output_file = "..\\data\\Multivariate_Imputed_Numerical_Columns.csv"
    
    # Create DataFrame
    #refinement(assayType, desired_result, coreComp, yearPub, input_file1, output_file)
    
    with pytest.raises(KeyError):
        assert refinement(assayType2, desired_result2, coreComp2, yearPub2, input_file2, output_file)

    # Process units
    #assert df['front scatter result_value'][0] == 1.01
    #assert df['front scatter result_value'][1] == 0.9
    #assert df['front scatter result_value'][2] == 0.78
  
def correctMisspellings(df):  
      # Turn strings to lowercase and remove extra white space before selecting the in vitro rows.
    df["assayType"] = df["assayType"].str.lower().str.strip()

    nrow = len(df.index)
    for irow in range (0, nrow):
        element = df.at[irow,"assayType"]
        if (element == "chemical charaterization"):
            element = "chemical characterization"
        elif (element == "physical charaterization"):
            element = "physical characterization"
        elif (element == "physical characterizaton"):
            element = "physical characterization"
        elif (element == "physical characteristic"):
            element = "physical characterization"
        df.at[irow,"assayType"] = element      

    return df

def countEachLabel(imp_array, classes):
    
    # Determine number of rows in data frame.
    nrow = len(imp_array)
    nclass = len(classes)

    for iclass in range(0, nclass):
        cnt = 0
        classVal = classes[iclass]
        for irow in range(0, nrow):
            # Check whether all result values are empty for this row.
            if (imp_array[irow,0]==classVal):
                # count DataFrame row
                cnt = cnt+1
        
        print(classVal, cnt)

