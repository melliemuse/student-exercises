# You must define a type for representing a cohort in code.

# The cohort's name (Evening Cohort 6, Day Cohort 26, etc.)
# The collection of students in the cohort.
# The collection of instructors in the cohort.

class Cohort:
    def __init__(self, name):
        self.name = name
        self.students = list()
        self.instructors = list()
    def __repr__(self):
        return f'{self.name}'
    def assign_instructor(self, new_instructor):
        self.instructors.append(new_instructor) 
    def assign_student(self, new_student):
        self.students.append(new_student) 
    def list_instructors(self): 
        for instructor in self.instructors:
            print(instructor.firstName)