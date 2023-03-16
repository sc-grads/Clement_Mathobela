CREATE TRIGGER trigger_tblDepartment
ON tblDepartment
AFTER DELETE,INSERT, UPDATE
AS
BEGIN
SELECT * FROM deleted
SELECT * FROM inserted

END
SELECT * FROM tblDepartment

INSERT INTO tblDepartment VALUES('SALES','Bob')

BEGIN TRAN
DELETE FROM tblDepartment WHERE DepartmentHead = ''

ROLLBACK TRAN