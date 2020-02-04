import sqlite3
from student import Student
from cohort import Cohort 

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

            # for student in all_students:
            #     # print(f'{student.first_name} {student.last_name} is in {student.cohort}')
            #     print(student)

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

            

reports = StudentExerciseReports()
reports.all_students()
reports.all_cohorts()