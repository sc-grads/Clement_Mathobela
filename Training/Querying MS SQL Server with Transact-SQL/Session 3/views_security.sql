CREATE VIEW view_te_tt WITH ENCRYPTION AS
SELECT te.EmployeeFirstName,te.Department,tt.Amount,tt.dateAdded
FROM tblEmployee AS te
JOIN tblTransaction AS tt
ON te.EmployeeNumber = tt.EmployeeNumber