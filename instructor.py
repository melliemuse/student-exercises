from person import NSSPerson

class Instructor(NSSPerson):
    def __init__(self, firstName, lastName, slackHandle, specialty, cohort):
        super().__init__(firstName, lastName, slackHandle, cohort)
        self.specialty = specialty

    def assign_exercise(self, student, *new_exercise):
        for exercise in new_exercise:
            student.exercises.append(exercise)
    def __str__(self):
        return f"Hello there, My name is {self.firstName} and I teach cohort {self.cohort}"