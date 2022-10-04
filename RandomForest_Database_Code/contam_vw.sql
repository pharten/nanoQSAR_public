CREATE OR REPLACE VIEW dev_naknowbase.contam_vw AS
-- detail view of contam self joined to compute rank. uses contam rank technique with CASE
-- to separate rows into columns. The contam fields are concatenated into one field. 
-- the contam joins and case statement transform up to 7 rows into seven columns field.
--  47 rows in contam
-- 20 is max contams per material.  
-- now 16 contams per material
-- rank() is not a function until mysql 8.0. so this uses the non-equi outer join and count to rank
SELECT ct.material_materialID, ct.material_publication_DOI,
      count(ct2.contamid)+1 idrank,
      ct.contamid, ct.Contaminant, ct.contamAmount, ct.contamUnit, ct.contamMethod,
      -- concat all contam fields into 1 field
      -- max lengths id=2 amt=6 unit=5 name=43 concat lengths id=2 amt=6 unit=5 name=45
      -- new lengths id=4 name=58 amt=7 unit=23
      dev_naknowbase.contam_concat_fun(ct.contamid, ct.contaminant, ct.contamAmount, ct.contamUnit, ct.contamMethod) contam_concat,
 -- cannot use max in case since it already has a count
 CASE WHEN count(ct2.contamid)+1 = 1 THEN 
    dev_naknowbase.contam_concat_fun(ct.contamid, ct.contaminant, ct.contamAmount, ct.contamUnit, ct.contamMethod)
 END AS  contam01_num_name_amt_unit_meth,
 CASE WHEN count(ct2.contamid)+1 = 2 THEN 
    dev_naknowbase.contam_concat_fun(ct.contamid, ct.contaminant, ct.contamAmount, ct.contamUnit, ct.contamMethod)
 END AS  contam02_num_name_amt_unit_meth,
 CASE WHEN count(ct2.contamid)+1 = 3 THEN 
    dev_naknowbase.contam_concat_fun(ct.contamid, ct.contaminant, ct.contamAmount, ct.contamUnit, ct.contamMethod)
 END AS  contam03_num_name_amt_unit_meth,
 CASE WHEN count(ct2.contamid)+1 = 4 THEN 
    dev_naknowbase.contam_concat_fun(ct.contamid, ct.contaminant, ct.contamAmount, ct.contamUnit, ct.contamMethod)
 END AS  contam04_num_name_amt_unit_meth,
 CASE WHEN count(ct2.contamid)+1 = 5 THEN 
    dev_naknowbase.contam_concat_fun(ct.contamid, ct.contaminant, ct.contamAmount, ct.contamUnit, ct.contamMethod)
 END AS  contam05_num_name_amt_unit_meth,
 CASE WHEN count(ct2.contamid)+1 = 6 THEN 
    dev_naknowbase.contam_concat_fun(ct.contamid, ct.contaminant, ct.contamAmount, ct.contamUnit, ct.contamMethod)
 END AS  contam06_num_name_amt_unit_meth,
 CASE WHEN count(ct2.contamid)+1 = 7 THEN 
    dev_naknowbase.contam_concat_fun(ct.contamid, ct.contaminant, ct.contamAmount, ct.contamUnit, ct.contamMethod)
 END AS  contam07_num_name_amt_unit_meth,
 CASE WHEN count(ct2.contamid)+1 = 8 THEN 
    dev_naknowbase.contam_concat_fun(ct.contamid, ct.contaminant, ct.contamAmount, ct.contamUnit, ct.contamMethod)
 END AS  contam08_num_name_amt_unit_meth,
 CASE WHEN count(ct2.contamid)+1 = 9 THEN 
    dev_naknowbase.contam_concat_fun(ct.contamid, ct.contaminant, ct.contamAmount, ct.contamUnit, ct.contamMethod)
 END AS  contam09_num_name_amt_unit_meth,
 CASE WHEN count(ct2.contamid)+1 = 10 THEN 
    dev_naknowbase.contam_concat_fun(ct.contamid, ct.contaminant, ct.contamAmount, ct.contamUnit, ct.contamMethod)
 END AS  contam10_num_name_amt_unit_meth,
 CASE WHEN count(ct2.contamid)+1 = 11 THEN 
    dev_naknowbase.contam_concat_fun(ct.contamid, ct.contaminant, ct.contamAmount, ct.contamUnit, ct.contamMethod)
 END AS  contam11_num_name_amt_unit_meth,
 CASE WHEN count(ct2.contamid)+1 = 12 THEN 
    dev_naknowbase.contam_concat_fun(ct.contamid, ct.contaminant, ct.contamAmount, ct.contamUnit, ct.contamMethod)
 END AS  contam12_num_name_amt_unit_meth,
 CASE WHEN count(ct2.contamid)+1 = 13 THEN 
    dev_naknowbase.contam_concat_fun(ct.contamid, ct.contaminant, ct.contamAmount, ct.contamUnit, ct.contamMethod)
 END AS  contam13_num_name_amt_unit_meth,
 CASE WHEN count(ct2.contamid)+1 = 14 THEN 
    dev_naknowbase.contam_concat_fun(ct.contamid, ct.contaminant, ct.contamAmount, ct.contamUnit, ct.contamMethod)
 END AS  contam14_num_name_amt_unit_meth,
 CASE WHEN count(ct2.contamid)+1 = 15 THEN 
    dev_naknowbase.contam_concat_fun(ct.contamid, ct.contaminant, ct.contamAmount, ct.contamUnit, ct.contamMethod)
 END AS  contam15_num_name_amt_unit_meth,
 CASE WHEN count(ct2.contamid)+1 = 16 THEN 
    dev_naknowbase.contam_concat_fun(ct.contamid, ct.contaminant, ct.contamAmount, ct.contamUnit, ct.contamMethod)
 END AS  contam16_num_name_amt_unit_meth,
 CASE WHEN count(ct2.contamid)+1 = 17 THEN 
    dev_naknowbase.contam_concat_fun(ct.contamid, ct.contaminant, ct.contamAmount, ct.contamUnit, ct.contamMethod)
 END AS  contam17_num_name_amt_unit_meth,
 CASE WHEN count(ct2.contamid)+1 = 18 THEN 
    dev_naknowbase.contam_concat_fun(ct.contamid, ct.contaminant, ct.contamAmount, ct.contamUnit, ct.contamMethod)
 END AS  contam18_num_name_amt_unit_meth,
 CASE WHEN count(ct2.contamid)+1 = 19 THEN 
    dev_naknowbase.contam_concat_fun(ct.contamid, ct.contaminant, ct.contamAmount, ct.contamUnit, ct.contamMethod)
 END AS  contam19_num_name_amt_unit_meth,
 CASE WHEN count(ct2.contamid)+1 = 20 THEN 
    dev_naknowbase.contam_concat_fun(ct.contamid, ct.contaminant, ct.contamAmount, ct.contamUnit, ct.contamMethod)
 END AS  contam20_num_name_amt_unit_meth
FROM dev_naknowbase.contam ct
LEFT OUTER JOIN dev_naknowbase.contam ct2
  ON ct.contamid > ct2.contamid
 AND ct.material_materialID = ct2.material_materialID
 AND ct.material_publication_DOI = ct2.material_publication_DOI
-- this group by returns the same number of rows as without group by. It is needed for the rank count
GROUP BY ct.contamid, ct.material_materialID, ct.material_publication_DOI
ORDER BY ct.material_materialID, ct.material_publication_DOI, idrank, ct.contamid
;
