--Default value:
ALTER TABLE tblTransaction
ADD dateAdded DATE DEFAULT GETDATE()

INSERT INTO tblTransaction(Amount,DateOfTransaction,EmployeeNumber)
VALUES (1200,'2020-06-23',823)

SELECT * FROM tblTransaction WHERE dateAdded IS NOT NULL

--Constraints:

ALTER TABLE tblTransaction
ADD TransactionID INT CONSTRAINT pk_tblTrasaction PRIMARY KEY  IDENTITY(100,1)


BEGIN TRAN
SELECT *  FROM tblEmployee WHERE EmployeeNumber = 123
DELETE FROM tblEmployee WHERE EmployeeNumber = 123
SELECT *  FROM tblEmployee WHERE EmployeeNumber = 123
COMMIT  TRAN

ALTER TABLE tblEmployee
ADD CONSTRAINT unq_tblEmployee UNIQUE (EmployeeNumber)

ALTER TABLE tblEmployee
ADD CONSTRAINT unq_tblEmployee CHECK (DateOfBirth BETWEEN '1905-10-28' AND GETDATE())

INSERT INTO tblDepartment
VALUES(2001,'Bob','M','Smith','AB098768Z','2030-12-01','HR')