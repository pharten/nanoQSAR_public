CREATE OR REPLACE VIEW dev_naknowbase.material_contam_vw AS
-- detail view of material joined to contam_vw. uses contam rank technique with CASE
-- to separate rows into columns. The contam fields are concatenated into one field. 
-- the contam joins and case statement transform up to 20 rows into 20 columns field.
-- 374 rows in material. pub is required. GROUP BY 1 row per material  374 rows
SELECT mt.materialID, mt.publication_DOI, mt.CoreComposition,
      mt.ShellComposition, mt.CoatingComposition, mt.SynthesisMethod, mt.SynthesisDate, mt.CASRN, 
      mt.Supplier, mt.ProductNumber, mt.LotNumber, mt.OuterDiameterValue, mt.OuterDiameterApproxSymbol, 
      mt.OuterDiameterUnit, mt.OuterDiameterUncertainty, mt.OuterDiameterLow, mt.OuterDiameterHigh, 
      mt.OuterDiameterMethod, mt.InnerDiameterValue, mt.InnerDiameterApproxSymbol, mt.InnerDiameterUnit, 
      mt.InnerDiameterUncertainty, mt.InnerDiameterLow, mt.InnerDiameterHigh, mt.InnerDiameterMethod, 
      mt.LengthValue, mt.LengthApproxSymbol, mt.LengthUnit, mt.LengthUncertainty, mt.LengthLow, mt.LengthHigh, 
      mt.LengthMethod, mt.ThicknessValue, mt.ThicknessApproxSymbol, mt.ThicknessUnit, mt.ThicknessUncertainty, 
      mt.ThicknessLow, mt.ThicknessHigh, mt.ThicknessMethod, mt.SurfaceAreaValue, mt.SurfaceAreaApproxSymbo, 
      mt.SurfaceAreaUnit, mt.SurfaceAreaUncertainty, mt.SurfaceAreaLow, mt.SurfaceAreaHigh, mt.SurfaceAreaMethod, 
      mt.Shape, mt.SDType, mt.SDModality, mt.SDMethod, mt.SDAvg, mt.SDApproxSymbol, mt.SDUnit, mt.SDUncertainty, 
      mt.SDLow, mt.SDHigh, mt.SDAvg2, mt.SDApproxSymbol2, mt.SDUnit2, mt.SDUncertainty2, mt.SDLow2, mt.SDHigh2, 
      mt.Purity, mt.PurityApproxSymbol, mt.PurityUnit, mt.PurityRefChemical, mt.PurityMethod, mt.medium_MediumID, 
      mt.medium_publication_DOI, mt.HydrodynamicDiameterValue, mt.HydrodynamicDiameterApproxSymbol, 
      mt.HydrodynamicDiameterUnit, mt.HydrodynamicDiameterUncertainty, mt.HydrodynamicDiameterLow, 
      mt.HydrodynamicDiameterHigh, mt.HydrodynamicDiameterMethod, mt.ShapeInMedium, mt.Solubility, 
      mt.SurfaceChargeType, mt.ChargeAvg, mt.ChargeApproxSymbol, mt.ChargeUnit, mt.ChargeUncertain, 
      mt.ChargeLow, mt.ChargeHigh, mt.ChargeMethod, mt.HydrodynamicDiameterValue2, 
      mt.HydrodynamicDiameterApproxSymbol2, mt.HydrodynamicDiameterUnit2, mt.HydrodynamicDiameterUncertainty2, 
      mt.HydrodynamicDiameterLow2, mt.HydrodynamicDiameterHigh2,
      -- material functional group
      mfg.MaterialFGID, mfg.functionalgroup_functionalgroup, mfg.FunctionalizationProtocol,
      -- rank columns over contam
       max(ctv.contam01_num_name_amt_unit_meth) AS contam01_num_name_amt_unit_meth,
       max(ctv.contam02_num_name_amt_unit_meth) AS contam02_num_name_amt_unit_meth,
       max(ctv.contam03_num_name_amt_unit_meth) AS contam03_num_name_amt_unit_meth,
       max(ctv.contam04_num_name_amt_unit_meth) AS contam04_num_name_amt_unit_meth,
       max(ctv.contam05_num_name_amt_unit_meth) AS contam05_num_name_amt_unit_meth,
       max(ctv.contam06_num_name_amt_unit_meth) AS contam06_num_name_amt_unit_meth,
       max(ctv.contam07_num_name_amt_unit_meth) AS contam07_num_name_amt_unit_meth,
       max(ctv.contam08_num_name_amt_unit_meth) AS contam08_num_name_amt_unit_meth,
       max(ctv.contam09_num_name_amt_unit_meth) AS contam09_num_name_amt_unit_meth,
       max(ctv.contam10_num_name_amt_unit_meth) AS contam10_num_name_amt_unit_meth,
       max(ctv.contam11_num_name_amt_unit_meth) AS contam11_num_name_amt_unit_meth,
       max(ctv.contam12_num_name_amt_unit_meth) AS contam12_num_name_amt_unit_meth,
       max(ctv.contam13_num_name_amt_unit_meth) AS contam13_num_name_amt_unit_meth,
       max(ctv.contam14_num_name_amt_unit_meth) AS contam14_num_name_amt_unit_meth,
       max(ctv.contam15_num_name_amt_unit_meth) AS contam15_num_name_amt_unit_meth,
       max(ctv.contam16_num_name_amt_unit_meth) AS contam16_num_name_amt_unit_meth,
       max(ctv.contam17_num_name_amt_unit_meth) AS contam17_num_name_amt_unit_meth,
       max(ctv.contam18_num_name_amt_unit_meth) AS contam18_num_name_amt_unit_meth,
       max(ctv.contam19_num_name_amt_unit_meth) AS contam19_num_name_amt_unit_meth,
       max(ctv.contam20_num_name_amt_unit_meth) AS contam20_num_name_amt_unit_meth
FROM dev_naknowbase.material mt
LEFT OUTER JOIN dev_naknowbase.contam_vw ctv
  ON mt.materialID = ctv.material_materialID
 AND mt.publication_DOI = ctv.material_publication_DOI
LEFT OUTER JOIN dev_naknowbase.materialfg mfg
  ON mt.materialID = mfg.material_materialID
 AND mt.publication_DOI = mfg.material_publication_DOI
-- this groups 1 row per material but is needed for max on rank columns
GROUP BY mt.materialID, mt.publication_DOI, mt.CoreComposition,
      mfg.MaterialFGID
ORDER BY mt.materialid, mt.publication_DOI
;