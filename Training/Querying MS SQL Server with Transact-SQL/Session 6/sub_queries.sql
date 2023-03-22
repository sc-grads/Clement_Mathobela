SELECT * FROM tblTransaction
WHERE EmployeeNumber In (SELECT EmployeeNumber FROM tblEmployee WHERE EmployeeLastName LIKE 'B%')


--all is similar to and
SELECT * FROM tblTransaction
WHERE EmployeeNumber <> all (SELECT EmployeeNumber FROM tblEmployee WHERE EmployeeLastName LIKE 'B%')

--Similar to any(or):
SELECT * FROM tblTransaction
WHERE EmployeeNumber =any (SELECT EmployeeNumber FROM tblEmployee WHERE EmployeeLastName LIKE 'B%')

SELECT * FROM tblTransaction AS tt
JOIN (SELECT * FROM tblEmployee WHERE EmployeeLastName LIKE 'B%') AS te
ON tt.EmployeeNumber = te.EmployeeNumber

----
SELECT D.Department, EmployeeNumber, EmployeeFirstName, EmployeeLastName,
       RANK() OVER(PARTITION BY D.Department ORDER BY E.EmployeeNumber) AS TheRank
FROM tblDepartment AS D
JOIN tblEmployee AS E ON D.Department = E.Department
ORDER BY D.Department,EmployeeNumber
