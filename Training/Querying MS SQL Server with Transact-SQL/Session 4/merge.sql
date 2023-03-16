CREATE TABLE tblTransaction2
(Amount SMALLMONEY NOT NULL,
DateOfTransaction SMALLDATETIME NULL,
EmployeeNumber INT NOT NULL,
dateAdded DATE NULL,
TransactionID INT PRIMARY KEY)

MERGE INTO tblTransaction AS T
USING tblTransaction2 AS S
ON T.TransactionID = S.TransactionID
WHEN MATCHED THEN
	UPDATE
	SET Amount = T.Amount + S.Amount
WHEN NOT MATCHED THEN
	INSERT
	VALUES(S.Amount,S.DateOfTransaction,S.EmployeeNumber,S.dateAdded,S.TransactionID);