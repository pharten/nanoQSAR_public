'''
This module contains the definition of a function that 
processes the units for the parameters. 

Created on Feb 15, 2021

@author: Wmelende
'''

import math

def process_parameters_units(df):
    '''
    Name
    ----
    process_parameters_units
    
    Description
    -----------
    This function processes the parameters' units.
    
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
    
    ########################################################################################################## 
    # Process parameter Units
    # 1 ppm = approximately 1 mg/L = 1 ug/mL
    # The inverse of log(x) = y is x = 10**y
    ##########################################################################################################
    # Process Particle Concentration units
    # The units of milligrams and micrograms are not compatible with concentration units.
    # The unit of micromolar is a concentration unit but we must know the molar weight of the 
    # particle/chemical in question.
    col_value = "particle concentration parameter_value"
    col_units = "particle concentration parameter_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'micrograms/milliliter' or 
                        str_units == 'milligrams/liter' or
                        str_units == 'parts per million' or 
                        str_units == 'parts per billion' or
                        str_units == 'micrograms/cubed meter' or 
                        str_units == 'milligrams' or 
                        str_units == 'micrograms' or 
                        str_units == 'micromolar' or 
                        str_units == 'log of micrograms/milliliter'):
                        if (str_units == 'micrograms/milliliter'):
                            if (df.loc[irow, col_value] < 0.0):
                                df.loc[irow, col_value] = 0.0
                        elif (str_units == 'parts per million' or str_units == 'milligrams/liter' ):
                            df.loc[irow, col_units] = 'micrograms/milliliter' 
                        elif (str_units == 'parts per billion'):
                            df.loc[irow, col_units] = 'micrograms/milliliter' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1E-3
                        elif (str_units == 'micrograms/cubed meter'):
                            df.loc[irow, col_units] = 'micrograms/milliliter' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1E-6
                        elif (str_units == 'log of micrograms/milliliter'):
                            df.loc[irow, col_units] = 'micrograms/milliliter' 
                            df.loc[irow, col_value] = 10**df.loc[irow, col_value] 
                        elif (str_units == 'log of micrograms/milliliter'):
                            print(df.loc[irow, col_value])
                            df.loc[irow, col_units] = 'micrograms/milliliter' 
                            df.loc[irow, col_value] = 10**df.loc[irow, col_value] 
                        elif(str_units == 'milligrams' or str_units == 'micrograms' or str_units == 'micromolar'):
                            df.loc[irow, col_units] = 'micrograms/milliliter' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
    
    # Process Particle Concentration Log units
    # This parameter is being merged with particle concentration (see above).
    col_value = "particle concentration log parameter_value"
    newcol_value = "particle concentration parameter_value"
    col_units = "particle concentration log parameter_unit"
    newcol_units = "particle concentration parameter_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'micrograms/milliliter' or 
                        str_units == 'milligrams/liter' or
                        str_units == 'parts per million' or 
                        str_units == 'parts per billion' or
                        str_units == 'micrograms/cubed meter'):
                        if (str_units == 'micrograms/milliliter' or 'milligrams/liter' or str_units == 'parts per million'):
                            df.loc[irow, newcol_units] = 'micrograms/milliliter' 
                            df.loc[irow, newcol_value] = 10**df.loc[irow, col_value] 
                        elif (str_units == 'parts per billion'):
                            df.loc[irow, newcol_units] = 'micrograms/milliliter' 
                            df.loc[irow, newcol_value] = 10**df.loc[irow, col_value] * 1E-3
                        elif (str_units == 'micrograms/cubed meter'):
                            df.loc[irow, newcol_units] = 'micrograms/milliliter' 
                            df.loc[irow, newcol_value] = 10**df.loc[irow, col_value] * 1E-6
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
    
    
    # Process Particle Mass units
    col_value = "particle mass parameter_value"
    col_units = "particle mass parameter_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
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
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+3
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
    
    
    # Process Irradiance Power units
    col_value = "irradiance power parameter_value"
    col_units = "irradiance power parameter_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'microwatts/square centimeter' or 
                        str_units == 'milliwatts/square centimeter'):
                        if (str_units == 'milliwatts/square centimeter'):
                            df.loc[irow, col_units] = 'microwatts/square centimeter' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+3
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
    
    # Process Duration Incubation units
    col_value = "duration incubation parameter_value"
    col_units = "duration incubation parameter_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'hours' or 
                        str_units == 'minutes'):
                        if (str_units == 'minutes'):
                            df.loc[irow, col_units] = 'hours' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] / 60
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " 
                                         + str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
        
    # Process concentration silver units
    col_value = "concentration silver nitrate parameter_value"
    col_units = "concentration silver nitrate parameter_unit"
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
                        error_message = ("Unrecognized units: " + str_units + ", column = " 
                                         + str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)      
        
    # Process PH units
    col_value = "ph parameter_value"
    col_units = "ph parameter_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'pH' or 
                        str_units == 'unitless'):
                        if (str_units == 'unitless'):
                            df.loc[irow, col_units] = 'pH' 
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " 
                                         + str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)   
    
    # Process measured zinc sulfate concentration units
    col_value = "measured zinc sulfate concentration parameter_value"
    col_units = "measured zinc sulfate concentration parameter_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
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
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " +
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)      
    
    # Process measured material concentration units
    col_value = "measured material concentration parameter_value"
    col_units = "measured material concentration parameter_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
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
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)      
    
    # Process concentration sodium chloride units
    col_value = "concentration sodium chloride parameter_value"
    col_units = "concentration sodium chloride parameter_unit"
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
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+03
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process concentration calcium chloride units
    col_value = "concentration calcium chloride parameter_value"
    col_units = "concentration calcium chloride parameter_unit"
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
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+03
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)   
    
    # Process time of measurement units
    col_value = "time of measurement parameter_value"
    col_units = "time of measurement parameter_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'days' or str_units == 'hours' or str_units == 'minutes'):
                        if (str_units == 'days'):
                            df.loc[irow, col_units] = 'hours' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 24
                        elif (str_units == 'minutes'):
                            df.loc[irow, col_units] = 'hours' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] / 60
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)     
    
    # Process hydrodynamic diameter units
    col_value = "hydrodynamic diameter parameter_value"
    col_units = "hydrodynamic diameter parameter_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
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
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)    
    
    # Process duration exposure units
    col_value = "duration exposure parameter_value"
    col_units = "duration exposure parameter_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'weeks' or str_units == 'days' or str_units == 'hours' or str_units == 'minutes'):
                        if (str_units == 'weeks'):
                            df.loc[irow, col_units] = 'hours' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 7 * 24
                        elif (str_units == 'days'):
                            df.loc[irow, col_units] = 'hours' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 24
                        elif (str_units == 'minutes'):
                            df.loc[irow, col_units] = 'hours' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] / 60
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)       
    
    # Process duration aging units
    col_value = "duration aging parameter_value"
    col_units = "duration aging parameter_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'days' or str_units == 'hours' or str_units == 'minutes'):
                        if (str_units == 'hours'):
                            df.loc[irow, col_units] = 'days' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] / 24
                        elif(str_units == 'minutes'):
                            df.loc[irow, col_units] = 'days' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] / (24 * 60)
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
        
    # Process duration irradiation units
    col_value = "duration irradiation parameter_value"
    col_units = "duration irradiation parameter_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'hour' or str_units == 'hours' or str_units == 'minutes'):
                        if (str_units == 'hour'):
                            df.loc[irow, col_units] = 'hours' 
                        elif(str_units == 'minutes'):
                            df.loc[irow, col_units] = 'hours' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] / 60
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)    
    
    # Process temperature units
    col_value = "temperature parameter_value"
    col_units = "temperature parameter_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'celsius' or str_units == 'Fahrenheit'):
                        if (str_units == 'Fahrenheit'):
                            df.loc[irow, col_units] = 'celsius' 
                            df.loc[irow, col_value] = (df[col_value].iloc[irow] - 32.0) * 5 / 9    
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)  
        
    # Process concentration zinc units
    col_value = "concentration zinc parameter_value"
    col_units = "concentration zinc parameter_unit"
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
        
    # Process concentration cadmium sulfate units
    col_value = "concentration cadmium sulfate parameter_value"
    col_units = "concentration cadmium sulfate parameter_unit"
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
        
    # Process duration dissolution units
    col_value = "duration dissolution parameter_value"
    col_units = "duration dissolution parameter_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'hours' or str_units == 'minutes'):
                        if(str_units == 'minutes'):
                            df.loc[irow, col_units] = 'hours' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] / 60
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message) 
    
    # Process concentration copper units
    col_value = "concentration copper parameter_value"
    col_units = "concentration copper parameter_unit"
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
        
    # Process concentration copper units
    col_value = "concentration suwannee river natural organic matter parameter_value"
    col_units = "concentration suwannee river natural organic matter parameter_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
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
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)    
    
    # Process concentration copper units
    col_value = "concentration lutein parameter_value"
    col_units = "concentration lutein parameter_unit"
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
    
    # Process concentration dehydroascorbic acid units
    col_value = "concentration dehydroascorbic acid parameter_value"
    col_units = "concentration dehydroascorbic acid parameter_unit"
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
    
    # Process concentration ascorbic acid 6-palmitate units
    col_value = "concentration ascorbic acid 6-palmitate parameter_value"
    col_units = "concentration ascorbic acid 6-palmitate parameter_unit"
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
    
    # Process irradiance contaminant units
    col_value = "irradiance parameter_value"
    col_units = "irradiance parameter_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'joules/square centimeter' or 
                        str_units == 'joules/square meter'):
                        if (str_units == 'joules/square meter'):
                            df.loc[irow, col_units] = 'joules/square centimeter' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E-04
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)            
    
    # Process concentration poly l-lysine units
    col_value = "concentration poly l-lysine parameter_value"
    col_units = "concentration poly l-lysine parameter_unit"
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
    
    # Process oxygen units
    col_value = "oxygen parameter_value"
    col_units = "oxygen parameter_unit"
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
    
    # Process laser wavelength units
    col_value = "laser wavelength parameter_value"
    col_units = "laser wavelength parameter_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
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
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)            
    
    # Process duration lutein exposure units
    col_value = "duration lutein exposure parameter_value"
    col_units = "duration lutein exposure parameter_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'hours' or 
                        str_units == 'days'):
                        if (str_units == 'days'):
                            df.loc[irow, col_units] = 'hours' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 24
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)            
    
    # Process duration lutein exposure units
    col_value = "duration dehydroascorbic acid exposure parameter_value"
    col_units = "duration dehydroascorbic acid exposure parameter_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'hours' or 
                        str_units == 'days'):
                        if (str_units == 'days'):
                            df.loc[irow, col_units] = 'hours' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 24
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)        
    
    # Process duration ascorbic acid 6-palmitate exposure units
    col_value = "duration ascorbic acid 6-palmitate exposure parameter_value"
    col_units = "duration ascorbic acid 6-palmitate exposure parameter_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'hours' or 
                        str_units == 'days'):
                        if (str_units == 'days'):
                            df.loc[irow, col_units] = 'hours' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 24
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)       
    
    # Process irradiation power units
    col_value = "irradiation power parameter_value"
    col_units = "irradiation power parameter_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'joules/square meter' or 
                        str_units == 'joules/square centimeter'):
                        if (str_units == 'joules/square centimeter'):
                            df.loc[irow, col_units] = 'joules/square meter' 
                            df.loc[irow, col_value] = df.loc[irow, col_value] * 1.0E+04
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)            
               
    # Process number of cells units
    col_value = "number of cells parameter_value"
    col_units = "number of cells parameter_unit"
    if col_value in df.columns:
        df[col_value] = df[df[col_value]!= None][col_value].astype(float)
        try:
            for irow in range(0, nrow):
                if (math.isnan(df[col_value].iloc[irow])):
                    continue
                else:
                    str_units = df[col_units].iloc[irow]
                    if (str_units == 'cells' or 
                        str_units == 'unitless'):
                        if (str_units == 'unitless'):
                            df.loc[irow, col_units] = 'cells'
                    else:
                        error_message = ("Unrecognized units: " + str_units + ", column = " + 
                                         str(col_value) + " at row " + str(irow))
                        raise ValueError(error_message) 
                                           
        except ValueError as msg:
            error_message = str(msg) + ", " + str(col_value) + ", " + col_units +  ", row = " + str(irow)
            print(error_message)            
    
    # Process bicucullin dose contaminant units
    col_value = "bicucullin dose parameter_value"
    col_units = "bicucullin dose parameter_unit"
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
    
    # Process concentration carbon dioxide units
    col_value = "concentration carbon dioxide parameter_value"
    col_units = "concentration carbon dioxide parameter_unit"
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
        
    # Process dose contaminant units
    col_value = "dose parameter_value"
    col_units = "dose parameter_unit"
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
            
    return df