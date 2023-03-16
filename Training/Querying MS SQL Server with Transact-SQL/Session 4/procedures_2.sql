CREATE PROCEDURE proc_tblEmployee(@EmployeeNumberFrom INT, @EmployeeNumberTo INT)
AS
BEGIN
	if exists (SELECT * FROM tblEmployee WHERE EmployeeNumber BETWEEN @EmployeeNumberFrom AND @EmployeeNumberTo)
	BEGIN
		SELECT EmployeeNumber,EmployeeFirstName,EmployeeLastName
		FROM tblEmployee
		WHERE EmployeeNumber BETWEEN @EmployeeNumberFrom AND @EmployeeNumberTo
	END

END
Go
proc_tblEmployee 136,140