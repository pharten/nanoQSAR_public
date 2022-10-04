USE `dev_naknowbase`;
DROP function IF EXISTS `contam_concat_fun`;

DELIMITER $$
USE `dev_naknowbase`$$
CREATE FUNCTION `dev_naknowbase`.`contam_concat_fun` 
				(p_contamid INTEGER, p_contaminant VARCHAR(45), p_contamamount VARCHAR(45), p_contamunit VARCHAR(45), p_contammethod VARCHAR(150) )
RETURNS VARCHAR(2000) 
COMMENT 'for a given contam key returns concatenated field of formatted contam fields, separated by fieldname:'
-- deterministic always returns the same values for the same inputs
DETERMINISTIC 
-- purpose: concatenate all contam fields into one text field for an contam. 
--          there are 47 distinct contams 
-- parameters:  p_contamid, p_contaminant, p_contamamount, p_contamunit, p_contammethod
-- returns: concatenated field of formatted contam fields, separated by fieldname:. retuns null if input fields null. 
-- to run:   SELECT dev_naknowbase.contam_concat_fun(128, 'Calcium', '2782.258', 'milligrams/kilogram', 'Inductively coupled plasma atomic emission spectroscopy') AS addit_concat;
-- example: 
	-- SELECT ct.contamid, 
	-- 		dev_naknowbase.contam_concat_fun( ct.contamid, ct.contaminant, ct.contamamount, ct.contamunit, ct.contammethod ) AS contam_concat
	-- FROM dev_naknowbase.contam ct
	-- ORDER BY ct.contamid;

BEGIN
	DECLARE r_contam VARCHAR(2000) DEFAULT NULL;  -- returned concatenated field
  DECLARE v_contamamount VARCHAR(45) DEFAULT NULL; -- optional amount
  DECLARE v_contamunit VARCHAR(45) DEFAULT NULL; -- optional unit
  DECLARE v_contammethod VARCHAR(150) DEFAULT NULL; -- optional method
  
  -- contamid and contaminant are NOT NULL fields on contam table
  -- the database stores empty strings as zero length strings rather than null
  IF p_contamid IS NOT NULL 
  AND length(trim(p_contaminant) ) > 0 THEN 
    -- an contam must have an id and name. amount, unit, method are optional.
    -- input as zero length string works, but null returns null for the whole statement without these
    -- convert null value and zero length string to space filled string
    SET v_contamamount = ifnull(p_contamamount, '' ) ;
    SET v_contamunit   = ifnull(p_contamunit, '' ) ;
    SET v_contammethod   = ifnull(p_contammethod, '' ) ;
        -- concatenate all contam fields into one text field 
      -- new lengths id=4 name=58 amt=7 unit=23

    SET r_contam = concat_ws(':', p_contamid, p_contaminant, v_contamamount, v_contamunit, v_contammethod);
  ELSE 
    -- not an contam
    SET r_contam = NULL;
  END IF;

	RETURN r_contam;
END$$

DELIMITER ;
