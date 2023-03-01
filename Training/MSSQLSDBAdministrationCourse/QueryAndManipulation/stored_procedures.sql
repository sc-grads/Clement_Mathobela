
--Procedure with parameters:

CREATE PROCEDURE GetCity @City VARCHAR(30)
--WITH ENCRYPTION
AS
SELECT * FROM Person.Address WHERE City = @City
Exec GetCity @City = 'Dallas'
--OR:
Exec GetCity 'Paris'