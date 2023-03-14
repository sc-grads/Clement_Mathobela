CREATE TABLE tblTransaction(
Amount SMALLMONEY NOT NULL,
DateOfTransaction SMALLDATETIME NULL,
EmployeeNumber INT NOT NULL
);


SELECT * FROM tblEmployee as te JOIN tblTransaction AS tt ON te.EmployeeNumber = tt.EmployeeNumber
GO
SELECT te.EmployeeNumber, EmployeeFirstName, EmployeeLastName, Amount From tblEmployee
AS te JOIN tblTransaction as tt
ON te.EmployeeNumber = tt.EmployeeNumber;

SELECT te.EmployeeNumber, EmployeeFirstName, EmployeeLastName, Sum(Amount) AS SumOfTransaction FROM tblEmployee as te
JOIN tblTransaction as tt ON te.EmployeeNumber = tt.EmployeeNumber
GROUP BY te.EmployeeNumber, EmployeeFirstName, EmployeeLastName
ORDER BY EmployeeNumber

---LEFT JOIN
SELECT te.EmployeeNumber, EmployeeFirstName, EmployeeLastName, Sum(Amount) AS SumOfTransaction FROM tblEmployee as te
LEFT JOIN tblTransaction as tt ON te.EmployeeNumber = tt.EmployeeNumber
GROUP BY te.EmployeeNumber, EmployeeFirstName, EmployeeLastName
ORDER BY EmployeeNumber

---RIGHT JOIN
SELECT te.EmployeeNumber, EmployeeFirstName, EmployeeLastName, Sum(Amount) AS SumOfTransaction FROM tblEmployee as te
RIGHT JOIN tblTransaction as tt ON te.EmployeeNumber = tt.EmployeeNumber
GROUP BY te.EmployeeNumber, EmployeeFirstName, EmployeeLastName
ORDER BY EmployeeNumber

----Coding exercise 3:

SELECT st.TeamID, st.TeamName, sg.Goals,sg.Points FROM SportTeams as st
JOIN SportGoals AS sg
ON st.TeamID = sg.Team