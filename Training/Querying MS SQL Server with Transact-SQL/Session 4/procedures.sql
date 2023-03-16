CREATE PROCEDURE proc_tblEmployee
AS
BEGIN
	SELECT EmployeeNumber,EmployeeFirstName,EmployeeLastName
	FROM tblEmployee
END
GO
proc_tblEmployee
exec proc_tblEmployee
Execute proc_tblEmployee

if exists (SELECT * FROM sys.procedures WHERE name= 'proc_tblEmployee')
	DROP PROCEDURE proc_tblEmployee
Go
ALTER PROCEDURE proc_tblEmployee(@EmployeeNumber INT)
AS
BEGIN
	SELECT EmployeeNumber,EmployeeFirstName,EmployeeLastName
	FROM tblEmployee
	WHERE EmployeeNumber = @EmployeeNumber
END
Go
proc_tblEmployee 235

-----------Exercise with IF:

Go
ALTER PROCEDURE proc_tblEmployee(@EmployeeNumber INT)
AS
BEGIN
	if @EmployeeNumber < 300
	BEGIN
		SELECT EmployeeNumber,EmployeeFirstName,EmployeeLastName
		FROM tblEmployee
		WHERE EmployeeNumber = @EmployeeNumber
	END
	ELSE
	BEGIN
		SELECT EmployeeNumber,EmployeeFirstName,EmployeeLastName ,EmployeeGovernment
		FROM tblEmployee
		WHERE EmployeeNumber = @EmployeeNumber
		SELECT * FROM tblTransaction WHERE EmployeeNumber = @EmployeeNumber


	END
END
Go
proc_tblEmployee 500