'''
Created on Nov 29, 2021

@author: PHARTEN
'''

from UtilRecords import read_from_csv, write_to_csv, delete_columns_with_all_equal_values
from Process_Units import process_data_units
from Fix_Categorical_Data_Errors import fix_categorical_data_errors
from Delete_Unwanted_Columns import delete_unwanted_columns
from UtilRecords import read_from_csv, write_to_csv, replace_null_with_none

def middleProcesses(desired_result, coreComp, yearPub, df):
    '''
    these middle processes:
    1) translates units from one to another (e.g. from joules to eVolts)
    2) fix misspellings in categorical values
    3) delete rows not used
    '''
    output_procesed_units = "data\\inVitro_processed_units.csv"
    output_post_processed_units = "data\\inVitro_post_processed_units.csv"
    output_fixedCategoricalData = "data\\inVitro_fixed_categorical.data.csv"
    output_Desired_Rows = "data\\Desired_Results_Rows.csv"
    
    # Replace NULL with None.
    df = replace_null_with_none(df)
    
    # Process units
    df = process_data_units(df)
    
    # Write DataFrame with processed units to a CSV file.
    write_to_csv(df, output_procesed_units)
    
    # Remove columns that were merged with other columns.
    df = delete_merged_columns(df)
    
     # Fix categorical data typos and misspellings.
    df = fix_categorical_data_errors(df)
    
    # Write DataFrame with fixed categorical data
    write_to_csv(df, output_fixedCategoricalData)
    
    # Delete columns that have no predictive capabilities.
    # These columns will not be needed for the Random Forest analysis.
    df = delete_unwanted_columns(df)
    
    # Extract only the rows with desired_result, coreComp, yearPub results
    df = extract_desired_rows(desired_result, coreComp, yearPub, df)
    
    # Write DataFrame to CSV file.
    #write_to_csv(df, output_Desired_Rows)
    
    # Remove rows that have no results
    #df = remove_rows_with_no_results(df)
    
    # Delete columns with the same value
    # This step is necessary because if rows with no results are removed (see step above), 
    # there is the possibility of having columns that are now empty.
    df = delete_columns_with_all_equal_values(df)
    
    # Write DataFrame with rows that have no results removed
    write_to_csv(df, output_post_processed_units)
    
    return df

def delete_merged_columns(df):
    '''
    Name
    ----
    delete_merged_columns
    
    Description
    -----------
    This function deletes columns that had been merged with other columns.
    
    Input Parameters
    ----------------
    df : DataFrame
        DataFrame containing the inVitro data.
    
    Output Parameters
    -----------------
    Modified DataFrame df.
    '''
    # Create list with columns to delete from DataFrame.  
    # These columns were merged with other columns.
    list_merged_columns = ['particle concentration log parameter_value',
                           'particle concentration log parameter_unit',
                           #'particle concentration log parameter_nonnum',
                           'penicilin additive_value', 
                           'penicilin additive_unit',
                           'relative fluorescence result_value', 
                           'relative fluorescence result_unit']
                        
    # Delete the merged columns
    column_names = list(df.columns)
    list_merged_columns = [icol for icol in list_merged_columns if icol in column_names]

    df.drop(list_merged_columns, axis = 1, inplace = True)
    
    return df

def extract_desired_rows(desired_result, coreComp, yearPub, df):
    column_name = desired_result+" result_value"
    
    #df1 = df.iloc[2062:2333].loc[df[column_name].isna() == False]
    df1 = df.loc[df[column_name].isna() == False]
    
    # Reset the rows indices.
    df1 = df1.reset_index(level = 0, drop = True)
    
    if desired_result=="expression levels":
        df2 = df1.loc[df1[column_name]<10.0]
        df2 = df2.reset_index(level = 0, drop = True)
        if coreComp == "":
            df1 = df2
        else:
            #column_name = "CoreComposition_"+coreComp
            df2 = df2.loc[df2["CoreComposition"]==coreComp]
            df2 = df2.reset_index(level = 0, drop = True)
            df1 = df2
            
    if yearPub != "":
        df1 = df1.loc[df1["year"]==yearPub]
        df1 = df1.reset_index(level = 0, drop = True)
        
    #df1 = df1.loc[df1["subpathway parameter_nonnum"]=="urea cycle"]
    #df1 = df1.reset_index(level = 0, drop = True)
    
    return df1

def remove_rows_with_no_results(df):
    # Extract the column headers
    col_names = list(df.columns)
    
    # Extract the columns headers associated with the values of the results
    subs_value = "result_value"
    list_result_value = [icol for icol in col_names if subs_value in icol]
    
    # Determine number of rows in data frame.
    nrow = len(df.index)
    
    for irow in range(0, nrow):
        # Check whether all result values are empty for this row.
        if (df.loc[irow, list_result_value].isna().values.all()):
            # Delete DataFrame row
            df.drop(index = irow, inplace = True)
            
    # Reset the rows indices. 
    df.reset_index(level = 0, drop = True, inplace = True)
    #print("rows =",nrow,", no results =",nrow-len(df.index))
    return df
    