'''
Created on Feb 11, 2021

@author: Wmelende & Paul Harten
'''

import pandas as pd
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
from sklearn.impute import SimpleImputer
from Write_to_CSV import write_to_csv
from pickle import FALSE

def encode_categorical_columns(df):
    output_expandedCategoricalData = "data\\inVitro_expanded_categorical.data.csv"
    
    # Use OrdinalEncoding instead of OneHotEncoder for columns_multicode when multi=True
    #multi=False
    multi=True
    
    # Create list of columns to be encoded.
    columns_encode = ['CoreComposition', 'ShellComposition', 'CoatingComposition', 'Shape', 'SurfaceChargeType',
                      'particle concentration parameter_nonnum', 'cell type parameter_nonnum',
                      'subject parameter_nonnum', 'light parameter_nonnum']
                      
    columns_multicode = ['biochemical name parameter_nonnum', 'subpathway parameter_nonnum']
    
    # Replace None with empty string to avoid an error with One-Hot Encoder.
    # for icol in columns_encode:
    #     df[icol].replace({None:""}, inplace = True)
    column_names = list(df.columns)
    columns_encode = [icol for icol in columns_encode if icol in column_names]
    columns_multicode = [icol for icol in columns_multicode if icol in column_names]
    
    # Create DataFrame with categorical data
    if (multi==False):     
        columns_encode = columns_encode + columns_multicode
        df_cat = df[columns_encode]
        original_headers_cat = list(df_cat.columns)
        df_multicat = pd.DataFrame() #create empty DataFrame
        original_headers_multicat = list(df_multicat.columns)
    else:
        df_cat = df[columns_encode]
        original_headers_cat = list(df_cat.columns)
        df_multicat = df[columns_multicode]
        original_headers_multicat = list(df_multicat.columns)
        
    # Start DataFrame for numerical data
    df_num = df
        
    # Create imputation transformer for completing missing values.
    imp_missing = SimpleImputer(missing_values = None, strategy = 'constant', fill_value = 'missing')
        
    dfnew = pd.DataFrame()
        
    if (len(original_headers_cat)!=0):
            
        # Drop categorical data
        df_num = df_num.drop(columns_encode, inplace = False, axis = 1)
            
        # Impute the categorical data.
        df_imp = imp_missing.fit_transform(df_cat)
        
        # Encode the categorical data using the One-Hot Encoder
        encoder = OneHotEncoder(handle_unknown='ignore')
        encoder.fit(df_imp)
        trans_X_cat = encoder.transform(df_imp).toarray()
        
        #newHeaders = encoder.get_feature_names(original_headers_cat) #python3.8
        newHeaders = encoder.get_feature_names_out(original_headers_cat) #python3.9
        
        # Create DataFrame with the transformed categorical data.
        df1 = pd.DataFrame(data = trans_X_cat, columns = newHeaders)
        # Combine the OneeHot encoded categorical data with the numerical data.    
        dfnew = pd.concat([dfnew, df1], axis = 1)
        
    if (len(original_headers_multicat)!=0):
            
        # Drop categorical data
        df_num = df_num.drop(columns_multicode, inplace = False, axis = 1)

        df_imp = imp_missing.fit_transform(df_multicat)

        # Encode the categorical data using the OrdinalEncoder
        multicoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
        multicoder.fit(df_imp)
        trans_X_multicat = multicoder.transform(df_imp)
    
        newHeaders_multi = original_headers_multicat
        
        # Create DataFrame with the transformed categorical data.
        df2 = pd.DataFrame(data = trans_X_multicat, columns = newHeaders_multi)
        # Combine the Ordinal encoded categorical data with the numerical data.
        dfnew = pd.concat([dfnew, df2], axis = 1)
            
    dfnew = pd.concat([dfnew, df_num], axis = 1)
        
    # Write results to CSV file.
    write_to_csv(dfnew, output_expandedCategoricalData)
    
    return dfnew
