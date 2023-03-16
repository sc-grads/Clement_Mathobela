DELETE FROM view_te_tt WHERE Amount= -999.28
SELECT * FROM view_te_tt


ALTER TRIGGER trigger_on_view
ON view_te_tt
INSTEAD OF DELETE
AS
BEGIN
DECLARE @EmployeeFirstName AS VARCHAR(20)
DECLARE  @Department AS VARCHAR(20)
DECLARE @Amount AS SMALLMONEY

SELECT @EmployeeFirstName = EmployeeFirstName, @Department = Department, @Amount = Amount
FROM deleted

DELETE tblTransaction FROM tblTransaction AS tt
WHERE tt.Amount = @Amount
END

SELECT * FROM tblTransaction WHERE Amount = -999.28