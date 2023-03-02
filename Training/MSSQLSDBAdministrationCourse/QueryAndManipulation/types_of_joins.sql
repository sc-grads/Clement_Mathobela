USE customerInfo
CREATE TABLE Course(
CourseID INT,
RollNo INT
)
CREATE TABLE Student(
RollNo INT PRIMARY KEY,
StudentName Varchar(50),
StudentCity Varchar (20),
StudentPhoneNo VARCHAR(20),
StudentAge INT
)
INSERT INTO Student VALUES
(1,'Bob','Polokwane','+27 67 982 3142',25),
(2,'Anne','Pretoria','+27 13 542 6542',22),
(3,'Marry','Durban','+27 82 534 8742',19),
(4,'Mason','Nelspruit','+27 71 654 0987',26),
(5,'Jack','Johannesburg','+27 72 876 1234',20),
(6,'Bob','Pretoria','+27 64 654 1230',28),
(7,'Kristy','Cape Town','+27 61 097 1297',25),
(8,'Mpho','Bloemfontein','+27 83 001 0942',23);

INSERT INTO Course VALUES (1,1),(2,2),(2,3),(3,4),(1,5),(4,9),(5,10),(4,11);

SELECT * FROM Student s
JOIN Course c
ON s.RollNo = c.RollNo;

SELECT * FROM Course LEFT JOIN Student ON Student.RollNo = Course.RollNo

SELECT * FROM Course RIGHT JOIN Student ON Student.RollNo = Course.RollNo

SELECT * FROM Course FULL JOIN Student ON Student.RollNo = Course.RollNo