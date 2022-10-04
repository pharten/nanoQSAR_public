CREATE OR REPLACE VIEW dev_naknowbase.assay_parameter_vw AS
-- detail view of assay joined to parameters, medium, material
-- joins to publication for assay_publication, medium_publication, material_publication
-- must join on assayID and publicationDOI
-- 13458 rows. same as parameters. There are 227 assays without parameters
SELECT ay.AssayID, ay.publication_DOI, ay.medium_MediumID, ay.medium_publication_DOI,
		ay.material_MaterialID, ay.material_publication_DOI,
		ay.AssayType, ay.AssayName,
		pm.idparameters, pm.parameterName, pm.ParameterNumberValue, pm.ParameterUnit, pm.ParameterNonNumberValue
FROM dev_naknowbase.assay ay
-- parameters.assay_assayID IS NOT NULL so the row count will match parameters on JOIN.
-- but LEFT OUTER JOIN will have 227 rows more with empty parameters fields.
JOIN dev_naknowbase.parameters pm
  ON ay.AssayID = pm.assay_AssayID
 AND ay.publication_DOI = pm.assay_publication_DOI
-- 227 assays without parameters
-- WHERE pm.assay_AssayID IS NULL
;