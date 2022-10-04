CREATE OR REPLACE VIEW dev_naknowbase.medium_vw AS
-- detail view of medium joined to publication. uses additive concat function
-- the medium_additive_concat_fun concatenates 0 to 6 additives into 1 field.
-- 86 rows in medium. pub is required. GROUP BY 1 row per medium
-- remove embedded line returns from publication fields
SELECT md.MediumID, md.publication_DOI, md.MediumDescription,
      dev_naknowbase.medium_additive_concat_fun( md.MediumID, md.publication_DOI ) AS additive_list,
      replace(pub.PubTitle, char(10), ' ') PubTitle, pub.Journal, pub.year, pub.`First Author` AS FirstAuthor, 
      pub.Volume, pub.Issue, pub.PageStart, pub.PageEnd, replace(pub.Keywords, char(10), ' ') Keywords, 
      pub.Correspondence, pub.Affiliation, replace(pub.Abstract, char(10), ' ') Abstract
FROM dev_naknowbase.medium md
JOIN dev_naknowbase.publication pub
  ON md.publication_DOI = pub.DOI
GROUP BY md.MediumID, md.publication_DOI, md.MediumDescription,
      additive_list,
      pub.PubTitle, pub.Journal, pub.year, FirstAuthor
ORDER BY md.mediumid, md.publication_DOI
;