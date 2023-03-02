
USE AdventureWorks2019

SELECT * FROM Sales.vIndividualCustomer

CREATE TABLE Customer(
CustomerID INT NOT NULL ,
CustomerName VARCHAR(30) NOT NULL,
PhoneNumber VARCHAR(30) NOT NULL,
Email VARCHAR(50) NOT NULL
)
DROP TABLE Customer

INSERT INTO Customer
SELECT BusinessEntityID, FirstName,PhoneNumber,EmailAddress FROM Sales.vIndividualCustomer

SELECT * FROM Customer

Begin Tran
--DELETE FROM Customer WHERE Customername = 'Aaron'
DELETE TOP(18000) FROM Customer

ROLLBACK
Commit

Begin Tran
DELETE Customer
TRUNCATE TABLE Customer
Commit