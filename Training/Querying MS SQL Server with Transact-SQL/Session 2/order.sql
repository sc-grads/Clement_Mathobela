CREATE TABLE [dbo].[tblEmployee](
	[EmployeeNumber] [int] NOT NULL,
	[EmployeeFirstName] [varchar](20) NOT NULL,
	[EmployeeMiddleName] [varchar](20) NULL,
	[EmployeeLastName] [varchar](20) NOT NULL,
	[EmployeeGovernment] [char](15) NULL,
	[DateOfBirth] [date] NULL,
	[Department] [varchar](20) NULL
) ON [PRIMARY]
GO

BULK INSERT tblEmployee
FROM 'C:\Users\Clement Mathobela\Downloads\70-461dataZIPFile\sample.csv'
WITH (
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);

SELECT * FROM tblEmployee

SELECT DATENAME(YEAR,DateOfBirth),COUNT(*) as numberOfBirth FROM tblEmployee
GROUP BY DATENAME(YEAR,DateOfBirth) ORDER BY DATENAME(YEAR,DateOfBirth)

SELECT EmployeeFirstName, RIGHT(EmployeeFirstName,2) AS last3chars FROM tblEmployee
ORDER BY RIGHT(EmployeeFirstName,2)