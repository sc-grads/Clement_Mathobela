SELECT *
FROM tblDepartment as td
LEFT JOIN tblEmployee AS te
ON td.Department = te.Department
LEFT JOIN tblTransaction AS tt
ON tt.EmployeeNumber = te.EmployeeNumber
WHERE tt.EmployeeNumber IS NULL