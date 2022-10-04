'''
This module contains the definition of a function that 
processes the units for the results.

Created on Feb 15, 2021

@author: Wmelende
'''

import math

def process_results_units(df):
    '''
    Name
    ----
    process_results_units
    
    Description
    -----------
    This function processes the results' units.
    
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
    # Determine number of rows in data frame.
    nrow = len(df.index)
    
    # ######################################################################################################
    # Process units of results
    # ######################################################################################################
    col_names = list(df.columns)
    subs_low = "result_low"
    subs_high = "result_high"    
    list_result_low = [icol for icol in col_names if subs_low in icol]
    list_result_high = [icol for icol in col_names if subs_high in icol]
        
    # Process front scatter units
    result_type = "front scatter"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'ratio to control' or 
                        str_units == 'ratio'):
                        if (str_units == 'ratio'):
                            df.loc[irow, col_units] = 'ratio to control'
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
        
    # Process fluorescence units
    # The fluorescence data appears to consist of 3 different data groups that are not comparable 
    # to one another.  Their data ranges are very different.
    result_type = "fluorescence"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow].lower()
                    if (str_units == 'ratio to control' or 
                        str_units == 'relative fluorescence units' or 
                        str_units == 'fluorescence intensity' or
                        str_units == 'Relative Fluorescence Units'):
                        if (str_units == 'Relative Fluorescence Units'):
                            df.loc[irow, col_units] = 'relative fluorescence units' 
                        elif (str_units == 'ratio to control' or str_units == 'fluorescence intensity'):
                            df.loc[irow, col_units] = None
                            df.loc[irow, col_value] = None
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = None
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = None                     
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
        
    # Process  units
    col_value = "side scatter result_value"
    col_units = "side scatter result_unit"
    col_low = " result_low"
    col_high = " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'ratio' or 
                        str_units == 'ratio to control'):
                        if (str_units == 'ratio'):
                            df.loc[irow, col_units] = 'ratio to control' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)    
    
    # Process dna damage units
    result_type = "dna damage"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'percent' or 
                        str_units == 'fraction'):
                        if (str_units == 'fraction'):
                            df.loc[irow, col_units] = 'percent' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+02
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 1.0E+02
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 1.0E+02
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
        
    # Process number of micronuclei  units
    result_type = "number of micronuclei"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'micronuclei' or 
                        str_units == 'unitless'):
                        if (str_units == 'unitless'):
                            df.loc[irow, col_units] = 'micronuclei' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)    
    
    # Process hydrodynamic diameter units
    result_type = "hydrodynamic diameter"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'nanometers' or 
                        str_units == 'micrometers'):
                        if (str_units == 'micrometers'):
                            df.loc[irow, col_units] = 'nanometers' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+03
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 1.0E+03
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 1.0E+03
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
        
    # Process nfkb activation units
    result_type = "nfkb activation"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'fold change over control' or 
                        str_units == 'fold change'):
                        if (str_units == 'fold change'):
                            df.loc[irow, col_units] = 'fold change over control' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)    
        
    # Process ap1 activation units
    result_type = "ap1 activation"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'fold change over control' or 
                        str_units == 'fold change'):
                        if (str_units == 'fold change'):
                            df.loc[irow, col_units] = 'fold change over control' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
        
    # Process concentration titanium dioxide units
    result_type = "concentration titanium dioxide"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'milligrams/liter' or 
                        str_units == 'micrograms/liter'):
                        if (str_units == 'micrograms/liter'):
                            df.loc[irow, col_units] = 'milligrams/liter' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E-03
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 1.0E-03
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 1.0E-03
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)    
    
    # Process growth rate units
    result_type = "growth rate"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'nanometers' or 
                        str_units == 'micrometers'):
                        if (str_units == 'micrometers'):
                            df.loc[irow, col_units] = 'nanometers' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+03
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 1.0E+03
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 1.0E+03
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
        
    # Process genomics units
    result_type = "genomics"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'fold change over control' or 
                        str_units == 'fold change'):
                        if (str_units == 'fold change'):
                            df.loc[irow, col_units] = 'fold change over control' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)    
    
    # Process alanine transaminase activity units
    result_type = "alanine transaminase activity"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'ratio' or 
                        str_units == 'unitless'):
                        if (str_units == 'unitless'):
                            df.loc[irow, col_units] = 'ratio' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
        
    # Process aspartate transaminase activity units
    result_type = "aspartate transaminase activity"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'ratio' or 
                        str_units == 'unitless'):
                        if (str_units == 'unitless'):
                            df.loc[irow, col_units] = 'ratio' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)    
    
    # Process lactate dehydrogenase activity units
    # Not sure how the units should be converted for this case.
    # The units 'ratio' and 'percent' are ambiguous because we don't know what they are 
    # measured in relation to.  Unfortunately, all 3 units appear to be incompatible to 
    # one another: their data ranges are quite different.
    result_type = "lactate dehydrogenase activity"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'ratio' or 
                        str_units == 'percent' or 
                        str_units == 'enzyme units/liter'):
                        if (str_units == 'percent' or str_units == 'ratio'):
                            df.loc[irow, col_units] = None
                            df.loc[irow, col_value] = None
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = None
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = None
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
        
    # Process alkaline phosphatase activity units
    result_type = "alkaline phosphatase activity"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'ratio' or 
                        str_units == 'unitless'):
                        if (str_units == 'unitless'):
                            df.loc[irow, col_units] = 'ratio' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)    
    
    # Process chloramphenicol acetyltransferase activity units
    result_type = "chloramphenicol acetyltransferase activity"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'ratio' or 
                        str_units == 'unitless'):
                        if (str_units == 'unitless'):
                            df.loc[irow, col_units] = 'ratio' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
        
    # Process glucose-6-phosphate dehydrogenase activity units
    result_type = "glucose-6-phosphate dehydrogenase activity"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'ratio' or 
                        str_units == 'unitless'):
                        if (str_units == 'unitless'):
                            df.loc[irow, col_units] = 'ratio' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)    
    
    # Process gamma-glutamyl transferase activity units
    result_type = "gamma-glutamyl transferase activity"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'ratio' or 
                        str_units == 'unitless'):
                        if (str_units == 'unitless'):
                            df.loc[irow, col_units] = 'ratio' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
        
    # Process glutathione peroxidase activity units
    result_type = "glutathione peroxidase activity"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'ratio' or 
                        str_units == 'unitless'):
                        if (str_units == 'unitless'):
                            df.loc[irow, col_units] = 'ratio' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)    
    
    # Process glutathione reductase activity units
    result_type = "glutathione reductase activity"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'ratio' or 
                        str_units == 'unitless'):
                        if (str_units == 'unitless'):
                            df.loc[irow, col_units] = 'ratio' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
        
    # Process glutathione activity units
    # Not sure how to convert these units.
    # Values with Relative Light units are much higher than those with ratio and 
    # Chemiluminescence units. The units reported are not compatible to one another.
    # Strictly speaking, Chemiluminescence units and Relative Light Units are not units of
    # glutathione activity.  Ratio would be the best unit choice in this case.
    result_type = "glutathione activity"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'ratio' or 
                        str_units == 'Relative Light Units' or 
                        str_units == 'Chemiluminescence units'):
                        if (str_units == 'Chemiluminescence units' or str_units == 'Relative Light Units'):
                            df.loc[irow, col_units] = None
                            df.loc[irow, col_value] = None
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = None
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = None
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)    
    
    # Process microalbulmin activity units
    result_type = "microalbulmin activity"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'ratio' or 
                        str_units == 'unitless'):
                        if (str_units == 'unitless'):
                            df.loc[irow, col_units] = 'ratio' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
        
    # Process released protein units
    result_type = "released protein"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'ratio' or 
                        str_units == 'unitless'):
                        if (str_units == 'unitless'):
                            df.loc[irow, col_units] = 'ratio' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)    
    
    # Process superoxide dismutase activity units
    result_type = "superoxide dismutase activity"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'ratio' or 
                        str_units == 'unitless'):
                        if (str_units == 'unitless'):
                            df.loc[irow, col_units] = 'ratio' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
        
    # Process released bilirubin units
    result_type = "released bilirubin"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'ratio' or 
                        str_units == 'unitless'):
                        if (str_units == 'unitless'):
                            df.loc[irow, col_units] = 'ratio' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)   
        
    # Process released thioredoxin reductase units
    result_type = "released thioredoxin reductase"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'ratio' or 
                        str_units == 'unitless'):
                        if (str_units == 'unitless'):
                            df.loc[irow, col_units] = 'ratio' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)    
    
    # Process released triglycerides units
    result_type = "released triglycerides"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'ratio' or 
                        str_units == 'unitless'):
                        if (str_units == 'unitless'):
                            df.loc[irow, col_units] = 'ratio' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)    
    
    # Process size units
    # Two of the units are incompatible.
    result_type = "size"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'nanometers' or 
                        str_units == 'micrometers' or 
                        str_units == 'micrograms/liter' or 
                        str_units == 'percent'):
                        if (str_units == 'micrometers'):
                            df.loc[irow, col_units] = 'nanometers' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+03
                        elif (str_units == 'percent' or str_units == 'micrograms/liter'):
                            df.loc[irow, col_units] = None
                            df.loc[irow, col_value] = None
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = None
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = None   
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
        
        
    # Process zeta potential units
    result_type = "zeta potential"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'millivolts' or 
                        str_units == 'volts'):
                        if (str_units == 'volts'):
                            df.loc[irow, col_units] = 'millivolts' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E-03
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 1.0E-03
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 1.0E-03 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)    
    
    # Process concentration silver units
    # Two of the units are not considered concentration units.
    result_type = "concentration silver"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'micrograms/milliliter' or 
                        str_units == 'micrograms/liter' or 
                        str_units == 'milligrams/kilogram' or 
                        str_units == 'nanometers'):
                        if (str_units == 'micrograms/liter'):
                            df.loc[irow, col_units] = 'micrograms/milliliter' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E-03
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 1.0E-03
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 1.0E-03 
                        elif (str_units == 'milligrams/kilogram' or str_units == 'nanometers'):
                            df.loc[irow, col_units] = None
                            df.loc[irow, col_value] = None
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = None
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = None    
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)    
    
    # Process cell activity units
    result_type = "cell activity"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'ratio' or 
                        str_units == 'unitless'):
                        if (str_units == 'unitless'):
                            df.loc[irow, col_units] = 'ratio' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process deposition units
    result_type = "deposition"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'percent' or 
                        str_units == 'fraction'):
                        if (str_units == 'fraction'):
                            df.loc[irow, col_units] = 'percent' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 100
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 100
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 100
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)   
        
    # Process mass silver  units
    result_type = "mass silver"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'micrograms' or 
                        str_units == 'milligrams'):
                        if (str_units == 'milligrams'):
                            df.loc[irow, col_units] = 'micrograms' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+03
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 1.0E+03
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 1.0E+03 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)    
    
    # Process caspase 3/7 activity units
    result_type = "caspase 3/7 activity"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'Chemiluminescence units' or 
                        str_units == 'unitless'):
                        if (str_units == 'unitless'):
                            df.loc[irow, col_units] = 'Chemiluminescence units' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)    
    
    # Process concentration nitrate units
    # Are the units correct??
    result_type = "concentration nitrate"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'Chemiluminescence units' or 
                        str_units == 'unitless'):
                        if (str_units == 'unitless'):
                            df.loc[irow, col_units] = 'Chemiluminescence units' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process total protein units
    result_type = "total protein"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'micrograms' or 
                        str_units == 'milligrams'):
                        if (str_units == 'milligrams'):
                            df.loc[irow, col_units] = 'micrograms' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+03
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 1.0E+03
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 1.0E+03 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
        
    # Process reactive oxygen species units
    # Not sure how to convert micromolar to fold activity or viceversa.
    result_type = "reactive oxygen species"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'fold activity' or 
                        str_units == 'micromolar'):
                        if (str_units == 'micromolar'):
                            df.loc[irow, col_units] = None
                            df.loc[irow, col_value] = None
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = None
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = None 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
        
    # Process fold increase units
    result_type = "fold increase"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'fold change over control' or 
                        str_units == 'fold change'):
                        if (str_units == 'fold change'):
                            df.loc[irow, col_units] = 'fold change over control' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process absorbance units
    result_type = "absorbance"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'absorbance units' or 
                        str_units == None):
                        if (str_units == None):
                            df.loc[irow, col_units] = 'absorbance units' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)   
    
    # Process metabolically active cells units
    result_type = "metabolically active cells"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'percent' or 
                        str_units == 'fraction'):
                        if (str_units == 'fraction'):
                            df.loc[irow, col_units] = 'percent' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+02
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 1.0E+02
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 1.0E+02 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process apoptosis units
    result_type = "apoptosis"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'percent' or 
                        str_units == 'fraction'):
                        if (str_units == 'fraction'):
                            df.loc[irow, col_units] = 'percent' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+02
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 1.0E+02
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 1.0E+02 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
        
    # Process caspase-3 activity units
    result_type = "caspase-3 activity"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'micromolar/(hour*milligram)' or 
                        str_units == 'millimolar/(hour*milligram)'):
                        if (str_units == 'millimolar/(hour*milligram)'):
                            df.loc[irow, col_units] = 'micromolar/(hour*milligram)' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+03
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 1.0E+03
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 1.0E+03 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
        
    # Process viability units
    result_type = "viability"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'percent' or 
                        str_units == 'fraction'):
                        if (str_units == 'fraction'):
                            df.loc[irow, col_units] = 'percent' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+02
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 1.0E+02
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 1.0E+02 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process lethal concentration 50 percent units
    # This result has nanometers as one of the its units but this has to be wrong. 
    result_type = "lethal concentration 50 percent"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'micrograms/milliliter' or 
                        str_units == 'nanometers'):
                        if (str_units == 'nanometers'):
                            df.loc[irow, col_units] = 'microgram/milliliter'
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process nrf2/are units
    result_type = "nrf2/are"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'fold change over control' or 
                        str_units == 'fold change'):
                        if (str_units == 'fold change'):
                            df.loc[irow, col_units] = 'fold change over control'
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process ap1 units
    result_type = "ap1"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'fold change over control' or 
                        str_units == 'fold change'):
                        if (str_units == 'fold change'):
                            df.loc[irow, col_units] = 'fold change over control'
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
        
    # Process nfkb units
    result_type = "nfkb"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'fold change over control' or 
                        str_units == 'fold change'):
                        if (str_units == 'fold change'):
                            df.loc[irow, col_units] = 'fold change over control'
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
        
    # Process glutathion units
    result_type = "glutathion"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'percent' or 
                        str_units == 'fraction'):
                        if (str_units == 'fraction'):
                            df.loc[irow, col_units] = 'percent' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+02
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 1.0E+02
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 1.0E+02 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process relative fluorescence units
    # This result type is being merged with the fluorescence result type.
    result_type = "relative fluorescence"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    
    new_result_type = "fluorescence"
    newcol_value = new_result_type + " result_value"
    newcol_units = new_result_type + " result_unit"
    newcol_low = new_result_type + " result_low"
    newcol_high = new_result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'Relative fluorescence units'):
                        df.loc[irow, newcol_units] = "relative fluorescence units"
                        df.loc[irow, newcol_value] = df.loc[irow, col_value]
                        if (col_low in list_result_low):
                            df.loc[irow, newcol_low] = df.loc[irow, col_low]
                        if (col_high in list_result_high):
                            df.loc[irow, newcol_high] = df.loc[irow, col_high]                       
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process change in active electrodes units
    result_type = "change in active electrodes"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'ratio to control' or 
                        str_units == None):
                        if (str_units == None):
                            df.loc[irow, col_units] = 'ratio to control' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process electrophoretic mobility units
    result_type = "electrophoretic mobility"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'micrometers*centimeters/(volt*second)' or 
                        str_units == 'millimeters*centimeters/(volt*second)'):
                        if (str_units == 'millimeters*centimeters/(volt*second)'):
                            df.loc[irow, col_units] = 'micrometers*centimeters/(volt*second)' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+03
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 1.0E+03
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 1.0E+03 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
        
    # Process deposition rate units
    # Hertz is the standard unit for frequency.
    # One Hertz = one cycle per second
    # One microhertz = 1.0E-06 Hertz
    result_type = "deposition rate"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'Hertz/second' or 
                        str_units == '10^-6/second'):
                        if (str_units == '10^-6/second'):
                            df.loc[irow, col_units] = 'Hertz/second' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E-06
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 1.0E-06
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 1.0E-06 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
        
    # Process produced biogas units
    result_type = "produced biogas"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'milliliters' or 
                        str_units == 'liters'):
                        if (str_units == 'liters'):
                            df.loc[irow, col_units] = 'milliliters' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+03
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 1.0E+03
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 1.0E+03 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process concentration dissolved zinc ions units
    result_type = "concentration dissolved zinc ions"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'micrograms/liter' or 
                        str_units == 'milligrams/liter'):
                        if (str_units == 'milligrams/liter'):
                            df.loc[irow, col_units] = 'micrograms/liter' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+03
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 1.0E+03
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 1.0E+03 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process initial deposition rate units
    result_type = "initial deposition rate"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'Hertz/minute' or 
                        str_units == 'Hertz/second'):
                        if (str_units == 'Hertz/second'):
                            df.loc[irow, col_units] = 'Hertz/minute' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 60
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 60
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 60 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process dissipation to frequency shift ratio units
    result_type = "dissipation to frequency shift ratio"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'ratio' or 
                        str_units == 'unitless'):
                        if (str_units == 'unitless'):
                            df.loc[irow, col_units] = 'ratio'
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
        
    # Process induced dna damage units
    result_type = "induced dna damage"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'percent' or 
                        str_units == 'fraction'):
                        if (str_units == 'fraction'):
                            df.loc[irow, col_units] = 'percent' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+02
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 1.0E+02
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 1.0E+02 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
        
    # Process micronuclei/1000 binucleated cells units
    result_type = "micronuclei/1000 binucleated cells"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'percent' or 
                        str_units == 'fraction'):
                        if (str_units == 'fraction'):
                            df.loc[irow, col_units] = 'percent' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+02
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 1.0E+02
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 1.0E+02
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process resistance units
    result_type = "resistance"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'ratio to control' or 
                        str_units == 'ratio'):
                        if (str_units == 'ratio'):
                            df.loc[irow, col_units] = 'ratio to control'
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process chemiluminescence units
    result_type = "chemiluminescence"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'Chemiluminescence units' or 
                        str_units == 'Chemiluminescence'):
                        if (str_units == 'Chemiluminescence'):
                            df.loc[irow, col_units] = 'chemiluminescence units' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process transcellular electrical resistance units
    result_type = "transcellular electrical resistance"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'ratio to control' or 
                        str_units == 'ratio'):
                        if (str_units == 'ratio'):
                            df.loc[irow, col_units] = 'ratio to control'
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
        
    # Process ap-1 activity units
    result_type = "ap-1 activity"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'Chemiluminescence units' or 
                        str_units == 'Chemiluminescence'):
                        if (str_units == 'Chemiluminescence'):
                            df.loc[irow, col_units] = 'chemiluminescence units'
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
        
    # Process gsta3 expression units
    result_type = "gsta3 expression"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'fold change over control' or 
                        str_units == 'fold change'):
                        if (str_units == 'fold change'):
                            df.loc[irow, col_units] = 'fold change over control'
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process expression levels units
    result_type = "expression levels"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'ratio to control' or 
                        str_units == 'ratio'):
                        if (str_units == 'ratio'):
                            df.loc[irow, col_units] = 'ratio to control' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process glutathione remaining units
    result_type = "glutathione remaining"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'percent' or 
                        str_units == 'fraction'):
                        if (str_units == 'fraction'):
                            df.loc[irow, col_units] = 'percent' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+02
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 1.0E+02
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 1.0E+02
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process effective concentration 5 percent units
    result_type = "effective concentration 5 percent"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'micrograms/liter' or 
                        str_units == 'milligrams/liter'):
                        if (str_units == 'milligrams/liter'):
                            df.loc[irow, col_units] = 'micrograms/liter' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+03
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 1.0E+03
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 1.0E+03 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
        
    # Process effective concentration 10 percent units
    result_type = "effective concentration 10 percent"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'micrograms/liter' or 
                        str_units == 'milligrams/liter'):
                        if (str_units == 'milligrams/liter'):
                            df.loc[irow, col_units] = 'micrograms/liter' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+03
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 1.0E+03
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 1.0E+03 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
        
    # Process effective concentration 20 percent units
    result_type = "effective concentration 20 percent"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'micrograms/liter' or 
                        str_units == 'milligrams/liter'):
                        if (str_units == 'milligrams/liter'):
                            df.loc[irow, col_units] = 'micrograms/liter' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+03
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 1.0E+03
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 1.0E+03 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process effective concentration 50 percent units
    result_type = "effective concentration 50 percent"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'micrograms/liter' or 
                        str_units == 'milligrams/liter'):
                        if (str_units == 'milligrams/liter'):
                            df.loc[irow, col_units] = 'micrograms/liter' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+03
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 1.0E+03
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 1.0E+03 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process total copper units
    result_type = "total copper"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'percent' or 
                        str_units == 'fraction'):
                        if (str_units == 'fraction'):
                            df.loc[irow, col_units] = 'percent' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+02
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 1.0E+02
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 1.0E+02
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)   
    
    # Process hydrogen peroxide production units
    result_type = "hydrogen peroxide production"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'Relative Light Units' or 
                        str_units == 'Light Units'):
                        if (str_units == 'Light Units'):
                            df.loc[irow, col_units] = 'Relative Light Units' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process recovery la4 cells units
    # Must double check unit conversion from 10000/well to 1000/well.
    result_type = "recovery la4 cells"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == '1000/well' or 
                        str_units == '10000/well'):
                        if (str_units == '10000/well'):
                            df.loc[irow, col_units] = '1000/well' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 10
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 10
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 10 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process endothelial nitric oxide synthase units
    result_type = "endothelial nitric oxide synthase"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'fold change over control' or 
                        str_units == 'fold change'):
                        if (str_units == 'fold change'):
                            df.loc[irow, col_units] = 'fold change over control'
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process rna content units
    result_type = "rna content"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'nanograms/microliter' or 
                        str_units == 'micrograms/microliter'):
                        if (str_units == 'micrograms/microliter'):
                            df.loc[irow, col_units] = 'nanograms/microliter' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+03
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 1.0E+03
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 1.0E+03 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process genomics (microarrays), genes induced units
    # Must double check unit conversion from percent to fold change over control.
    result_type = "genomics (microarrays), genes induced"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'fold change over control' or 
                        str_units == 'percent'):
                        if (str_units == 'percent'):
                            df.loc[irow, col_units] = 'fold change over control' 
                            if (df[col_value].iloc[irow] >= 0):
                                df.loc[irow, col_value] = 1 + (df[col_value].iloc[irow] / 100)
                            else:
                                df.loc[irow, col_value] = -1 + (df[col_value].iloc[irow] / 100)  
                            if (col_low in list_result_low):
                                if (df[col_low].iloc[irow] >= 0.0):
                                    df[irow, col_low] = 1 + (df[col_low].iloc[irow] / 100)
                                else:
                                    df[irow, col_low] = -1 + (df[col_low].iloc[irow] / 100)                            
                            if (col_high in list_result_high):
                                if (df[col_high].iloc[irow] >= 0.0):
                                    df[irow, col_high] = 1 + (df[col_high].iloc[irow] / 100)
                                else:
                                    df[irow, col_high] = -1 + (df[col_high].iloc[irow] / 100)                        
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)   
    
    # Process genomics (microarrays), genes repressed units
    result_type = "genomics (microarrays), genes repressed"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'percent' or 
                        str_units == 'fraction'):
                        if (str_units == 'fraction'):
                            df.loc[irow, col_units] = 'percent' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+02
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 1.0E+02
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 1.0E+02 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process percent control units
    result_type = "percent control"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'percent' or 
                        str_units == 'fraction'):
                        if (str_units == 'fraction'):
                            df.loc[irow, col_units] = 'percent' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+02
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 1.0E+02
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 1.0E+02 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    
    # Process ratio reactive oxygen species to reactive nitrogen species units
    result_type = "ratio reactive oxygen species to reactive nitrogen species"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'fold activity' or 
                        str_units == 'ratio'):
                        if (str_units == 'ratio'):
                            df.loc[irow, col_units] = 'fold activity' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process 8-oxo-dg activity units
    result_type = "8-oxo-dg activity"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'fold activity' or 
                        str_units == 'ratio'):
                        if (str_units == 'ratio'):
                            df.loc[irow, col_units] = 'fold activity' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)   
    
    # Process ap sites production units
    result_type = "ap sites production"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'fold activity' or 
                        str_units == 'ratio'):
                        if (str_units == 'ratio'):
                            df.loc[irow, col_units] = 'fold activity' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process total endogenous dna units
    result_type = "total endogenous dna"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'fold activity' or 
                        str_units == 'ratio'):
                        if (str_units == 'ratio'):
                            df.loc[irow, col_units] = 'fold activity' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process 4-hne activity units
    result_type = "4-hne activity"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'fold activity' or 
                        str_units == 'ratio'):
                        if (str_units == 'ratio'):
                            df.loc[irow, col_units] = 'fold activity' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process mda activity units
    result_type = "mda activity"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'fold activity' or 
                        str_units == 'ratio'):
                        if (str_units == 'ratio'):
                            df.loc[irow, col_units] = 'fold activity' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process metabolic activity units
    result_type = "metabolic activity"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'ratio to control' or 
                        str_units == 'ratio'):
                        if (str_units == 'ratio'):
                            df.loc[irow, col_units] = 'ratio to control' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)   
    
    # Process il-6 activity units
    result_type = "il-6 activity"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'picograms/milliliter' or 
                        str_units == 'nanograms/milliliter'):
                        if (str_units == 'nanograms/milliliter'):
                            df.loc[irow, col_units] = 'picograms/milliliter' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+03
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 1.0E+03
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 1.0E+03 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process free radical generation units
    result_type = "free radical generation"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'Chemiluminescence units' or 
                        str_units == 'Relative Light Units'):
                        if (str_units == 'Relative light units'):
                            df.loc[irow, col_units] = 'chemiluminescence units' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process change in total spikes units
    result_type = "change in total spikes"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'ratio to control' or 
                        str_units == 'ratio'):
                        if (str_units == 'ratio'):
                            df.loc[irow, col_units] = 'ratio to control' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process firing rat units
    result_type = "firing rate"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'ratio to control' or 
                        str_units == 'ratio'):
                        if (str_units == 'ratio'):
                            df.loc[irow, col_units] = 'ratio to control' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process stain index units
    result_type = "stain index"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'ratio to control' or 
                        str_units == 'ratio'):
                        if (str_units == 'ratio'):
                            df.loc[irow, col_units] = 'ratio to control' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)   
    
    # Process cytokinesis-blocked proliferation index units
    # This result has units of ratio and percent.  Both units have values that are very
    # similar to one another. That being said, we are making the assumption that ratio and 
    # percent are interchangeable for this result type. 
    result_type = "cytokinesis-blocked proliferation index"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'ratio' or 
                        str_units == 'percent'):
                        if (str_units == 'percent'):
                            df.loc[irow, col_units] = 'ratio' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process number of silver particles units
    result_type = "number of silver particles"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'ratio' or 
                        str_units == 'unitless'):
                        if (str_units == 'unitless'):
                            df.loc[irow, col_units] = 'ratio' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process forward scatter units
    result_type = "forward scatter"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'ratio to control' or 
                        str_units == 'ratio'):
                        if (str_units == 'ratio'):
                            df.loc[irow, col_units] = 'ratio to control' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process concentration total zinc units
    result_type = "concentration total zinc"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'micrograms/liter' or 
                        str_units == 'milligrams/liter'):
                        if (str_units == 'milligrams/liter'):
                            df.loc[irow, col_units] = 'micrograms/liter' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+03
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 1.0E+03
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 1.0E+03 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process g1-phase cells units
    result_type = "g1-phase cells"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'percent' or 
                        str_units == 'unitless'):
                        if (str_units == 'unitless'):
                            df.loc[irow, col_units] = 'percent' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)   
    
    # Process are activity units
    result_type = "are activity"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'Chemiluminescence units' or 
                        str_units == 'Relative Light Units'):
                        if (str_units == 'Relative Light Units'):
                            df.loc[irow, col_units] = 'Chemiluminescence units' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process endothelin-1 units
    result_type = "endothelin-1"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'fold change over control' or 
                        str_units == 'fold change'):
                        if (str_units == 'fold change'):
                            df.loc[irow, col_units] = 'fold change over control' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process surface area units
    result_type = "surface area"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'nanometers squared' or 
                        str_units == 'micrometers squared'):
                        if (str_units == 'micrometers squared'):
                            df.loc[irow, col_units] = 'nanometers squared' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+06
                            if (col_low in list_result_low):
                                df.loc[irow, col_low] = df.loc[irow, col_low] * 1.0E+06
                            if (col_high in list_result_high):
                                df.loc[irow, col_high] = df.loc[irow, col_high] * 1.0E+06 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process are/nrf2 activity units
    result_type = "are/nrf2 activity"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'Chemiluminescence units' or 
                        str_units == 'Relative Light Units'):
                        if (str_units == 'Relative Light Units'):
                            df.loc[irow, col_units] = 'Chemiluminescence units' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process mitosox fluorescence units
    result_type = "mitosox fluorescence"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'ratio to control' or 
                        str_units == 'ratio'):
                        if (str_units == 'ratio'):
                            df.loc[irow, col_units] = 'ratio to control' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)   
    
    # Process s-phase cells units
    result_type = "s-phase cells"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'percent' or 
                        str_units == 'unitless'):
                        if (str_units == 'unitless'):
                            df.loc[irow, col_units] = 'percent' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process endothelin receptor b  units
    result_type = "endothelin receptor b"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'fold change over control' or 
                        str_units == 'fold change'):
                        if (str_units == 'fold change'):
                            df.loc[irow, col_units] = 'fold change over control' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process g2/m-phase cells  units
    result_type = "g2/m-phase cells"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'percent' or 
                        str_units == 'unitless'):
                        if (str_units == 'unitless'):
                            df.loc[irow, col_units] = 'percent'
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process tissue plasminogen activator units
    result_type = "tissue plasminogen activator"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'fold change over control' or 
                        str_units == 'fold change'):
                        if (str_units == 'fold change'):
                            df.loc[irow, col_units] = 'fold change over control' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process plasminogen activator inhibitor-1 units
    result_type = "plasminogen activator inhibitor-1"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'fold change over control' or 
                        str_units == 'fold change'):
                        if (str_units == 'fold change'):
                            df.loc[irow, col_units] = 'fold change over control' 
                    else:
                        error_message = "Unrecognized units: " + str_units + ", column = " + str(col_value) 
                        + " at row " + str(irow)
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)   
    
    # Process tissue factor units
    result_type = "tissue factor"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'fold change over control' or 
                        str_units == 'fold change'):
                        if (str_units == 'fold change'):
                            df.loc[irow, col_units] = 'fold change over control' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process tummor necrosis factor-α units
    result_type = "tummor necrosis factor-α"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'fold change over control' or 
                        str_units == 'fold change'):
                        if (str_units == 'fold change'):
                            df.loc[irow, col_units] = 'fold change over control' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process angiotensin receptor type 1a units
    result_type = "angiotensin receptor type 1a"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'fold change over control' or 
                        str_units == 'fold change'):
                        if (str_units == 'fold change'):
                            df.loc[irow, col_units] = 'fold change over control' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process caveolin-1 units
    result_type = "caveolin-1"
    col_value = result_type + " result_value"
    col_units = result_type + " result_unit"
    col_low = result_type + " result_low"
    col_high = result_type + " result_high"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        if (col_low in list_result_low):
            df[col_low] = df[df[col_low]!= None][col_low].astype(float)
            
        if (col_high in list_result_high):
            df[col_high] = df[df[col_high]!= None][col_high].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'fold change over control' or 
                        str_units == 'fold change'):
                        if (str_units == 'fold change'):
                            df.loc[irow, col_units] = 'fold change over control' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)
            
    return df