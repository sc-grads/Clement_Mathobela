SELECT DateOfTransaction, EmployeeNumber,Amount,[dbo].[AmountPlusOne](Amount)
AS AmountAndOne FROM tblTransaction
WHERE EmployeeNumber BETWEEN 650 AND 660
FOR XML RAW('MyRow'), elements
--
SELECT DateOfTransaction, EmployeeNumber,Amount,[dbo].[AmountPlusOne](Amount)
AS AmountAndOne FROM tblTransaction
WHERE EmployeeNumber BETWEEN 650 AND 660
FOR XML PATH('Employees'), root('MyRoot')

--
SELECT 1 AS Tag,NULL AS Parent, DateOfTransaction AS [Elements!1!DateOfTransaction]
, EmployeeNumber AS [Elements!1!EmployeeNumber],Amount AS [Elements!1!Amount] FROM tblTransaction
WHERE EmployeeNumber BETWEEN 650 AND 660
FOR XML EXPLICIT