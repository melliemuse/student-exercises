class Instructor:
    def __init__(self, firstName, lastName, slackHandle, specialty):
        self.firstName = firstName
        self.lastName = lastName
        self.slackHandle = slackHandle
        self.cohort = ""
        self.specialty = specialty

    def assign_exercise(self, student, *new_exercise):
        for exercise in new_exercise:
            student.exercises.append(exercise)
    def __str__(self):
        return f"Hello there, My name is {self.firstName}"