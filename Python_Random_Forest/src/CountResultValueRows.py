'''
Created on Nov 30, 2021

@author: PHARTEN
'''
import pandas as pd
from UtilRecords import read_from_csv, replace_null_with_none
from pandas.tests.extension.test_external_block import df

def main():
    
    #input_file = "data\\inVitro_expanded_categorical.data.csv"
    input_file = "data\\inVitro_No_Concatenated_Fields.csv"
    #input_file = "data\\assay_all_vw_out_inVitro.csv"
    
    # Read from CSV file.  
    df = read_from_csv(input_file)
    
    df = replace_null_with_none(df)
    
    # Extract the column headers
    col_names = list(df.columns)
    
    # Extract the columns headers associated with the values of the results
    subs_value = "result_value"
    list_result_value = [icol for icol in col_names if subs_value in icol]
    list_result_index = []
    for icol in range(0,len(list_result_value)):
        list_result_index.append(col_names.index(list_result_value[icol]))
    
    # Determine number of rows in data frame.
    nrow = len(df.index)
    nrescol = len(list_result_value)
    print(nrow,nrescol)
    
    for icol in range(0, nrescol):
        cnt = 0
        df2 = df.xs(list_result_value[icol],1)
        for irow in range(0, nrow):
        # Check whether all result values are empty for this row.
            if (df2[irow]==None):
            # count DataFrame row
                cnt = cnt+1
        
        name = list_result_value[icol]
        print(icol,name.encode('utf-8',errors='ignore'),nrow-cnt)
        
            
    # Reset the rows indices. 
    df.reset_index(level = 0, drop = True, inplace = True)
    #print("rows =",nrow,", no results =",nrow-len(df.index))

if __name__ == "__main__":
    main()
    
