SELECT Department,'' as DepartmentHead
INTO tblDepartment
FROM tblEmployee
GROUP BY Department

SELECT * FROM tblDepartment
ALTER TABLE tblDepartment
ALTER COLUMN DepartmentHead VARCHAR(20)

--Using Distinct:
SELECT DISTINCT Department FROM tblEmployee

--Derived Table:

SELECT Department FROM
(SELECT Department,Count(*) as NoOfDepartment FROM tblEmployee GROUP BY Department ) as NewTable

--Joining three(3) tables:
SELECT td.Department, SUM(Amount) AS SumOfAmount
FROM tblDepartment as td
LEFT JOIN tblEmployee AS te
ON td.Department = te.Department
LEFT JOIN tblTransaction AS tt
ON tt.EmployeeNumber = te.EmployeeNumber
GROUP BY td.Department
ORDER BY SUM(Amount)

INSERT INTO tblDepartment VALUES('Accounts','Samuel')