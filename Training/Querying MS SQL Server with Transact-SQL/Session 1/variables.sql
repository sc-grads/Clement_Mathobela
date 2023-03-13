DECLARE @myvar AS SMALLINT = 20000
SET @myvar = 200000
--
DECLARE @myvar2 AS INT
SET @myvar2 = 200000

DECLARE @myvar3 AS TINYINT
SET @myvar3 = 20000

SELECT @myvar as Num

-------Activity 4:

select system_type_id, column_id, FLOOR(Convert(decimal,system_type_id) / column_id) as Calculation
from sys.all_columns

select system_type_id, column_id, CEILING(Convert(decimal,system_type_id) / column_id) as Calculation
from sys.all_columns

select system_type_id, column_id, ROUND(Convert(decimal,system_type_id) / column_id,1) as Calculation
from sys.all_columns

select CONVERT(smallint,system_type_id *2)  as Calculation
from sys.all_columns