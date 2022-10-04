USE `dev_naknowbase`;
DROP function IF EXISTS `parameters_concat_fun`;

DELIMITER $$
USE `dev_naknowbase`$$
CREATE FUNCTION `dev_naknowbase`.`parameters_concat_fun` 
				(
        p_idparameters INTEGER, p_parametername VARCHAR(100), 
        p_parameternumbervalue FLOAT, p_parameterunit VARCHAR(100),
        p_parameternonnumbervalue VARCHAR(100)
        )
RETURNS VARCHAR(2000) 
COMMENT 'for a given parameters key returns concatenated field of formatted parameters fields, separated by :'
-- deterministic always returns the same values for the same inputs
DETERMINISTIC 
-- purpose: concatenate all parameters fieldss into one text field for an parametepm. 
--          there are 83233 parameterss over 22264 assays max of nn parameters per assay
-- parameters:  idparameters, parametername, 
--        parameternumbervalue, parameterunit,
--        parameternonnumbervalue
-- returns: concatenated field of formatted parameters fields, separated by fieldname:. retuns null if input fields null. 
-- to run:   
-- SELECT dev_naknowbase.parameters_concat_fun( 1179632, 'medium saturation', 15, 'percent', '' ) AS parameters_concat;
-- example: 
	-- SELECT pm.idparameters, 
	-- 		dev_naknowbase.parameters_concat_fun( pm.idparameters, pm.parametername, pm.parameternumbervalue, 
  -- pm.parameterunit, pm.parametersuncertainty ) AS parameters_concat
	-- FROM dev_naknowbase.parameters pm
	-- ORDER BY pm.idparameters;

BEGIN
	DECLARE r_parameters VARCHAR(2000) DEFAULT NULL;  -- returned concatenated field
  DECLARE v_parametername VARCHAR(100) DEFAULT NULL; -- optional name
  DECLARE v_parameternumbervalue VARCHAR(45) DEFAULT NULL; -- optional value
  DECLARE v_parameterunit VARCHAR(100) DEFAULT NULL; -- optional unit
  DECLARE v_parameternonnumbervalue VARCHAR(100) DEFAULT NULL; -- optional nonnumber
  
  -- idparameters are NOT NULL fields on parameters table
  -- the database stores empty strings as zero length strings rather than null
  IF p_idparameters IS NOT NULL THEN 
    -- an parameters must have an id. other fields are optional.
    -- input as zero length string works, but null returns null for the whole statement without these
    -- convert null value and zero length string to space filled string
    SET v_parametername = ifnull(p_parametername, '' ) ;
    SET v_parameternumbervalue = ifnull(p_parameternumbervalue, '' ) ;
    SET v_parameterunit   = ifnull(p_parameterunit, '' ) ;
    SET v_parameternonnumbervalue = ifnull(p_parameternonnumbervalue, '' ) ;

        -- concatenate all parameters fields into one text field 
    SET r_parameters = concat_ws( ':', p_idparameters, v_parametername,  
        v_parameternumbervalue,  v_parameterunit, v_parameternonnumbervalue );
  ELSE 
    -- not an parameters
    SET r_parameters = NULL;
  END IF;

	RETURN r_parameters;
END$$

DELIMITER ;
