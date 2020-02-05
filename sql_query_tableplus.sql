DROP TABLE IF EXISTS Exercise;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Instructor;
DROP TABLE IF EXISTS StudentExercises;



CREATE TABLE Cohort (
Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
Name TEXT NOT NULL UNIQUE
);

CREATE TABLE Student (
Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
FirstName TEXT NOT NULL,
LastName TEXT NOT NULL,
SlackHandle TEXT NOT NULL,
CohortId INTEGER, 
FOREIGN KEY(CohortId) REFERENCES Cohort(Id) 
);

CREATE TABLE Instructor (
Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
FirstName TEXT NOT NULL,
LastName TEXT NOT NULL,
SlackHandle TEXT NOT NULL,
Specialty TEXT NOT NULL,
CohortId INTEGER,
FOREIGN KEY(CohortId) REFERENCES Cohort(Id)
);

CREATE TABLE Exercise (
Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
Name TEXT NOT NULL,
Language TEXT NOT NULL
);

CREATE TABLE StudentExercises (
Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
StudentId INTEGER,
ExerciseId INTEGER,
FOREIGN KEY (StudentId) REFERENCES Student(Id),
FOREIGN KEY (ExerciseId) REFERENCES Exercise(Id)
);

INSERT INTO Cohort(Name) 
VALUES('36');

INSERT INTO Cohort(Name)
VALUES('2');

INSERT INTO Cohort(Name)
VALUES('35');

INSERT INTO Exercise(Name, Language)
VALUES('Universe Creation', 'Python');

INSERT INTO Exercise(Name, Language)
VALUES('Tuples', 'Python');

INSERT INTO Exercise(Name, Language)
VALUES('REGEX', 'HTML');

INSERT INTO Exercise(Name, Language)
VALUES('Front End Capstone', 'React');

INSERT INTO Exercise(Name, Language)
VALUES('Festivus website', 'JavaScript');

INSERT INTO Instructor
SELECT null, 'Joe', 'Shepard', 'joes', 'the jokes', Id
FROM Cohort
WHERE Name = '36';

INSERT INTO Instructor 
SELECT null, 'Jisie', 'David', 'jisie', 'all around badass', Id
FROM Cohort
WHERE Name = '36';

INSERT INTO Instructor
SELECT null, 'Bryan', 'Nilsen', 'bryan nilsen', 'high fives', Id
FROM Cohort 
WHERE Name = '35';


INSERT INTO Student(FirstName, LastName, SlackHandle, CohortId) 
VALUES('Melody', 'Stern', '@melodystern', 1);

INSERT INTO Student(FirstName, LastName, SlackHandle, CohortId)
VALUES('SamSam', 'PitaPita', '@sampita', 1);

INSERT INTO Student
SELECT null, 'Steven', 'Gentry', '@sgentry', Id
FROM Cohort 
WHERE Name = '2';

INSERT INTO Student 
SELECT null, 'Sophie', 'Sensat', '@ssat', Id
FROM Cohort 
WHERE Name = '35';

INSERT INTO Student 
SELECT null, 'Madame', 'Thunderbolt', '@mthunder', Id
FROM Cohort 
WHERE Name = '2';

INSERT INTO Student
SELECT null, 'Heimlich', 'Hunterbaum', '@hhbaum', Id
FROM Cohort 
WHERE Name = '36';

INSERT INTO Student (FirstName, LastName, SlackHandle, CohortId)
VALUES('Geoffry', 'Von Pendleglast', '@pendy', 3);

INSERT INTO StudentExercises
SELECT null, 5, Id
FROM Exercise
WHERE Name = 'Tuples';

INSERT INTO StudentExercises
SELECT null, 5, Id
FROM Exercise
WHERE Name = 'Universe Creation';

INSERT INTO StudentExercises
SELECT null, 1, Id
FROM Exercise 
WHERE Name = 'REGEX';

INSERT INTO StudentExercises
SELECT null, 1, Id
FROM Exercise 
WHERE Name = 'Festivus website';

INSERT INTO StudentExercises
SELECT null, Id, 1
FROM Student 
WHERE FirstName = 'SamSam';

INSERT INTO StudentExercises
SELECT null, Id, 4
FROM Student 
WHERE FirstName = 'SamSam';

INSERT INTO StudentExercises(StudentId, ExerciseId)
VALUES(3, 4);

INSERT INTO StudentExercises(StudentId, ExerciseId)
VALUES(3, 2);

INSERT INTO StudentExercises(StudentId, ExerciseId)
VALUES(4, 1);

INSERT INTO StudentExercises(StudentId, ExerciseId)
VALUES(4, 5);

INSERT INTO StudentExercises(StudentId, ExerciseId)
VALUES(6, 3);

INSERT INTO StudentExercises(StudentId, ExerciseId)
VALUES(6, 5);

INSERT INTO StudentExercises(StudentId, ExerciseId)
VALUES(7, 4);

INSERT INTO StudentExercises(StudentId, ExerciseId)
VALUES(7, 3);

