'''
This module contains the definition of the main function of the  
program.  

Created on Oct 29, 2020

@author: Wilson Melendez & Paul Harten
'''

from DeconcatenationProcess import deconcatenationProcess
from MiddleProcesses import middleProcesses
from FinalProcesses import finalProcesses
#from Replace_Null_with_None import replace_null_with_none
#from Write_to_CSV import write_to_csv
#from Delete_Concatenated_Columns import delete_concatenated_columns
#from Delete_Columns_With_All_Equal_Values import delete_columns_with_all_equal_values
#from Process_Units import process_data_units
#from Remove_Rows_NoResults import remove_rows_with_no_results
#from Delete_Merged_Columns import delete_merged_columns
#from Fix_Categorical_Data_Errors import fix_categorical_data
from Encode_Categorical_Data import encode_categorical_columns
#from Delete_Unwanted_Columns import delete_unwanted_columns
from Impute_Numerical_Columns import impute_missing_data_of_numerical_columns
from Perform_Multivariate_Imputation import iteratively_impute_numerical_columns
from UtilRecords import read_from_csv, write_to_csv, delete_columns_with_all_equal_values
import pandas

def main():
    assayType = "in vitro"
    
    desired_result = "viability"
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

    input_file = "data\\assay_all_vw_out_22325rows.csv"
    output_file = "data\\Multivariate_Imputed_Numerical_Columns.csv"
    
    df = refinement(assayType, desired_result, coreComp, yearPub, input_file, output_file)

    print("Refinement Complete")

    
def refinement(assayType, desiredResult, coreComp, yearPub, inputFile, outputFile):
    
    # initial processes only, translate concatenated data
    df = deconcatenationProcess(inputFile, assayType)
    
    # middle processes only, translate units into most common
    df = middleProcesses(desiredResult, coreComp, yearPub, df)
    
    # final processes only, translate units into most common
    df = finalProcesses(desiredResult, df)
    
    # Write imputed DataFrame to a CSV file
    write_to_csv(df, outputFile)

    return df


if __name__ == "__main__":
    main()
        
    