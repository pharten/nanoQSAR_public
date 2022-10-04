CREATE OR REPLACE VIEW dev_naknowbase.parameter_group_vw AS
-- summary view of parameters and units
SELECT parameterName, ParameterUnit
FROM dev_naknowbase.parameters
GROUP BY parameterName, ParameterUnit
;