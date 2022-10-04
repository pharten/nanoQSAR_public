'''
This module contains the definition of a function that 
processes the units for the additives.

Created on Feb 15, 2021

@author: Wmelende
'''
import math

def process_additive_units(df):
    '''
    Name
    ----
    process_additives_units
    
    Description
    -----------
    This function processes the additives' units.
    
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
    
    # #######################################################################################################
    #  Process additive units
    # #######################################################################################################
    
    # Process fetal bovine serum units
    # The number '5' is not a unit.
    col_value = "fetal bovine serum additive_value"
    col_units = "fetal bovine serum additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'percent' or 
                        str_units == '5'):
                        if (str_units == '5'):
                            df.loc[irow, col_units] = 'percent'
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
        
    # Process bovine serum albumin units
    col_value = "bovine serum albumin additive_value"
    col_units = "bovine serum albumin additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
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
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
    
    # Process deionized water units
    col_value = "deionized water additive_value"
    col_units = "deionized water additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
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
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
        
    # Process potassium chloride units
    # Chemical formula: KCl
    # molar mass = 74.5513 g/mol
    # 1 molar = 1 mol/liter
    # 1 molar = 1000 * millimolar
    # 1 millimolar = 1.0E-3 * molar
    col_value = "potassium chloride additive_value"
    col_units = "potassium chloride additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'millimolar' or 
                        str_units == 'molar' or 
                        str_units == 'grams/liter'):
                        if (str_units == 'molar'):
                            df.loc[irow, col_units] = 'millimolar' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+03
                        elif(str_units == 'grams/liter'):
                            df.loc[irow, col_units] = 'millimolar' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+03 / 74.5513
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
        
    # Process phosphate buffer units
    # Why is there an 'unspecified' unit?
    col_value = "phosphate buffer additive_value"
    col_units = "phosphate buffer additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'millimolar' or 
                        str_units == 'unspeficied'):
                        if (str_units == 'unspeficied'):
                            df.loc[irow, col_units] = None 
                            df.loc[irow, col_value] = None
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
        
    # Process trichloroacetic acid units
    col_value = "trichloroacetic acid additive_value"
    col_units = "trichloroacetic acid additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'millimolar' or 
                        str_units == 'molar'):
                        if (str_units == 'molar'):
                            df.loc[irow, col_units] = 'millimolar' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E-03
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
    
    # Process sodium chloride units
    # Chemical formula: NaCl
    # molar mass = 58.44 g/mol
    # 1 molar = 1 mol/liter
    # 1 molar = 1000 * millimolar
    # 1 millimolar = 1.0E-3 * molar
    col_value = "sodium chloride additive_value"
    col_units = "sodium chloride additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'millimolar' or 
                        str_units == 'molar' or 
                        str_units == 'grams/liter' or 
                        str_units == "milligrams/liter" or 
                        str_units == "millimoles"):
                        if (str_units == 'molar'):
                            df.loc[irow, col_units] = 'millimolar' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+03
                        elif(str_units == 'grams/liter'):
                            df.loc[irow, col_units] = 'millimolar' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+03 / 58.44
                        elif(str_units == 'milligrams/liter'):
                            df.loc[irow, col_units] = 'millimolar' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] / 58.44
                        elif(str_units == 'millimoles'):
                            df.loc[irow, col_units] = 'millimolar'
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
       
    # Process 2',7'dichlorohydrofluorescein diacetate units
    col_value = "2',7'dichlorohydrofluorescein diacetate additive_value"
    col_units = "2',7'dichlorohydrofluorescein diacetate additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'micromolar' or 
                        str_units == 'millimolar'):
                        if (str_units == 'millimolar'):
                            df.loc[irow, col_units] = 'micromolar' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+03
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
    
    # Process water units
    col_value = "water additive_value"
    col_units = "water additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
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
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
    
    # Process dimethyl sulfoxide units
    col_value = "dimethyl sulfoxide additive_value"
    col_units = "dimethyl sulfoxide additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
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
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
    
    # Process calcium chloride units
    # Chemical formula: CaCl_2
    # molar mass = 110.98 g/mol
    # 1 molar = 1 mol/liter
    # 1 molar = 1000 * millimolar
    # 1 millimolar = 1.0E-3 * molar
    col_value = "calcium chloride additive_value"
    col_units = "calcium chloride additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'millimolar' or
                        str_units == 'molar' or
                        str_units == 'grams/liter' or 
                        str_units == "milligrams/liter" or 
                        str_units == "millimoles"):                     
                        if (str_units == 'molar'):
                            df.loc[irow, col_units] = 'millimolar' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+03
                        elif(str_units == 'grams/liter'):
                            df.loc[irow, col_units] = 'millimolar' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+03 / 110.98
                        elif(str_units == 'milligrams/liter'):
                            df.loc[irow, col_units] = 'millimolar' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] / 110.98
                        elif(str_units == 'millimoles'):
                            df.loc[irow, col_units] = None
                            df.loc[irow, col_value] = None
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
    
    # Process calcium sulfate units
    # Chemical formula: CaSO4
    # molar mass = 136.14 g/mol
    # 1 molar = 1 mol/liter
    # 1 molar = 1000 * millimolar
    # 1 millimolar = 1.0E-3 * molar
    col_value = "calcium sulfate additive_value"
    col_units = "calcium sulfate additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'grams/liter' or                     
                        str_units == "milligrams/liter" or 
                        str_units == "millimoles"):                     
                        if (str_units == 'milligrams/liter'):
                            df.loc[irow, col_units] = 'grams/liter' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E-03
                        elif(str_units == 'millimoles'):
                            df.loc[irow, col_units] = None
                            df.loc[irow, col_value] = None
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
    
    # Process glucose units
    col_value = "glucose additive_value"
    col_units = "glucose additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'grams/liter' or                     
                        str_units == "milligrams/liter" or 
                        str_units == "millimoles"):                     
                        if (str_units == 'milligrams/liter'):
                            df.loc[irow, col_units] = 'grams/liter' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E-03
                        elif(str_units == 'millimoles'):
                            df.loc[irow, col_units] = None
                            df.loc[irow, col_value] = None
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
    
    # Process gentamicin units
    col_value = "gentamicin additive_value"
    col_units = "gentamicin additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'micrograms/milliliter' or                     
                        str_units == "milligrams/milliliter" or 
                        str_units == "millimoles"):                     
                        if (str_units == 'milligrams/milliliter'):
                            df.loc[irow, col_units] = 'micrograms/milliliter' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+03
                        elif(str_units == 'millimoles'):
                            df.loc[irow, col_units] = None
                            df.loc[irow, col_value] = None
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
    
    # Process l-cysteine units
    # 
    col_value = "l-cysteine additive_value"
    col_units = "l-cysteine additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'milligrams/milliliter' or                     
                        str_units == "micrograms/milliliter" or 
                        str_units == "millimoles"):                     
                        if (str_units == 'micrograms/milliliter'):
                            df.loc[irow, col_units] = 'milligrams/milliliter' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E-03
                        elif(str_units == 'millimoles'):
                            df.loc[irow, col_units] = None
                            df.loc[irow, col_value] = None
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
    
    # Process ethylenediaminetetraacetic acid units
    col_value = "ethylenediaminetetraacetic acid additive_value"
    col_units = "ethylenediaminetetraacetic acid additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'millimolar' or 
                        str_units == 'micromolar'):
                        if (str_units == 'micromolar'):
                            df.loc[irow, col_units] = 'millimolar' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E-03
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
    
    # Process penicillin units
    # Penicillin, with double ll, is the correct spelling.
    col_value = "penicillin additive_value"
    col_units = "penicillin additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'units/milliliter' or 
                        str_units == 'units/milliliters'):
                        df.loc[irow, col_units] = 'enzyme units/milliliter' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
    
    # Process hank's balanced salt solution units
    col_value = "hank's balanced salt solution additive_value"
    col_units = "hank's balanced salt solution additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
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
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
    
    # Process citrate buffer units
    col_value = "citrate buffer additive_value"
    col_units = "citrate buffer additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
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
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
    
    # Process sodium bromide units
    # Chemical formula: NaBr
    # molar mass = 102.894 g/mol
    # 1 molar = 1 mol/liter
    # 1 molar = 1000 * millimolar
    # 1 millimolar = 1.0E-3 * molar
    col_value = "sodium bromide additive_value"
    col_units = "sodium bromide additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'milligrams/liter' or                     
                        str_units == "grams/liter" or 
                        str_units == "millimoles"):                     
                        if (str_units == 'grams/liter'):
                            df.loc[irow, col_units] = 'milligrams/liter' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+03
                        elif(str_units == 'millimoles'):
                            df.loc[irow, col_units] = None
                            df.loc[irow, col_value] = None
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
    
    # Process l-glutamine units
    # Chemical formula: C5H10N2O3
    # molar mass = 146.146 g/mol
    # 1 molar = 1 mol/liter
    # 1 molar = 1000 * millimolar
    # 1 millimolar = 1.0E-3 * molar
    col_value = "l-glutamine additive_value"
    col_units = "l-glutamine additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'millimolar' or                     
                        str_units == "micromolar" or 
                        str_units == "millimole"):                     
                        if (str_units == 'micromolar'):
                            df.loc[irow, col_units] = 'millimolar' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E-03
                        elif(str_units == 'millimole'):
                            df.loc[irow, col_units] = 'millimolar' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
    
    # Process penicillin / streptomycin units
    col_value = "penicillin / streptomycin additive_value"
    col_units = "penicillin / streptomycin additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
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
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
    
    # Process 1,2-dipalmitoyl-sn-glycero-3-phosphocholine units
    col_value = "1,2-dipalmitoyl-sn-glycero-3-phosphocholine additive_value"
    col_units = "1,2-dipalmitoyl-sn-glycero-3-phosphocholine additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
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
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
    
    # Process sodium pyruvate additive_unit units
    col_value = "sodium pyruvate additive_value"
    col_units = "sodium pyruvate additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'millimole' or 
                        str_units == 'micromole'):
                        if (str_units == 'micromole'):
                            df.loc[irow, col_units] = 'millimole' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E-03
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
    
    # Process amphotericin b units
    # Chemical formula: C47H73NO17
    # molar mass = 924.091 g/mol
    # 1 molar = 1 mol/liter
    # 1 molar = 1000 * millimolar
    # 1 millimolar = 1.0E-3 * molar
    col_value = "amphotericin b additive_value"
    col_units = "amphotericin b additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'micrograms/milliliter' or                     
                        str_units == "milligrams/milliliter" or 
                        str_units == "millimoles"):                     
                        if (str_units == 'milligrams/milliliter'):
                            df.loc[irow, col_units] = 'micrograms/milliliter' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+03
                        elif(str_units == 'millimoles'):
                            df.loc[irow, col_units] = None
                            df.loc[irow, col_value] = None
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
    
    # Process trypan units
    col_value = "trypan additive_value"
    col_units = "trypan additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
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
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
    
    # Process thymidine units
    # Chemical formula: C10H14N2O5
    # molar mass = 242.231 g/mol
    # 1 molar = 1 mol/liter
    # 1 molar = 1000 * millimolar
    # 1 millimolar = 1.0E-3 * molar
    col_value = "thymidine additive_value"
    col_units = "thymidine additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'micrograms/milliliter' or  
                        str_units == 'millimolar' or
                        str_units == "milligrams/milliliter" or 
                        str_units == "millimoles"):                     
                        if (str_units == 'milligrams/milliliter'):
                            df.loc[irow, col_units] = 'micrograms/milliliter' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+03
                        elif (str_units == 'millimolar'):
                            df.loc[irow, col_units] = 'micrograms/milliliter' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 242.231 
                        elif (str_units == 'millimoles'):
                            df.loc[irow, col_units] = None
                            df.loc[irow, col_value] = None
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
    
    # Process streptomycin units
    # Chemical formula: C21H39N7O12
    # molar mass = 581.580 g/mol
    # 1 molar = 1 mol/liter
    # 1 molar = 1000 * millimolar
    # 1 millimolar = 1.0E-3 * molar
    col_value = "streptomycin additive_value"
    col_units = "streptomycin additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'micrograms/milliliter' or                     
                        str_units == "milligrams/milliliter" or 
                        str_units == "millimolar" or 
                        str_units == "millimoles"):                     
                        if (str_units == 'milligrams/milliliter'):
                            df.loc[irow, col_units] = 'micrograms/milliliter' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+03
                        elif (str_units == "millimolar"):
                            df.loc[irow, col_units] = 'micrograms/milliliter' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 581.580
                        elif(str_units == 'millimoles'):
                            df.loc[irow, col_units] = None
                            df.loc[irow, col_value] = None
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
    
    # Process magnesium sulfate units
    # Chemical formula: MgSO4
    # molar mass = 120.366 g/mol
    # 1 molar = 1 mol/liter
    # 1 molar = 1000 * millimolar
    # 1 millimolar = 1.0E-3 * molar
    col_value = "magnesium sulfate additive_value"
    col_units = "magnesium sulfate additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'grams/liter' or                     
                        str_units == 'milligrams/liter' or 
                        str_units == 'millimolar' or 
                        str_units == "millimoles"):                     
                        if (str_units == 'milligrams/liter'):
                            df.loc[irow, col_units] = 'grams/liter' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E-03
                        elif (str_units == 'millimolar'):
                            df.loc[irow, col_units] = 'grams/liter' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 120.366 * 1.0E+03
                        elif(str_units == 'millimoles'):
                            df.loc[irow, col_units] = None
                            df.loc[irow, col_value] = None
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
    
    # Process sodium bicarbonate units
    # Chemical formula: NaHCO3
    # molar mass = 84.007 g/mol
    # 1 molar = 1 mol/liter
    # 1 molar = 1000 * millimolar
    # 1 millimolar = 1.0E-3 * molar
    col_value = "sodium bicarbonate additive_value"
    col_units = "sodium bicarbonate additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'grams/liter' or   
                        str_units == 'millimolar' or  
                        str_units == "milligrams/liter" or 
                        str_units == "millimoles"):                     
                        if (str_units == 'milligrams/liter'):
                            df.loc[irow, col_units] = 'grams/liter' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E-03
                        elif (str_units == 'millimolar'):
                            df.loc[irow, col_units] = 'grams/liter' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 84.007 * 1.0E+03
                        elif(str_units == 'millimoles'):
                            df.loc[irow, col_units] = None
                            df.loc[irow, col_value] = None
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
    
    # Process ferric nitrate units
    col_value = "ferric nitrate additive_value"
    col_units = "ferric nitrate additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'milligrams/milliliter' or 
                        str_units == 'micrograms/milliliter'):
                        if (str_units == 'micrograms/milliliter'):
                            df.loc[irow, col_units] = 'milligrams/milliliter' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E-03
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
    
    # Process steptomycin units
    col_value = "steptomycin additive_value"
    col_units = "steptomycin additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'micrograms/milliliter' or 
                        str_units == 'milligrams/milliliter'):
                        if (str_units == 'milligrams/milliliter'):
                            df.loc[irow, col_units] = 'micrograms/milliliter' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+03
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
       
    # Process phosphate units
    col_value = "phosphate additive_value"
    col_units = "phosphate additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'millimoles' or 
                        str_units == 'micromoles'):
                        if (str_units == 'micromoles'):
                            df.loc[irow, col_units] = 'millimoles' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E-03
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
    
    # Process potassium bisulfate units
    col_value = "potassium bisulfate additive_value"
    col_units = "potassium bisulfate additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'normality' or 
                        str_units == 'unitless'):
                        if (str_units == 'unitless'):
                            df.loc[irow, col_units] = 'normality' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
        
    # Process penicilin units
    # Spelling is wrong.  This additive is being merged with penicillin.
    col_value = "penicilin additive_value"
    col_units = "penicilin additive_unit"
    newcol_value = "penicillin additive_value"
    newcol_units = "penicillin additive_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'enzyme units/milliliter' or 
                        str_units == 'enzyme units/liter'):
                        if (str_units == 'enzyme units/liter'):
                            df.loc[irow, newcol_units] = 'enzyme units/milliliter' 
                            df.loc[irow, newcol_value] = df.loc[irow, col_value] * 1.0E-03
                        elif (str_units == 'enzyme units/milliliter'):
                            df.loc[irow, newcol_units] = 'enzyme units/milliliter' 
                            df.loc[irow, newcol_value] = df.loc[irow, col_value]
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)
            
    return df 