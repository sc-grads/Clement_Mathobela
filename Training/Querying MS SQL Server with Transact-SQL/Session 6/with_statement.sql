WITH Numbers AS (
SELECT TOP(1125) ROW_NUMBER() OVER(ORDER BY (SELECT NULL))
AS RowNumber FROM tblTransaction AS U)

SELECT U.RowNumber FROM Numbers AS U
LEFT JOIN tblTransaction AS T
ON U.RowNumber = T.EmployeeNumber
WHERE T.EmployeeNumber IS NULL
ORDER BY U.RowNumber