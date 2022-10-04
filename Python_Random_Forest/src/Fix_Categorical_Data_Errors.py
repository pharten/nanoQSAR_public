'''
Created on Feb 17, 2021

@author: Wmelende
'''


def fix_categorical_data_errors(df):
    # Fix typos/misspellings
    df["CoatingComposition"].replace({"polyvinyl pyrrolidone": "polyvinylpyrrolidone"}, inplace = True)
    df["Shape"].replace({"sphere":"spherical", "shperical":"spherical"}, inplace = True)
    
    # Combine subpathway and sub pathway columns into subpathway column.
    if "sub pathway parameter_nonnum" in df.columns:
        if "subpathway parameter_nonnum" in df.columns:
            df["subpathway parameter_nonnum"] = df["subpathway parameter_nonnum"].combine_first(df["sub pathway parameter_nonnum"])
            # Delete 'sub pathway parameter_nonnum' column
            df.drop("sub pathway parameter_nonnum", axis = 1, inplace = True)
        else:
            df["sub pathway parameter_nonnum"].rename("subpathway parameter_nonnum")
    
    # Create list of categorical columns.
    categorical_columns = ['CoreComposition', 'ShellComposition', 'CoatingComposition', 
                           'Shape', 'SurfaceChargeType', 'particle concentration parameter_nonnum', 
                           'cell type parameter_nonnum', 'subject parameter_nonnum', 
                           'light parameter_nonnum',
                           'biochemical name parameter_nonnum', 'subpathway parameter_nonnum']
    
    # Change case of categories to lowercase.
    for column in categorical_columns:
        if column in df.columns:
            df[column] = df[column].str.lower()
    
    return df                