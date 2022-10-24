'''
Created on Nov 29, 2021

@author: PHARTEN
'''
from Encode_Categorical_Data import encode_categorical_columns
from Impute_Numerical_Columns import impute_missing_data_of_numerical_columns
from Perform_Multivariate_Imputation import iteratively_impute_numerical_columns
from UtilRecords import read_from_csv, write_to_csv, replace_null_with_none, delete_columns_with_all_equal_values

def finalProcesses(desired_result, df):
    '''
    these final processes:
    1) encode categorical columns
    2) delete columns with all value the same
    3) delete columns with unit notation
    4) iteratively impute values in numerical columns
    '''
    output_DifferentValues = "data\\inVitro_Columns_with_Different_Values.csv"
    output_ProcessedData = "data\\InVitro_ProcessedData.csv"
    output_Desired_Rows = "data\\Desired_Results_Rows.csv"
    output_NonEmptyColumns_Desired_Rows = "data\\Desired_Results_Rows_NonEmptyColumns.csv"
    
    # Encode categorical data
    df = encode_categorical_columns(df)

    # Delete columns with the same value
    df = delete_columns_with_all_equal_values(df)
    
    # Delete columns with the same value
    df = delete_columns_with_units(df)
    
    # Impute_missing_data_of_numerical_columns(df)
    df = iteratively_impute_numerical_columns(desired_result, df)
    
    return df

def delete_columns_with_units(df):

    for column in df:
        if ("_unit" in column or "Unit" in column):
            df.drop(column, axis = 1, inplace = True)

    return df

    