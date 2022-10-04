CREATE OR REPLACE VIEW dev_naknowbase.medium_additive_vw AS
-- detail view of medium joined to additive_vw. uses additive rank technique with CASE
-- to separate rows into columns. The additive fields are concatenated into one field. 
-- the additive joins and case statement transform up to 16 rows into 16 columns field.
-- 86 rows in medium. pub is required. GROUP BY 1 row per medium  86 rows
SELECT md.MediumID, md.publication_DOI, md.MediumDescription,
       max(additive01_num_name_amt_unit) AS additive01_num_name_amt_unit,
       max(additive02_num_name_amt_unit) AS additive02_num_name_amt_unit,
       max(additive03_num_name_amt_unit) AS additive03_num_name_amt_unit,
       max(additive04_num_name_amt_unit) AS additive04_num_name_amt_unit,
       max(additive05_num_name_amt_unit) AS additive05_num_name_amt_unit,
       max(additive06_num_name_amt_unit) AS additive06_num_name_amt_unit,
       max(additive07_num_name_amt_unit) AS additive07_num_name_amt_unit,
       max(additive08_num_name_amt_unit) AS additive08_num_name_amt_unit,
       max(additive09_num_name_amt_unit) AS additive09_num_name_amt_unit,
       max(additive10_num_name_amt_unit) AS additive10_num_name_amt_unit,
       max(additive11_num_name_amt_unit) AS additive11_num_name_amt_unit,
       max(additive12_num_name_amt_unit) AS additive12_num_name_amt_unit,
       max(additive13_num_name_amt_unit) AS additive13_num_name_amt_unit,
       max(additive14_num_name_amt_unit) AS additive14_num_name_amt_unit,
       max(additive15_num_name_amt_unit) AS additive15_num_name_amt_unit,
       max(additive16_num_name_amt_unit) AS additive16_num_name_amt_unit
FROM dev_naknowbase.medium md
LEFT OUTER JOIN dev_naknowbase.additive_vw adv
  ON md.MediumID = adv.medium_MediumID
 AND md.publication_DOI = adv.medium_publication_DOI
GROUP BY md.MediumID, md.publication_DOI, md.MediumDescription
ORDER BY md.mediumid, md.publication_DOI
;