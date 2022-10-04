'''
This module contains the definition of a function that 
processes the nanomaterial units. 

Created on Feb 15, 2021

@author: Wmelende
'''

import math

def process_nanomaterial_units(df): 
    '''
    Name
    ----
    process_nanomaterial_units
    
    Description
    -----------
    This function processes the nanomaterial units.
    
    Input Parameters
    ----------------
    df : DataFrame
        DataFrame containing the inVitro data.
    
    Output Parameters
    -----------------
    Modified DataFrame df.
    
    Raises
    ------
    ValueError
        If units are unknown or incompatible.
    '''   
    # Determine column headers
    col_names = list(df.columns)
    
    # Determine number of rows in data frame.
    nrow = len(df.index)
    
    # Process Outer Diameter units
    col_value = "OuterDiameterValue"
    col_units = "OuterDiameterUnit"
    col_low = "OuterDiameterLow"
    col_high = "OuterDiameterHigh"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    if (df[col_units].iloc[irow] == 'nanometers' or df[col_units].iloc[irow] == 'micrometers'):
                        if (df[col_units].iloc[irow] == 'micrometers'):
                            df.loc[irow, col_units] = 'nanometers'
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1000
                            if (col_low in col_names):
                                if (df[col_low].iloc[irow] != None):
                                    df.loc[irow, col_low] = df.loc[irow, col_low] * 1000
                            if (col_high in col_names):   
                                if (df[col_high].iloc[irow] != None):
                                    df.loc[irow, col_high] = df.loc[irow, col_high] * 1000                        
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)
        
        
    # Process Thickness units
    col_value = "ThicknessValue"
    col_units = "ThicknessUnit"
    col_low = "ThicknessLow"
    col_high = "ThicknessHigh"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        # df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    if (df[col_units].iloc[irow] == 'nanometers' or df[col_units].iloc[irow] == 'micrometers'):
                        if (df[col_units].iloc[irow] == 'micrometers'):
                            df.loc[irow, col_units] = 'nanometers'
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1000
                            if (col_low in col_names):
                                if (df[col_low].iloc[irow] != None):
                                    df.loc[irow, col_low] = df.loc[irow, col_low] * 1000
                            if (col_high in col_names):   
                                if (df[col_high].iloc[irow] != None):
                                    df.loc[irow, col_high] = df.loc[irow, col_high] * 1000                        
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
                
    
    # Process SurfaceArea units
    # The units of cubed meters/gram and milligrams/gram are not compatible with surface area.
    # We are assuming cubed meters/gram and milligrams/gram are entry errors and that the units are
    # square meters/gram.
    col_value = "SurfaceAreaValue"
    col_units = "SurfaceAreaUnit"
    col_low = "SurfaceAreaLow"
    col_high = "SurfaceAreaHigh"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    if (df[col_units].iloc[irow] == 'square meters/gram' or 
                        df[col_units].iloc[irow] == 'square centimeters/gram' or 
                        df[col_units].iloc[irow] == 'square meter/gram' or 
                        df[col_units].iloc[irow] == 'cubed meters/gram' or 
                        df[col_units].iloc[irow] == 'milligrams/gram'):
                        if (df[col_units].iloc[irow] == 'square meter/gram'):
                            df.loc[irow, col_units] = 'square meters/gram'
                        elif (df[col_units].iloc[irow] == 'square centimeters/gram'):
                            df.loc[irow, col_units] = 'square meters/gram'
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1E-4
                            if (col_low in col_names):
                                if (df[col_low].iloc[irow] != None):
                                    df.loc[irow, col_low] = df.loc[irow, col_low] * 1E-4
                            if (col_high in col_names):   
                                if (df[col_high].iloc[irow] != None):
                                    df.loc[irow, col_high] = df.loc[irow, col_high] * 1E-4
                        elif (df[col_units].iloc[irow] == 'cubed meters/gram'): 
                            df.loc[irow, col_units] = 'square meters/gram'
                        elif (df[col_units].iloc[irow] == 'milligrams/gram'): 
                            df.loc[irow, col_units] = 'square meters/gram'
                            
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
        
    # Process Purity units
    col_value = "Purity"
    col_units = "PurityUnit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    if (df[col_units].iloc[irow] == 'percent' or df[col_units].iloc[irow] == 'fraction'):
                        if (df[col_units].iloc[irow] == 'fraction'):
                            df.loc[irow, col_units] = 'percent'
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 100                     
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)
        
    # Process Hydrodynamic Diameter units
    col_value = "HydrodynamicDiameterValue"
    col_units = "HydrodynamicDiameterUnit"
    col_low = "HydrodynamicDiameterLow"
    col_high = "HydrodynamicDiameterHigh"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        #df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    if (df[col_units].iloc[irow] == 'nanometers' or df[col_units].iloc[irow] == 'micrometers'):
                        if (df[col_units].iloc[irow] == 'micrometers'):
                            df.loc[irow, col_units] = 'nanometers'
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1000
                            if (col_low in col_names):
                                if (df[col_low].iloc[irow] != None):
                                    df.loc[irow, col_low] = df.loc[irow, col_low] * 1000
                            if (col_high in col_names):   
                                if (df[col_high].iloc[irow] != None):
                                    df.loc[irow, col_high] = df.loc[irow, col_high] * 1000                        
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
        
    # Process Charge units
    col_value = "ChargeAvg"
    col_units = "ChargeUnit"
    col_low = "ChargeLow"
    col_high = "ChargeHigh"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        #df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        #df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    if (df[col_units].iloc[irow] == 'millivolts' or df[col_units].iloc[irow] == 'volts'):
                        if (df[col_units].iloc[irow] == 'volts'):
                            df.loc[irow, col_units] = 'millivolts'
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1000
                            if (col_low in col_names):
                                if (df[col_low].iloc[irow] != None):
                                    df.loc[irow, col_low] = df.loc[irow, col_low] * 1000
                            if (col_high in col_names):   
                                if (df[col_high].iloc[irow] != None):
                                    df.loc[irow, col_high] = df.loc[irow, col_high] * 1000                        
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)
            
    return df