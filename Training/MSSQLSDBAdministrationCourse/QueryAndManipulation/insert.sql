USE customerInfo

SELECT * INTO Student_bkp FROM dbo.Student;

CREATE TABLE StudentPhone(
StudentNAME NVARCHAR(30) NOT NULL,
StudentPhoneNo VARCHAR(30) NOT NULL);

INSERT StudentPhone(StudentNAME,StudentPhoneNo)
SELECT StudentName,StudentPhoneNo FROM Student;

SELECT * FROM StudentPhone