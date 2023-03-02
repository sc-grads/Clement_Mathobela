USE customerInfo;

SELECT * FROM Student

CREATE TRIGGER forInsert
ON Student
AFTER INSERT
AS
INSERT INTO InsertHistory VALUES((Select Max(RollNo) FROM Student),'insert')

CREATE TABLE InsertHistory(
RollNo Int,
TypeOfMod VARCHAR(50)
)
SELECT * FROM InsertHistory