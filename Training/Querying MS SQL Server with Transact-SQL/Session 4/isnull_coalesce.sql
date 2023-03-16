
--Function that return first not null input:

DECLARE @myvar AS CHAR(10)
DECLARE @myvar2 AS VARCHAR(20)--= 'Hello'
--ISNULL Only takes two inputs and if both inputs are null,returns NULL:
SELECT ISNULL(@myvar,@myvar2) AS My_Output
--COALESCE takes at least two:
SELECT COALESCE(@myvar,'') AS MY_Output_2