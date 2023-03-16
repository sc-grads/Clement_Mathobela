CREATE VIEW dbo.view_te_tt  with schemabinding AS
SELECT te.EmployeeFirstName,te.Department,tt.Amount
FROM dbo.tblEmployee AS te
JOIN dbo.tblTransaction AS tt
ON te.EmployeeNumber = tt.EmployeeNumber

--Cannot do the following , case you modifying more than one base tables:
DELETE FROM view_te_tt WHERE Amount= -999.28

CREATE UNIQUE CLUSTERED INDEX index_view ON view_te_tt(Amount)