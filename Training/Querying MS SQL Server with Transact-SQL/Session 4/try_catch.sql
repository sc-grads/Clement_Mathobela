CREATE PROC Average(@EmployeeNumberFrom INT,@EmployeeNumberTo INT,@Average INT OUTPUT)
AS
BEGIN
	DECLARE @TotalAmount MONEY
	DECLARE @NumberOfEmployee INT
	BEGIN TRY
		SELECT @TotalAmount = SUM(Amount) FROM tblTransaction
		WHERE EmployeeNumber BETWEEN @EmployeeNumberFrom AND @EmployeeNumberTo
		SELECT @NumberOfEmployee = COUNT(DISTINCT EmployeeNumber) FROM tblEmployee
		WHERE EmployeeNumber BETWEEN @EmployeeNumberFrom AND @EmployeeNumberTo
		SET @Average = @TotalAmount/@NumberOfEmployee
		RETURN
	END TRY
	BEGIN CATCH
		SET @Average = 0
		RETURN 1
	END CATCH
END

DECLARE @AvgBalance int, @ReturnStatus int
EXEC @ReturnStatus = Average 0,1, @AvgBalance OUTPUT
select @AvgBalance as Average_Balance, @ReturnStatus as Return_Status