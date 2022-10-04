CREATE OR REPLACE VIEW dev_naknowbase.additive_vw AS
-- detail view of additive self-joined to compute rank. uses additive rank technique with CASE
-- to separate rows into columns. The additive fields are concatenated into one field. 
-- the additive joins and case statement transform up to 7 rows into seven columns field.
-- 302 rows in additive
-- now 16 additives per medium
-- rank() is not a function until mysql 8.0. so this uses the non-equi outer join and count to rank
SELECT ad.medium_MediumID, ad.medium_publication_DOI,
      count(ad2.idadditive)+1 idrank,
      ad.idadditive, ad.AdditiveAmount, ad.AdditiveUnit, ad.AdditiveName,
      -- concat all additive fields into 1 field
      -- max lengths id=2 amt=6 unit=5 name=43 concat lengths id=2 amt=6 unit=5 name=45
      -- new lengths id=4 name=58 amt=7 unit=23
      dev_naknowbase.additive_concat_fun(ad.idadditive, ad.AdditiveAmount, ad.AdditiveUnit, ad.AdditiveName) additive_concat,
 -- cannot use max in case since it already has a count
 CASE WHEN count(ad2.idadditive)+1 = 1 THEN 
    dev_naknowbase.additive_concat_fun(ad.idadditive, ad.AdditiveAmount, ad.AdditiveUnit, ad.AdditiveName)
 END AS  additive01_num_name_amt_unit,
 CASE WHEN count(ad2.idadditive)+1 = 2 THEN 
    dev_naknowbase.additive_concat_fun(ad.idadditive, ad.AdditiveAmount, ad.AdditiveUnit, ad.AdditiveName)
 END AS  additive02_num_name_amt_unit,
 CASE WHEN count(ad2.idadditive)+1 = 3 THEN 
    dev_naknowbase.additive_concat_fun(ad.idadditive, ad.AdditiveAmount, ad.AdditiveUnit, ad.AdditiveName)
 END AS  additive03_num_name_amt_unit,
 CASE WHEN count(ad2.idadditive)+1 = 4 THEN 
    dev_naknowbase.additive_concat_fun(ad.idadditive, ad.AdditiveAmount, ad.AdditiveUnit, ad.AdditiveName)
 END AS  additive04_num_name_amt_unit,
 CASE WHEN count(ad2.idadditive)+1 = 5 THEN 
    dev_naknowbase.additive_concat_fun(ad.idadditive, ad.AdditiveAmount, ad.AdditiveUnit, ad.AdditiveName)
 END AS  additive05_num_name_amt_unit,
 CASE WHEN count(ad2.idadditive)+1 = 6 THEN 
    dev_naknowbase.additive_concat_fun(ad.idadditive, ad.AdditiveAmount, ad.AdditiveUnit, ad.AdditiveName)
 END AS  additive06_num_name_amt_unit,
 CASE WHEN count(ad2.idadditive)+1 = 7 THEN 
    dev_naknowbase.additive_concat_fun(ad.idadditive, ad.AdditiveAmount, ad.AdditiveUnit, ad.AdditiveName)
 END AS  additive07_num_name_amt_unit,
 CASE WHEN count(ad2.idadditive)+1 = 8 THEN 
    dev_naknowbase.additive_concat_fun(ad.idadditive, ad.AdditiveAmount, ad.AdditiveUnit, ad.AdditiveName)
 END AS  additive08_num_name_amt_unit,
 CASE WHEN count(ad2.idadditive)+1 = 9 THEN 
    dev_naknowbase.additive_concat_fun(ad.idadditive, ad.AdditiveAmount, ad.AdditiveUnit, ad.AdditiveName)
 END AS  additive09_num_name_amt_unit,
 CASE WHEN count(ad2.idadditive)+1 = 10 THEN 
    dev_naknowbase.additive_concat_fun(ad.idadditive, ad.AdditiveAmount, ad.AdditiveUnit, ad.AdditiveName)
 END AS  additive10_num_name_amt_unit,
 CASE WHEN count(ad2.idadditive)+1 = 11 THEN 
    dev_naknowbase.additive_concat_fun(ad.idadditive, ad.AdditiveAmount, ad.AdditiveUnit, ad.AdditiveName)
 END AS  additive11_num_name_amt_unit,
 CASE WHEN count(ad2.idadditive)+1 = 12 THEN 
    dev_naknowbase.additive_concat_fun(ad.idadditive, ad.AdditiveAmount, ad.AdditiveUnit, ad.AdditiveName)
 END AS  additive12_num_name_amt_unit,
 CASE WHEN count(ad2.idadditive)+1 = 13 THEN 
    dev_naknowbase.additive_concat_fun(ad.idadditive, ad.AdditiveAmount, ad.AdditiveUnit, ad.AdditiveName)
 END AS  additive13_num_name_amt_unit,
 CASE WHEN count(ad2.idadditive)+1 = 14 THEN 
    dev_naknowbase.additive_concat_fun(ad.idadditive, ad.AdditiveAmount, ad.AdditiveUnit, ad.AdditiveName)
 END AS  additive14_num_name_amt_unit,
 CASE WHEN count(ad2.idadditive)+1 = 15 THEN 
    dev_naknowbase.additive_concat_fun(ad.idadditive, ad.AdditiveAmount, ad.AdditiveUnit, ad.AdditiveName)
 END AS  additive15_num_name_amt_unit,
 CASE WHEN count(ad2.idadditive)+1 = 16 THEN 
    dev_naknowbase.additive_concat_fun(ad.idadditive, ad.AdditiveAmount, ad.AdditiveUnit, ad.AdditiveName)
 END AS  additive16_num_name_amt_unit
FROM dev_naknowbase.additive ad
LEFT OUTER JOIN dev_naknowbase.additive ad2
  ON ad.idadditive > ad2.idadditive
 AND ad.medium_MediumID = ad2.medium_MediumID
 AND ad.medium_publication_DOI = ad2.medium_publication_DOI
-- this group by returns the same number of rows as without group by. It is needed for the rank count
GROUP BY ad.idadditive, ad.medium_MediumID, ad.medium_publication_DOI
ORDER BY ad.medium_MediumID, ad.medium_publication_DOI, idrank, ad.idadditive
;
