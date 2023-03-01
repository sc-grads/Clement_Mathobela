USE AdventureWorks2019;
SELECT * FROM Person.Person
SELECT e.BusinessEntityID, EmailAddress, LastName FROM Person.EmailAddress e
JOIN Person.Person p ON e.BusinessEntityID = p.BusinessEntityID
