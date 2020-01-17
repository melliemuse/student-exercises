class Instructor:
    def __init__(self, firstName, lastName, slackHandle, specialty):
        firstName = firstName
        lastName = lastName
        slackHandle = slackHandle
        cohort = ""
        specialty = specialty
    def assign_exercise(self, student, new_exercise):
        student.exercises.append(new_exercise)