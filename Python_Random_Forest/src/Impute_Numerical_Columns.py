'''
Created on Mar 10, 2021

@author: Wmelende
'''

def impute_missing_data_of_numerical_columns(df):
    
    # Extract column names
    column_names = list(df.columns)
    
    # Make temporary copy of df.
    df_temp = df.copy()
    
    # Build list with columns to be imputed with zeros.
    columns_zero = ['SurfaceAreaValue', 'HydrodynamicDiameterValue', 
                    'particle concentration parameter_value','duration incubation parameter_value', 
                    'duration aging parameter_value', 'duration irradiation parameter_value', 
                    'concentration zinc parameter_value', 'concentration copper parameter_value', 
                    'irradiance parameter_value', 'irradiation power parameter_value'] 
    
    # Extract columns with additive_value
    subs_value = "additive_value"
    additive_columns  = [icol for icol in column_names if subs_value in icol]
    if ("fetal bovine serum additive_value" in additive_columns):
        additive_columns.remove("fetal bovine serum additive_value")
    
    cols_zero = columns_zero + additive_columns
    total_cols_zero = []
    for icol in cols_zero:
        if icol in column_names:
            total_cols_zero.append(icol)
    
    # Build list with columns to be imputed with most common value.
    cols_most_common = ['Purity', 'ChargeAvg', 'duration exposure parameter_value',
                        'number of cells parameter_value', 'concentration carbon dioxide parameter_value',
                        'fetal bovine serum additive_value']
    
    columns_most_common = []
    for icol in cols_most_common:
        if icol in column_names:
            columns_most_common.append(icol)
    
    # Impute missing values with zeros.
    df_temp[total_cols_zero] = df_temp[total_cols_zero].fillna(value = 0.0)
    
    # Impute missing temperatures with 25.0 Celsius.
    temperature = 'temperature parameter_value'
    if temperature in column_names:
        df_temp[temperature] = df_temp[temperature].fillna(value = 25.0)
    
    # Use the most frequent/common value.  This is also known as the mode.
    df_temp = df_temp.fillna(df_temp[columns_most_common].mode().iloc[0])
    
       # Use other OuterDiameter values
    if ('OuterDiameterValue' in column_names):
        if ('OuterDiameterLow' in column_names):
            df['OuterDiameterLow'] = df['OuterDiameterLow'].fillna(df['OuterDiameterValue'])
        if ('OuterDiameterHigh' in column_names):    
            df['OuterDiameterHigh'] = df['OuterDiameterHigh'].fillna(df['OuterDiameterValue'])
        if ('OuterDiameterLow' in column_names and 'OuterDiameterHigh' in column_names):
            df['OuterDiameterValue'] = df['OuterDiameterValue'].fillna(0.5*(df['OuterDiameterLow']+df['OuterDiameterHigh']))
    else:
        if ('OuterDiameterLow' in column_names and 'OuterDiameterHigh' in column_names):
            df['OuterDiameterLow'] = df['OuterDiameterLow'].fillna(df['OuterDiameterHigh'])
            df['OuterDiameterHigh'] = df['OuterDiameterHigh'].fillna(df['OuterDiameterLow']) 
     
    return df_temp