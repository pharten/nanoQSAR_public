-- This command runs the assay_all_vw that joins, concatenates, and pivots the data.
-- It generates one row per assay. 

-- 22325 rows
SELECT * FROM dev_naknowbase.assay_all_vw ORDER BY publication_DOI, assayID ;
-- Then click the export icon to export to a CSV file on your network drive. 
-- Then follow the instructions How to Import CSV UTF8 Into Excel .pdf

/* The hierarchy of view and table joins and function calls
assay_all_vw
  assay table
  publication table
  medium_additive_vw
    additive_vw
      additive_concat_fun
      additive table
  material_contam_vw
    contam_vw
      contam_concat_fun
      contam table
    materialfg table
  result_vw
    result_concat_fun
    result table
  parameters_vw
    parameters_concat_fun
    parameters table
  molecular_result table
*/