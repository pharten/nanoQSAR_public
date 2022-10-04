CREATE OR REPLACE VIEW dev_naknowbase.material_vw AS
-- detail view of material joined to publication, materialfg. uses fixed pivot technique for contam
-- not null columns are publication_DOI, core_composition, mediumID, medium_DOI, 
-- 136 rows in material. pub is required. GROUP BY 1 row per material. 4 rows in materialfg. 7 rows in contam.
-- materialID 1 through 4 have materialfg. so one to one. Other materials null materialfg
-- materialID 1 has 7 contam rows. No other materials have matching contam. Only contaminant column has data
-- other columns are null
SELECT mt.materialID, mt.publication_DOI, mt.CoreComposition, mt.medium_MediumID, mt.medium_publication_DOI,
      mfg.MaterialFGID, mfg.functionalgroup_functionalgroup, mfg.FunctionalizationProtocol,
      max(CASE WHEN ContamID = 1 THEN ct.Contaminant END) AS contam1,
      max(CASE WHEN ContamID = 2 THEN ct.Contaminant END) AS contam2,
      max(CASE WHEN ContamID = 3 THEN ct.Contaminant END) AS contam3,
      max(CASE WHEN ContamID = 4 THEN ct.Contaminant END) AS contam4,
      max(CASE WHEN ContamID = 5 THEN ct.Contaminant END) AS contam5,
      max(CASE WHEN ContamID = 6 THEN ct.Contaminant END) AS contam6,
      max(CASE WHEN ContamID = 7 THEN ct.Contaminant END) AS contam7,
      replace(pub.PubTitle, char(10), ' ') PubTitle, pub.Journal, pub.year, pub.`First Author` AS FirstAuthor, 
      pub.Volume, pub.Issue, pub.PageStart, pub.PageEnd, replace(pub.Keywords, char(10), ' ') Keywords, 
      pub.Correspondence, pub.Affiliation, replace(pub.Abstract, char(10), ' ') Abstract
FROM dev_naknowbase.material mt
JOIN dev_naknowbase.publication pub
  ON mt.publication_DOI = pub.DOI
-- must be outer join because most materials do not have materialfg
LEFT OUTER JOIN dev_naknowbase.materialfg mfg
  ON mt.MaterialID = mfg.material_MaterialID
 AND mt.publication_DOI = mfg.material_publication_DOI
LEFT OUTER JOIN dev_naknowbase.contam ct
  ON mt.MaterialID = ct.material_MaterialID
 AND mt.publication_DOI = ct.material_publication_DOI
GROUP BY mt.materialID, mt.publication_DOI, mt.CoreComposition, mt.medium_MediumID, mt.medium_publication_DOI,
      mfg.MaterialFGID, mfg.functionalgroup_functionalgroup, mfg.FunctionalizationProtocol,
      pub.PubTitle, pub.Journal, pub.year, FirstAuthor, 
      pub.Volume, pub.Issue, pub.PageStart, pub.PageEnd, pub.Keywords, pub.Correspondence,
      pub.Affiliation, pub.Abstract
ORDER BY mt.materialid, mt.publication_DOI
;