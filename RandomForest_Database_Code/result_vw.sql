CREATE OR REPLACE VIEW dev_naknowbase.result_vw AS
-- detail view of result self joined to compute rank. uses result rank technique with CASE
-- to separate rows into columns. The result fields are concatenated into one field. 
-- the result joins and case statement transform up to 18 rows into 18 columns field.
-- 24693 rows in result

-- rank() is not a function until mysql 8.0. so this uses the non-equi outer join and count to rank
SELECT rs.assay_assayID, rs.assay_publication_DOI,
      count(rs2.resultid)+1 idrank,
      rs.resultid, rs.resultType, rs.resultValue, rs.resultUnit, 
      -- concat all result fields into 1 field
      -- max lengths id=2 amt=6 unit=5 name=43 concat lengths id=2 amt=6 unit=5 name=45
      -- new lengths id=4 name=58 amt=7 unit=23
      dev_naknowbase.result_concat_fun( rs.resultid, rs.resulttype, rs.resultdetails, rs.resultvalue,
      rs.resultapproxsymbol, rs.resultunit, rs.resultuncertainty, rs.resultlow, rs.resulthigh ) result_concat,
 -- cannot use max in case since it already has a count
 CASE WHEN count(rs2.resultid)+1 = 1 THEN 
    dev_naknowbase.result_concat_fun( rs.resultid, rs.resulttype, rs.resultdetails, rs.resultvalue, 
    rs.resultapproxsymbol, rs.resultunit, rs.resultuncertainty, rs.resultlow, rs.resulthigh )
 END AS  result01_num_type_dtl_val_approx_unit_uncert_low_hi,
 CASE WHEN count(rs2.resultid)+1 = 2 THEN 
    dev_naknowbase.result_concat_fun( rs.resultid, rs.resulttype, rs.resultdetails, rs.resultvalue, 
    rs.resultapproxsymbol, rs.resultunit, rs.resultuncertainty, rs.resultlow, rs.resulthigh )
 END AS  result02_num_type_dtl_val_approx_unit_uncert_low_hi,
 CASE WHEN count(rs2.resultid)+1 = 3 THEN 
    dev_naknowbase.result_concat_fun( rs.resultid, rs.resulttype, rs.resultdetails, rs.resultvalue, 
    rs.resultapproxsymbol, rs.resultunit, rs.resultuncertainty, rs.resultlow, rs.resulthigh )
 END AS  result03_num_type_dtl_val_approx_unit_uncert_low_hi,
 CASE WHEN count(rs2.resultid)+1 = 4 THEN 
    dev_naknowbase.result_concat_fun( rs.resultid, rs.resulttype, rs.resultdetails, rs.resultvalue, 
    rs.resultapproxsymbol, rs.resultunit, rs.resultuncertainty, rs.resultlow, rs.resulthigh )
 END AS  result04_num_type_dtl_val_approx_unit_uncert_low_hi,
 CASE WHEN count(rs2.resultid)+1 = 5 THEN 
    dev_naknowbase.result_concat_fun( rs.resultid, rs.resulttype, rs.resultdetails, rs.resultvalue, 
    rs.resultapproxsymbol, rs.resultunit, rs.resultuncertainty, rs.resultlow, rs.resulthigh )
 END AS  result05_num_type_dtl_val_approx_unit_uncert_low_hi,
 CASE WHEN count(rs2.resultid)+1 = 6 THEN 
    dev_naknowbase.result_concat_fun( rs.resultid, rs.resulttype, rs.resultdetails, rs.resultvalue, 
    rs.resultapproxsymbol, rs.resultunit, rs.resultuncertainty, rs.resultlow, rs.resulthigh )
 END AS  result06_num_type_dtl_val_approx_unit_uncert_low_hi,
 CASE WHEN count(rs2.resultid)+1 = 7 THEN 
    dev_naknowbase.result_concat_fun( rs.resultid, rs.resulttype, rs.resultdetails, rs.resultvalue, 
    rs.resultapproxsymbol, rs.resultunit, rs.resultuncertainty, rs.resultlow, rs.resulthigh )
 END AS  result07_num_type_dtl_val_approx_unit_uncert_low_hi,
 CASE WHEN count(rs2.resultid)+1 = 8 THEN 
    dev_naknowbase.result_concat_fun( rs.resultid, rs.resulttype, rs.resultdetails, rs.resultvalue, 
    rs.resultapproxsymbol, rs.resultunit, rs.resultuncertainty, rs.resultlow, rs.resulthigh )
 END AS  result08_num_type_dtl_val_approx_unit_uncert_low_hi,
 CASE WHEN count(rs2.resultid)+1 = 9 THEN 
    dev_naknowbase.result_concat_fun( rs.resultid, rs.resulttype, rs.resultdetails, rs.resultvalue, 
    rs.resultapproxsymbol, rs.resultunit, rs.resultuncertainty, rs.resultlow, rs.resulthigh )
 END AS  result09_num_type_dtl_val_approx_unit_uncert_low_hi,
 CASE WHEN count(rs2.resultid)+1 = 10 THEN 
    dev_naknowbase.result_concat_fun( rs.resultid, rs.resulttype, rs.resultdetails, rs.resultvalue, 
    rs.resultapproxsymbol, rs.resultunit, rs.resultuncertainty, rs.resultlow, rs.resulthigh )
 END AS  result10_num_type_dtl_val_approx_unit_uncert_low_hi,
 CASE WHEN count(rs2.resultid)+1 = 11 THEN 
    dev_naknowbase.result_concat_fun( rs.resultid, rs.resulttype, rs.resultdetails, rs.resultvalue, 
    rs.resultapproxsymbol, rs.resultunit, rs.resultuncertainty, rs.resultlow, rs.resulthigh )
 END AS  result11_num_type_dtl_val_approx_unit_uncert_low_hi,
 CASE WHEN count(rs2.resultid)+1 = 12 THEN 
    dev_naknowbase.result_concat_fun( rs.resultid, rs.resulttype, rs.resultdetails, rs.resultvalue, 
    rs.resultapproxsymbol, rs.resultunit, rs.resultuncertainty, rs.resultlow, rs.resulthigh )
 END AS  result12_num_type_dtl_val_approx_unit_uncert_low_hi,
 CASE WHEN count(rs2.resultid)+1 = 13 THEN 
    dev_naknowbase.result_concat_fun( rs.resultid, rs.resulttype, rs.resultdetails, rs.resultvalue, 
    rs.resultapproxsymbol, rs.resultunit, rs.resultuncertainty, rs.resultlow, rs.resulthigh )
 END AS  result13_num_type_dtl_val_approx_unit_uncert_low_hi,
 CASE WHEN count(rs2.resultid)+1 = 14 THEN 
    dev_naknowbase.result_concat_fun( rs.resultid, rs.resulttype, rs.resultdetails, rs.resultvalue, 
    rs.resultapproxsymbol, rs.resultunit, rs.resultuncertainty, rs.resultlow, rs.resulthigh )
 END AS  result14_num_type_dtl_val_approx_unit_uncert_low_hi,
 CASE WHEN count(rs2.resultid)+1 = 15 THEN 
    dev_naknowbase.result_concat_fun( rs.resultid, rs.resulttype, rs.resultdetails, rs.resultvalue, 
    rs.resultapproxsymbol, rs.resultunit, rs.resultuncertainty, rs.resultlow, rs.resulthigh )
 END AS  result15_num_type_dtl_val_approx_unit_uncert_low_hi,
 CASE WHEN count(rs2.resultid)+1 = 16 THEN 
    dev_naknowbase.result_concat_fun( rs.resultid, rs.resulttype, rs.resultdetails, rs.resultvalue, 
    rs.resultapproxsymbol, rs.resultunit, rs.resultuncertainty, rs.resultlow, rs.resulthigh )
 END AS  result16_num_type_dtl_val_approx_unit_uncert_low_hi,
 CASE WHEN count(rs2.resultid)+1 = 17 THEN 
    dev_naknowbase.result_concat_fun( rs.resultid, rs.resulttype, rs.resultdetails, rs.resultvalue, 
    rs.resultapproxsymbol, rs.resultunit, rs.resultuncertainty, rs.resultlow, rs.resulthigh )
 END AS  result17_num_type_dtl_val_approx_unit_uncert_low_hi,
 CASE WHEN count(rs2.resultid)+1 = 18 THEN 
    dev_naknowbase.result_concat_fun( rs.resultid, rs.resulttype, rs.resultdetails, rs.resultvalue, 
    rs.resultapproxsymbol, rs.resultunit, rs.resultuncertainty, rs.resultlow, rs.resulthigh )
 END AS  result18_num_type_dtl_val_approx_unit_uncert_low_hi
FROM dev_naknowbase.result rs
LEFT OUTER JOIN dev_naknowbase.result rs2
  ON rs.resultid > rs2.resultid
 AND rs.assay_assayID = rs2.assay_assayID
 AND rs.assay_publication_DOI = rs2.assay_publication_DOI
-- this group by returns the same number of rows as without group by. It is needed for the rank count
GROUP BY rs.resultid, rs.assay_assayID, rs.assay_publication_DOI
ORDER BY rs.assay_assayID, rs.assay_publication_DOI, idrank, rs.resultid
;
