'''
Created on Feb 25, 2021

@author: Wmelende
'''


def delete_unwanted_columns(df):
    # Generate list containing columns to be deleted.
    columns_to_be_deleted = ['assayID', 'publication_DOI', 'medium_MediumID', 'medium_publication_DOI',
                             'material_MaterialID', 'material_publication_DOI', 'AssayName',
                             'mediumDescription', 'SynthesisMethod', 'CASRN', 'Supplier',
                             'ProductNumber', 'LotNumber', 'material_medium_MediumID',
                             'material_medium_publication_DOI', 'PubTitle', 'Journal',
                             #'year',
                             'FirstAuthor', 'Volume', 'Issue', 'PageStart', 'PageEnd', 'Keywords',
                             'Correspondence', 'Affiliation', 'Abstract', 'OuterDiameterApproxSymbol',
                             #'OuterDiameterUnit',
                             'OuterDiameterUncertainty', 'OuterDiameterMethod',
                             #'ThicknessUnit',
                             'ThicknessUncertainty', 'SurfaceAreaApproxSymbo',
                             #'SurfaceAreaUnit',
                             'SurfaceAreaMethod', 'PurityApproxSymbol',
                             #'PurityUnit', 
                             'PurityRefChemical', 'PurityMethod', 'HydrodynamicDiameterApproxSymbol', 
                             #'HydrodynamicDiameterUnit',
                             'HydrodynamicDiameterMethod',
                             #'ChargeUnit', 
                             'ChargeMethod', 'MaterialFGID', 'product type parameter_nonnum',  
                             'sensor type parameter_nonnum', 'subject source parameter_nonnum', 
                             'air parameter_nonnum', 'product parameter_nonnum', 'substrate parameter_nonnum',
                             #'biochemical name parameter_nonnum',
                             'copper source parameter_nonnum', 
                             'synthesis pathway parameter_nonnum',
                             #'subpathway parameter_nonnum',
                             'cell fixation parameter_nonnum', 'product component parameter_nonnum', 
                             'sample parameter_nonnum', 'gene parameter_nonnum', 'instrument parameter_nonnum',
                             'band pass filter parameter_nonnum', 'strain parameter_nonnum',
                             'filter parameter_nonnum', 'drug challenge parameter_nonnum']
    
    # Extract column names
    column_names = list(df.columns)
    
    columns_to_be_deleted = [icol for icol in columns_to_be_deleted if icol in column_names]
    
    # Extract the columns with contaminant_method fields
    subs_value = "contaminant_method"
    contaminant_method_columns  = [icol for icol in column_names if subs_value in icol]
    
    # Extract columns with result_uncertainty 
    subs_value = "result_uncertainty"
    result_uncertainty_columns  = [icol for icol in column_names if subs_value in icol]
    
    # Extract columns with result_approximation 
    subs_value = "result_approximation"
    result_approximation_columns  = [icol for icol in column_names if subs_value in icol]
    
    # Extract columns with result_detail
    subs_value = "result_detail"
    result_detail_columns  = [icol for icol in column_names if subs_value in icol]
    
    # Extract all unwanted columns
    unwanted_columns = (columns_to_be_deleted + contaminant_method_columns +
                        result_uncertainty_columns + result_approximation_columns + result_detail_columns)
    
    df.drop(unwanted_columns, inplace = True, axis = 1)
    
    return df