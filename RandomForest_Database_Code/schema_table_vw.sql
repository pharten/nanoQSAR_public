desc information_schema.tables;
-- a view over information_schema.tables
CREATE OR REPLACE VIEW `dev_naknowbase`.`schema_table_vw`
AS
SELECT ta.table_type, ta.table_name, ta.table_rows, nullif(ta.table_comment, '') tab_comment
FROM information_schema.tables ta
WHERE ta.table_schema = 'dev_naknowbase'
ORDER BY ta.table_type, ta.table_name
;

desc information_schema.columns;
-- a view over information_schema.columns and tables
CREATE OR REPLACE VIEW `dev_naknowbase`.`schema_table_column_vw`
AS
-- columns by table, view with comments. 
SELECT ta.table_type, co.table_name, co.column_name, co.column_default, co.is_nullable, 
			co.data_type, co.character_maximum_length, co.numeric_precision,
            co.numeric_scale, co.datetime_precision, co.column_type, nullif(co.column_key, '') colkey, 
            nullif(co.column_comment, '') col_comment
FROM information_schema.columns co
JOIN information_schema.tables ta
  ON co.table_name = ta.table_name
 AND co.table_schema = ta.table_schema
WHERE co.table_schema = 'dev_naknowbase'
ORDER BY ta.table_type, co.table_name, co.ordinal_position
;

-- a view over information_schema.view dependencies on tables, functions, and views
CREATE OR REPLACE VIEW `dev_naknowbase`.`schema_view_dependency_vw`
AS
SELECT vw.table_name view_name, tab.table_name dependency, tab.table_type depend_type
FROM information_schema.views vw
-- views that select tables
LEFT OUTER JOIN information_schema.tables tab
  ON vw.view_definition LIKE concat('%', tab.table_name, '%')
 AND vw.table_schema = tab.table_schema
WHERE vw.table_schema = 'dev_naknowbase'
-- show the dependencies in the same columns
UNION
SELECT vw.table_name view_name,  
			fun.routine_name function_name , fun.routine_type
FROM information_schema.views vw
-- views that select functions
LEFT OUTER JOIN information_schema.routines fun
   ON vw.view_definition LIKE concat('%', fun.routine_name, '%')
 AND vw.table_schema = fun.routine_schema
WHERE vw.table_schema = 'dev_naknowbase'
ORDER BY view_name, depend_type, dependency
;