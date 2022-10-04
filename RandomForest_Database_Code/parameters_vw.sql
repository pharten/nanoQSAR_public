CREATE OR REPLACE VIEW dev_naknowbase.parameters_vw AS
-- detail view of parameters self joined to compute rank. uses parameters rank technique with CASE
-- to separate rows into columns. The parameters fields are concatenated into one field. 
-- the parameters joins and case statement transform up to 18 rows into 18 columns field.
-- 83233 rows in parameters

-- rank() is not a function until mysql 8.0. so this uses the non-equi outer join and count to rank
SELECT pm.assay_assayID, pm.assay_publication_DOI,
      count(pm2.idparameters)+1 idrank,
      pm.idparameters, pm.parameterName, pm.parameterNumberValue, pm.parameterUnit, pm.parameterNonNumberValue, 
      -- concat all parameters fields into 1 field
      dev_naknowbase.parameters_concat_fun( pm.idparameters, pm.parameterName, pm.parameterNumberValue,
      pm.parameterUnit, pm.parameterNonNumberValue ) parameters_concat,
 -- cannot use max in case since it already has a count
-- now max 19 parameters per assay
 CASE WHEN count(pm2.idparameters)+1 = 1 THEN 
    dev_naknowbase.parameters_concat_fun( pm.idparameters, pm.parameterName,  pm.parameterNumberValue, 
     pm.parameterUnit, pm.parameterNonNumberValue )
 END AS  parameters01_num_name_numval_unit_nonnum,
 CASE WHEN count(pm2.idparameters)+1 = 2 THEN 
    dev_naknowbase.parameters_concat_fun( pm.idparameters, pm.parameterName,  pm.parameterNumberValue, 
     pm.parameterUnit, pm.parameterNonNumberValue )
 END AS  parameters02_num_name_numval_unit_nonnum,
 CASE WHEN count(pm2.idparameters)+1 = 3 THEN 
    dev_naknowbase.parameters_concat_fun( pm.idparameters, pm.parameterName,  pm.parameterNumberValue, 
     pm.parameterUnit, pm.parameterNonNumberValue )
 END AS  parameters03_num_name_numval_unit_nonnum,
 CASE WHEN count(pm2.idparameters)+1 = 4 THEN 
    dev_naknowbase.parameters_concat_fun( pm.idparameters, pm.parameterName,  pm.parameterNumberValue, 
     pm.parameterUnit, pm.parameterNonNumberValue )
 END AS  parameters04_num_name_numval_unit_nonnum,
 CASE WHEN count(pm2.idparameters)+1 = 5 THEN 
    dev_naknowbase.parameters_concat_fun( pm.idparameters, pm.parameterName,  pm.parameterNumberValue, 
     pm.parameterUnit, pm.parameterNonNumberValue )
 END AS  parameters05_num_name_numval_unit_nonnum,
 CASE WHEN count(pm2.idparameters)+1 = 6 THEN 
    dev_naknowbase.parameters_concat_fun( pm.idparameters, pm.parameterName,  pm.parameterNumberValue, 
     pm.parameterUnit, pm.parameterNonNumberValue )
 END AS  parameters06_num_name_numval_unit_nonnum,
 CASE WHEN count(pm2.idparameters)+1 = 7 THEN 
    dev_naknowbase.parameters_concat_fun( pm.idparameters, pm.parameterName,  pm.parameterNumberValue, 
     pm.parameterUnit, pm.parameterNonNumberValue )
 END AS  parameters07_num_name_numval_unit_nonnum,
 CASE WHEN count(pm2.idparameters)+1 = 8 THEN 
    dev_naknowbase.parameters_concat_fun( pm.idparameters, pm.parameterName,  pm.parameterNumberValue, 
     pm.parameterUnit, pm.parameterNonNumberValue )
 END AS  parameters08_num_name_numval_unit_nonnum,
 CASE WHEN count(pm2.idparameters)+1 = 9 THEN 
    dev_naknowbase.parameters_concat_fun( pm.idparameters, pm.parameterName,  pm.parameterNumberValue, 
     pm.parameterUnit, pm.parameterNonNumberValue )
 END AS  parameters09_num_name_numval_unit_nonnum,
 CASE WHEN count(pm2.idparameters)+1 = 10 THEN 
    dev_naknowbase.parameters_concat_fun( pm.idparameters, pm.parameterName,  pm.parameterNumberValue, 
     pm.parameterUnit, pm.parameterNonNumberValue )
 END AS  parameters10_num_name_numval_unit_nonnum,
 CASE WHEN count(pm2.idparameters)+1 = 11 THEN 
    dev_naknowbase.parameters_concat_fun( pm.idparameters, pm.parameterName,  pm.parameterNumberValue, 
     pm.parameterUnit, pm.parameterNonNumberValue )
 END AS  parameters11_num_name_numval_unit_nonnum,
 CASE WHEN count(pm2.idparameters)+1 = 12 THEN 
    dev_naknowbase.parameters_concat_fun( pm.idparameters, pm.parameterName,  pm.parameterNumberValue, 
     pm.parameterUnit, pm.parameterNonNumberValue )
 END AS  parameters12_num_name_numval_unit_nonnum,
 CASE WHEN count(pm2.idparameters)+1 = 13 THEN 
    dev_naknowbase.parameters_concat_fun( pm.idparameters, pm.parameterName,  pm.parameterNumberValue, 
     pm.parameterUnit, pm.parameterNonNumberValue )
 END AS  parameters13_num_name_numval_unit_nonnum,
 CASE WHEN count(pm2.idparameters)+1 = 14 THEN 
    dev_naknowbase.parameters_concat_fun( pm.idparameters, pm.parameterName,  pm.parameterNumberValue, 
     pm.parameterUnit, pm.parameterNonNumberValue )
 END AS  parameters14_num_name_numval_unit_nonnum,
 CASE WHEN count(pm2.idparameters)+1 = 15 THEN 
    dev_naknowbase.parameters_concat_fun( pm.idparameters, pm.parameterName,  pm.parameterNumberValue, 
     pm.parameterUnit, pm.parameterNonNumberValue )
 END AS  parameters15_num_name_numval_unit_nonnum,
 CASE WHEN count(pm2.idparameters)+1 = 16 THEN 
    dev_naknowbase.parameters_concat_fun( pm.idparameters, pm.parameterName,  pm.parameterNumberValue, 
     pm.parameterUnit, pm.parameterNonNumberValue )
 END AS  parameters16_num_name_numval_unit_nonnum,
 CASE WHEN count(pm2.idparameters)+1 = 17 THEN 
    dev_naknowbase.parameters_concat_fun( pm.idparameters, pm.parameterName,  pm.parameterNumberValue, 
     pm.parameterUnit, pm.parameterNonNumberValue )
 END AS  parameters17_num_name_numval_unit_nonnum,
 CASE WHEN count(pm2.idparameters)+1 = 18 THEN 
    dev_naknowbase.parameters_concat_fun( pm.idparameters, pm.parameterName,  pm.parameterNumberValue, 
     pm.parameterUnit, pm.parameterNonNumberValue )
 END AS  parameters18_num_name_numval_unit_nonnum,
 CASE WHEN count(pm2.idparameters)+1 = 19 THEN 
    dev_naknowbase.parameters_concat_fun( pm.idparameters, pm.parameterName,  pm.parameterNumberValue, 
     pm.parameterUnit, pm.parameterNonNumberValue )
 END AS  parameters19_num_name_numval_unit_nonnum
FROM dev_naknowbase.parameters pm
LEFT OUTER JOIN dev_naknowbase.parameters pm2
  ON pm.assay_assayID = pm2.assay_assayID
 AND pm.assay_publication_DOI = pm2.assay_publication_DOI
 AND pm.idparameters > pm2.idparameters
-- this group by returns the same number of rows as without group by. It is needed for the rank count
GROUP BY pm.idparameters, pm.assay_assayID, pm.assay_publication_DOI
ORDER BY pm.assay_assayID, pm.assay_publication_DOI, idrank, pm.idparameters
;
