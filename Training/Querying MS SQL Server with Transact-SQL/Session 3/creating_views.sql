CREATE VIEW view_te_tt AS
SELECT te.EmployeeFirstName,te.Department,tt.Amount
FROM tblEmployee AS te
JOIN tblTransaction AS tt
ON te.EmployeeNumber = tt.EmployeeNumber

SELECT * FROM view_te_tt
DROP VIEW view_te_tt

SELECT * FROM sys.views WHERE name = '[dbo].[view_te_tt]'

ALTER VIEW view_te_tt AS
SELECT te.EmployeeFirstName,te.Department,tt.Amount,tt.dateAdded
FROM tblEmployee AS te
JOIN tblTransaction AS tt
ON te.EmployeeNumber = tt.EmployeeNumber