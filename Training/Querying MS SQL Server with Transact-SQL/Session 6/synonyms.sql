CREATE synonym Emptbl
FOR tblEmployee

SELECT * FROM Emptbl

--Dynamic: sql query inside a string

DECLARE @command as VARCHAR(255);
SET @command = 'SELECT * FROM tblTransaction WHERE EmployeeNumber = 203'
EXECUTE (@command);

