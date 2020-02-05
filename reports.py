import sqlite3
from student import Student
from cohort import Cohort 
from exercise import Exercise
from instructor import Instructor

# student = Student('Bart', 'Simpson', '@bart', 'Cohort 8')
# print(f'{student.first_name} {student.last_name} is in {student.cohort}')

class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/nss4/workspace/python/exercises/tracking-student-exercises/studentexercises.db"

    def all_students(self):
        
        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(
                row[1], row[2], row[3], row[5]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.Id,
                s.FirstName,
                s.LastName,
                s.SlackHandle,
                s.CohortId,
                c.Name
            from Student s
            join Cohort c on s.CohortId = c.Id
            order by s.CohortId
            """)

            all_students = db_cursor.fetchall()

            [print(s) for s in all_students]

    def all_cohorts(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(
                row[1]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT Id, Name
            FROM Cohort
            """)

            all_cohorts = db_cursor.fetchall()

            [print(c) for c in all_cohorts]

    def all_exercises(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(
                row[1], row[2]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT 
            Id, 
            Name, 
            Language
            FROM Exercise
            """)

            all_exercises = db_cursor.fetchall()

            [print(e) for e in all_exercises]

    def all_js_exercises(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(
                row[1], row[2]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT 
            Id, 
            Name,
            Language
            FROM Exercise 
            WHERE Language = "JavaScript"
            OR Language = "React"
            """)

            all_js_exercises = db_cursor.fetchall()

            [print(js) for js in all_js_exercises]

    def all_python_exercises(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(
                row[1], row[2]
            )
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT 
        Id, 
        Name,
        Language
        FROM Exercise
        WHERE Language = "Python"
        """)
        all_python_exercises = db_cursor.fetchall()

        [print(py) for py in all_python_exercises]
    
    def all_html_exercises(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(
                row[1], row[2]
            )
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT 
        Id, 
        Name,
        Language
        FROM Exercise
        WHERE Language = "HTML"
        """)
        all_html_exercises = db_cursor.fetchall()

        [print(h) for h in all_html_exercises]

        # Display all instructors with cohort name.

    def all_instructors(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructor(
                row[1], row[2], row[3], row[4], row[6]
            )
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT 
        i.Id,
        i.FirstName,
        i.LastName,
        i.SlackHandle,
        i.Specialty,
        i.CohortId,
        c.Name
        FROM Instructor i
        JOIN Cohort c
        ON i.CohortId = c.Id
        """)

        all_instructors = db_cursor.fetchall()
        [print(inst) for inst in all_instructors]

    # List the exercises assigned to each student. Display each student name and the exercises s/he has been assigned beneath their name. Use a dictionary to track each student. Remember that the key should be the student id and the value should be the entire student object.

    def all_student_exercises(self):
        exercises = dict()
        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT e.Id ExerciseId,
        e.Name,
        s.Id,
        s.FirstName,
        s.LastName 
        FROM Exercise e
        JOIN StudentExercises se 
        ON se.ExerciseId = e.Id
        JOIN Student s 
        ON se.StudentId = s.Id
        """)

        data = db_cursor.fetchall()

        for row in data:
            exercise_id = row[0]
            exercise_name = row[1]
            student_id = row[2]
            student_name = f'{row[3]} {row[4]}'

            if exercise_name not in exercises:
                exercises[exercise_name] = [student_name]
            else: 
                exercises[exercise_name].append(student_name)

        print(exercises)

reports = StudentExerciseReports()
reports.all_students()
reports.all_cohorts()
# reports.all_exercises()
# reports.all_js_exercises()
reports.all_python_exercises()
reports.all_html_exercises()
reports.all_instructors()
reports.all_student_exercises()