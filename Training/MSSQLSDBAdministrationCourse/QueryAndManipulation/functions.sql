USE AdventureWorks2019


SELECT * FROM Person.Person

CREATE FUNCTION PersonFullName(@FirstName VARCHAR(50),@MiddleName VARCHAR(50) = 'DOE', @LastName VARCHAR(50 ))

RETURNS VARCHAR(205)
AS
BEGIN
RETURN (SELECT @FirstName +' '+@MiddleName+' '+ @LastName);

END

DROP FUNCTION dbo.PersonFullName

SELECT dbo.PersonFullName(FirstName,MiddleName,LastName) as FullName,ModifiedDate FROM Person.Person
WHERE MiddleName IS NOT NULL

-----------------
CREATE FUNCTION GetTable()
RETURNS Table
AS
BEGIN
RETURN SELECT * FROM Person.ContactType
END