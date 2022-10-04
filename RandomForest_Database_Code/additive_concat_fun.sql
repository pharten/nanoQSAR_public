USE `dev_naknowbase`;
DROP function IF EXISTS `additive_concat_fun`;

DELIMITER $$
USE `dev_naknowbase`$$
CREATE FUNCTION `dev_naknowbase`.`additive_concat_fun` 
				(p_idadditive INTEGER, p_additiveamount FLOAT, p_additiveunit VARCHAR(45), p_additivename VARCHAR(100) )
RETURNS VARCHAR(2000) 
COMMENT 'for a given additive key returns concatenated field of formatted additive fields, separated by fieldname:'
-- deterministic always returns the same values for the same inputs
DETERMINISTIC 
-- purpose: concatenate all additive fieldss into one text field for an additive. 
--          there are 91 distinct additives 
-- parameters:  idadditive, additiveamount, additiveunit, additivename
-- returns: concatenated field of formatted additive fields, separated by fieldname:. retuns null if input fields null. 
-- to run:   SELECT dev_naknowbase.additive_concat_fun(52, 1.2, 'ml', 'NaCl') AS addit_concat;
-- example: 
	-- SELECT ad.idadditive, 
	-- 		dev_naknowbase.additive_concat_fun(ad.idadditive, ad.additiveamount, ad.additiveunit, ad.additivename ) AS additive_concat
	-- FROM dev_naknowbase.additive ad
	-- ORDER BY ad.idadditive;

BEGIN
	DECLARE r_additive VARCHAR(2000) DEFAULT NULL;  -- returned concatenated field
  DECLARE v_additiveamount VARCHAR(45) DEFAULT NULL; -- optional amount
  DECLARE v_additiveunit VARCHAR(45) DEFAULT NULL; -- optional unit
  
  -- idadditive and additiveName are NOT NULL fields on additive table
  -- the database stores empty strings as zero length strings rather than null
  IF p_idadditive IS NOT NULL 
  AND length(trim(p_additivename) ) > 0 THEN 
    -- an additive must have an id and name. amount and unit are optional.
    -- input as zero length string works, but null returns null for the whole statement without these
    -- convert null value and zero length string to space filled string
    SET v_additiveamount = ifnull(p_additiveamount, '' ) ;
    SET v_additiveunit   = ifnull(p_additiveunit, '' ) ;
        -- concatenate all additive fields into one text field 
      -- max lengths id=2 name=43 amt=6 unit=5
      -- new lengths id=4 name=58 amt=7 unit=23

    SET r_additive = concat_ws(':', p_idadditive, p_additivename, v_additiveamount, v_additiveunit);
  ELSE 
    -- not an additive
    SET r_additive = NULL;
  END IF;

	RETURN r_additive;
END$$

DELIMITER ;
