CREATE OR REPLACE VIEW dev_naknowbase.assay_all_vw AS
-- detail view of assay joined to publication. uses additive rank technique with CASE
-- to separate rows into columns. The additive fields are concatenated into one field. 
-- the additive joins and case statement transform up to 16 rows into 16 columns field.
-- 22325 rows in assay. pub is required. GROUP BY 1 row per assay  22325 rows
SELECT ay.assayID, ay.publication_DOI, 
      ay.medium_MediumID, ay.medium_publication_DOI,
      ay.material_MaterialID, ay.material_publication_DOI,
      ay.assayType, ay.AssayName, 
      mav.mediumDescription,
      -- medium_additive_vw concatenated fields 0 to 16
      max(mav.additive01_num_name_amt_unit) AS additive01_num_name_amt_unit,
      max(mav.additive02_num_name_amt_unit) AS additive02_num_name_amt_unit,
      max(mav.additive03_num_name_amt_unit) AS additive03_num_name_amt_unit,
      max(mav.additive04_num_name_amt_unit) AS additive04_num_name_amt_unit,
      max(mav.additive05_num_name_amt_unit) AS additive05_num_name_amt_unit,
      max(mav.additive06_num_name_amt_unit) AS additive06_num_name_amt_unit,
      max(mav.additive07_num_name_amt_unit) AS additive07_num_name_amt_unit,
      max(mav.additive08_num_name_amt_unit) AS additive08_num_name_amt_unit,
      max(mav.additive09_num_name_amt_unit) AS additive09_num_name_amt_unit,
      max(mav.additive10_num_name_amt_unit) AS additive10_num_name_amt_unit,
      max(mav.additive11_num_name_amt_unit) AS additive11_num_name_amt_unit,
      max(mav.additive12_num_name_amt_unit) AS additive12_num_name_amt_unit,
      max(mav.additive13_num_name_amt_unit) AS additive13_num_name_amt_unit,
      max(mav.additive14_num_name_amt_unit) AS additive14_num_name_amt_unit,
      max(mav.additive15_num_name_amt_unit) AS additive15_num_name_amt_unit,
      max(mav.additive16_num_name_amt_unit) AS additive16_num_name_amt_unit,
      -- material 
      mcv.CoreComposition, mcv.ShellComposition, mcv.CoatingComposition, 
      mcv.SynthesisMethod, mcv.SynthesisDate, mcv.CASRN, mcv.Supplier, mcv.ProductNumber, mcv.LotNumber, 
      mcv.OuterDiameterValue, mcv.OuterDiameterApproxSymbol, mcv.OuterDiameterUnit, mcv.OuterDiameterUncertainty, mcv.OuterDiameterLow, mcv.OuterDiameterHigh, mcv.OuterDiameterMethod, 
      mcv.InnerDiameterValue, mcv.InnerDiameterApproxSymbol, mcv.InnerDiameterUnit, mcv.InnerDiameterUncertainty, mcv.InnerDiameterLow, mcv.InnerDiameterHigh, mcv.InnerDiameterMethod, 
      mcv.LengthValue, mcv.LengthApproxSymbol, mcv.LengthUnit, mcv.LengthUncertainty, mcv.LengthLow, mcv.LengthHigh, mcv.LengthMethod, 
      mcv.ThicknessValue, mcv.ThicknessApproxSymbol, mcv.ThicknessUnit, mcv.ThicknessUncertainty, mcv.ThicknessLow, mcv.ThicknessHigh, mcv.ThicknessMethod, 
      mcv.SurfaceAreaValue, mcv.SurfaceAreaApproxSymbo, mcv.SurfaceAreaUnit, mcv.SurfaceAreaUncertainty, mcv.SurfaceAreaLow, mcv.SurfaceAreaHigh, mcv.SurfaceAreaMethod,Shape, 
      mcv.SDType, mcv.SDModality, mcv.SDMethod, mcv.SDAvg, mcv.SDApproxSymbol, mcv.SDUnit, mcv.SDUncertainty, mcv.SDLow, mcv.SDHigh, mcv.SDAvg2, mcv.SDApproxSymbol2, mcv.SDUnit2, mcv.SDUncertainty2, mcv.SDLow2, mcv.SDHigh2, 
      mcv.Purity, mcv.PurityApproxSymbol, mcv.PurityUnit, mcv.PurityRefChemical, mcv.PurityMethod, 
      mcv.medium_MediumID AS material_medium_MediumID, mcv.medium_publication_DOI AS material_medium_publication_DOI, 
      mcv.HydrodynamicDiameterValue, mcv.HydrodynamicDiameterApproxSymbol, mcv.HydrodynamicDiameterUnit, mcv.HydrodynamicDiameterUncertainty, mcv.HydrodynamicDiameterLow, mcv.HydrodynamicDiameterHigh, mcv.HydrodynamicDiameterMethod, 
      mcv.ShapeInMedium, mcv.Solubility, 
      mcv.SurfaceChargeType, mcv.ChargeAvg, mcv.ChargeApproxSymbol, mcv.ChargeUnit, mcv.ChargeUncertain, mcv.ChargeLow, mcv.ChargeHigh, mcv.ChargeMethod,
      mcv.HydrodynamicDiameterValue2, mcv.HydrodynamicDiameterApproxSymbol2, mcv.HydrodynamicDiameterUnit2, mcv.HydrodynamicDiameterUncertainty2, mcv.HydrodynamicDiameterLow2, mcv.HydrodynamicDiameterHigh2, 
      -- materialfg
      mcv.MaterialFGID, mcv.functionalgroup_functionalgroup, mcv.FunctionalizationProtocol, 
      -- material_contam_vw concatenated fields 0 to 20
      max(mcv.contam01_num_name_amt_unit_meth) AS contam01_num_name_amt_unit_meth,
      max(mcv.contam02_num_name_amt_unit_meth) AS contam02_num_name_amt_unit_meth,
      max(mcv.contam03_num_name_amt_unit_meth) AS contam03_num_name_amt_unit_meth,
      max(mcv.contam04_num_name_amt_unit_meth) AS contam04_num_name_amt_unit_meth,
      max(mcv.contam05_num_name_amt_unit_meth) AS contam05_num_name_amt_unit_meth,
      max(mcv.contam06_num_name_amt_unit_meth) AS contam06_num_name_amt_unit_meth,
      max(mcv.contam07_num_name_amt_unit_meth) AS contam07_num_name_amt_unit_meth,
      max(mcv.contam08_num_name_amt_unit_meth) AS contam08_num_name_amt_unit_meth,
      max(mcv.contam09_num_name_amt_unit_meth) AS contam09_num_name_amt_unit_meth,
      max(mcv.contam10_num_name_amt_unit_meth) AS contam10_num_name_amt_unit_meth,
      max(mcv.contam11_num_name_amt_unit_meth) AS contam11_num_name_amt_unit_meth,
      max(mcv.contam12_num_name_amt_unit_meth) AS contam12_num_name_amt_unit_meth,
      max(mcv.contam13_num_name_amt_unit_meth) AS contam13_num_name_amt_unit_meth,
      max(mcv.contam14_num_name_amt_unit_meth) AS contam14_num_name_amt_unit_meth,
      max(mcv.contam15_num_name_amt_unit_meth) AS contam15_num_name_amt_unit_meth,
      max(mcv.contam16_num_name_amt_unit_meth) AS contam16_num_name_amt_unit_meth,
      max(mcv.contam17_num_name_amt_unit_meth) AS contam17_num_name_amt_unit_meth,
      max(mcv.contam18_num_name_amt_unit_meth) AS contam18_num_name_amt_unit_meth,
      max(mcv.contam19_num_name_amt_unit_meth) AS contam19_num_name_amt_unit_meth,
      max(mcv.contam20_num_name_amt_unit_meth) AS contam20_num_name_amt_unit_meth,
      
      -- result_vw concatenated fields 0 to 18
      max(rv.result01_num_type_dtl_val_approx_unit_uncert_low_hi) AS result01_num_type_dtl_val_approx_unit_uncert_low_hi,
      max(rv.result02_num_type_dtl_val_approx_unit_uncert_low_hi) AS result02_num_type_dtl_val_approx_unit_uncert_low_hi,
      max(rv.result03_num_type_dtl_val_approx_unit_uncert_low_hi) AS result03_num_type_dtl_val_approx_unit_uncert_low_hi,
      max(rv.result04_num_type_dtl_val_approx_unit_uncert_low_hi) AS result04_num_type_dtl_val_approx_unit_uncert_low_hi,
      max(rv.result05_num_type_dtl_val_approx_unit_uncert_low_hi) AS result05_num_type_dtl_val_approx_unit_uncert_low_hi,
      max(rv.result06_num_type_dtl_val_approx_unit_uncert_low_hi) AS result06_num_type_dtl_val_approx_unit_uncert_low_hi,
      max(rv.result07_num_type_dtl_val_approx_unit_uncert_low_hi) AS result07_num_type_dtl_val_approx_unit_uncert_low_hi,
      max(rv.result08_num_type_dtl_val_approx_unit_uncert_low_hi) AS result08_num_type_dtl_val_approx_unit_uncert_low_hi,
      max(rv.result09_num_type_dtl_val_approx_unit_uncert_low_hi) AS result09_num_type_dtl_val_approx_unit_uncert_low_hi,
      max(rv.result10_num_type_dtl_val_approx_unit_uncert_low_hi) AS result10_num_type_dtl_val_approx_unit_uncert_low_hi,
      max(rv.result11_num_type_dtl_val_approx_unit_uncert_low_hi) AS result11_num_type_dtl_val_approx_unit_uncert_low_hi,
      max(rv.result12_num_type_dtl_val_approx_unit_uncert_low_hi) AS result12_num_type_dtl_val_approx_unit_uncert_low_hi,
      max(rv.result13_num_type_dtl_val_approx_unit_uncert_low_hi) AS result13_num_type_dtl_val_approx_unit_uncert_low_hi,
      max(rv.result14_num_type_dtl_val_approx_unit_uncert_low_hi) AS result14_num_type_dtl_val_approx_unit_uncert_low_hi,
      max(rv.result15_num_type_dtl_val_approx_unit_uncert_low_hi) AS result15_num_type_dtl_val_approx_unit_uncert_low_hi,
      max(rv.result16_num_type_dtl_val_approx_unit_uncert_low_hi) AS result16_num_type_dtl_val_approx_unit_uncert_low_hi,
      max(rv.result17_num_type_dtl_val_approx_unit_uncert_low_hi) AS result17_num_type_dtl_val_approx_unit_uncert_low_hi,
      max(rv.result18_num_type_dtl_val_approx_unit_uncert_low_hi) AS result18_num_type_dtl_val_approx_unit_uncert_low_hi,
      
      -- parameters_vw concatenated fields 0 to 19
      max(pv.parameters01_num_name_numval_unit_nonnum) AS parameters01_num_name_numval_unit_nonnum,
      max(pv.parameters02_num_name_numval_unit_nonnum) AS parameters02_num_name_numval_unit_nonnum,
      max(pv.parameters03_num_name_numval_unit_nonnum) AS parameters03_num_name_numval_unit_nonnum,
      max(pv.parameters04_num_name_numval_unit_nonnum) AS parameters04_num_name_numval_unit_nonnum,
      max(pv.parameters05_num_name_numval_unit_nonnum) AS parameters05_num_name_numval_unit_nonnum,
      max(pv.parameters06_num_name_numval_unit_nonnum) AS parameters06_num_name_numval_unit_nonnum,
      max(pv.parameters07_num_name_numval_unit_nonnum) AS parameters07_num_name_numval_unit_nonnum,
      max(pv.parameters08_num_name_numval_unit_nonnum) AS parameters08_num_name_numval_unit_nonnum,
      max(pv.parameters09_num_name_numval_unit_nonnum) AS parameters09_num_name_numval_unit_nonnum,
      max(pv.parameters10_num_name_numval_unit_nonnum) AS parameters10_num_name_numval_unit_nonnum,
      max(pv.parameters11_num_name_numval_unit_nonnum) AS parameters11_num_name_numval_unit_nonnum,
      max(pv.parameters12_num_name_numval_unit_nonnum) AS parameters12_num_name_numval_unit_nonnum,
      max(pv.parameters13_num_name_numval_unit_nonnum) AS parameters13_num_name_numval_unit_nonnum,
      max(pv.parameters14_num_name_numval_unit_nonnum) AS parameters14_num_name_numval_unit_nonnum,
      max(pv.parameters15_num_name_numval_unit_nonnum) AS parameters15_num_name_numval_unit_nonnum,
      max(pv.parameters16_num_name_numval_unit_nonnum) AS parameters16_num_name_numval_unit_nonnum,
      max(pv.parameters17_num_name_numval_unit_nonnum) AS parameters17_num_name_numval_unit_nonnum,
      max(pv.parameters18_num_name_numval_unit_nonnum) AS parameters18_num_name_numval_unit_nonnum,
      max(pv.parameters19_num_name_numval_unit_nonnum) AS parameters19_num_name_numval_unit_nonnum,
      
      -- molecularresult 0 to 1
      mr.GEO_accession, mr.OrganismName, mr.SpeciesID, mr.AssayType molecularAssayType, mr.Platform, 
      mr.Series, mr.SampleCount, mr.url,
      
      -- the assay publication matches the medium and material publication except when
      -- medium or material are No Publication
      replace(pub.PubTitle, char(10), ' ') PubTitle, pub.Journal, pub.year, pub.`First Author` AS FirstAuthor, 
      pub.Volume, pub.Issue, pub.PageStart, pub.PageEnd, replace(pub.Keywords, char(10), ' ') Keywords, 
      pub.Correspondence, pub.Affiliation, replace(pub.Abstract, char(10), ' ') Abstract

      
