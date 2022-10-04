USE `dev_naknowbase`;
DROP function IF EXISTS `result_concat_fun`;

DELIMITER $$
USE `dev_naknowbase`$$
CREATE FUNCTION `dev_naknowbase`.`result_concat_fun` 
				(
        p_resultid INTEGER, p_resulttype VARCHAR(100), p_resultdetails VARCHAR(100), 
        p_resultvalue FLOAT, p_resultapproxsymbol VARCHAR(45), p_resultunit VARCHAR(45),
        p_resultuncertainty VARCHAR(45), p_resultlow FLOAT, p_resulthigh FLOAT
        )
RETURNS VARCHAR(2000) 
COMMENT 'for a given result key returns concatenated field of formatted result fields, separated by :'
-- deterministic always returns the same values for the same inputs
DETERMINISTIC 
-- purpose: concatenate all result fieldss into one text field for an result. 
--          there are 24693 results over 22264 assays max of 18 results per assay
-- parameters:  resultid, resulttype, resultdetails, 
--        resultvalue, resultapproxsymbol, resultunit,
--        result_uncertainty, resultlow, resulthigh 
-- returns: concatenated field of formatted result fields, separated by fieldname:. retuns null if input fields null. 
-- to run:   
-- SELECT dev_naknowbase.result_concat_fun(166095, 'quadrature conductivity', '', '1.682', '', 
--  '10^-6*seimens/meter', '',  NULL, NULL) AS result_concat;
-- example: 
	-- SELECT rs.resultid, 
	-- 		dev_naknowbase.result_concat_fun( rs.resultid, rs.resulttype, rs.resultdetails, rs.resultvalue, 
  -- rs.resultapproxsymbol, rs.resultunit, rs.result_uncertainty, rs.resultlow, rs.resulthigh ) AS result_concat
	-- FROM dev_naknowbase.result rs
	-- ORDER BY rs.resultid;

BEGIN
	DECLARE r_result VARCHAR(2000) DEFAULT NULL;  -- returned concatenated field
  DECLARE v_resulttype VARCHAR(100) DEFAULT NULL; -- optional type
  DECLARE v_resultdetails VARCHAR(100) DEFAULT NULL; -- optional details
  DECLARE v_resultvalue VARCHAR(45) DEFAULT NULL; -- optional value
  DECLARE v_resultapproxsymbol VARCHAR(45) DEFAULT NULL; -- optional approximate symbol
  DECLARE v_resultunit VARCHAR(45) DEFAULT NULL; -- optional unit
  DECLARE v_resultuncertainty VARCHAR(45) DEFAULT NULL; -- optional uncertainty
  DECLARE v_resultlow VARCHAR(45) DEFAULT NULL; -- optional low value
  DECLARE v_resulthigh VARCHAR(45) DEFAULT NULL; -- optional high value
  
  -- resultid are NOT NULL fields on result table
  -- the database stores empty strings as zero length strings rather than null
  IF p_resultid IS NOT NULL THEN 
    -- an result must have an id. other fields are optional.
    -- input as zero length string works, but null returns null for the whole statement without these
    -- convert null value and zero length string to space filled string
    SET v_resulttype = ifnull(p_resulttype, '' ) ;
    SET v_resultdetails = ifnull(p_resultdetails, '' ) ;
    SET v_resultvalue = ifnull(p_resultvalue, '' ) ;
    SET v_resultapproxsymbol = ifnull(p_resultapproxsymbol, '' ) ;
    SET v_resultunit   = ifnull(p_resultunit, '' ) ;
    SET v_resultuncertainty = ifnull(p_resultuncertainty, '' ) ;
    SET v_resultlow = ifnull(p_resultlow, '' ) ;
    SET v_resulthigh = ifnull(p_resulthigh, '' ) ;

        -- concatenate all result fields into one text field 
    SET r_result = concat_ws( ':', p_resultid, v_resulttype, v_resultdetails, 
        v_resultvalue, v_resultapproxsymbol, v_resultunit, v_resultuncertainty, v_resultlow, v_resulthigh );
  ELSE 
    -- not an result
    SET r_result = NULL;
  END IF;

	RETURN r_result;
END$$

DELIMITER ;
