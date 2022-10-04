USE `dev_naknowbase`;
DROP function IF EXISTS `medium_additive_concat_fun`;

DELIMITER $$
USE `dev_naknowbase`$$
CREATE FUNCTION `dev_naknowbase`.`medium_additive_concat_fun` 
				(p_mediumid INTEGER, p_medium_publication_doi VARCHAR(45))
RETURNS VARCHAR(2000) 
COMMENT 'for a given medium key returns concatenated list of formatted additives, separated by space pipe space'
DETERMINISTIC READS SQL DATA
-- purpose: concatenate all additives into one text field for a medium. There are 0 to 6 additives per medium.
--          there are 91 distinct additives for the mediums, 92 with null
-- parameters:  mediumID, publication_DOI
-- returns: concatenated list of formatted additives, separated by space pipe space. retuns null if no matching row. 
-- to run:   SELECT `dev_naknowbase`.`medium_additive_concat_fun`(1, '10.1016/j.cej.2012.02.074');
-- example: 
	-- SELECT md.mediumID, md.publication_DOI, 
	-- 		dev_naknowbase.medium_additive_concat_fun( md.MediumID, md.publication_DOI ) AS additive_list
	-- FROM dev_naknowbase.medium md
	-- ORDER BY md.mediumID, md.publication_DOI;

BEGIN
	DECLARE r_additive_list VARCHAR(2000) DEFAULT NULL;  -- returned list of additives

	SELECT 
        	-- concatenate all additives into one text field for a group by on medium keys
          -- max lengths id=2 name=43 amt=6 unit=5
			  group_concat(concat('addit:', lpad(ad.idadditive,2,'0'), ' amt:', lpad(ad.AdditiveAmount,6,'0'), ' ', 
        rpad(ad.AdditiveUnit, 5, ' '), ' ', rpad(ad.AdditiveName, 45, ' ') ) separator ' | ') AS additive_list
	INTO r_additive_list
	FROM dev_naknowbase.additive ad
	WHERE ad.medium_MediumID = p_mediumid
    AND ad.medium_publication_DOI = p_medium_publication_doi
	GROUP BY ad.medium_publication_DOI = p_medium_publication_doi
	;

	RETURN r_additive_list;
END$$

DELIMITER ;