FROM dev_naknowbase.assay ay
JOIN dev_naknowbase.publication pub
  ON ay.publication_DOI = pub.DOI
JOIN dev_naknowbase.medium_additive_vw mav
  ON ay.medium_MediumID = mav.MediumID
 AND ay.medium_publication_DOI = mav.publication_DOI
JOIN dev_naknowbase.material_contam_vw mcv
  ON ay.material_MaterialID = mcv.materialID
 AND ay.material_publication_DOI = mcv.publication_DOI
-- result can have 0 to 18 rows per assay, ranked and concatenated
LEFT OUTER JOIN dev_naknowbase.result_vw rv
  ON ay.AssayID = rv.assay_AssayID
 AND ay.publication_DOI = rv.assay_publication_DOI
-- parameters can have 0 to 19 rows per assay, ranked and concatenated
LEFT OUTER JOIN dev_naknowbase.parameters_vw pv
  ON ay.AssayID = pv.assay_AssayID
 AND ay.publication_DOI = pv.assay_publication_DOI
-- molecularresult can have 0 to 1 child rows
LEFT OUTER JOIN dev_naknowbase.molecularresult mr
  ON ay.AssayID = mr.assay_AssayID
 AND ay.publication_DOI = mr.assay_publication_DOI
GROUP BY ay.assayID, ay.publication_DOI, pub.DOI,
      mav.mediumID, mcv.materialID, mr.MolecularResultID, mcv.MaterialFGID
      
ORDER BY ay.assayid, ay.publication_DOI
;